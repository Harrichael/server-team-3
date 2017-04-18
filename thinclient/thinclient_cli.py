"""
cli for thinclient
"""

import cmd

import rest_methods
from cli_helpers import tokenize, num_tokens

class Thinclient(cmd.Cmd):
    def __init__(self):
        super(Thinclient, self).__init__()
        self.api = rest_methods.Rest('http://localhost:8000/api')

    @tokenize
    @num_tokens(1)
    def do_set_session_key(self, session_key):
        self.api.set_header('session-key', session_key)

    @tokenize
    @num_tokens(3)
    def do_register(self, username, password, email):
        data = {
            'username': username,
            'password': password,
            'email': email
        }
        self.api.post('/users', data)

    @tokenize
    @num_tokens(2)
    def do_login(self, username, password):
        data = {
            'username': username,
            'password': password,
        }
        self.api.post('/session', data)

if __name__ == '__main__':
    Thinclient().cmdloop()
