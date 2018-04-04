#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
App config
"""

from .config import Config


class AppConfig(Config):
    
    def __init__(self, config_file):
        "Load app config"
        self.load(config_file)
    
    def appurl(self):
        "Get app url"
        return self.get('app', 'url')
