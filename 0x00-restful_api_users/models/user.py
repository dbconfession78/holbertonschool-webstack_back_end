#!/usr/bin/python3
"""
Module: contains User class definition
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User class definition """
    email = None
    first_name = None
    last_name = None
    _password = None

    def display_name(self):
        """ displays User attritbues as a string """
        if self.email == self.first_name == self.last_name is None:
            return ""
        if (self.first_name is None and self.last_name is None and self.email):
            return self.email
        if (self.last_name is None and self.first_name):
            return self.first_name
        if (self.first_name is None and self.last_name):
            return self.last_name
        return "{} {}".format(self.first_name, self.last_name)
