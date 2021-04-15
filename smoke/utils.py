#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Utils functions
"""

import os
import re
from os import listdir
from os.path import isfile
from os.path import join


class Utils(object):
    "Utils class"

    @staticmethod
    def get_path(basepath, filename):
        "Return file real path"
        if basepath:
            return os.path.join(os.path.dirname(os.path.realpath(basepath)), filename)
        return filename

    @staticmethod
    def vars_replace(string, variables):
        "Find and replace config variables from strings"
        finder = re.findall('%([a-zA-Z0-9_]+)%', string)
        for match in finder:
            find = '%{0}%'.format(match)
            if match in variables.keys():
                string = string.replace(find, variables[match])
        return string

    @staticmethod
    def list_files(path):
        "Return a list of test on the folder"
        return [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('_test.json')]

    def parse_tests(self, tests_object):
        "Parse tests string to convert it to object"
        valid_tests = []
        for entry in tests_object:
            key = entry.strip()
            value = self.__guess_value(tests_object[entry])
            valid_tests.append((key, value))
        return valid_tests

    @staticmethod
    def __guess_value(value):
        "Guess value"
        # check if true or false
        if isinstance(value, str):    
            if value.lower() == 'true':
                return True
            if value.lower() == 'false':
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
