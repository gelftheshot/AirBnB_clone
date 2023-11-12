#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models import storage

import os


class BaseModelTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        try:
            os.rename("file.json", "tmp_file.json")
        except IOError:
            pass

    @classmethod
    def tearDownClass(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp_file.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}


class TestFileStorage_init(BaseModelTest):

    def setUp(self):
        self.storage = FileStorage()

    def test_init(self):
        self.assertIsInstance(self.storage, FileStorage)

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_file_path_is_private_str(self):
        self.assertEqual(str, type(self.storage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        self.assertEqual(dict, type(self.storage._FileStorage__objects))
    
    def test_file_storge_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
    def test_storage_initializes(self):
        self.assertEqual(type(storage), FileStorage)

class TestFileStorage_new(BaseModelTest):

    def setUp(self):
        self.storage = FileStorage()
        self.obj = BaseModel()

    def test_new(self):
        self.storage.new(self.obj)
        self.assertIn(self.obj, self.storage.all().values())

    def test_base_model_new(self):
        base_model = BaseModel()
        self.storage.new(base_model)
        self.assertIn(self.obj, self.storage.all().values())
        self.assertIn("BaseModel." + base_model.id, storage.all().keys())

    def test_user_new(self):
        user = User()
        self.storage.new(user)
        self.assertIn(self.obj, self.storage.all().values())
        self.assertIn("User." + user.id, storage.all().keys())

    def test_state_new(self):
        state = State()
        self.storage.new(state)
        self.assertIn(self.obj, self.storage.all().values())
        self.assertIn("State." + state.id, storage.all().keys())

    def test_city_new(self):
        city = City()
        self.storage.new(city)
        self.assertIn(self.obj, self.storage.all().values())
        self.assertIn("City." + city.id, storage.all().keys())

    def test_place_new(self):
        place = Place()
        self.storage.new(place)
        self.assertIn(self.obj, self.storage.all().values())
        self.assertIn("Place." + place.id, storage.all().keys())

    def test_review_new(self):
        review = Review()
        self.storage.new(review)
        self.assertIn(self.obj, self.storage.all().values())
        self.assertIn("Review." + review.id, storage.all().keys())

    def test_amenity_new(self):
        amenity = Amenity()
        self.storage.new(amenity)
        self.assertIn(self.obj, self.storage.all().values())
        self.assertIn("Amenity." + amenity.id, storage.all().keys())

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            self.storage.new(None)
    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_new_with_no_args(self):
        with self.assertRaises(TypeError):
            self.storage.new()

    def test_new_with_two_args(self):
        with self.assertRaises(TypeError):
            self.storage.new(self.obj, None)

    def test_new_with_three_args(self):
        with self.assertRaises(TypeError):
            self.storage.new(self.obj, None, None)


class TestFileStorage_save(BaseModelTest):
    def setUp(self):
        self.storage = FileStorage()
        self.obj = FileStorage()



    def test_save_base_model(self):
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + base_model.id, f.read())

    def test_save_user(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("User." + user.id, f.read())

    def test_save_state(self):
        state = State()
        self.storage.new(state)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("State." + state.id, f.read())

    def test_save_city(self):
        city = City()
        self.storage.new(city)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("City." + city.id, f.read())

    def test_save_place(self):
        place = Place()
        self.storage.new(place)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("Place." + place.id, f.read())

    def test_save_review(self):
        review = Review()
        self.storage.new(review)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("Review." + review.id, f.read())

    def test_save_amenity(self):
        amenity = Amenity()
        self.storage.new(amenity)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("Amenity." + amenity.id, f.read())

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_save_with_two_args(self):
        with self.assertRaises(TypeError):
            self.storage.save(self.obj, None)

    def test_save_with_three_args(self):
        with self.assertRaises(TypeError):
            self.storage.save(self.obj, None, None)


class TestFileStorage_reload(BaseModelTest):

    def test_reaload(self):
        base_model = BaseModel()
        user = User()
        state = State()
        city = City()
        place = Place()
        review = Review()
        amenity = Amenity()
        obj = [base_model, user, state, city, place, review, amenity]
        for o in obj:
            storage.new(o)
        storage.save()
        storage.reload()
        dic = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, dic)
        self.assertIn("User." + user.id, dic)
        self.assertIn("State." + state.id, dic)
        self.assertIn("City." + city.id, dic)
        self.assertIn("Place." + place.id, dic)
        self.assertIn("Review." + review.id, dic)
        self.assertIn("Amenity." + amenity.id, dic)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_reload_no_file(self):
        os.remove("file.json")
        with self.assertRaises(FileNotFoundError):
            storage.reload()
        

if __name__ == "__main__":
    unittest.main()