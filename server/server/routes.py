"""
Sets up routes to resources
"""

import lib.bottle.bottle as bottle

from server.api import Api
from server.resource import Resource
from server.session import Session

def add_resource(uri, resource):
    rest_methods = [
        'get', 'post', 'delete', 'put', 'patch'
    ]

    for resource_method in dir(resource):
        if not resource_method.startswith('on_'):
            continue
        for method in rest_methods:
            if resource_method.startswith('on_' + method):
                uri_extension = uri
                if resource_method in resource.method_uris:
                    uri_extension += resource.method_uris[resource_method]

                method_uri = Api.cmn_uri_prefix + uri_extension
                getattr(bottle, method)(method_uri)( getattr(resource, resource_method) )
                break

def set_routes(session, users):
    add_resource(Api.session, session)
    add_resource(Api.res_users, users)
