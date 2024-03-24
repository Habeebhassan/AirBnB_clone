#!/usr/bin/python3
"""
Module: __init__.py

This module initializes the storage system for the application.
"""

from models.engine import file_storage

# Initialize file storage
storage = file_storage.FileStorage()
storage.reload()
