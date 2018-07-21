#!/usr/bin/python3
"""
Module: contains tests for the User class
"""
from models.base_model import BaseModel
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ tests for the User  class """
    def setUp(self):
        """ setup tests """
        self.cls = User()

    def test_user_model(self):
        """ test User """
        self.assertIsNotNone(self.cls)
        self.assertIsInstance(self.cls, BaseModel)

    def test_display_name(self):
        """ test display_name() """
        self.assertEqual(self.cls.display_name(), "")
        self.cls.email = "hbtn@holbertonschool.com"
        self.assertEqual(self.cls.display_name(), "hbtn@holbertonschool.com")
        self.cls.first_name = "Bob"
        self.assertEqual(self.cls.display_name(), "Bob")
        self.cls.last_name = "Dylan"
        self.assertEqual(self.cls.display_name(), "Bob Dylan")

if __name__ == "__main__":
    unittest.main()
