#!/usr/bin/env python3
"""Template for all authentication system"""
from typing import List, TypeVar
from flask import Flask, request
import os
import fnmatch


class Auth():
    """
    Authentication class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to check if auth is required.
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(normalized_path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method to get authorization header.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to get user from request.
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie from a request
        Args:
            request : request object
        Return:
            value of _my_session_id cookie from request object
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        return request.cookies.get(session_name)
