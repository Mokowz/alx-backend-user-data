#!/usr/bin/env python3
"""API Authentication Module"""
from flask import request
from typing import TypeVar, List


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require Auth Method"""
        if excluded_paths and path:
            if path[-1] == '/':
                new_path = path[:-1]
            else:
                new_path = path
            new_excluded_path = []
            for element in excluded_paths:
                if element[-1] == '/':
                    new_excluded_path.append(element[:-1])
                if element[-1] == '*':
                    if new_path.startswith(element[:-1]):
                        return False

            if new_path not in new_excluded_path:
                return True
            else:
                return False

        if path is None:
            return True

        if not excluded_paths:
            return True

    def authorization_header(self, request=None) -> str:
        """Validate all requests"""
        if request is None:
            return None
        auth = request.headers.get('Authorization')
        if auth is None:
            return None
        else:
            return auth

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user"""
        return None
