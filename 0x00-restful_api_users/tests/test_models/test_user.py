#!/usr/bin/python3
"""
Module: contains tests for the User class
"""
from datetime import datetime
import hashlib
import inspect
from models.base_model import BaseModel
from models.user import User
import models
import unittest


class ModelTests(unittest.TestCase):
    """ tests for the User  class """
    def setUp(self):
        """ setup tests """
        self.model = User()

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
        """ tests display_name() when first_name and last_name are not None """
        self.model.first_name = "Bob"
        self.model.last_name = "Dylan"
        self.assertEqual(self.model.display_name(), "Bob Dylan")

    def test_display_name_all_None(self):
        """ tests display_name() when all attributes are None """
        self.assertEqual(self.model.display_name(), "")

    def test_display_name_first_last_None(self):
        """ tests display_name() when first_name and last_name are None """
        self.model.email = "hbtn@holbertonschool.com"
        self.assertEqual(self.model.display_name(), "hbtn@holbertonschool.com")

    def test_display_last_None(self):
        """ tests display_name() when last name is None """
        self.model.first_name = "Bob"
        self.assertEqual(self.model.display_name(), "Bob")

    def test_display_name_first_None(self):
        """ tests display_name() when first_name is None """
        self.model.last_name = "Dylan"
        self.assertEqual(self.model.display_name(), "Dylan")

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

    def test_is_valid_password_true(self):
        """ test a valid password """
        pw = "my_password"
        self.model.password = pw
        self.assertEqual(self.model.is_valid_password(pw), True)

    def test_is_valid_password_false(self):
        """ test an invalid password """
        pw = "my_password"
        self.model.password = pw
        self.assertEqual(self.model.is_valid_password("my_passw0rd"), False)

    def test_is_valid_password_none_param(self):
        """ test None pwd """
        pw = "my_password"
        self.model.password = pw
        self.assertEqual(self.model.is_valid_password(None), False)

    def test_is_valid_password_none_self(self):
        """ test None self._password """
        pw = None
        self.model.password = pw
        self.assertEqual(self.model.is_valid_password("my_password"), False)

    def test_to_dict(self):
        """ test to_dict class method """
        str_format = "%Y-%m-%d %H:%M:%S"
        expected = {"id": self.model.id,
                    "email": "hbtn@holbertonschool.com",
                    "first_name": "Bob",
                    "last_name": "Dylan",
                    "created_at": self.model.created_at.strftime(str_format),
                    "updated_at": self.model.updated_at.strftime(str_format)}
        self.model.first_name = "Bob"
        self.model.last_name = "Dylan"
        self.model.email = "hbtn@holbertonschool.com"
        self.assertEqual(expected, self.model.to_dict())


if __name__ == "__main__":
    unittest.main()
