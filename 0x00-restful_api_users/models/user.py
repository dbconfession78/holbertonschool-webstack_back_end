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
