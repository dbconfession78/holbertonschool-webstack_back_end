#!/usr/bin/python3
""" Auth: contains the Auth class """


class Auth:
    """ Authorization class """
    def require_auth(self, path, excluded_paths):
        """ Returns False if 'path' is in 'excluded_paths' """
        if not path or not excluded_paths:
            return True

        if not path.endswith("/"):
            path += "/"

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None):
        """ Returns None  """
        if request is None:
            return None
        headers = request.headers
#        input('headers: {}'.format(headers))
        if "Authorization" not in headers.keys():
            return None
        return headers['Authorization']

    def current_user(self, request=None):
        """ returns None """
        return None
