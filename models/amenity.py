#!/usr/bin/python3
"""
Module: amenity.py

This module defines the `Amenity` class, which represents an amenity within
the application. It subclasses the `BaseModel` class.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity provided for a place/house.

    Attributes:
        name (str): The name of the amenity.
    """

    name: str = ""
