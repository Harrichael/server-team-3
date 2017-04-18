"""
Rest methods abstracted into how we user them for our server
"""

import json
import requests

def rest_wrapper(rest_func):
    def wrapper(*args, **kwargs):
        response = rest_func(*args, **kwargs)
        print(response.status_code)
        print(response.json())
        return response
    return wrapper

class Rest(object):
    def __init__(self, root_url):
        self.root_url = root_url
        self.headers = {
            'Content-Type': 'application/json'
        }

    def set_header(self, key, value):
        self.headers[key] = value

    @rest_wrapper
    def post(self, uri, data):
        return requests.post(self.root_url + uri, data=json.dumps(data), headers=self.headers)

    @rest_wrapper
    def put(self, uri, data):
        return requests.put(self.root_url + uri, data=json.dumps(data), headers=self.headers)

    @rest_wrapper
    def get(self, uri):
        return requests.get(self.root_url + uri, headers=self.headers)

    @rest_wrapper
    def delete(self, uri):
        return requests.delete(self.root_url + uri, headers=self.headers)

