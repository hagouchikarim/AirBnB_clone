#!/usr/bin/python3
""" This is an unit test for Amenity """
import unittest
from models.amenity import Amenity
from datetime import datetime


class AmenityTestCase(unittest.TestCase):
    """ This is a class for amenity test """

    def test_amenity_attributes_existence(self):
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_attribute_types(self):
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.name, str)

    def test_amenity_initialization(self):
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)
        self.assertEqual(amenity.name, "") 

    def test_amenity_to_dict_method(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_amenity_string_representation(self):
        amenity = Amenity()
        string_repr = str(amenity)
        self.assertIn("[Amenity]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)
        self.assertIn("'name':", string_repr)


if __name__ == '__main__':
    unittest.main()
