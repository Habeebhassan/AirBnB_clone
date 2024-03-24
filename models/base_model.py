#!/usr/bin/python3
"""
Module: base.py

This module defines the base class `BaseModel`, which serves as the foundation
for other classes in the application. It provides common attributes and methods
that are inherited by subclasses.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    This Base class states all common
    methods and attributes for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an object with its attributes.

        Parameters:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        If keyword arguments are provided (`kwargs`), it initializes the object
        with the values provided. If not, it generates a new unique identifier
        (`id`) and sets the creation and update times (`created_at` and
        `updated_at`) to the current time. Additionally, it registers the new
        instance with the storage system.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the instance.

        Returns:
            str: A string containing the class name, instance id, and its
            attributes.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the public instance attribute `updated_at` with the current
        datetime and saves the changes to the storage system.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
            dict: A dictionary containing all keys/values of the instance's
            attributes. Additionally, it includes the class name and formatted
            creation/update times.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict

