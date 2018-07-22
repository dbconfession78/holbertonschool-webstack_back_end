#!/usr/bin/python3
"""
Module: contains User class definition
"""
from models.base_model import BaseModel
import hashlib


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
        if self.email and (self.first_name == self.last_name is None):
            return self.email
        if self.first_name and self.last_name is None:
            return self.first_name
        if self.last_name and self.first_name is None:
            return self.last_name
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        """ displays the User object as a string """
        return "[{}] {} - {} - {}".format(
            self.__class__.__name__,
            self.id,
            self.email,
            self.display_name())

    @property
    def password(self):
        """ password getter """
        return self._password

    @password.setter
    def password(self, pw):
        """ password setter """
        if pw is None or type(pw) is not str:
            self._password = None
        else:
            b = bytes(pw.encode("utf-8"))
            m = hashlib.md5(b).hexdigest()
            self._password = m
