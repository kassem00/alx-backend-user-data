#!/usr/bin/env python3
"""
auth class
"""

from typing import List, TypeVar
from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        that returns the Base64 part of the Authorization header for a
        Basic Authentication
        """
        if authorization_header is None or\
           isinstance(authorization_header) is not str or\
           "Basis " not in authorization_header:
            return None
        else:
            a = authorization_header.split(" ")
            return a[1]
