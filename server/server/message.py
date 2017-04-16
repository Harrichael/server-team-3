"""
Message class used for pms and channel messages
"""

from server.utility import epoch_timestamp
from server.api import Api
from server.sorted_collection import SortedCollection

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
        self.msgs = SortedCollection(key=lambda msg: msg.msg_id)

    def add_msg(self, username, message_text):
        msg_id = 0
        if self.msgs:
            msg_id = self.msgs[-1].msg_id + 1
        new_msg = Message(username, msg_id, message_text)
        self.msgs.append(new_msg)
        return new_msg

    def remove_msg_id(self, msg_id):
        self.msgs.remove_by_key(msg_id)

    def last_page(self, page_size):
        if not self.msgs:
            return 0
        return (len(self.msgs)-1) // max(page_size,1)

    def get_dict(self, page=0, page_size=None):
        if not page_size:
            page_size = len(self.msgs)
        page_size = max(page_size, 1)

        page = max(page, 0)
        page = min(self.last_page(page_size), page)

        msgs = self.msgs[page*page_size:(page+1)*page_size]
        return {
            Api.messages: [msg.get_dict() for msg in msgs]
        }
