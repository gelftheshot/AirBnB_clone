#!/usr/bin/python3
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from time import sleep
FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class TestPlaceInit(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.place.city_id = ""
        self.place.user_id = ""
        self.place.name = ""
        self.place.description = ""
        self.place.number_rooms = 0
        self.place.number_bathrooms = 0
        self.place.max_guest = 0
        self.place.price_by_night = 0
        self.place.latitude = 0.0
        self.place.longitude = 0.0
        self.place.amenity_ids = []


    def test_init(self):
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
    def test_inheritance(self):
        self.assertTrue(issubclass(Place, BaseModel))

    def test_id_is_string(self):
        self.assertIsInstance(self.place.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.place.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.place.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.place.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_attributes(self):
        self.assertTrue("city_id" in self.place.__dict__)
        self.assertTrue("user_id" in self.place.__dict__)
        self.assertTrue("name" in self.place.__dict__)
        self.assertTrue("description" in self.place.__dict__)
        self.assertTrue("number_rooms" in self.place.__dict__)
        self.assertTrue("number_bathrooms" in self.place.__dict__)
        self.assertTrue("max_guest" in self.place.__dict__)
        self.assertTrue("price_by_night" in self.place.__dict__)
        self.assertTrue("latitude" in self.place.__dict__)
        self.assertTrue("longitude" in self.place.__dict__)
        self.assertTrue("amenity_ids" in self.place.__dict__)
class TestPlaceInheritedInit(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.place1 = Place()
        self.place2 = Place()

    def test_init(self):
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_id_is_string(self):
        self.assertIsInstance(self.place.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.place.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.place.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.place.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.place.created_at, datetime)

    def test_place_instantiates_with_kwargs(self):
        place = Place(name="Test", value=42)
        self.assertEqual(place.name, "Test")
        self.assertEqual(place.value, 42)


    def test_two_places_different_created_at(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_two_places_different_updated_at(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.place.updated_at, datetime)


    def test_id_is_unique(self):
        self.assertNotEqual(self.place1.id, self.place2.id)

    def test_place_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_place_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_place_instantiates_without_args(self):
        self.assertEqual(Place, type(Place()))

    def test_new_place_instance_in_objects(self):
        self.assertIn(Place(), storage.all().values())

    def test_place_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

class TestPlaceStr(unittest.TestCase):
    
    def setUp(self):
        self.place = Place()

    def test_str(self):
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_str_format(self):
        expected_str_format = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str_format)

class TestPlaceSave(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_save(self):
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated_at)

    def test_save_does_not_change_created_at(self):
        old_created_at = self.place.created_at
        self.place.save()
        self.assertEqual(self.place.created_at, old_created_at)

    def test_save_changes_updated_at(self):
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated_at)

    def test_save_updates_updated_at(self):
        updated_at_before_save = self.place.updated_at
        self.place.save()
        updated_at_after_save = self.place.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(12)

class TestPlaceToDict(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.place.new_attr = "new attribute value"
        self.place.int_attr = 66

    def test_to_dict(self):
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["created_at"], self.place.created_at.strftime(FORMAT))
        self.assertEqual(place_dict["updated_at"], self.place.updated_at.strftime(FORMAT))

    def test_to_dict_returns_dict(self):
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        place_dict = self.place.to_dict()
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)

    def test_to_dict_formats_dates(self):
        place_dict = self.place.to_dict()
        created_at = datetime.strptime(place_dict["created_at"], FORMAT)
        updated_at = datetime.strptime(place_dict["updated_at"], FORMAT)
        self.assertEqual(created_at, self.place.created_at)
        self.assertEqual(updated_at, self.place.updated_at)

    def test_to_dict_includes_all_attributes(self):
        place_dict = self.place.to_dict()
        self.assertIn("new_attr", place_dict)
        self.assertEqual(place_dict["new_attr"], "new attribute value")

    def test_to_dict_handles_non_string_attributes(self):
        place_dict = self.place.to_dict()
        self.assertIn("int_attr", place_dict)
        self.assertEqual(place_dict["int_attr"], 66)

    def test_to_dict_handles_boolean_attributes(self):
        self.place.bool_attr = True
        place_dict = self.place.to_dict()
        self.assertIn("bool_attr", place_dict)
        self.assertEqual(place_dict["bool_attr"], True)

    def test_to_dict_handles_list_attributes(self):
        self.place.list_attr = [1, 2, 3]
        place_dict = self.place.to_dict()
        self.assertIn("list_attr", place_dict)
        self.assertEqual(place_dict["list_attr"], [1, 2, 3])

class TestPlaceToDict(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.place.to_dict(12)

    def test_to_dict_handles_tuple_attributes(self):
        self.place.tuple_attr = (4, 5, 6)
        place_dict = self.place.to_dict()
        self.assertIn("tuple_attr", place_dict)
        self.assertEqual(place_dict["tuple_attr"], (4, 5, 6))



    def test_to_dict_handles_dict_attributes(self):
        self.place.dict_attr = {"key": "value"}
        place_dict = self.place.to_dict()
        self.assertIn("dict_attr", place_dict)
        self.assertEqual(place_dict["dict_attr"], {"key": "value"})

    def test_to_dict_handles_float_attributes(self):
        self.place.float_attr = 10.11
        place_dict = self.place.to_dict()
        self.assertIn("float_attr", place_dict)
        self.assertEqual(place_dict["float_attr"], 10.11)

    def test_to_dict_handles_none_attributes(self):
        self.place.none_attr = None
        place_dict = self.place.to_dict()
        self.assertIn("none_attr", place_dict)
        self.assertEqual(place_dict["none_attr"], None)

    def test_to_dict_with_arg(self):
        """Tests to_dict method with an argument"""
        with self.assertRaises(TypeError):
            self.place.to_dict(12)

if __name__ == "__main__":  
    unittest.main()
