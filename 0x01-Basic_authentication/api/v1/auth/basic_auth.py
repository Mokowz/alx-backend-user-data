#!/usr/bin/env python3
"""API Authentication Module"""
from . import auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(auth.Auth):
    """Basic Auth Class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract base64 authorization"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        encoded_string = authorization_header.split(" ", 1)[1]

        return encoded_string

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """Encode data"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            encoded_str = base64_authorization_header.encode('utf-8')
            decoded_str_b64 = base64.b64decode(encoded_str)
            decoded = decoded_str_b64.decode('utf-8')
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Extract user credentials"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)

        return email, password

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd:
                                     str) -> TypeVar('User'):
        """Get user object from credentials"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users_db = User.search({'email': user_email})
        except Exception:
            return None

        for user in users_db:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user"""
        authorization_header = self.authorization_header(request)
        extract_header = self.extract_base64_authorization_header(
            authorization_header)
        decoded_header = self.decode_base64_authorization_header(
            extract_header)
        email, passwd = self.extract_user_credentials(decoded_header)
        usr_obj = self.user_object_from_credentials(email, passwd)

        return usr_obj
