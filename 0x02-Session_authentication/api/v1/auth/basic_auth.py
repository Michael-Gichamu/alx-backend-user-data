#!/usr/bin/env python3
"""Contains class BasicAuth."""
from api.v1.auth.auth import Auth
import re
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Basic Authentication.
    Inherits from Auth.
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """Method to extact authorization token."""
        if authorization_header:
            if type(authorization_header) == str:
                pattern = r'^Basic\s(.+)$'
                match = re.match(pattern, authorization_header)
                if match:
                    return match.group(1)
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """Method to decode base64 from authorization token."""
        if base64_authorization_header:
            if type(base64_authorization_header) == str:
                try:
                    decoded = base64.b64decode(base64_authorization_header)
                    return decoded.decode('utf-8')
                except (base64.binascii.Error, UnicodeDecodeError):
                    return None
        return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """Method to extract user credentials."""
        if decoded_base64_authorization_header:
            if type(decoded_base64_authorization_header) == str:
                pattern = r':'
                if re.search(pattern, decoded_base64_authorization_header):
                    user = decoded_base64_authorization_header.split(':', 1)
                    user_email = user[0]
                    user_password = user[1]
                    return (user_email, user_password)
        return (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Method to extract and return formatted user credentials."""
        if user_email and type(user_email) == str:
            if user_pwd and type(user_pwd) == str:
                try:
                    users = User.search({'email': user_email})
                except Exception:
                    return None
                if len(users) <= 0:
                    return None
                if users[0].is_valid_password(user_pwd):
                    return users[0]
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to extract data from authorization header,
        and user credentials.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
