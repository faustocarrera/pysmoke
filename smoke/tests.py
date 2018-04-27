#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test class
"""


class Tests(object):

    def __init__(self):
        self.test_to_run = None
        self.errors = {}

    def test(self, request, tests_list, error_index):
        "Run tests_list"
        self.test_to_run = tests_list
        # walk the tests_list
        for test in tests_list:
            self.errors[error_index] = []
            if test[0] == 'http_status':
                self.__add_error(error_index, self.http_status(test[1], request))
            else:
                self.__add_error(error_index, self.__validate(test[0], test[1], request['response']))
        print(self.errors)
        
    def get_errors(self):
        "Return errors list"
        return self.errors

    def http_status(self, expected, request):
        "Check http status"
        if request['http_status'] == expected:
            return None
        else:
            return 'HTTP status error expected value {0} returned value {1}'.format(
                expected,
                request['http_status']
            )

    def __validate(self, index, value, request):
        "Validate the request with the tests"
        req_value = self.__get_value(index, request)
        # check for booleans
        if type(value) == type(True):
            return self.__test_boolean(index, value, req_value)
        else:
            return self.__test_equal(index, value, req_value)

    def __add_error(self, index, error):
        "Add error to list"
        if error:
            self.errors[index].append(error)

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
                return None
            else:
                return '{0} error expected value {1} returned value {2}'.format(
                    index,
                    expected,
                    returned
                )
        else:
            if returned:
                return '{0} error expected value {1} returned value {2}'.format(
                    index,
                    expected,
                    returned
                )
            else:
                return None

    @staticmethod
    def __test_equal(index, expected, returned):
        "Test if two values are equal"
        if returned == expected:
            return None
        else:
            return '{0} error expected value {1} returned value {2}'.format(
                index,
                expected,
                returned
            )
