#!/usr/bin/python3
"""
Module: user.py

This module defines the `User` class, which represents a user within
the application. It subclasses the `BaseModel` class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user in the application.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
