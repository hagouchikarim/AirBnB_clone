#!/usr/bin/python3
""" This is an unit test for review """
import unittest
from models.review import Review
from datetime import datetime


class ReviewTestCase(unittest.TestCase):
    """this is a class reviewtestcase"""
    def test_attributes_existence(self):
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_attribute_types(self):
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_initialization(self):
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_custom_initialization(self):
        review = Review(text="Wonderful Place", user_id="12", place_id="46")
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        self.assertEqual(review.place_id, "46")
        self.assertEqual(review.user_id, "13")
        self.assertEqual(review.text, "Wonderful place")

    def test_to_dict_method(self):
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

    def test_string_representation(self):
        review = Review()
        string_repr = str(review)
        self.assertIn("[Review]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)
        self.assertIn("'place_id':", string_repr)
        self.assertIn("'user_id':", string_repr)
        self.assertIn("'text':", string_repr)


if __name__ == '__main__':
    unittest.main()
