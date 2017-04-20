"""
Sets up routes to resources
"""

import lib.bottle.bottle as bottle

from server.api import Api

def route(uri=''):
    def decorator(func):
        func.resource_route = uri
        return func
    return decorator

def add_resource(root_url, resource):
    rest_methods = [
        'get', 'post', 'delete', 'put', 'patch'
    ]
    for resource_method_name in dir(resource):
        resource_method = getattr(resource, resource_method_name)
        if hasattr(resource_method, 'resource_route'):
            method_uri = root_url + resource_method.resource_route
            rest_method = resource_method_name.split('_')[0]
            if rest_method not in rest_methods:
                raise NotImplementedError('Prefix of method: {}'.format(rest_method)) 
            getattr(bottle, rest_method)(method_uri)( resource_method )

def set_routes(session, users, channels, static):
    add_resource(Api.api + Api.session, session)
    add_resource(Api.api + Api.res_users, users)
    add_resource(Api.api + Api.res_channels, channels)
    add_resource('', static)
