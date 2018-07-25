#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Utils functions
"""

import os
import re


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
