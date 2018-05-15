#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utils class
"""

class Utils(object):
    "Utils class"

    def parse_tests_string(self, tests_string):
        "Parse tests string to convert it to object"
        valid_tests = []
        tests_list = tests_string.split("\n")
        for entry in tests_list:
            if entry:
                test = entry.split(':')
                key = test[0].strip()
                value = self.__guess_value(test[1].strip())
                valid_tests.append((key, value))
        return valid_tests

    @staticmethod
    def __guess_value(value):
        "Guess value"
        # check if true or false
        if value == 'true':
            return True
        if value == 'false':
            return False
        # check if number
        try:
            return int(value)
        except ValueError:
            pass
        # check if float
        try:
            return float(value)
        except ValueError:
            pass
        # just return the value
        return value

    @staticmethod
    def get_dummy_response():
        "Dummy server response"
        return {
            'elapsed_time': 0.10376,
            'http_status': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'ORIGIN, X-REQUESTED-WITH, AUTHORIZATION',
                'Keep-Alive': 'timeout=5, max=100',
                'Access-Control-Max-Age': '60000',
                'Content-Type': 'application/json',
                'expires': '-1',
                'Access-Control-Allow-Credentials': 'true',
                'Server': 'Apache/2.4.18 (Ubuntu)',
                'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT, DELETE',
                'Content-Length': '81',
                'pragma': 'no-cache',
                'Date': 'Sat, 14 Apr 2018 20:43:57 GMT',
                'Cache-Control': 'private, must-revalidate',
                'Connection': 'Keep-Alive',
                'Access-Control-Allow-Origin': '*'
            },
            'response': {
                'metadata': None,
                'result': {
                    'version': '0.8.0',
                    'API': 'Sistema Nacional de Turnos'
                }
            }
        }
