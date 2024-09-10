#!/usr/bin/env python3
"""API Authentication Module"""
from . import auth
import base64


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
