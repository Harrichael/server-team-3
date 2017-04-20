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
    @num_tokens(2)
    def do_login(self, username, password):
        data = {
            'username': username,
            'password': password
        }
        self.api.post('/session', data)

    @tokenize
    @num_tokens(1)
    def do_logout(self):
        self.api.delete('/session')

    @tokenize 
    @num_tokens(0)
    def do_get_online_users(self):
        self.api.get('/session/users')

    @tokenize
    @num_tokens(3)
    def do_register_user(self, username, password, email):
        data = {
            'username': username,
            'password': password,
            'email': email
        }
        self.api.post('/users', data)

    @tokenize   
    @num_tokens(2)
    def do_change_password(self, session_key, password):
        data = {
            'session-key': session_key,
            'password': password
        }
        self.api.put('/users/<username>/password', data)

    @tokenize   
    @num_tokens(2)
    def do_verify_email(self, email, email_code):
        data = {
            'email': email,
            'email_code': email_code
        }
        self.api.put('/users/<username>/emails', data)

    @tokenize  
    @num_tokens(0)
    def do_get_user_config(self):
        self.api.get('/users/<username>/config')

    @tokenize  
    @num_tokens(4)
    def do_update_user_config(self, ... ):
        data = {

        """argparse stuff"""

        }
        self.api.put('/users/<username>/config')

    @tokenize   
    @num_tokens(0)
    def do_get_user_profile(self):
        self.api.get('/users/<user>/profile')

    @tokenize    
    @num_tokens(4)
    def do_update_user_profile(self, ... ):
        data = {

        """argparse stuff"""

        }
        self.api.put('/users/<username>/profile', data)

    @tokenize    
    @num_tokens(0)
    def do_get_pm_history(self):
        self.api.get('/users/<username>/pm/<user>')

    @tokenize    
    @num_tokens(1)
    def do_send_pm(self, message):
        data = {
            'message': message
        }
        self.api.post('/users/<username>/pm/<user>', data)

    @tokenize    
    @num_tokens(0)
    def do_delete_pm(self):
        self.api.delete('/users/<username>/pm/<user>/<id>')

    @tokenize
    @num_tokens(0)
    def do_get_channel_list(self):
        self.api.get('/channels')

    @tokenize   
    @num_tokens(1)
    def do_create_channel(self, channel_name):
        data = {
            'channel_name': channel_name
        }
        self.api.post('/channels', data)

    @tokenize  
    @num_tokens(0)
    def do_delete_channel(self):
        self.api.delete('/channels/<channel>')

    @tokenize   
    @num_tokens(0)
    def do_get_channel_admins(self):
        self.api.get('/channels/<channel>/admins')

    @tokenize   
    @num_tokens(2)
    def do_adjust_admin_level(self, admins, chiefAdmin):
        data = {
            'admins': admin_list,
            'chiefAdmin': admin
        }
        self.api.put('/channels/<channel>/admins', data)

    @tokenize    
    @num_tokens(0)
    def do_get_channel_subscribers(self):
        self.api.get('/channels/<channel>/subscriptions')

    @tokenize   
    @num_tokens(0)
    def do_subscribe_to_channel(self):
        self.api.post('/channels/<channel>/subscriptions')

    @tokenize  
    @num_tokens(0)
    def do_unsubscribe_to_channel(self):
        self.api.delete('/channels/<channel>/subscriptions')

    @tokenize      
    @num_tokens(2)
    def do_get_blocked_users(self):

        self.api.get('/channels/<channel>/black-list')

    @tokenize  
    @num_tokens(0)
    def do_block_user_channel(self, username, time):
        data = {
            'username': username,
            'time': time
        }
        self.api.post('/channels/<channel>/black-list', data)

    @tokenize
    @num_tokens(0)
    def do_get_channel_history(self):
        self.api.get('/channels/<channel>/chat')

    @tokenize
    @num_tokens(1)
    def do_send_message(self, message):
        data = {
            'message': message
        }
        self.api.post('/channels/<channel>/chat', data)

    @tokenize
    @num_tokens(0)
    def do_delete_message(self):
        self.api.delete('/channels/<channel>/chat/<id>')


if __name__ == '__main__':
    Thinclient().cmdloop()
