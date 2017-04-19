"""
Defines the session resurce that handles user login sessions
"""

from collections import defaultdict
import string

from server.api import Api
from server.resource import Resource
from server.resource_helpers import expect_data, expect_session_key
from server.utility import choice
from server.routes import route

class Session(Resource):
    """
    Resource Parameters
    """
    session_key_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    session_key_len = 60

    """
    Resource Data
    """
    def __init__(self):
        self._user_sessions = {} # Key: session_key, Value: username
        self._account_sessions = defaultdict(set) # Key: username, Value: [session_key]
        self.session = self
        self.users = None

    def _users(self):
        return self._account_sessions.keys()

    """
    Resource Methods
    """
    def get_user(self, session_key):
        return self._user_sessions[session_key]

    def set_users_resource(self, users_resource):
        self.users = users_resource

    def logout(self, session_key):
        username = self._user_sessions[session_key]
        self._account_sessions[username].remove(session_key)
        del self._user_sessions[session_key]

    def logout_user(self, username):
        for session_key in list(self._account_sessions[username]):
            self.logout(session_key)

    def validate_session_key(self, session_key):
        return session_key in self._user_sessions

    def _gen_session_key(self):
        return ''.join(choice(self.session_key_chars) for _ in range(self.session_key_len))

    """
    Rest Methods
    """
    @route('/' + Api.users)
    @expect_session_key
    def get_online_users(self, session_key):
        self.response.status = 200
        return {Api.users: list(self._users())}

    @route()
    @expect_data(Api.username, Api.password)
    def post_login(self, username, password):
        if self.users.validate_username(username):
            if self.users.validate_password(username, password):
                new_session_key = self._gen_session_key()
                self._user_sessions[new_session_key] = username
                self._account_sessions[username].add(new_session_key)
                self.response.status = 201
                return {Api.session_key: new_session_key}
            else:
                self.response.status = 422
                return {Api.username: username}
        else:
            self.response.status = 422
            return {}

    @route()
    @expect_session_key
    def delete_logout(self, session_key):
        self.logout(session_key)
        self.response.status = 204
        return {}

