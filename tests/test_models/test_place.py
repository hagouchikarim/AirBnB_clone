#!/usr/bin/python3
"""This an unit test for place"""
import unittest
from models.place import Place
from datetime import datetime


class PlaceTestCase(unittest.TestCase):

    def test_place_attributes_existence(self):
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_place_attribute_types(self):
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_initialization(self):
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_to_dict_method(self):
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_place_string_representation(self):
        place = Place()
        string_repr = str(place)
        self.assertIn("[Place]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)
        self.assertIn("'city_id':", string_repr)
        self.assertIn("'user_id':", string_repr)
        self.assertIn("'name':", string_repr)
        self.assertIn("'description':", string_repr)
        self.assertIn("'number_rooms':", string_repr)
        self.assertIn("'number_bathrooms':", string_repr)
        self.assertIn("'max_guest':", string_repr)
        self.assertIn("'price_by_night':", string_repr)
        self.assertIn("'latitude':", string_repr)
        self.assertIn("'longitude':", string_repr)
        self.assertIn("'amenity_ids':", string_repr)


if __name__ == '__main__':
    unittest.main()
