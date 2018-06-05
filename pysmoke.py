#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Pysmoke command entry point
"""

import os
import click
from helper import Config
from helper import AppConfig
from helper import ApiCalls
from smoke import SmokeTests


def get_path(filename):
    "Return file real path"
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


@click.command()
@click.option('-f', '--filter', 'filtered_class', default='', help='Run just this test')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Verbose mode')
def cli(filtered_class, verbose):
    "Run your smoke tests from python"
    config = AppConfig(get_path('config/app.conf'))
    tests = SmokeTests(
        get_path('tests'),
        ApiCalls(config.appurl(), config.vars())
    )
    tests.set_verbose(verbose)
    tests.set_filter(filtered_class)
    tests.run(Config())


if __name__ == '__main__':
    cli()
