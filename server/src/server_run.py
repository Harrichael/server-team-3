"""
Sets up the server
"""

import lib.bottle.bottle as bottle

@bottle.route('/hello')
def hello():
    return 'Hello World'

def run(host, port, debug=False):
    bottle.run(host=host, port=port, debug=debug)
