
import requests

class Rest(object):
    def __init__(self, root_url):
        self.root_url = root_url
        self.headers = {
            'Content-Type': 'application/json'
        }

    def post(self, uri, data):
        response = requests.post(self.root_url + uri, data=data, headers=self.headers
        print(response)
        return response
