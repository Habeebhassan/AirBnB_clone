#!/usr/bin/python3
"""
Module: review.py

This module defines the `Review` class, which represents a review within
the application. It subclasses the `BaseModel` class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review in the application.

    Attributes:
        text (str): The content of the review.
        user_id (str): The ID of the user who posted the review.
        place_id (str): The ID of the place/house being reviewed.
    """

    text: str = ""
    user_id: str = ""
    place_id: str = ""
