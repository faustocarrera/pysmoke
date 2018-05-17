#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pysmoke class
"""

from __future__ import print_function
import sys
from os import listdir
from os.path import isfile
from os.path import join
from smoke.tests import Tests
from smoke.utils import Utils


class SmokeTests(object):
    "Class to run the tests"

    def __init__(self, tests_src, api_calls):
        "Entry point"
        self.pytest = Tests()
        self.utils = Utils()
        self.tests_src = tests_src
        self.api_calls = api_calls
        self.total_tests = 0
        self.tests_list = self.list_tests(tests_src)
        self.tests_to_run = {}

    def set_verbose(self, verbose):
        "Set the verbose flag"
        self.verbose = verbose

    def set_filter(self, filtered_class):
        "Set the filtered class to run"
        self.filtered_class = filtered_class

    @staticmethod
    def list_tests(path):
        "Return a list of test on the folder"
        return [f for f in listdir(path) if isfile(join(path, f))]

    def run(self, config):
        "Load and run the tests"
        self.load_tests(config)
        errors = self.run_tests()
        self.show_errors(self.total_tests, errors)

    def compose(self, config, filename):
        "Parse config sections"
        count = 0
        for section in config.sections():
            index = '{0}::{1}::{2}'.format(filename, count, section)
            self.tests_to_run[index] = self.options(config, section)
            count += 1
        return None

    def load_tests(self, config):
        "Load the tests to run"
        # run just the filtered class
        if self.filtered_class:
            config.load(join(self.tests_src, self.filtered_class))
            self.compose(config, self.filtered_class)
            return
        # run all the tests
        for test_file in self.tests_list:
            config.load(join(self.tests_src, test_file))
            self.compose(config, test_file)
        return

    @staticmethod
    def options(config, section):
        "Get options"
        options = {}
        count = 0
        for option in config.options(section):
            options[option] = config.get(section, option)
            count += 1
        return options

    def run_tests(self):
        "Run the tests"
        for key in sorted(self.tests_to_run.keys()):
            # display wich test are we running
            index_parts = key.split('::')
            error_index = '{0} :: {1}'.format(index_parts[0], index_parts[2])
            # end display
            test = self.tests_to_run[key]
            tests = self.utils.parse_tests_string(test['tests'])
            # total tests to run
            self.total_tests += len(tests)
            # response = self.utils.get_dummy_response()
            response = self.api_calls.call(test)
            # verbose mode
            if self.verbose:
                self.__verbose(
                    test['method'],
                    index_parts[0],
                    index_parts[2],
                    self.api_calls.get_api_url(),
                    test,
                    response
                )
            # run tests  on the response
            self.pytest.test(self.verbose, response, tests, error_index)
        # the errors
        return self.pytest.get_errors()

    @staticmethod
    def show_errors(total_tests, errors):
        "Show error in the console"
        total_errors = len(errors)
        # display errors
        if total_errors > 0:
            print('Executed {0} tests found {1} errors'.format(
                total_tests,
                total_errors
            ))
            for error in errors:
                print('{0}'.format(error))
        # exit program
        if total_errors > 0:
            sys.exit(1)
        sys.exit(0)

    @staticmethod
    def __verbose(method, filename, testname, apiurl, test, response):
        "Print request and response data"
        print('Test: {0} :: {1}'.format(filename, testname))
        print('Endpoint: {0}{1}'.format(apiurl, test['url']))
        print('Method: {0}'.format(method))
        print('Authorization: {0}'.format(test['authorization']))
        print('Payload:')
        print(test['payload'])
        print('Response:')
        for item in response:
            print('{0}: {1}'.format(item, response[item]))
        print('')
