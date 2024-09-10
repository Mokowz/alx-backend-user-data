#!/usr/bin/env python3
"""API Authentication Module"""
from . import auth


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
