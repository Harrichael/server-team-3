
import requests

class Rest(object):
    def __init__(self, root_url):
        self.root_url = root_url
        self.headers = {
            'Content-Type': 'application/json'
        }

    def post(self, uri, data):
        return requests.post(self.root_url + uri, data=data, headers=self.headers)

    def put(self, uri, data):
        return requests.put(self.root_url + uri, data=data, headers=self.headers)

    def get(self, uri):
        return requests.get(self.root_url + uri, headers=self.headers)

    def delete(self, uri):
        return requests.delete(self.root_url + uri, headers=self.headers)