#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
App config
"""

from .config import Config
from os import listdir
from os.path import isfile
from os.path import join


class Tests(Config):

    def __init__(self, app_url, tests_src):
        "Entry point"
        self.app_url = app_url
        self.tests_list = self.list_tests(tests_src)

    def list_tests(self, path):
        "Return a list of test on the folder"
        return [f for f in listdir(path) if isfile(join(path, f))]

    def run(self):
        pass
