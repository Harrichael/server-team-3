"""
Api class for our api routes and json data field names
"""

import re

class Api(object):
    admins = 'admins'
    api = 'api'
    bio = 'bio'
    black_list = 'black-list'
    blocked = 'blocked'
    channel = 'channel'
    channel_name = 'channel-name'
    channel_param = '<channel>'
    channels = 'channels'
    channels = 'channels'
    chat = 'chat'
    chat_filter = 'chat-filter'
    chief_admin = 'chief-admin'
    config = 'config'
    email = 'email'
    email_code = 'code'
    emails = 'emails'
    error_fields = 'malformed-fields'
    firstname = 'first-name'
    gender = 'gender'
    lastname = 'last-name'
    message = 'message'
    messages = 'messages'
    msg = 'msg'
    msg_id = 'msg-id'
    msg_id_p = 'msg_id'
    msg_id_param = '<msg_id>'
    password = 'password'
    pm = 'pm'
    profile = 'profile'
    sender = 'sender'
    session = 'session'
    session_key = 'session-key'
    subscriptions = 'subscriptions'
    time = 'time'
    time_end = 'time-end'
    timestamp = 'timestamp'
    user = 'user'
    user_param = '<user>'
    username = 'username'
    username_param = '<username>'
    users = 'users'
    users = 'users'
    web = 'web'

    """
    Values
    """
    default_chat_filter = 'none'

    """
    Regex Validators
    """
    c_username = re.compile('^[a-zA-Z0-9_.-]*$')
    @classmethod
    def re_username(cls, username):
        return cls.c_username.match(username)

    c_email = re.compile('^.*[@].*[.].*$')
    @classmethod
    def re_email(cls, email):
        return cls.c_email.match(email)

    c_channel_name = re.compile('^[a-zA-Z0-9_.-]*$')
    @classmethod
    def re_channel_name(cls, channel_name):
        return cls.c_channel_name.match(channel_name)
