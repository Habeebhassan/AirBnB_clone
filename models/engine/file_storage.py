#!/usr/bin/python3
"""
Module: file_storage.py

Defines a `FileStorage` class for serializing instances to a JSON file and deserializing
JSON file to instances.
"""

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """
    A class for serializing instances to a JSON file and deserializing JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all stored objects.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the storage.

        Args:
            obj: The object to be added to the storage.
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize the objects to a JSON file.
        """
        serialized_objects = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserialize the JSON file and load objects into storage.
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as f:
            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                return

            self.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}

