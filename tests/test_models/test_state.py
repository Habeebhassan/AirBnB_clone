#!/usr/bin/python3
"""Unit tests for the `State` module."""

import os
import unittest
from datetime import datetime
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage as model_storage


class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for checking class attributes"""
        state1 = State()
        state3 = State("hello", "wait", "in")
        key = f"{type(state1).__name__}.{state1.id}"

        # Test if attributes are correctly initialized
        self.assertIsInstance(state1.name, str)
        self.assertEqual(state3.name, "")

        # Test modification of attributes
        state1.name = "Chicago"
        self.assertEqual(state1.name, "Chicago")
        self.assertIn(key, model_storage.all())

    def test_init(self):
        """Test method for checking public instances"""
        state1 = State()
        state2 = State(**state1.to_dict())

        # Test if instances are correctly initialized
        self.assertIsInstance(state1.id, str)
        self.assertIsInstance(state1.created_at, datetime)
        self.assertIsInstance(state1.updated_at, datetime)
        self.assertEqual(state1.updated_at, state2.updated_at)

    def test_str(self):
        """Test method for checking string representation"""
        state1 = State()
        string = f"[{type(state1).__name__}] ({state1.id}) {state1.__dict__}"
        self.assertEqual(state1.__str__(), string)

    def test_save(self):
        """Test method for checking save"""
        state1 = State()
        old_update = state1.updated_at
        state1.save()
        self.assertNotEqual(state1.updated_at, old_update)

    def test_todict(self):
        """Test method for checking dictionary"""
        state1 = State()
        state2 = State(**state1.to_dict())
        a_dict = state2.to_dict()

        # Test if object can be converted to dictionary and back
        self.assertIsInstance(a_dict, dict)
        self.assertEqual(a_dict['__class__'], type(state2).__name__)
        self.assertIn('created_at', a_dict.keys())
        self.assertIn('updated_at', a_dict.keys())
        self.assertNotEqual(state1, state2)


if __name__ == "__main__":
    unittest.main()
