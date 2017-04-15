"""
Message class used for pms and channel messages
"""

from server.utility import epoch_timestamp
from server.api import Api

class Message(object):
    def __init__(self, sender, msg_id, msg):
        self.sender = sender
        self.msg_id = msg_id
        self.msg = msg
        self.timestamp = epoch_timestamp()

    def get_dict(self):
        return {
            Api.sender: self.sender,
            Api.msg_id: self.msg_id,
            Api.msg: self.msg,
            Api.timestamp: self.timestamp,
        }

class MessageBox(object):
    def __init__(self):
        self.msgs = []

    def add_msg(self, username, message_text):
        msg_id = 0
        if self.msgs:
            msg_id = self.msgs[-1].msg_id + 1
        new_msg = Message(username, msg_id, message_text)
        self.msgs.append(new_msg)
        return new_msg

    def get_dict(self):
        return {
            Api.messages: [msg.get_dict() for msg in self.msgs]
        }
