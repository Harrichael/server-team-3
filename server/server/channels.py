"""
Channels resource to handle channel attributes and chat
"""

from server.api import Api
from server.resource import Resource
from server.resource_helpers import ( expect_data,
                                      expect_session_key,
                                      verify_username,
                                      verify_user,
                                      verify_msg_id,
                                      verify_channel,
                                    )
from server.message import MessageBox
from server.utility import epoch_timestamp
from server.routes import route

class Channel(object):
    def __init__(self, name, username):
        self.name = name
        self.chief_admin = username
        self.admins = set()
        self.subscribers = set([username])
        self.black_list = {}
        self.chat = MessageBox()

        self.min_release_time = 0

    def is_chief_admin(self, username):
        return username == self.chief_admin

    def is_admin(self, username):
        return self.is_chief_admin(username) or username in self.admins

    def promote_admin(self, username):
        if not self.is_subscribed(username) or self.is_blocked(username):
            return False

        if not self.is_chief_admin(username):
            self.admins.add(username)
            return True

        return False

    def demote_admin(self, username):
        if self.is_admin(username):
            self.admins.remove(username)
            return True
        return False

    def promote_chief_admin(self, username):
        if self.is_admin(username):
            self.admins.add(self.chief_admin)
            self.chief_admin = username
            return True
        return False

    def is_subscribed(self, username):
        return username in self.subscribers

    def subscribe(self, username):
        if self.is_blocked(username):
            return False

        self.subscribers.add(username)
        return True

    def unsubscribe(self, username):
        if self.is_chief_admin(username):
            return False

        if self.is_admin(username):
            self.admins.remove(username)

        if self.is_subscribed(username):
            self.subscribers.remove(username)

        return True

    def is_blocked(self, username):
        self.update_block_list()

        return username in self.black_list

    def update_block_list(self):
        removed_users = []

        if self.min_release_time:
            timestamp = epoch_timestamp()
            if timestamp > self.min_release_time:
                self.min_release_time = 0
                for user in self.black_list:
                    time = self.black_list[user]
                    if time < timestamp:
                        removed_users.append(user)
                    else:
                        self.min_release_time = min(self.min_release_time, time)

        for user in removed_users:
            del self.black_list[user]

    def block(self, username, duration):
        if self.is_admin(username):
            return False

        if self.is_subscribed(username):
            self.subscribers.remove(username)
        release_time = max(duration, 0) + epoch_timestamp()
        if self.min_release_time:
            self.min_release_time = min(self.min_release_time, release_time)
        else:
            self.min_release_time = release_time
        self.black_list[username] = release_time
        return True

    def blocked_get_dict(self):
        return {
            Api.blocked: [{
                Api.username: user,
                Api.time_end: self.black_list[user]
            } for user in self.black_list]
        }

