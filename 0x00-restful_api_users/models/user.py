#!/usr/bin/python3
from models.base_model import BaseModel
"""
Module: contains user class definition
"""


class User(BaseModel):
    """ User class definition """
    email = None
    first_name = None
    last_name = None
    _password = None

    def display_name(self):
        if self.email == self.first_name == self.last_name is None:
            return ""
        if (self.first_name is None and self.last_name is None and self.email):
            return self.email
        if (self.last_name is None and self.first_name):
            return self.first_name
        if (self.first_name is None and self.last_name):
            return self.last_name
        return "{} {}".format(self.first_name, self.last_name)
