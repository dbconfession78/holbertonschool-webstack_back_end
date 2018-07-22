#!/usr/bin/python3
"""
Module: contains tests for the BaseModel class
"""
from datetime import datetime
import inspect
from models.base_model import BaseModel
from models import base_model as module
import unittest
import uuid


class ModelTests(unittest.TestCase):
    """ base model  tests """
    def setUp(self):
        """ testing stup """
        self.cls = BaseModel()
        self.module = module

    def test_module_doc(self):
        """ test module for doc """
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

    def test_base_model(self):
        """ test class """
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

if __name__ == "__main__":
    unittest.main()
