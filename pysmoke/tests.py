#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test class
"""

import sys


class Tests(object):

    def __init__(self):
        pass

    def test(self, request, tests):
        "Run tests"
        self.tests = tests
        # elapsed time
        'Request elapsed time {0}'.format(request['elapsed_time'])
        # display response
        print(request['response'])
        # http_status
        print(self.http_status(request, tests))
        # walk the tests
        for test in tests:
            print(self.__validate(test, tests[test], request['response']))
        # close the tests
        print(' ')
        # print(request)
        # print(tests)

    def http_status(self, request, tests):
        "Check http status"
        if 'http_status' in self.tests.keys():
            if request['http_status'] == tests['http_status']:
                test_result = 'ok'
            else:
                test_result = 'error expected value {0} returned value {1}'.format(
                    tests['http_status'],
                    request['http_status']
                )
            self.tests.pop('http_status', 0)
            return 'HTTP status test {0}'.format(test_result)
        return None

    def __validate(self, index, value, request):
        "Validate the request with the tests"
        req_value = self.__get_value(index, request)
        if type(value) == type(True) and value is not None:
            test_result = 'ok expected value {0} returned value {1}'.format(value, req_value)
        elif req_value == value:
            test_result = 'ok expected value {0} returned value {1}'.format(value, req_value)
        else:
            test_result = 'error expected value {0} returned value {1}'.format(value, req_value)
        return '{0} test {1}'.format(index, test_result)

    @staticmethod
    def __get_value(index, request):
        "Get the request value"
        index_parts = index.split('.')
        value = None
        for ind in index_parts:
            if ind in request.keys():
                value = request[ind]
                request = request[ind]
        return value
