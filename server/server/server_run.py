"""
Sets up the server
"""

import lib.bottle.bottle as bottle

from server.routes import set_routes
from server.session import Session
from server.users import Users
from server.channels import Channels
from server.static import Static

def setup_app():
    bottle.response.headers['Content-Type'] = 'application/json' 

    session_inst = Session()
    users_inst = Users()
    channels_inst = Channels(session_inst, users_inst)
    static_inst = Static()
    session_inst.set_users_resource(users_inst)
    users_inst.set_session_resource(session_inst)

    set_routes(
        session_inst,
        users_inst,
        channels_inst,
        static_inst,
    )

def run(host, port, debug=False):
    setup_app()
    bottle.run(host=host, port=port, debug=debug)
