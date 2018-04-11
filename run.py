#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Burn motherfucker, burn
"""

import os
import click
from helper import Config
from helper import AppConfig
from helper import ApiCalls
from pysmoke import SmokeTests


def get_path(filename):
    "Return file real path"
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


def get_app_url():
    "Get the app url"
    app_config = AppConfig(get_path('config/app.conf'))
    return app_config.appurl()


@click.command()
def cli():
    "Run your smoke tests from python" 
    tests = SmokeTests(get_path('tests'), ApiCalls(get_app_url()))
    tests.run(Config())


if __name__ == '__main__':
    cli()
