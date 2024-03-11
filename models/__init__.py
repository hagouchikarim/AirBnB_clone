#!/usr/bin/python3
""" A reload of storage """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
