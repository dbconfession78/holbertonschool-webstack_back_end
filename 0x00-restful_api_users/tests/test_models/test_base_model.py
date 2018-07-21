#!/usr/bin/python3
"""
Module: contains tests for the BaseModel class
"""
from datetime import datetime
from models.base_model import BaseModel
import unittest
import uuid


class TestBaseModel(unittest.TestCase):
    """ tests for the BaseModel class """
    def setUp(self):
        """ setup tests """
        self.bm = BaseModel()

    def test_base_model(self):
        """ test base_model """
        self.assertIsNotNone(self.bm)
        self.assertIsInstance(self.bm, BaseModel)

    def test_id(self):
        """ test id """
        self.assertIsNotNone(self.bm.id)
        self.assertIsInstance(self.bm.id, str)

    def test_created_at(self):
        """ test created_at """
        self.assertIsNotNone(self.bm.created_at)
        self.assertIsInstance(self.bm.created_at, datetime)

    def test_updated_at(self):
        """ test created_at """
        self.assertIsNotNone(self.bm.created_at)
        self.assertIsInstance(self.bm.updated_at, datetime)
        self.assertEqual(self.bm.created_at, self.bm.updated_at)

if __name__ == "__main__":
    unittest.main()
