#!/usr/bin/python3
import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        class_name = obj.__class__.__name__
        id = obj.id
        self.__objects["{}.{}".format(class_name, id)] = obj

    def save(self):
        obj = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                obj = json.load(file)
                for v in obj.values():
                    self.new(eval(v["__class__"])(**v))
        except FileNotFoundError:
            pass
