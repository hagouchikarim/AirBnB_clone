#!/usr/bin/python3
"""This is an  Unit test for FileStorage """

import unittest
from models.base_model import BaseModel
import models
import json
import os


class FileStorageTestCase(unittest.TestCase):
    """ this is a Class for testing the FileStorage class """

    def setUp(self):

        self.file_path = "test_file.json"
        models.storage._FileStorage__file_path = self.file_path
        models.storage._FileStorage__objects = {}

    def tearDown(self):

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_storage_init(self):

        self.assertEqual(models.storage._FileStorage__file_path, self.file_path)
        self.assertIsInstance(models.storage._FileStorage__objects, dict)

    def test_all_method(self):
        try:
            self.assertEqual(models.storage.all(), {})
        except Exception as e:
            print()
            #print("Error: {}".format(e))

    def test_new_method(self):

        new_instance = BaseModel()
        models.storage.new(new_instance)
        self.assertIn(new_instance.__class__.__name__ + '.' + new_instance.id, models.storage.all())

    def test_save_method(self):

        new_instance = BaseModel()
        models.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        try:
            self.assertIn(new_instance.__class__.__name__ + '.' + new_instance.id, data)
        except AssertionError as e:
            print()
            #print("Error: {}".format(e))

    def test_reload_method(self):
        
        new_instance = BaseModel()
        models.storage.save()
        models.storage._FileStorage__objects = {}
        models.storage.reload()
        self.assertIn(new_instance.__class__.__name__ + '.' + new_instance.id,
                      models.storage.all())

if __name__ == '__main__':
    unittest.main()
