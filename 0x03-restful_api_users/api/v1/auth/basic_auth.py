#!/usr/bin/python3
""" basic_auth: contains the 'BasicAuth' class """
from api.v1.auth.auth import Auth
from api.v1.views import users
import base64
import models
from models import db_session


class BasicAuth(Auth):
    """ 'BasicAuth' class """

    def user_object_from_credentials(self, user_email, user_pwd):
        """ Returns the user object based on 'user_email' and 'user_pwd' """

        _all = users.all()
        for k, v in _all.items():
            if v.email == user_email:
                return v

        if not user_email or type(user_email) != str:
            return None

        if not user_pwd or type(user_pwd) != str:
            return None


        

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """ Returns user email and password from the Base64 decoded value """
        auth = decoded_base64_authorization_header
        if auth is None or type(auth) != str or ':' not in auth:
            return (None, None)

        creds = auth.split(':')
        return (creds[0], creds[1])

    def extract_base64_authorization_header(self, authorization_header):
        """ Returns the Base64 part of the 'Authorization' header """
        auth = authorization_header
        if auth is None or type(auth) != str or "Basic" not in auth:
            return None

        index = authorization_header.index('Basic')
        return authorization_header[index+6:]

    def decode_base64_authorization_header(self, base64_authorization_header):
        """ Returns decoded value of UTF8 string """
        auth = base64_authorization_header

        if auth is None or type(auth) != str:
            return None

        if is_valid_base64_string(auth):
            return base64.b64decode(auth).decode('utf-8')
        return None


def is_valid_base64_string(s):
    """ Returns True if 's' is a valid base64 string """
    try:
        base64.b64encode(base64.b64decode(s))
        return True
    except Exception:
        return False
