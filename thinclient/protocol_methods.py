"""
Protocol methods to interact with our server
"""

import rest_methods

class Protocol(object):
    def __init__(self):
        self.rest = rest_methods.Rest('http://localhost:8000/api')

    def register(self, username, password, email):
        data = {
            'username': username,
            'password': password,
            'email': email
        }
        self.rest.post('/users', data)