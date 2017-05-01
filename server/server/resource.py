"""
Base class for our resource objects
"""

import lib.bottle.bottle as bottle

from server.api import Api
from server.routes import route

"""
Base Resource object
"""
class Resource(object):
    response = bottle.response
    request = bottle.request

    @classmethod
    def set_config(cls, config):
        cls.config = config

    @classmethod
    @route(Api.hello)
    def get_hello(cls):
        reply = {}
        for el in dir(cls.config):
            if not el.startswith('_'):
                reply[el] = getattr(cls.config, el)

        cls.response.status = 200
        return reply

