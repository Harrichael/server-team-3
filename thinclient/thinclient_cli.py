"""
cli for thinclient
"""

import cmd
import argparse
import rest_methods

from cli_helpers import tokenize, num_tokens

class Thinclient(cmd.Cmd):
    def __init__(self): 
        super(Thinclient, self).__init__()
        self.api = rest_methods.Rest('http://localhost:8000/api')
        self.prompt = 'Thinclient> '

    def do_EOF(self):
        return True

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
    @num_tokens(0)
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
    @num_tokens(3)
    def do_change_password(self, session_key, password, username):
        data = {
            'session-key': session_key,
            'password': password
        }
        self.api.put('/users/' + username + '/password', data)

    @tokenize   
    @num_tokens(3)
    def do_verify_email(self, email, email_code, username):
        data = {
            'email': email,
            'email_code': email_code
        }
        self.api.put('/users/' + username + '/emails', data)

    @tokenize  
    @num_tokens(1)
    def do_get_user_config(self, username):
        self.api.get('/users/' + username + '/config')

    def do_update_user_config(self, line):
        parser = argparse.argumentparser()
        parser.add_argument('-u', '--username', required=True)
        parser.add_argument('-b', '--blocked', default=None)
        parser.add_argument('-c', '--chat_filter', default=None)

        try:
            args = parser.parse_args(line.split())
        except SystemExit:
            return

        data = {}
        if args.blocked is not None:
            data['blocked'] = args.blocked
        if args.chat_filter is not None:
            data['chat-filter'] = args.chat_filter

        self.api.put('/users/' + args.username + '/config', data)

    @tokenize   
    @num_tokens(1)
    def do_get_user_profile(self, user):
        self.api.get('/users/' + user + '/profile')

    def do_update_user_profile(self, line):
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--username', required=True)
        parser.add_argument('-f', '--firstname', default=None)
        parser.add_argument('-l', '--lastname', default=None)
        parser.add_argument('-b', '--bio', default=None)
        parser.add_argument('-g', '--gender', default=None)

        try:
            args = parser.parse_args(line.split())
        except SystemExit:
            return

        data = {}
        if args.firstname is not None:
            data['firstname'] = args.firstname
        if args.lastname is not None:
            data['lastname'] = args.lastname
        if args.bio is not None:
            data['bio'] = args.bio
        if args.gender is not None:
            data['gender'] = args.gender
 
        self.api.put('/users/' + args.username + '/profile', data)

    @tokenize    
    @num_tokens(1)
    def do_get_pm_history(self, username):
        self.api.get('/users/' + username + '/pm/<user>')

    @tokenize    
    @num_tokens(3)
    def do_send_pm(self, message, username, user):
        data = {
            'message': message
        }
        self.api.post('/users/' + username + '/pm/' + user, data)

    @tokenize    
    @num_tokens(2)
    def do_delete_pm(self, username, user):
        self.api.delete('/users/' + username + '/pm/' + user + '/<id>')

    @tokenize
    @num_tokens(0)
    def do_get_channel_list(self):
        self.api.get('/channels')

    @tokenize   
    @num_tokens(1)
    def do_create_channel(self, channel_name):
        data = {
            'channel-name': channel_name
        }
        self.api.post('/channels', data)

    @tokenize  
    @num_tokens(1)
    def do_delete_channel(self, channel):
        self.api.delete('/channels/' + channel)

    @tokenize   
    @num_tokens(1)
    def do_get_channel_admins(self, channel):
        self.api.get('/channels/' + channel + '/admins')

    @tokenize   
    @num_tokens(3)
    def do_adjust_admin_level(self, admins, chiefAdmin, channel):
        parser = argparse.argumentparser()
        parser.add_argument('-c', '--channel', required=True)
        parser.add_argument('-a', '--admins', default=None)
        parser.add_argument('-o', '--chief_admin', default=None)

        try:
            args = parser.parse_args(line.split())
        except SystemExit:
            return

        data = {}
        if args.admins is not None:
            data['admins'] = args.admins.split(',')
        if args.chief_admin is not None:
            data['chief-admin'] = args.chief_admin

        self.api.put('/channels/' + args.channel + '/admins', data)

    @tokenize    
    @num_tokens(1)
    def do_get_channel_subscribers(self, channel):
        self.api.get('/channels/' + channel + '/subscriptions')

    @tokenize   
    @num_tokens(1)
    def do_subscribe_to_channel(self, channel):
        self.api.post('/channels/' + channel + '/subscriptions')

    @tokenize  
    @num_tokens(1)
    def do_unsubscribe_to_channel(self, channel):
        self.api.delete('/channels/' + channel + '/subscriptions')

    @tokenize      
    @num_tokens(1)
    def do_get_blocked_users(self, channel):
        self.api.get('/channels/' + channel + '/black-list')

    @tokenize  
    @num_tokens(3)
    def do_block_user_channel(self, username, time, channel):
        data = {
            'username': username,
            'time': time
        }
        self.api.post('/channels/' + channel + '/black-list', data)

    @tokenize
    @num_tokens(1)
    def do_get_channel_history(self, channel):
        self.api.get('/channels/' + channel + '/chat')

    @tokenize
    @num_tokens(2)
    def do_send_message(self, message, channel):
        data = {
            'message': message
        }
        self.api.post('/channels/' + channel + '/chat', data)

    @tokenize
    @num_tokens(2)
    def do_delete_message(self, channel, id):
        self.api.delete('/channels/' + channel + '/chat/' + id)


if __name__ == '__main__':
    Thinclient().cmdloop()
