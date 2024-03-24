#!/usr/bin/python3
"""
Module: place.py

This module defines the `Place` class, which represents a place or house within
the application. It subclasses the `BaseModel` class.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place or house in the application.

    Attributes:
        name (str): The name of the place.
        user_id (str): The ID of the user who uploaded the place.
        city_id (str): The ID of the city where the place is located.
        description (str): Description of the place.
        number_bathrooms (int): The number of bathrooms in the place.
        price_by_night (int): The price per night for staying at the place.
        number_rooms (int): The number of rooms in the place.
        longitude (float): The longitude coordinate of the place.
        latitude (float): The latitude coordinate of the place.
        max_guest (int): The maximum number of guests allowed in the place.
        amenity_ids (list): List of facility IDs available in the place.
    """

    name: str = ""
    user_id: str = ""
    city_id: str = ""
    description: str = ""
    number_bathrooms: int = 0
    price_by_night: int = 0
    number_rooms: int = 0
    longitude: float = 0.0
    latitude: float = 0.0
    max_guest: int = 0
    amenity_ids: list = []
