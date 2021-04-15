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
        files = []
        for file in listdir(path):
            if isfile(join(path, f)):
               files.append(f) 
        return files
        # return [f for f in listdir(path) if isfile(join(path, f))]

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
        if value == 'True':
            return True
        if value == 'False':
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
