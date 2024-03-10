#!/usr/bin/python3
""" This is an unit test for City """
import unittest
from models.city import City
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ This is a class for testing the City class """

    def test_city_attributes_existence(self):
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))

    def test_city_attribute_types(self):
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_initialization(self):
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_to_dict_method(self):
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_city_string_representation(self):
        city = City()
        string_repr = str(city)
        self.assertIn("[City]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)
        self.assertIn("'state_id':", string_repr)
        self.assertIn("'name':", string_repr)


if __name__ == '__main__':
    unittest.main()
