#!/usr/bin/python3
"""
Module: contains tests for the User class
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest
from models.user import User
import uuid


class TestUser(unittest.TestCase):
    """ tests for the BaseModel class """
    def setUp(self):
        """ setup tests """
        self.cls = User()

    def test_base_model(self):
        """ test base_model """
        self.assertIsNotNone(self.cls)
        self.assertIsInstance(self.cls, BaseModel)

    def test_id(self):
        """ test id """
        self.assertIsNotNone(self.cls.id)
        self.assertIsInstance(self.cls.id, str)

    def test_created_at(self):
        """ test created_at """
        self.assertIsNotNone(self.cls.created_at)
        self.assertIsInstance(self.cls.created_at, datetime)

    def test_updated_at(self):
        """ test created_at """
        self.assertIsNotNone(self.cls.created_at)
        self.assertIsInstance(self.cls.updated_at, datetime)
        self.assertEqual(self.cls.created_at, self.cls.updated_at)

    def test_display_name(self):
        self.assertEqual(self.cls.display_name(), "")
        self.cls.email = "hbtn@holbertonschool.com"
        self.assertEqual(self.cls.display_name(), "hbtn@holbertonschool.com")
        self.cls.first_name = "Bob"
        self.assertEqual(self.cls.display_name(), "Bob")
        self.cls.last_name = "Dylan"
        self.assertEqual(self.cls.display_name(), "Bob Dylan")

if __name__ == "__main__":
    unittest.main()
