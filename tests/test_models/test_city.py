#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from models import storage
from time import sleep
FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class TestCityInit(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.city.name = ""
        self.city.state_id = ""


    def test_init(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
    def test_inheritance(self):
        self.assertTrue(issubclass(City, BaseModel))
    def test_id_is_string(self):
        self.assertIsInstance(self.city.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.city.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.city.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.city.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_state_id_attribute(self):
        self.assertTrue("state_id" in self.city.__dict__)
        self.assertIsInstance(self.city.state_id, str)

    def test_name_attribute(self):
        self.assertTrue("name" in self.city.__dict__)
        self.assertIsInstance(self.city.name, str)
class TestCityInheritedInit(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.city1 = City()
        self.city2 = City()

    def test_init(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_id_is_string(self):
        self.assertIsInstance(self.city.id, str)

    def test_id_not_empty(self):
        self.assertNotEqual(self.city.id, "")

    def test_created_at_not_none(self):
        self.assertIsNotNone(self.city.created_at)

    def test_updated_at_not_none(self):
        self.assertIsNotNone(self.city.updated_at)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.city.created_at, datetime)

    def test_city_instantiates_with_kwargs(self):
        city = City(name="Test", value=42)
        self.assertEqual(city.name, "Test")
        self.assertEqual(city.value, 42)


    def test_two_cities_different_created_at(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)


    def test_two_cities_different_updated_at(self):
        sleep(0.05)
        self.assertLess(self.city1.updated_at, self.city2.updated_at)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.city1.updated_at, datetime)
    
    def test_id_is_unique(self):
        self.assertNotEqual(self.city1.id, self.city2.id)

    def test_city_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_city_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_city_instantiates_without_args(self):
        self.assertEqual(City, type(City()))

    def test_new_city_instance_in_objects(self):
        self.assertIn(City(), storage.all().values())

    def test_city_id_is_public_str(self):
        self.assertEqual(str, type(City().id))
class TestCityStr(unittest.TestCase):
    
    def setUp(self):
        self.city = City()

    def test_str(self):
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_str_format(self):
        expected_str_format = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str_format)
class TestCitySave(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_save(self):
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)

    def test_save_does_not_change_created_at(self):
        old_created_at = self.city.created_at
        self.city.save()
        self.assertEqual(self.city.created_at, old_created_at)

    def test_save_changes_updated_at(self):
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)

    def test_save_updates_updated_at(self):
        updated_at_before_save = self.city.updated_at
        self.city.save()
        updated_at_after_save = self.city.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)

    def test_save_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(12)
class TestCityToDict(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.city.new_attr = "new attribute value"
        self.city.int_attr = 66

    def test_to_dict(self):
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["created_at"], self.city.created_at.strftime(FORMAT))
        self.assertEqual(city_dict["updated_at"], self.city.updated_at.strftime(FORMAT))

    def test_to_dict_returns_dict(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        city_dict = self.city.to_dict()
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)

    def test_to_dict_formats_dates(self):
        city_dict = self.city.to_dict()
        created_at = datetime.strptime(city_dict["created_at"], FORMAT)
        updated_at = datetime.strptime(city_dict["updated_at"], FORMAT)
        self.assertEqual(created_at, self.city.created_at)
        self.assertEqual(updated_at, self.city.updated_at)

    def test_to_dict_includes_all_attributes(self):
        city_dict = self.city.to_dict()
        self.assertIn("new_attr", city_dict)
        self.assertEqual(city_dict["new_attr"], "new attribute value")

    def test_to_dict_handles_non_string_attributes(self):
        self.city.int_attr = 66
        city_dict = self.city.to_dict()
        self.assertIn("int_attr", city_dict)
        self.assertEqual(city_dict["int_attr"], 66)

    def test_to_dict_handles_boolean_attributes(self):
        self.city.bool_attr = True
        city_dict = self.city.to_dict()
        self.assertIn("bool_attr", city_dict)
        self.assertEqual(city_dict["bool_attr"], True)

    def test_to_dict_handles_list_attributes(self):
        self.city.list_attr = [1, 2, 3]
        city_dict = self.city.to_dict()
        self.assertIn("list_attr", city_dict)
        self.assertEqual(city_dict["list_attr"], [1, 2, 3])

    def test_to_dict_handles_tuple_attributes(self):
        self.city.tuple_attr = (4, 5, 6)
        city_dict = self.city.to_dict()
        self.assertIn("tuple_attr", city_dict)
        self.assertEqual(city_dict["tuple_attr"], (4, 5, 6))



    def test_to_dict_handles_dict_attributes(self):
        self.city.dict_attr = {"key": "value"}
        city_dict = self.city.to_dict()
        self.assertIn("dict_attr", city_dict)
        self.assertEqual(city_dict["dict_attr"], {"key": "value"})

    def test_to_dict_handles_float_attributes(self):
        self.city.float_attr = 10.11
        city_dict = self.city.to_dict()
        self.assertIn("float_attr", city_dict)
        self.assertEqual(city_dict["float_attr"], 10.11)

    def test_to_dict_handles_none_attributes(self):
        self.city.none_attr = None
        city_dict = self.city.to_dict()
        self.assertIn("none_attr", city_dict)
        self.assertEqual(city_dict["none_attr"], None)

    def test_to_dict_with_arg(self):
        """Tests to_dict method with an argument"""
        with self.assertRaises(TypeError):
            self.city.to_dict(12)

if __name__ == "__main__":
    unittest.main()