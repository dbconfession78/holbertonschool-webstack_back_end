#!/usr/bin/python3
"""
Module: contains User class definition
"""
from models.base_model import BaseModel
import hashlib
import inspect
from datetime import datetime


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

    def is_valid_password(self, pwd):
        """ checks for valid password """
        if pwd is None or type(pwd) is not str or self._password is None:
            return False
        return hashlib.md5(bytes(pwd.encode(
            "utf8"))).hexdigest() == self._password

    def to_dict(self):
        """ returns a serializable representation of a User instance """
        retval = {}
        for k, v in self.__dict__.items():
            if k != "_password":
                if type(v).__name__ == datetime.__name__:
                    retval[k] = v.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    retval[k] = str(v)
        return retval
