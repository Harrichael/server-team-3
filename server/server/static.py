"""
Serves up our static files
"""

from lib.bottle.bottle import static_file
from server.resource import Resource
from server.routes import route

class Static(Resource):
    @route('<filepath:re:(?!static).*>')
    def get_html(self, filepath):
        return static_file(filepath + '.html', root='server/static/html')

    @route('static/css/<filepath:re:.*\.css>')
    def get_css(self, filepath):
        return static_file(filepath, root='server/static/css')

    @route('static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>')
    def get_img(self, filepath):
        return static_file(filepath, root='server/static/img')

    @route('static/js/<filepath:re:.*\.js>')
    def get_js(self, filepath):
        return static_file(filepath, root='server/static/js')

class Client(Resource):
    @route('<filepath:re:(?!(web|api|client)).*>')
    def get_html(self, filepath):
        return static_file(filepath + '.html', root='server/lib/ChatBareBones2/html')

    @route('client/css/<filepath:re:.*\.css>')
    def get_css(self, filepath):
        return static_file(filepath, root='server/lib/ChatBareBones2/css')

    @route('client/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>')
    def get_img(self, filepath):
        return static_file(filepath, root='server/lib/ChatBareBones2/img')

    @route('client/js/<filepath:re:.*\.js>')
    def get_js(self, filepath):
        return static_file(filepath, root='server/lib/ChatBareBones2/js')

