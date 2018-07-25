#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pysmoke class
"""


class SmokeTests(object):
    "Class to run the tests"

    def __init__(self, config_path, tests_path):
        self.config_path = config_path
        self.tests_path = tests_path
        self.verbose = False
        self.filtered_class = ''

    def set_verbose(self, verbose):
        "Set the verbose flag"
        self.verbose = verbose

    def set_filter(self, filtered_class):
        "Set the filtered class to run"
        self.filtered_class = filtered_class

    def debug(self):
        print(self.config_path)
        print(self.tests_path)
        print(self.verbose)
        print(self.filtered_class)
