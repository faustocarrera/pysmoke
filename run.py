#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Burn motherfucker, burn
"""

import os
import click
from helper import AppConfig
from helper import Tests


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
    tests = Tests(get_app_url(), get_path('tests'))
    tests.run()


if __name__ == '__main__':
    cli()
