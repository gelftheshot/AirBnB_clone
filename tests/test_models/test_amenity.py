#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
from models import storage
FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class TestAmenityInit(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = ""

    def test_init(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_inheritance(self):
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_id_is_string(self):
        self.assertIsInstance(self.amenity.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.amenity.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.amenity.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.amenity.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_name_attribute(self):
        self.assertTrue("name" in self.amenity.__dict__)
        self.assertIsInstance(self.amenity.name, str)

class TestAmenityInheritedInit(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()
        self.amenity.name = ""
    def test_init(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_id_is_string(self):
        self.assertIsInstance(self.amenity.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.amenity.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.amenity.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.amenity.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_amenity_instantiates_with_kwargs(self):
        amenity = Amenity(name="Test", value=42)
        self.assertEqual(amenity.name, "Test")
        self.assertEqual(amenity.value, 42)


    def test_two_amenities_different_created_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.created_at, amenity2.created_at)

    def test_two_amenities_different_updated_at(self):
        amenity1 = Amenity()
        sleep(0.05)
        amenity2 = Amenity()
        self.assertLess(amenity1.updated_at, amenity2.updated_at)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.amenity.updated_at, datetime)


    def test_id_is_unique(self):
        self.assertNotEqual(self.amenity1.id, self.amenity2.id)

    def test_amenity_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_amenity_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_amenity_instantiates_without_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_amenity_instance_in_objects(self):
        self.assertIn(Amenity(), storage.all().values())

    def test_amenity_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))
class TestAmenityStr(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_str(self):
        self.assertEqual(str, type(str(self.amenity)))

class TestAmenityStr(unittest.TestCase):
    
    def setUp(self):
        self.amenity = Amenity()

    def test_str(self):
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_str_format(self):
        expected_str_format = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str_format)

class TestAmenitySave(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_save(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)

    def test_save_does_not_change_created_at(self):
        old_created_at = self.amenity.created_at
        self.amenity.save()
        self.assertEqual(self.amenity.created_at, old_created_at)

    def test_save_changes_updated_at(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)

    def test_save_updates_updated_at(self):
        updated_at_before_save = self.amenity.updated_at
        self.amenity.save()
        updated_at_after_save = self.amenity.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

class TestAmenityToDict(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.amenity.new_attr = "new attribute value"
        self.amenity.int_attr = 66

    def test_to_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertEqual(amenity_dict["created_at"], self.amenity.created_at.strftime(FORMAT))
        self.assertEqual(amenity_dict["updated_at"], self.amenity.updated_at.strftime(FORMAT))

    def test_to_dict_returns_dict(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertIn("__class__", amenity_dict)

    def test_to_dict_formats_dates(self):
        amenity_dict = self.amenity.to_dict()
        created_at = datetime.strptime(amenity_dict["created_at"], FORMAT)
        updated_at = datetime.strptime(amenity_dict["updated_at"], FORMAT)
        self.assertEqual(created_at, self.amenity.created_at)
        self.assertEqual(updated_at, self.amenity.updated_at)

    def test_to_dict_includes_all_attributes(self):
        amenity_dict = self.amenity.to_dict()
        self.assertIn("new_attr", amenity_dict)
        self.assertEqual(amenity_dict["new_attr"], "new attribute value")
    def test_to_dict_handles_non_string_attributes(self):
        self.amenity.int_attr = 66
        amenity_dict = self.amenity.to_dict()
        self.assertIn("int_attr", amenity_dict)
        self.assertEqual(amenity_dict["int_attr"], 66)

    def test_to_dict_handles_boolean_attributes(self):
        self.amenity.bool_attr = True
        amenity_dict = self.amenity.to_dict()
        self.assertIn("bool_attr", amenity_dict)
        self.assertEqual(amenity_dict["bool_attr"], True)

    def test_to_dict_handles_list_attributes(self):
        self.amenity.list_attr = [1, 2, 3]
        amenity_dict = self.amenity.to_dict()
        self.assertIn("list_attr", amenity_dict)
        self.assertEqual(amenity_dict["list_attr"], [1, 2, 3])

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.amenity.to_dict(12)

    def test_to_dict_handles_tuple_attributes(self):
        self.amenity.tuple_attr = (4, 5, 6)
        amenity_dict = self.amenity.to_dict()
        self.assertIn("tuple_attr", amenity_dict)
        self.assertEqual(amenity_dict["tuple_attr"], (4, 5, 6))



    def test_to_dict_handles_dict_attributes(self):
        self.amenity.dict_attr = {"key": "value"}
        amenity_dict = self.amenity.to_dict()
        self.assertIn("dict_attr", amenity_dict)
        self.assertEqual(amenity_dict["dict_attr"], {"key": "value"})

    def test_to_dict_handles_float_attributes(self):
        self.amenity.float_attr = 10.11
        amenity_dict = self.amenity.to_dict()
        self.assertIn("float_attr", amenity_dict)
        self.assertEqual(amenity_dict["float_attr"], 10.11)

    def test_to_dict_handles_none_attributes(self):
        self.amenity.none_attr = None
        amenity_dict = self.amenity.to_dict()
        self.assertIn("none_attr", amenity_dict)
        self.assertEqual(amenity_dict["none_attr"], None)

    def test_to_dict_with_arg(self):
        """Tests to_dict method with an argument"""
        with self.assertRaises(TypeError):
            self.amenity.to_dict(12)

if __name__ == "__main__":
    unittest.main()
