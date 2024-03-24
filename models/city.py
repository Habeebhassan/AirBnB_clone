#!/usr/bin/python3
"""
Module: city.py

This module defines the `City` class, which represents a city within the
application. It subclasses the `BaseModel` class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city in the application.

    Attributes:
        name (str): The name of the city.
        state_id (str): The ID of the state to which the city belongs.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a City instance.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.

        Attributes:
            name (str): The name of the city.
            state_id (str): The ID of the state to which the city belongs.
        """
        super().__init__(*args, **kwargs)
        self.name = ""
        self.state_id = ""

