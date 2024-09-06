#!/usr/bin/env python3
"""
BasicAuth class
"""

from typing import TypeVar
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


 def user_object_from_credentials(self, user_email: str, user_pwd: str) -> User:
        """
        Returns the User instance based on the email and password.
        """
        # Check if email or password is None or not strings
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Debugging: Print email to verify
        print(f"Searching for user with email: {user_email}")

        # Search for the user by email using the search method
        users = User.search({'email': user_email})
        
        # Debugging: Print search results
        print(f"Users found: {users}")

        if not users:
            return None

        # Assuming the first match (there should only be one)
        user = users[0]

        # Debugging: Print to check password comparison
        print(f"User found: {user.display_name()}, checking password...")

        # Verify if the password is valid
        if not user.is_valid_password(user_pwd):
            print(f"Password check failed for user: {user.display_name()}")
            return None

        print(f"Password check passed for user: {user.display_name()}")
        return user
