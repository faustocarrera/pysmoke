#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pysmoke class
"""

from os import listdir
from os.path import isfile
from os.path import join
from smoke.tests import Tests
from smoke.utils import Utils
import sys


class SmokeTests(object):

    def __init__(self, tests_src, api_calls, verbose):
        "Entry point"
        self.pytest = Tests()
        self.utils = Utils()
        self.tests_src = tests_src
        self.api_calls = api_calls
        self.tests_list = self.list_tests(tests_src)
        self.tests_to_run = {}
        self.verbose = verbose

    def list_tests(self, path):
        "Return a list of test on the folder"
        return [f for f in listdir(path) if isfile(join(path, f))]

    def run(self, config):
        "Load and pysmoke the tests"
        for test_file in self.tests_list:
            config.load(join(self.tests_src, test_file))
            self.compose(config, test_file)
        # pysmoke the tests
        errors = self.run_tests()
        self.show_errors(errors)

    def compose(self, config, filename):
        "Parse config sections"
        count = 0
        for section in config.sections():
            index = '{0}::{1}::{2}'.format(filename, count, section)
            self.tests_to_run[index] = self.options(config, section)
            count += 1
        return None

    def options(self, config, section):
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
            response = self.api_calls.call(test)
            # verbose mode
            self.__verbose(
                self.verbose,
                index_parts[0],
                index_parts[2],
                self.api_calls.get_api_url(),
                test['url'],
                test['payload'],
                response
            )
            # response = self.utils.get_dummy_response()
            self.pytest.test(response, tests, error_index)
        # the errors
        return self.pytest.get_errors()

    def show_errors(self, errors):
        "Show error in the console"
        for error in errors:
            print(error, file=sys.stderr)
        # exit program
        if len(errors):
            sys.exit(1)
        sys.exit(0)

    @staticmethod
    def __verbose(verbose, filename, testname, apiurl, testurl, payload, response):
        "Print request and response data"
        if verbose:
            print('File: {0}'.format(filename))
            print('Test: {0}'.format(testname))
            print('API: {0}'.format(apiurl))
            print('Resource: {0}'.format(testurl))
            print('Payload')
            print(payload)
            print('Response')
            for item in response:
                print('{0}: {1}'.format(item, response[item]))
            print('')
