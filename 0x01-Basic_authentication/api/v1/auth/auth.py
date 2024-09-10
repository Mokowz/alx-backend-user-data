#!/usr/bin/env python3
"""API Authentication Module"""
from flask import request
from typing import TypeVar, List


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require Auth Method"""
        return False
    
    def authorization_header(self, request=None) -> str:
        """Validate all requests"""
        if request is None:
            return None
        auth = request.headers.get('Authorization')
        if auth is None:
            return None
        return auth
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user"""
        return None