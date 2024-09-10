#!/usr/bin/env python3
"""API Authentication Module"""
from . import auth


class BasicAuth(auth.Auth):
    """Basic Auth Class"""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extract base64 authorization"""
        pass
