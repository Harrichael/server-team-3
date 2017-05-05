"""
Users resource to handle registered users and their profiles
"""

from collections import defaultdict

from server.api import Api
from server.resource import Resource
from server.resource_helpers import ( expect_data,
                                      expect_session_key,
                                      verify_username,
                                      verify_user,
                                      verify_msg_id,
                                    )
from server.message import MessageBox
from server.routes import route
from server.sendmail import Email
from server.utility import choice

class UserConfig(object):
    def __init__(self):
        #TODO: implement blocked behavior
        self.blocked = set()
        self.chat_filter = Api.default_chat_filter

    def set_blocked(self, blocked):
        self.blocked = set(blocked)

    def get_dict(self):
        return {
            Api.blocked: list(self.blocked),
            Api.chat_filter: self.chat_filter,
        }

class UserProfile(object):
    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.bio = ""
        self.gender = ""

    def get_dict(self):
        return {
            Api.firstname: self.firstname,
            Api.lastname: self.lastname,
            Api.bio: self.bio,
            Api.gender: self.gender,
        }

class User(object):
    pm_boxes = defaultdict(MessageBox)

    def __init__(self, username, password, email, code):
        self.username = username
        self.password = password
        self.email = email
        self.code = code
        self.verified = False
        self.config = UserConfig()
        self.profile = UserProfile()

    def attempt_verify(self, code):
        if code == self.code:
            self.verified = True

        return self.verified

    def get_pm_box(self, user):
        key = tuple(sorted([self.username, user]))
        return self.pm_boxes[key]

class Users(Resource):
    """
    Resource Parameters
    """
    default_page_size = 10
    code_len = 6
    code_chars = '0123456789'
    _verify_email = """\
Your e-mail verification code {} can be used to verify your account's email.

If you are not expecting this e-mail, you may ignore it.
Do not reply to this e-mail.

- Server 3
"""

    """
    Resource Data
    """
    def __init__(self):
        self._users = {} # Key: username, Value: User()
        self._email = Email('server3.dreamteam@gmail.com', 'dream.mst')
        self.session = None
        self.users = self

    """
    Resource Methods
    """
    def validate_username(self, username):
        return username in self._users

    def validate_password(self, username, password):
        user = self._users[username]
        return password == user.password and user.verified

    def username_verified(self, username):
        return self._users[username].verified

    def set_session_resource(self, session_resource):
        self.session = session_resource

    def _gen_email_code(self):
        return ''.join(choice(self.code_chars) for _ in range(self.code_len))

    """
    Rest Methods
    """
    @route()
    @expect_data(Api.username, Api.password, Api.email)
    def post_register(self, username, password, email):
        valid_username = Api.re_username(username)
        valid_email = Api.re_email(email)
        if not valid_username or not valid_email:
            self.response.status = 400
            invalid_fields = []
            if not valid_username:
                invalid_fields.append(Api.username)
            if not valid_email:
                invalid_fields.append(Api.email)
            return { Api.error_fields: invalid_fields }

        if username not in self._users:
            code = self._gen_email_code()
            self._users[username] = User(username, password, email, code)
            if self.config.verify_email:
                self._email.send( email,
                                  'Verification E-mail: Server3',
                                  self._verify_email.format(code)
                                )
            else:
                self._users[username].attempt_verify(code)
            self.response.status = 201
        else:
            self.response.status = 409
        return {}

    @route(Api.username_param, Api.password)
    @expect_session_key
    @expect_data(Api.password)
    @verify_username
    def put_change_password(self, session_key, password, username):
        self._users[username].password = password
        self.session.logout_user(username)
        self.response.status = 200
        return {}

    @route(Api.user_param, Api.emails)
    @expect_data(Api.email, Api.email_code)
    @verify_user
    def put_verify_email(self, email, email_code, username):
        user = self._users[username]
        if user.email == email:
            if user.attempt_verify(email_code):
                self.response.status = 200
                return {}
            else:
                self.response.status = 422
                return {Api.error_fields: [Api.email_code]}
        else:
            self.response.status = 422
            return {Api.error_fields: [Api.email]}

    @route(Api.username_param, Api.config)
    @expect_session_key
    @verify_username
    def get_user_config(self, session_key, username):
        user = self._users[username]
        self.response.status = 200
        return user.config.get_dict()

    @route(Api.username_param, Api.config)
    @expect_session_key
    @verify_username
    def put_user_config(self, session_key, username):
        user = self._users[username]
        json_data = self.request.json
        if Api.blocked in json_data:
            user.config.set_blocked(json_data[Api.blocked])
        if Api.chat_filter in json_data:
            user.config.chat_filter = json_data[Api.chat_filter]

        self.response.status = 200
        return user.config.get_dict()

    @route(Api.username_param, Api.profile)
    @expect_session_key
    @verify_user
    def get_user_profile(self, session_key, user):
        self.response.status = 200
        return self._users[user].profile.get_dict()

    @route(Api.username_param, Api.profile)
    @expect_session_key
    @verify_username
    def put_user_profile(self, session_key, username):
        user = self._users[username]
        json_data = self.request.json
        if Api.firstname in json_data:
            user.profile.firstname = json_data[Api.firstname]
        if Api.lastname in json_data:
            user.profile.lastname = json_data[Api.lastname]
        if Api.bio in json_data:
            user.profile.bio = json_data[Api.bio]
        if Api.gender in json_data:
            user.profile.gender = json_data[Api.gender]

        self.response.status = 200
        return user.profile.get_dict()

    @route(Api.username_param, Api.pm, Api.user_param)
    @expect_session_key
    @verify_username
    @verify_user
    def get_user_pm(self, session_key, username, user):
        pm = self._users[username].get_pm_box(user)
        try:
            page_size = int(self.request.query.page_size or self.default_page_size)
            page = int(self.request.query.page or pm.last_page(page_size))
        except ValueError:
            self.response.status = 400
            return {}
        self.response.status = 200
        return pm.get_dict(page, page_size)

    @route(Api.username_param, Api.pm, Api.user_param)
    @expect_session_key
    @expect_data(Api.message)
    @verify_username
    @verify_user
    def post_user_pm(self, session_key, message_text, username, user):
        pm = self._users[username].get_pm_box(user)
        self.response.status = 201
        return pm.add_msg(username, message_text).get_dict()

    @route(Api.username_param, Api.pm, Api.user_param, Api.msg_id_param)
    @expect_session_key
    @verify_username
    @verify_user
    @verify_msg_id
    def delete_pm(self, session_key, username, user, msg_id):
        pm = self._users[username].get_pm_box(user)
        try:
            pm.remove_msg_id(msg_id, username)
            self.response.status = 200
        except ValueError:
            self.response.status = 404

        return {}

