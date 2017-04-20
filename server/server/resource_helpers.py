"""
Helper methods and decorators for common patterns
"""

import lib.bottle.bottle
from server.api import Api

"""
Decorator to extract expect
"""
def expect_data(*args):
    fields = list(args)

    def decorator(resource_method):

        def wrapper(resource_inst, *args, **kwargs):
            args = list(args)
            try:
                json_data = resource_inst.request.json
            except bottle.HTTPError:
                resource_inst.response.status = 400
                return {}
                
            try:
                for field in fields:
                    args.append(json_data[field])
            except KeyError:
                resource_inst.response.status = 422
                return {}

            return resource_method(resource_inst, *args, **kwargs)

        return wrapper

    return decorator

"""
Handles requiring the session key
"""
def expect_session_key(resource_method):

    def wrapper(resource_inst, *args, **kwargs):
        try:
            session_key = resource_inst.request.get_header(Api.session_key)
        except KeyError:
            resource_inst.response.status = 422
            return {}

        if resource_inst.session.validate_session_key(session_key):
            return resource_method(resource_inst, session_key, *args, **kwargs)

        resource_inst.response.status = 410
        return {}

    return wrapper

"""
Handles valid username check for username routes
Assumes session_key is first arg
"""
def verify_username(resource_method):

    def wrapper(resource_inst, *args, **kwargs):
        args = list(args)
        username = kwargs[Api.username]
        del kwargs[Api.username]
        args.append(username)
        if resource_inst.users.validate_username(username):
            if resource_inst.session.get_user(args[0]) == username:
                return resource_method(resource_inst, *args, **kwargs)
            else:
                resource_inst.response.status = 404
                return {}
        else:
            resource_inst.response.status = 404
            return {}

    return wrapper

"""
Handles valid user check for user routes
User need not be matched with session_key
"""
def verify_user(resource_method):

    def wrapper(resource_inst, *args, **kwargs):
        args = list(args)
        username = kwargs[Api.user]
        del kwargs[Api.user]
        args.append(username)
        if resource_inst.users.validate_username(username):
            return resource_method(resource_inst, *args, **kwargs)
        else:
            resource_inst.response.status = 404
            return {}

    return wrapper

"""
Handles validity check for msg id parameter
"""
def verify_msg_id(resource_method):

    def wrapper(resource_inst, *args, **kwargs):
        args = list(args)
        try:
            msg_id = int(kwargs[Api.msg_id_p])
        except (KeyError, ValueError):
            resource_inst.response.status = 400
            return {}
        del kwargs[Api.msg_id_p]
        args.append(msg_id)
        return resource_method(resource_inst, *args, **kwargs)

    return wrapper

"""
Handles validity check for channel existence
"""
def verify_channel(resource_method):

    def wrapper(resource_inst, *args, **kwargs):
        args = list(args)
        channel_name = kwargs[Api.channel]
        del kwargs[Api.channel]
        args.append(channel_name)
        if resource_inst.validate_channel_name(channel_name):
            return resource_method(resource_inst, *args, **kwargs)
        else:
            resource_inst.response.status = 404
            return {}

    return wrapper

