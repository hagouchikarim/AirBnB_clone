#!/usr/bin/python3
"""Module for File Storage"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """It handles serialization and deserialization of the instances"""
    __file_path = "json file"
    __objects = {}
    
    def all(self):
        """It returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """it sets in __objects the obj with key <obj class name>.id"""
        id = obj.to_dict()["id"]
        _ClassName = obj.to_dict()["__class__"]
        _KeyName = _ClassName+"."+id
        FileStorage.__objects[_KeyName] = obj
    
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)
    def reload(self):
        """It deserializes the JSON file to __objects if the file exists."""
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = {}
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    # Instantiate object based on class name and ID
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except Exception:
            pass