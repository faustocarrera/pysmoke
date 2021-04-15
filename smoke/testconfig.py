#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Handle the configuration file
"""

from os.path import join
import json
from pathlib import Path


class TestConfig(object):
    "Class to handle the configuration files"

    config = None

    def load(self, *args):
        "Load config file and parse the content"
        config_file = join(*args)
        filepath = Path(config_file)
        if filepath.resolve():
            with open(config_file) as json_file:
                self.config = json.loads(json_file.read())
            return self
        else:
            return None

    def sections(self):
        "Get the config sections"
        sections = []
        for section in self.config:
            sections.append(section)
        return sections

    def options(self, section):
        "Get options on the section"
        options = []
        for option in self.config[section]:
            options.append(option)
        return options

    def get(self, section, option):
        "Get the option value for the named section"
        return self.config[section][option]
