#!/usr/bin/python3
"""Initialize package to create a unique FileStorage instance for the application"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
