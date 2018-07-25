#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pysmoke class
"""

from os.path import join
from . import utils
from .testconfig import TestConfig
from .appconfig import AppConfig
from .apicalls import ApiCalls


class SmokeTests(object):
    "Class to run the tests"

    def __init__(self, config_path, tests_path):
        self.tests_config = TestConfig()
        self.app_config = AppConfig(config_path)
        self.api_calls = ApiCalls(
            self.app_config.appurl(), self.app_config.vars())
        self.tests_path = tests_path
        self.verbose = False
        self.filtered_class = ''
        self.single_test = None

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
        tests = self.load_tests(self.tests_path)
        print(tests)

    def load_tests(self, test_path):
        "Load tests from config files"
        tests_to_run = {}
        tests_files = utils.list_files(test_path)
        # just one filtered class
        if self.filtered_class:
            self.tests_config.load(join(self.tests_path, self.filtered_class))
            return self.compose(self.filtered_class)
        # run all the tests
        for tests_file in tests_files:
            self.tests_config.load(join(self.tests_path, tests_file))
            tests_to_run.update(self.compose(tests_file))
        return tests_to_run

    def compose(self, filename):
        "Parse config sections"
        tests_to_run = {}
        count = 0
        # if we have a single test
        if self.single_test:
            index = '{0}::{1}::{2}'.format(filename, count, self.single_test)
            tests_to_run[index] = self.options(
                self.tests_config, self.single_test)
            return tests_to_run
        # load all sections
        for section in self.tests_config.sections():
            index = '{0}::{1}::{2}'.format(filename, count, section)
            tests_to_run[index] = self.options(self.tests_config, section)
            count += 1
        return tests_to_run

    @staticmethod
    def options(config, section):
        "Get options"
        options = {}
        for option in config.options(section):
            options[option] = config.get(section, option)
        return options

    def debug(self):
        "Print the data entered to the module"
        print(self.app_config.debug())
        print(self.tests_path)
        print(self.verbose)
        print(self.filtered_class)
