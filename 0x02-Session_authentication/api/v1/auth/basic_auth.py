#!/usr/bin/env python3
"""
BasicAuth class
"""

from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """ BasicAuth class """

    def extract_base64_authorization_header(self, authorization_header: str):
        """
        Returns the Base64 part of the Authorization header
        for Basic Authentication
        """
        if authorization_header is None or\
           not isinstance(authorization_header, str) or\
           not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(self, base64_authorization_header):
        """
        Decodes Base64 string to plain text.
        """
        if base64_authorization_header is None or\
           not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (ValueError, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """
        Extracts user email and password from the decoded Base64 string.
        """
        if decoded_base64_authorization_header is None or\
           not isinstance(decoded_base64_authorization_header, str) or\
           ":" not in decoded_base64_authorization_header:
            return (None, None)

        credentials = decoded_base64_authorization_header.split(":", 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str):
        """
        Returns a User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        users = User.search({'email': user_email})
        if not users:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request.
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth = self.extract_base64_authorization_header(auth_header)
        if base64_auth is None:
            return None

        decoded_auth = self.decode_base64_authorization_header(base64_auth)
        if decoded_auth is None:
            return None

        email, password = self.extract_user_credentials(decoded_auth)
        if email is None or password is None:
            return None

        return self.user_object_from_credentials(email, password)
