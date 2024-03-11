#!/usr/bin/python3
"""This Is An Unit test for BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys
from unittest.mock import patch
import json

captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """ This a Class for testing the BaseModel class """

    def setUp(self):
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        iNew = BaseModel()

        self.assertTrue(hasattr(iNew, "__init__"))
        self.assertTrue(hasattr(iNew, "__str__"))
        self.assertTrue(hasattr(iNew, "save"))
        self.assertTrue(hasattr(iNew, "to_dict"))

        self.assertTrue(hasattr(iNew, "id"))
        self.assertTrue(hasattr(iNew, "created_at"))
        self.assertTrue(hasattr(iNew, "updated_at"))

        self.assertIsInstance(iNew.id, str)
        self.assertIsInstance(iNew.created_at, datetime)
        self.assertIsInstance(iNew.updated_at, datetime)

        _ikeyName = "BaseModel."+iNew.id
        self.assertIn(_ikeyName, models.storage.all())
        self.assertTrue(models.storage.all()[_ikeyName] is iNew)

        iNew.name = "My First Model"
        iNew.my_number = 89
        self.assertTrue(hasattr(iNew, "name"))
        self.assertTrue(hasattr(iNew, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[_ikeyName], "name"))
        self.assertTrue(hasattr(models.storage.all()[_ikeyName], "my_number"))

        old_time = iNew.updated_at
        iNew.save()
        self.assertNotEqual(old_time, iNew.updated_at)
        self.assertGreater(iNew.updated_at, old_time)


        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        _ikeyName = "BaseModel."+iNew.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        try:
            self.assertIn(_ikeyName, saved_data)
        except AssertionError as e:
            print("Error: {}".format(e))
        try:
            self.assertEqual(saved_data[_ikeyName], iNew.to_dict())
        except KeyError as e:
            print("Error: {}".format(e))

    def test_basemodel_init2(self):
        iNew = BaseModel()
        iNew.name = "John"
        iNew.my_number = 89
        iNew2 = BaseModel(**iNew.to_dict())
        self.assertEqual(iNew.id, iNew2.id)
        self.assertEqual(iNew.name, "John")
        self.assertEqual(iNew.my_number, 89)
        self.assertEqual(iNew.to_dict(), iNew2.to_dict())

    def test_basemodel_init3(self):
        iNew = BaseModel()
        iNew2 = BaseModel(**iNew.to_dict())
        self.assertEqual(iNew.id, iNew2.id)
        self.assertEqual(iNew.__class__, iNew2.__class__)

        old_time = iNew.updated_at
        iNew.save()
        self.assertGreater(iNew.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
