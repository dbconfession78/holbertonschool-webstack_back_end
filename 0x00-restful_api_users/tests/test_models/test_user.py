#!/usr/bin/python3
"""
Module: contains tests for the User class
"""
from datetime import datetime
import hashlib
import inspect
from models.base_model import BaseModel
from models.user import User
from models import user
import unittest


class ModelTests(unittest.TestCase):
    """ tests for the User  class """
    def setUp(self):
        """ setup tests """
        self.model = User()
        self.module = user

    def test_module_doc(self):
        """ test module has doc """
        self.assertGreater(len(self.module.__doc__), 0)

    def test_class_doc(self):
        """ test class for doc """
        self.assertGreater(len(self.model.__doc__), 0)

    def test_function_docs(self):
        """ test class methods for doc """
        attr_list = inspect.getmembers(self.model)
        for attr in attr_list:
            attr_type = type(attr[1]).__name__
            if type(attr_type) == "method":
                self.assertGreater(len(attr[1].__doc__, 0))

    def test_model(self):
        """ test User """
        self.assertIsNotNone(self.model)
        self.assertIsInstance(self.model, BaseModel)

    def test_id(self):
        """ test id """
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """ test created_at """
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """ test created_at """
        self.assertIsNotNone(self.model.created_at)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_display_name(self):
        """ test display_name() """
        self.assertEqual(self.model.display_name(), "")
        self.model.email = "hbtn@holbertonschool.com"
        self.assertEqual(self.model.display_name(), "hbtn@holbertonschool.com")
        self.model.first_name = "Bob"
        self.assertEqual(self.model.display_name(), "Bob")
        self.model.last_name = "Dylan"
        self.assertEqual(self.model.display_name(), "Bob Dylan")

    def test_str_email(self):
        """ test with valid email """
        self.model.email = "hbtn@holbertonschool.com"
        self.assertEqual(self.model.__str__(), "[User] " +
                         self.model.id +
                         " - hbtn@holbertonschool.com - " +
                         "hbtn@holbertonschool.com")

    def test_str_first_name(self):
        """ test with first name only """
        self.model.first_name = "Bob"
        self.assertEqual(self.model.__str__(), "[User] " +
                         self.model.id +
                         " - None - Bob")

    def test_str_last_name(self):
        """ test with last name only """
        self.model.last_name = "Dylan"
        self.assertEqual(self.model.__str__(), "[User] " +
                         self.model.id +
                         " - None - Dylan")

    def test_str_format(self):
        """ test with first and last name, and email """
        self.model.first_name = "Bob"
        self.model.last_name = "Dylan"
        self.model.email = "hbtn@holbertonschool.com"
        self.assertEqual(self.model.__str__(), "[User] " +
                         self.model.id +
                         " - hbtn@holbertonschool.com - Bob Dylan")

    def test_password_set(self):
        """ test password set and get """
        self.model.password = "my_password"
        expect = hashlib.md5(bytes("my_password".encode("utf8"))).hexdigest()
        self.assertEqual(self.model.password, expect)

    def test_is_valid_password(self):
        """ test password validity checker """
        pw = "my_password"
        self.model.password = pw
        self.assertEqual(self.model.is_valid_password(pw), True)
        self.assertEqual(self.model.is_valid_password("my_passw0rd"), False)


if __name__ == "__main__":
    unittest.main()
