#!/usr/bin/python3
""" basic_auth: contains the 'BasicAuth' class """
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """ 'BasicAuth' class """
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
