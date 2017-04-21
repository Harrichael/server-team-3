"""
Sets up the server
"""

import lib.bottle.bottle as bottle

from server.api import Api
from server.routes import add_resource
from server.session import Session
from server.users import Users
from server.channels import Channels
from server.static import Static, Client

def setup_app():
    bottle.response.headers['Content-Type'] = 'application/json' 

    session_inst = Session()
    users_inst = Users()
    channels_inst = Channels(session_inst, users_inst)
    static_inst = Static()
    client_inst = Client()
    session_inst.set_users_resource(users_inst)
    users_inst.set_session_resource(session_inst)

    add_resource('/' + Api.api + '/' + Api.session, session_inst)
    add_resource('/' + Api.api + '/' + Api.users, users_inst)
    add_resource('/' + Api.api + '/' + Api.channels, channels_inst)
    add_resource('/web', static_inst)
    add_resource('', client_inst)

def run(host, port, debug=False):
    setup_app()
    bottle.run(host=host, port=port, debug=debug)

