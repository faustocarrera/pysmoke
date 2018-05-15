#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test class
"""


class Tests(object):
    "Class to validate the tests"

    def __init__(self):
        self.test_to_run = None
        self.errors = []

    def test(self, request, tests_list, error_index):
        "Run tests_list"
        # walk the tests_list
        for test in tests_list:
            if test[0] == 'http_status':
                self.__add_error(
                    error_index,
                    self.http_status(test[1], request)
                )
            else:
                self.__add_error(
                    error_index,
                    self.__validate(test[0], test[1], request['response'])
                )
        return self.errors

    def get_errors(self):
        "Return errors list"
        return self.errors

    @staticmethod
    def http_status(expected, request):
        "Check http status"
        if request['http_status'] == expected:
            return None

        return 'HTTP status error expected value {0} returned value {1}'.format(
            expected,
            request['http_status']
        )

    def __validate(self, index, value, response):
        "Validate the response with the tests"
        req_value = self.__get_value(index, response)
        # check for booleans
        if isinstance(value, bool):
            return self.__test_boolean(index, value, req_value)
        # return default
        return self.__test_equal(index, value, req_value)

    def __add_error(self, index, error):
        "Add error to list"
        if error:
            self.errors.append('{0} :: {1}'.format(index, error))

    def __get_value(self, index, response):
        "Get the response value"
        index_parts = index.split('.')
        value = None
        for ind in index_parts:
            if isinstance(response, list):
                value = self.__get_list_value(ind, response)
                response = value
            elif isinstance(response, dict):
                value = self.__get_dict_value(ind, response)
                response = value
        return value

    @staticmethod
    def __get_list_value(index, items):
        "Get the item from a list of items"
        try:
            return items[int(index)]
        except IndexError:
            return None

    @staticmethod
    def __get_dict_value(index, items):
        "Get the item from a dictionary with items"
        if index in items.keys():
            return items[index]
        return None

    @staticmethod
    def __test_boolean(index, expected, returned):
        "Test true or false"
        if expected is True:
            if returned:
                return None
            # error
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
            # default
            return None

    @staticmethod
    def __test_equal(index, expected, returned):
        "Test if two values are equal"
        if returned == expected:
            return None
        # error
        return '{0} error expected value {1} returned value {2}'.format(
            index,
            expected,
            returned
        )
