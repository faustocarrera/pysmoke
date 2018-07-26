#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Handle the configuration file
"""

from os.path import join
import configparser
from pathlib import Path


class TestConfig(object):
    "Class to handle the configuration files"

    config_parser = None

    def load(self, *args):
        "Load config file and parse the content"
        config_file = join(*args)
        filepath = Path(config_file)
        if filepath.resolve():
            self.config_parser = configparser.RawConfigParser()
            self.config_parser.read(config_file)
            return self
        else:
            return None

    def sections(self):
        "Get the config sections"
        return self.config_parser.sections()

    def options(self, section):
        "Get options on the section"
        return self.config_parser.options(section)

    def get(self, section, option):
        "Get the option value for the named section"
        return self.config_parser.get(section, option)