#!/usr/bin/python3
"""This is an Unit test for State """
import unittest
from models.state import State
from datetime import datetime


class StateTestCase(unittest.TestCase):
    """This is a  Class for testing the State class """

    def test_state_attributes_existence(self):
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

    def test_state_attribute_types(self):
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)
        self.assertIsInstance(state.name, str)

    def test_state_initialization(self):
        state = State()
        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)
        self.assertEqual(state.name, "")

    def test_state_to_dict_method(self):
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_state_string_representation(self):
        state = State()
        string_repr = str(state)
        self.assertIn("[State]", string_repr)
        self.assertIn("'id':", string_repr)
        self.assertIn("'created_at':", string_repr)
        self.assertIn("'updated_at':", string_repr)
        self.assertIn("'name':", string_repr)


if __name__ == '__main__':
    unittest.main()
