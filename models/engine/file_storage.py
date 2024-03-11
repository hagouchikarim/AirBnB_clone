#!/usr/bin/python3
"""Module for File Storage"""

import json
import os

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Handles serialization and deserialization of instances"""
    FILE_PATH = "storage_file.json"
    objects = {}

    def __init__(self):
        if not hasattr(self, '__file_path'):
            self.__file_path = FileStorage.FILE_PATH
        if not hasattr(self, '__objects'):
            self.__objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets in objects the obj with key <obj class name>.id"""
        if obj is None:
            raise TypeError('obj must not be None')
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to the JSON file (path: FILE_PATH)"""
        if self.__file_path is None:
            raise ValueError('__file_path must not be None')
        if self.__objects is None:
            raise ValueError('__objects must not be None')
        file_path = self.__file_path
        data = dict(self.__objects)
        for key, value in data.items():
            if value is None:
                raise ValueError(f'{key} must not be None')
            data[key] = value.to_dict()
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f)
        except (FileNotFoundError, TypeError, OSError) as e:
            raise e

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if self.__file_path is None:
            raise ValueError('__file_path must not be None')
        if self.__objects is None:
            raise ValueError('__objects must not be None')
        _pFile = self.__file_path
        iData = self.__objects
        try:
            with open(_pFile) as f:
                for key, value in json.load(f).items():
                    if "BaseModel" in key:
                        iData[key] = BaseModel(**value)
                    if "User" in key:
                        iData[key] = User(**value)
                    if "Place" in key:
                        iData[key] = Place(**value)
                    if "State" in key:
                        iData[key] = State(**value)
                    if "City" in key:
                        iData[key] = City(**value)
                    if "Amenity" in key:
                        iData[key] = Amenity(**value)
                    if "Review" in key:
                        iData[key] = Review(**value)
        except FileNotFoundError as e:
            pass
        except (TypeError, json.JSONDecodeError, OSError) as e:
            raise e

