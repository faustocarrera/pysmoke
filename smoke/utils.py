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


def get_path(basepath, filename):
    "Return file real path"
    return os.path.join(os.path.dirname(os.path.realpath(basepath)), filename)


def vars_replace(string, variables):
    "Find and replace config variables from strings"
    finder = re.findall('%([a-zA-Z0-9_]+)%', string)
    for match in finder:
        find = '%{0}%'.format(match)
        if variables.has_key(match):
            string = string.replace(find, variables[match])
    return string

def list_files(path):
    "Return a list of test on the folder"
    return [f for f in listdir(path) if isfile(join(path, f))]
