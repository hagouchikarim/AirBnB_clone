#!/usr/bin/python3
"""This is an  Unit test for User """
import unittest
from models.user import User
from datetime import datetime


class UserTestCase(unittest.TestCase):
    """This is a Class for testing the User class """

    def test_user_attributes_existence(self):
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_attribute_types(self):
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_initialization(self):
        user = User()
        self.assertIsNotNone(user.id)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_to_dict_method(self):
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

    def test_user_string_representation(self):
        user = User()
        string_repr = str(user)
        self.assertIn("[User]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)
        self.assertIn("'email':", string_repr)
        self.assertIn("'password':", string_repr)
        self.assertIn("'first_name':", string_repr)
        self.assertIn("'last_name':", string_repr)


if __name__ == '__main__':
    unittest.main()
