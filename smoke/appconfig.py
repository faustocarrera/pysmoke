#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
App config
"""

from .testconfig import TestConfig


class AppConfig(TestConfig):
    "Global app configuration"

    def __init__(self, config_file):
        "Load app config"
        self.load(config_file)

    def app_url(self):
        "Get app url"
        return self.get('app', 'url')

    def ssl_verify(self):
        "Get verify ssl"
        ssl_verify = self.get('app', 'ssl_verify')
        if ssl_verify == 'True':
            return True
        return False

    def vars(self):
        "Get the config variables"
        app_variables = {}
        variables = self.options('vars')
        for var in variables:
            app_variables[var] = self.get('vars', var)
        return app_variables

    def debug(self):
        "Module debug"
        return  {'app_url': self.app_url(), 'vars': self.vars()}
