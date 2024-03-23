#!/usr/bin/python3

""" A class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances:"""

import json
from os import path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class Filestorage:
    """
    A class that uses the following  private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id
    (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)"""

    classes = {
            "BaseModel": BaseModel, "User": User, "Place": Place, "State": State, "City": City, "Amenity": Amenity, "Review": Review
    }

    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # dictionary to store all objects by <class name>.id

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file does not exist, no exception should be raised.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                serialized_objects = json.load(file)
                for key, obj_data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    # Dynamically create an instance of
                    # the class based on class_name
                    obj_class = globals()[class_name]
                    obj_instance = obj_class(**obj_data)
                    # Store the instance in __objects
                    self.__objects[key] = obj_instance