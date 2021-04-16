#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Utils functions
"""

import os
import re
import json
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
        if string:
            # check if we have a dictionary
            if isinstance(string, dict):
                string = json.dumps(string)
            # find the places we have to replace
            finder = re.findall('%([a-zA-Z0-9_]+)%', string)
            for match in finder:
                find = '%{0}%'.format(match)
                if match in variables.keys():
                    string = string.replace(find, str(variables[match]))
        return string

    @staticmethod
    def list_files(path):
        "Return a list of test on the folder"
        return [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('_test.json')]

    @staticmethod
    def guess_value(value):
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

    @staticmethod
    def get_test_name(test_name):
        "Remove the .json from the test name"
        parts = test_name.split('_')
        return parts[0]
