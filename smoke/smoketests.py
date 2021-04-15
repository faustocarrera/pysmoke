#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pysmoke class
"""

from __future__ import print_function
import sys
from .utils import Utils
from .testconfig import TestConfig
from .appconfig import AppConfig
from .apicalls import ApiCalls
from .validator import Validator


class SmokeTests(object):
    "Class to run the tests"

    def __init__(self, basepath, config_path, tests_path):
        self.validator = Validator()
        self.utils = Utils()
        self.tests_config = TestConfig()
        self.app_config = AppConfig(self.utils.get_path(basepath, config_path))
        self.api_calls = ApiCalls(
            self.app_config.app_url(),
            self.app_config.vars(),
            self.app_config.ssl_verify(),
            self.utils
        )
        self.tests_path = self.utils.get_path(basepath, tests_path)
        self.tests_to_run = {}
        self.verbose = False
        self.filtered_class = ''
        self.single_test = None
        self.total_tests = 0

    def set_verbose(self, verbose):
        "Set the verbose flag"
        self.verbose = verbose

    def set_filter(self, filtered_class):
        "Set the filtered class to run"
        if filtered_class and ':' in filtered_class:
            parts = filtered_class.split(':')
            self.filtered_class = parts[0]
            self.single_test = parts[1]
        else:
            self.filtered_class = filtered_class

    def run(self):
        "Load and run the tests"
        self.tests_to_run = self.load_tests(self.tests_path)
        errors = self.run_thread(self.tests_to_run)
        self.show_errors(self.total_tests, errors)

    def load_tests(self, test_path):
        "Load tests from config files"
        tests_to_run = {}
        tests_files = self.utils.list_files(test_path)
        # just one filtered class
        if self.filtered_class:
            self.tests_config.load(self.tests_path, self.filtered_class)
            return self.compose(self.filtered_class)
        # run all the tests
        for tests_file in tests_files:
            self.tests_config.load(self.tests_path, tests_file)
            tests_to_run.update(self.compose(tests_file))
        return tests_to_run

    def compose(self, filename):
        "Parse config sections"
        tests_to_run = {}
        # if we have a single test
        if self.single_test:
            index = '{0}::{1}::{2}'.format(filename, 0, self.single_test)
            tests_to_run[index] = self.options(
                self.tests_config,
                self.single_test
            )
            return tests_to_run
        # load all sections
        for section in self.tests_config.sections():
            index = '{0}::{1}'.format(filename, section)
            tests_to_run[index] = self.options(self.tests_config, section)
        return tests_to_run

    def run_thread(self, tests):
        "Run the tests"
        for test in tests:
            self.run_tests(test)
        return self.validator.get_errors()

    def run_tests(self, key):
        "Run the test"
        # display wich test are we running
        index_parts = key.split('::')
        error_index = '{0} :: {1}'.format(index_parts[0], index_parts[1])
        # end display
        test = self.tests_to_run[key]
        tests = self.utils.parse_tests(test['tests'])
        # total tests to run
        self.total_tests += len(tests)
        # make the call
        response = self.api_calls.call(test)
        # verbose mode
        if self.verbose:
            self.__verbose(
                test['method'],
                index_parts[0],
                index_parts[1],
                test,
                response
            )
        # run tests  on the response
        self.validator.test(
            self.verbose,
            response['response'],
            tests,
            error_index
        )

    @staticmethod
    def options(config, section):
        "Get options"
        options = {}
        for option in config.options(section):
            options[option] = config.get(section, option)
        return options

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
    def __verbose(method, filename, testname, test, response):
        "Print request and response data"
        print('Test: {0} :: {1}'.format(filename, testname))
        print('Endpoint: {0}'.format(response['url']))
        print('Method: {0}'.format(method))
        print('Authorization: {0}'.format(test['authorization']))
        print('Payload: {0}'.format(response['payload']))
        for item in response['response']:
            print('Response {0}: {1}'.format(item, response['response'][item]))
        print('')
