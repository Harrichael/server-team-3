"""
Api class for our api routes and json data field names
"""

class Api(object):
    """
    Routes
    """
    cmn_uri_prefix = '/api'
    session = '/session'
    res_users = '/users'
    res_emails = '/emails'
    res_password = '/password'
    res_config = '/config'
    res_profile = '/profile'
    res_pm = '/pm'
    username_param = '/<username>'
    user_param = '/<user>'
    msg_id_param = '/<msg_id>'

    """
    Data fields
    """
    session_key = 'session-key'
    username = 'username'
    user = 'user'
    password = 'password'
    email = 'email'
    users = 'users'
    email_code = 'code'
    blocked = 'blocked'
    chat_filter = 'chat-filter'
    default_chat_filter = 'none'
    firstname = 'first-name'
    lastname = 'last-name'
    bio = 'bio'
    gender = 'gender'
    sender = 'sender'
    msg_id = 'msg_id'
    msg = 'msg'
    timestamp = 'timestamp'
    message = 'message'
    messages = 'messages'

