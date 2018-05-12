#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Make API calls
"""

import requests
import json


class ApiCalls():

    def __init__(self, app_url):
        self.app_url = app_url

    def call(self, test):
        url = self.app_url + test['url']
        method = test['method']
        headers = {'authorization': test['authorization']}
        payload = self.convert_payload(test['payload'])
        if method == 'GET':
            return self.get(url, headers, payload)
        if method == 'POST':
            return self.post(url, headers, payload)
        if method == 'PUT':
            return self.put(url, headers, payload)
        if method == 'DELETE':
            return self.delete(url, headers, payload)
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

    def get_api_url(self):
        "Get the API url"
        return self.app_url

    @staticmethod
    def convert_payload(payload):
        "Try to convert payload to object or leave it"
        try:
            return json.loads(payload)
        except ValueError:
            return payload

    @staticmethod
    def prepare(request):
        return {
            'http_status': request.status_code,
            'headers': request.headers,
            'response': request.json(),
            'elapsed_time': request.elapsed.total_seconds()
        }
