"""
Base class for our resource objects
"""

import lib.bottle.bottle as bottle

"""
Base Resource object
"""
class Resource(object):
    response = bottle.response
    request = bottle.request

    method_uris = {}
