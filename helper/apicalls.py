#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Make API calls
"""

import requests


class ApiCalls():

    def __init__(self, app_url):
        self.app_url = app_url

    def call(self, test):
        method = test['method']
        url = self.app_url + test['url']
        headers = {'authorization': test['authorization']}
        if method == 'GET':
            return self.get(url, headers, test['payload'])
        if method == 'POST':
            return self.post(url, headers, test['payload'])
        if method == 'PUT':
            return self.put(url, headers, test['payload'])
        if method == 'DELETE':
            return self.delete(url, headers, test['payload'])
        return None

    def get(self, url, headers, payload):
        "Make a get call"
        req = requests.get(url, headers=headers, data=payload)
        return self.prepare(req)
    
    def post(self, url, headers, payload):
        "Make a post call"
        req = requests.post(url, headers=headers, data=payload)
        return self.prepare(req)
    
    def put(self, url, headers, payload):
        "Make a put call"
        req = requests.put(url, headers=headers, data=payload)
        return self.prepare(req)
    
    def delete(self, url, headers, payload):
        "Make a get call"
        req = requests.delete(url, headers=headers, data=payload)
        return self.prepare(req)

    @staticmethod
    def prepare(request):
        return {
            'http_status': request.status_code,
            'headers': request.headers,
            'response': request.json(),
            'elapsed_time': request.elapsed.total_seconds()
        }
