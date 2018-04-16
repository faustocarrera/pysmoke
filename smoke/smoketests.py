#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pysmoke class
"""

from os import listdir
from os.path import isfile
from os.path import join
from smoke.tests import Tests


class SmokeTests():

    def __init__(self, tests_src, api_calls):
        "Entry point"
        self.pytest = Tests()
        self.tests_src = tests_src
        self.api_calls = api_calls
        self.tests_list = self.list_tests(tests_src)
        self.tests_to_run = {}

    def list_tests(self, path):
        "Return a list of test on the folder"
        return [f for f in listdir(path) if isfile(join(path, f))]

    def run(self, config):
        "Load and pysmoke the tests"
        for test_file in self.tests_list:
            config.load(join(self.tests_src, test_file))
            self.compose(config, test_file)
        # pysmoke the tests
        self.run_tests()

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
            print('Running test {1} from {0}'.format(index_parts[0], index_parts[2]))
            # end display
            test = self.tests_to_run[key]
            tests = self.parse_tests_string(test['tests'])
            response = self.api_calls.call(test)
            # response = self.__get_dummy_response()
            self.pytest.test(response, tests)

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
    def __get_dummy_response():
        return {
            'elapsed_time': 0.10376,
            'http_status': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'ORIGIN, X-REQUESTED-WITH, CONTENT-TYPE, AUTHORIZATION',
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
