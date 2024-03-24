#!/usr/bin/python3
"""
Module: state.py

This module defines the `State` class, which represents a state within
the application. It subclasses the `BaseModel` class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state in the application.

    Attributes:
        name (str): The name of the state.
    """

    name: str = ""
