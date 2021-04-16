#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test class
"""


class Validator(object):
    "Class to validate the tests"

    def __init__(self):
        self.test_to_run = None
        self.errors = []

    def test(self, verbose, response, tests_list, error_index):
        "Run tests_list"
        if verbose:
            print('Tests running')
        # walk the tests_list
        for test in tests_list:
            if verbose:
                print('checkig if {0} is {1}'.format(test[0], test[1]))
            # run tests
            if test[0] == 'http_status':
                self.__add_error(
                    error_index,
                    self.http_status(test[1], response['http_status'])
                )
            else:
                self.__add_error(
                    error_index,
                    self.__validate(test[0], test[1], response)
                )
        if verbose:
            print('')
        return self.errors

    def get_errors(self):
        "Return errors list"
        return self.errors

    @staticmethod
    def http_status(expected, http_status):
        "Check http status"
        if http_status == expected:
            return None

        return 'HTTP status error expected value {0} returned value {1}'.format(
            expected,
            http_status
        )

    def __validate(self, index, value, response):
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
        # response type
        if index_parts[0] == 'headers':
            return self.__get_dict_value(index_parts[1], response['headers'])
        else:
            return self.__get_response_value(index_parts, response['response'])

    def __get_response_value(self, index_parts, response):
        "Obtain an item from the response"
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
            return 'IndexError'

    @staticmethod
    def __get_dict_value(index, items):
        "Get the item from a dictionary with items"
        if index in items.keys():
            return items[index]
        return 'IndexError'

    @staticmethod
    def __test_boolean(index, expected, returned):
        "Test true or false"
        # the attribute must exists
        if expected is True:
            if returned == 'IndexError':
                return '{0} :: error attribute not found'.format(index)
            return None
        # the attribute must not exists
        if expected is False:
            if returned == 'IndexError':
                return None
            return '{0} :: error attribute found'.format(index)

    @staticmethod
    def __test_equal(index, expected, returned):
        "Test if two values are equal"
        # test if the attribute exists
        if returned == 'IndexError':
            return '{0} :: error attribute not found'.format(index)
        # test if null is expected
        if expected == 'null' and returned is None:
            return None
        # test if equal
        if returned == expected:
            return None
        # error
        return '{0} :: error expected value {1} returned value {2}'.format(
            index,
            expected,
            returned
        )
