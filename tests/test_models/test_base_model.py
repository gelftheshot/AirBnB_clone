#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.base_model import storage
from datetime import sleep
FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class TestBaseModelInit(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_init(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.model.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.model.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.model.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)
        
    def test_id_is_unique(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()
        self.assertNotEqual(self.model1.id, self.model2.id)

    
    def test_base_model_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_base_model_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_base_model_instantiates_without_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_base_model_instance_in_objects(self):
        
        self.assertIn(BaseModel(), storage.all().values())

    def test_base_model_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_base_model_instantiates_with_kwargs(self):
        model = BaseModel(name="Test", value=42)
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.value, 42)

    def test_base_model_instantiates_without_kwargs(self):
        model = BaseModel()
        self.assertIsNone(getattr(model, "name", None))
        self.assertIsNone(getattr(model, "value", None))

    def test_two_models_different_created_at(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_two_models_different_updated_at(self):
        model1 = BaseModel()
        sleep(0.05)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)


class TestBaseModelStr(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_str_format(self):
        expected_str_format = "[BaseModel] ({}) {{'id': '{}', 'created_at': '{}', 'updated_at': '{}'}}".format(self.model.id, self.model.id, self.model.created_at.isoformat(), self.model.updated_at.isoformat())
        self.assertEqual(str(self.model), expected_str_format)

class TestBaseModelSave(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_save_does_not_change_created_at(self):
        old_created_at = self.model.created_at
        self.model.save()
        self.assertEqual(self.model.created_at, old_created_at)

    def test_save_changes_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_save_updates_updated_at(self):
        updated_at_before_save = self.model.updated_at
        self.model.save()
        updated_at_after_save = self.model.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)
    
    def test_save_with_arg(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save(12)

class TestBaseModelToDict(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()
        self.model.new_attr = "new attribute value"
        self.model.int_attr = 66

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], self.model.created_at.strftime(FORMAT))
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.strftime(FORMAT))

    def test_to_dict_returns_dict(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        model_dict = self.model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

    def test_to_dict_formats_dates(self):
        model_dict = self.model.to_dict()
        created_at = datetime.strptime(model_dict["created_at"], FORMAT)
        updated_at = datetime.strptime(model_dict["updated_at"], FORMAT)
        self.assertEqual(created_at, self.model.created_at)
        self.assertEqual(updated_at, self.model.updated_at)

    def test_to_dict_includes_all_attributes(self):
        model_dict = self.model.to_dict()
        self.assertIn("new_attr", model_dict)
        self.assertEqual(model_dict["new_attr"], "new attribute value")

    def test_to_dict_handles_non_string_attributes(self):
        model_dict = self.model.to_dict()
        self.assertIn("int_attr", model_dict)
        self.assertEqual(model_dict["int_attr"], 66)
    def test_to_dict_handles_boolean_attributes(self):
            self.model.bool_attr = True
            model_dict = self.model.to_dict()
            self.assertIn("bool_attr", model_dict)
            self.assertEqual(model_dict["bool_attr"], True)
    def test_to_dict_handles_list_attributes(self):
        self.model.list_attr = [1, 2, 3]
        model_dict = self.model.to_dict()
        self.assertIn("list_attr", model_dict)
        self.assertEqual(model_dict["list_attr"], [1, 2, 3])

    def test_to_dict_with_arg(self):
        """Tests to_dict method with an argument"""
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(12)

    def test_to_dict_handles_tuple_attributes(self):
        self.model.tuple_attr = (4, 5, 6)
        model_dict = self.model.to_dict()
        self.assertIn("tuple_attr", model_dict)
        self.assertEqual(model_dict["tuple_attr"], (4, 5, 6))

    def test_to_dict_handles_set_attributes(self):
        self.model.set_attr = {7, 8, 9}
        model_dict = self.model.to_dict()
        self.assertIn("set_attr", model_dict)
        self.assertEqual(model_dict["set_attr"], {7, 8, 9})

    def test_to_dict_handles_dict_attributes(self):
        self.model.dict_attr = {"key": "value"}
        model_dict = self.model.to_dict()
        self.assertIn("dict_attr", model_dict)
        self.assertEqual(model_dict["dict_attr"], {"key": "value"})

    def test_to_dict_handles_float_attributes(self):
        self.model.float_attr = 10.11
        model_dict = self.model.to_dict()
        self.assertIn("float_attr", model_dict)
        self.assertEqual(model_dict["float_attr"], 10.11)

    def test_to_dict_handles_none_attributes(self):
        self.model.none_attr = None
        model_dict = self.model.to_dict()
        self.assertIn("none_attr", model_dict)
        self.assertEqual(model_dict["none_attr"], None)
    
    def test_to_dict_with_arg(self):
        """Tests to_dict method with an argument"""
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(12)

    def test_to_dict_with_arg(self):
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.to_dict(12)

if __name__ == "__main__":
    unittest.main()
