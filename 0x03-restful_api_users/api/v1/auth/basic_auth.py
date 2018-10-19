#!/usr/bin/python3
""" basic_auth: contains the 'BasicAuth' class """
from api.v1.auth.auth import Auth
from models import (db_session, User)
import base64


class BasicAuth(Auth):
    """ 'BasicAuth' class """

    def current_user(self, request=None):
        """ Retrives user instance for a request """
        if request:
            token = self.authorization_header(request)
            token = self.extract_base64_authorization_header(token)
            token = self.decode_base64_authorization_header(token)
            creds = self.extract_user_credentials(token)
            email = creds[0]
            password = creds[1]
            user_obj = self.user_object_from_credentials(email, password)
            return user_obj

    @staticmethod
    def user_object_from_credentials(user_email, user_pwd):
        """ Returns the user object based on 'user_email' and 'user_pwd' """
        if not user_email or type(user_email) != str:
            return None

        if not user_pwd or type(user_pwd) != str:
            return None

        query = db_session.query(User).filter(User.email == user_email)
        count = query.count()
        if count == 1:
            user = query.one()
            if user.is_valid_password(user_pwd):
                return user
        if count > 1:
            raise Exception("ERROR: duplicate emails found in database")
        return None

    @staticmethod
    def extract_user_credentials(decoded_base64_authorization_header):
        """ Returns user email and password from the Base64 decoded value """
        auth = decoded_base64_authorization_header
        if auth is None or type(auth) != str or ':' not in auth:
            return None, None

        creds = auth.split(':')
        return creds[0], creds[1]

    @staticmethod
    def extract_base64_authorization_header(authorization_header):
        """ Returns the Base64 part of the 'Authorization' header """
        auth = authorization_header
        if auth is None or type(auth) != str or "Basic" not in auth:
            return None

        index = authorization_header.index('Basic')
        return authorization_header[index+6:]

    @staticmethod
    def decode_base64_authorization_header(base64_authorization_header):
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
