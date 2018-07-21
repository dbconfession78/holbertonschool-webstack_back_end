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
        if (not self.email and not self.first_name and not self.last_name):
            return ""
        if (not self.first_name and not self.last_name and self.email):
            return self.email
        if (not self.last_name and self.first_name):
            return self.first_name
        if (not self.first_name and self.last_name):
            return self.last_name
        return "{} {}".format(self.first_name, self.last_name)


if __name__ == "__main__":
    u = User()
    print(u.display_name())
    input()

    u.email = "hbtn@holbertonschool.com"
    print(u.display_name())
    input()

    u.last_name = "Dylan"
    print(u.display_name())
