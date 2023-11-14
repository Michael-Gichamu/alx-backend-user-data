#!/usr/bin/env python3
"""
Definition of class SessionAuth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Implement Session Authorization protocol methods
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user with id user_id
        Args:
            user_id (str): user's user id
        Return:
            None is user_id is None or not a string
            Session ID in string format
        """
        if user_id is None:
            return None
        if type(user_id) == str:
            session_id = uuid4()
            self.user_id_by_session_id[str(session_id)] = user_id
            return str(session_id)
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a user ID based on a session ID
        Args:
            session_id (str): session ID
        Return:
            user id or None if session_id is None or not a string
        """
        if session_id is None:
            return None
        if type(session_id) == str:
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """
        Return a user instance based on a cookie value
        Args:
            request : request object containing cookie
        Return:
            User instance
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id:
            user = User.get(user_id)
            return user

    def destroy_session(self, request=None):
        """
        Deletes a user session
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)
        if session_cookie is None:
            return False
        user_id = self.user_id_for_session_id(session_cookie)
        if user_id is None:
            return False
        del self.user_id_for_session_id[session_cookie]
        return True
