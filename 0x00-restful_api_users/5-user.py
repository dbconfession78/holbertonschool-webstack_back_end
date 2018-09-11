#!/usr/bin/python3
"""
Test is_valid_password(pwd) on User instance
"""
from models.user import User

user = User()
user.email = "hbtn@holbertonschool.com"
user.password = "toto1234"

print(user.is_valid_password(None))
print(user.is_valid_password(89))
print(user.is_valid_password("tutu1234"))
print(user.is_valid_password("toto1234"))
