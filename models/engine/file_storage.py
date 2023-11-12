#!/usr/bin/python3
import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

"""
The FileStorage class serializes instances to
 a JSON file and deserializes JSON file to instances.

Attributes:
    __file_path (str): The path to the JSON file.
    __objects (dict): A dictionary of all objects,
      where the key is the class name and id, and the value is the object.

Methods:
    all(): Returns all objects stored in the file storage.
    new(obj): Adds a new object to the file storage.
    save(): Saves all objects in the file storage to the JSON file.
    reload(): Loads all objects from the JSON file to the file storage.
"""


class FileStorage:
    """
    This class handles the storage of objects to a JSON
      file and loading of objects from the JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all objects stored in the file storage.

        Returns:
            dict: A dictionary of all objects, where the key is the
              class name and id, and the value is the object.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the file storage.

        Args:
            obj (BaseModel): The object to add to the file storage.
        """

        class_name = obj.__class__.__name__
        id = obj.id
        self.__objects["{}.{}".format(class_name, id)] = obj

    def save(self):
        """
        Saves all objects in the file storage to the JSON file.
        """
        obj = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(obj, file)

    def reload(self):
        """
        Loads all objects from the JSON file to the file storage.
        """
        try:
            with open(self.__file_path, "r") as file:
                obj = json.load(file)
                for v in obj.values():
                    self.new(eval(v["__class__"])(**v))
        except FileNotFoundError:
            pass