class Channels(Resource):
    """
    Resource Parameters
    """
    default_page_size = 10

    """
    Resource Data
    """
    def __init__(self, session, users):
        self._channels = {} # Key: channel_name, Value: Channel()
        self.session = session
        self.users = users

    """
    Resource Methods
    """
    def channel_names(self):
        return list(self._channels.keys())

    def validate_channel_name(self, channel_name):
        return channel_name in self._channels

    """
    Rest Methods
    """
    @route()
    @expect_session_key
    def get_channel_names(self, session_key):
        self.response.status = 200
        return {
            Api.channels: self.channel_names()
        }

    @route()
    @expect_session_key
    @expect_data(Api.channel_name)
    def post_channel(self, session_key, channel_name):
        username = self.session.get_user(session_key)
        if channel_name not in self._channels:
            self._channels[channel_name] = Channel(channel_name, username)
            self.response.status = 201
        else:
            self.response.status = 409
        return {}

    @route(Api.channel_param)
    @expect_session_key
    @verify_channel
    def delete_channel(self, session_key, channel_name):
        username = self.session.get_user(session_key)
        channel = self._channels[channel_name]
        if channel.is_chief_admin(username):
            del self._channels[channel_name]
            self.response.status = 200
        else:
            self.response.status = 403
        return {}

    @route(Api.channel_param + '/' + Api.subscriptions)
    @expect_session_key
    @verify_channel
    def get_chnl_subscriptions(self, session_key, channel_name):
        channel = self._channels[channel_name]
        self.response.status = 200
        return {
            Api.subscriptions: list(channel.subscribers)
        }

    @route(Api.channel_param + '/' + Api.subscriptions)
    @expect_session_key
    @verify_channel
    def post_subscribe(self, session_key, channel_name):
        channel = self._channels[channel_name]
        username = self.session.get_user(session_key)
        if channel.subscribe(username):
            self.response.status = 200
        else:
            self.response.status = 422
        return {}

    @route(Api.channel_param + '/' + Api.subscriptions)
    @expect_session_key
    @verify_channel
    def delete_unsubscribe(self, session_key, channel_name):
        channel = self._channels[channel_name]
        username = self.session.get_user(session_key)
        if channel.unsubscribe(username):
            self.response.status = 200
        else:
            self.response.status = 422
        return {}

    @route(Api.channel_param + '/' + Api.black_list)
    @expect_session_key
    @verify_channel
    def get_black_list(self, session_key, channel_name):
        channel = self._channels[channel_name]
        channel.update_block_list()
        self.response.status = 200
        return channel.blocked_get_dict()

    @route(Api.channel_param + '/' + Api.black_list)
    @expect_session_key
    @expect_data(Api.username, Api.time)
    @verify_channel
    def post_block_user(self, session_key, username, duration, channel_name):
        channel = self._channels[channel_name]
        user = self.session.get_user(session_key)
        if all([
                channel.is_admin(user),
                self.users.validate_username(username),
                channel.block(username, duration),
            ]):
            self.response.status = 200
        else:
            self.response.status = 422
        return {}

    @route(Api.channel_param + '/' + Api.admins)
    @expect_session_key
    @verify_channel
    def get_chnl_admins(self, session_key, channel_name):
        channel = self._channels[channel_name]
        self.response.status = 200
        return {
            Api.admins: list(channel.admins),
            Api.chief_admin: channel.chief_admin
        }

    @route(Api.channel_param + '/' + Api.admins)
    @expect_session_key
    @verify_channel
    def put_update_admins(self, session_key, channel_name):
        failed_admin_updates = []

        channel = self._channels[channel_name]
        user = self.session.get_user(session_key)
        if not channel.is_chief_admin(user):
            self.response.status = 404
            return {}

        json_data = self.request.json

        if Api.chief_admin in json_data:
            chief_admin = json_data[Api.chief_admin]
            if not channel.is_admin(chief_admin):
                if not channel.promote_admin(chief_admin):
                    self.response.status = 422
                    return {}
            channel.promote_chief_admin(chief_admin)

        if Api.admins in json_data:
            admins = set(json_data[Api.admins])
            for admin in channel.admins:
                if admin not in admins:
                    if not channel.demote_admin(admin):
                        failed_admin_updates.append(admin)

            for admin in admins:
                if admin not in channel.admins:
                    if not channel.promote_admin(admin):
                        failed_admin_updates.append(admin)
            
        if failed_admin_updates:
            self.response.status = 422
            return {
                Api.admins: failed_admin_updates
            }
        else:
            self.response.status = 200
            return {}

    @route(Api.channel_param + '/' + Api.chat)
    @expect_session_key
    @verify_channel
    def get_chnl_chat(self, session_key, channel_name):
        channel = self._channels[channel_name]
        username = self.session.get_user(session_key)
        if not channel.is_subscribed(username):
            self.response.status = 404
            return {}

        try:
            page_size = int(self.request.query.page_size or self.default_page_size)
            page = int(self.request.query.page or channel.chat.last_page(page_size))
        except:
            raise
            self.response.status = 400
            return {}

        self.response.status = 200
        return channel.chat.get_dict(page, page_size)

    @route(Api.channel_param + '/' + Api.chat)
    @expect_session_key
    @verify_channel
    @expect_data(Api.message)
    def post_chnl_new_msg(self, session_key, channel_name, message_text):
        channel = self._channels[channel_name]
        username = self.session.get_user(session_key)
        if not channel.is_subscribed(username):
            self.response.status = 404
            return {}

        self.response.status = 201
        return channel.chat.add_msg(username, message_text).get_dict()

    @route(Api.channel_param + '/' + Api.chat + Api.msg_id_param)
    @expect_session_key
    @verify_channel
    @verify_msg_id
    def delete_chnl_del_msg(self, session_key, channel_name, msg_id):
        channel = self._channels[channel_name]
        username = self.session.get_user(session_key)
        if not channel.is_subscribed(username):
            self.response.status = 404
            return {}

        try:
            channel.chat.remove_msg_id(msg_id, username)
            self.response.status = 200
        except ValueError:
            self.response.status = 404

        return {}

