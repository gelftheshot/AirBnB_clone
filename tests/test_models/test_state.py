#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
from models import storage
FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.state.name = ""
        

    def test_init(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_inheritance(self):
        self.assertTrue(issubclass(State, BaseModel))

    def test_id_is_string(self):
        self.assertIsInstance(self.state.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.state.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.state.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.state.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_name_attribute(self):
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

class TestStateInheritedInit(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.state1 = State()
        self.state2 = State()

    def test_init(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_id_is_string(self):
        self.assertIsInstance(self.state.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.state.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.state.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.state.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.state.created_at, datetime)

    def test_state_instantiates_with_kwargs(self):
        state = State(name="Test", value=42)
        self.assertEqual(state.name, "Test")
        self.assertEqual(state.value, 42)


    def test_two_states_different_created_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_two_states_different_updated_at(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_id_is_unique(self):
        self.assertNotEqual(self.state1.id, self.state2.id)

    def test_state_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_state_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_state_instantiates_without_args(self):
        self.assertEqual(State, type(State()))

    def test_new_state_instance_in_objects(self):
        self.assertIn(State(), storage.all().values())

    def test_state_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

class TestStateStr(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_str(self):
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_str_format(self):
        expected_str_format = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str_format)

class TestStateSave(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_save(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)

    def test_save_does_not_change_created_at(self):
        old_created_at = self.state.created_at
        self.state.save()
        self.assertEqual(self.state.created_at, old_created_at)

    def test_save_changes_updated_at(self):
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)

    def test_save_updates_updated_at(self):
        updated_at_before_save = self.state.updated_at
        self.state.save()
        updated_at_after_save = self.state.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(12)
class TestStateToDict(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.state.new_attr = "new attribute value"
        self.state.int_attr = 66

    def test_to_dict(self):
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["created_at"], self.state.created_at.strftime(FORMAT))
        self.assertEqual(state_dict["updated_at"], self.state.updated_at.strftime(FORMAT))

    def test_to_dict_returns_dict(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        state_dict = self.state.to_dict()
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertIn("__class__", state_dict)

    def test_to_dict_formats_dates(self):
        state_dict = self.state.to_dict()
        created_at = datetime.strptime(state_dict["created_at"], FORMAT)
        updated_at = datetime.strptime(state_dict["updated_at"], FORMAT)
        self.assertEqual(created_at, self.state.created_at)
        self.assertEqual(updated_at, self.state.updated_at)

    def test_to_dict_includes_all_attributes(self):
        state_dict = self.state.to_dict()
        self.assertIn("new_attr", state_dict)
        self.assertEqual(state_dict["new_attr"], "new attribute value")

    def test_to_dict_handles_non_string_attributes(self):
        state_dict = self.state.to_dict()
        self.assertIn("int_attr", state_dict)
        self.assertEqual(state_dict["int_attr"], 66)


if __name__ == "__main__":
    unittest.main()
