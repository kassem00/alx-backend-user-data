#!/usr/bin/env python3
"""
auth class
"""

from typing import List, TypeVar
from flask import request
from basic_auth import *

class Auth():
    """ auth module """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is
        required based on path and excluded_paths.
        """
        if path is None or not isinstance(path, str) or\
           excluded_paths is None or not excluded_paths:
            return True

        path = path.rstrip('/')
        excluded_paths = [p.rstrip('/') for p in excluded_paths]

        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header if present, otherwise returns None
        ."""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

