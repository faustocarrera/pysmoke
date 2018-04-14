#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test class
"""


class Tests(object):

    def __init__(self):
        self.test_to_run = None

    def test(self, request, tests_list):
        "Run tests_list"
        self.test_to_run = tests_list
        # elapsed time
        'Request elapsed time {0}'.format(request['elapsed_time'])
        # display response
        print(request['response'])
        # walk the tests_list
        for test in tests_list:
            if test[0] == 'http_status':
                print(self.http_status(test[1], request))
            else:
                print(self.__validate(test[0], test[1], request['response']))
        # close the tests
        print(' ')

    def http_status(self, expected, request):
        "Check http status"
        if request['http_status'] == expected:
            test_result = 'ok'
        else:
            test_result = 'error expected value {0} returned value {1}'.format(
                expected,
                request['http_status']
            )
        return 'HTTP status test {0}'.format(test_result)

    def __validate(self, index, value, request):
        "Validate the request with the tests"
        req_value = self.__get_value(index, request)
        # check for booleans
        if type(value) == type(True):
            return self.__test_boolean(index, value, req_value)
        else:
            return self.__test_equal(index, value, req_value)

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

    @staticmethod
    def __test_boolean(index, expected, returned):
        "Test true or false"
        if expected is True:
            if returned:
                test_result = 'ok'.format(expected, returned)
            else:
                test_result = 'error expected value {0} returned value {1}'.format(
                    expected,
                    returned
                )
        else:
            if returned:
                test_result = 'error expected value {0} returned value {1}'.format(
                    expected,
                    returned
                )
            else:
                test_result = 'ok'.format(expected, returned)
        return '{0} test {1}'.format(index, test_result)

    @staticmethod
    def __test_equal(index, expected, returned):
        "Test if two values are equal"
        if returned == expected:
            test_result = 'ok'.format(expected, returned)
        else:
            test_result = 'error expected value {0} returned value {1}'.format(
                expected,
                returned
            )
        return '{0} test {1}'.format(index, test_result)
