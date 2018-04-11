#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Handle the configuration file
"""

import configparser


class Config(object):
    "Class to handle the configuration files"

    config_parser = None

    def load(self, config_file):
        "Load config file and parse the content"
        self.config_parser = configparser.RawConfigParser()
        self.config_parser.read(config_file)
        return self

    def sections(self):
        "Get the config sections"
        return self.config_parser.sections()

    def options(self, section):
        "Get options on the section"
        return self.config_parser.options(section)

    def get(self, section, option):
        "Get the option value for the named section"
        return self.config_parser.get(section, option)
