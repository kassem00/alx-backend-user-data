#!/usr/bin/env python3
"""
BasicAuth class
"""

from api.v1.auth.auth import Auth
import base64

class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Returns the Base64 part of the Authorization header
        for Basic Authentication
        """
        if authorization_header is None or\
           not isinstance(authorization_header, str) or\
           not authorization_header.startswith("Basic "):
            return None

        return authorization_header.split(" ")[1]

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or\
           not isinstance(decoded_base64_authorization_header, str) or\
           ":" not in decoded_base64_authorization_header:
            return (None, None)

        credentials = decoded_base64_authorization_header.split(":")


        if len(credentials) != 2:
            return (None, None)

        return (credentials[0], credentials[1])
