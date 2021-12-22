#!/usr/bin/python3
# serializes instances to a JSON file and deserializes
# JSON file to instances.

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Serializes instances to a JSON and deserializes JSON instances"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initializes the class FileStorage"""
        pass

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            dictionary = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    dictionary[key] = value
            return dictionary
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __object to JSON file"""
        obj_dict = {
            key: value.to_dict()
            for key, value in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                obj_dict = json.load(json_file)
                for obj_str in obj_dict.values():
                    cls = eval(obj_str["__class__"])
                    new_object = cls(**obj_str)
                    self.new(new_object)

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it's inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
