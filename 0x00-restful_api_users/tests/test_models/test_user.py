#!/usr/bin/python3
"""
Module: contains tests for the User class
"""
import inspect
from models.base_model import BaseModel
from models.user import User
from models import user
import unittest


class ModelTests(unittest.TestCase):
    """ tests for the User  class """
    def setUp(self):
        """ setup tests """
        self.cls = User()
        self.module = user

    def test_module_doc(self):
        """ test module has doc """
        self.assertGreater(len(self.module.__doc__), 0)

    def test_class_doc(self):
        """ test class for doc """
        self.assertGreater(len(self.cls.__doc__), 0)

    def test_function_docs(self):
        """ test class methods for doc """
        attr_list = inspect.getmembers(self.cls)
        for attr in attr_list:
            attr_type = type(attr[1]).__name__
            if type(attr_type) == "method":
                self.assertGreater(len(attr[1].__doc__, 0))

    def test_model(self):
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
