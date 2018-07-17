#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Pysmoke command entry point
"""

import os
import click
from helper import TestConfig
from helper import AppConfig
from helper import ApiCalls
from smoke import SmokeTests


def get_path(filename):
    "Return file real path"
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


@click.command()
@click.option('-c', '--config', 'config_path', default='config/app.conf', help='Config file path')
@click.option('-s', '--source', 'source_path', default='tests', help='Tests folder path')
@click.option('-f', '--filter', 'filtered_class', default='', help='Run just this test')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Verbose mode')
def cli(filtered_class, verbose, config_path, source_path):
    "Run your smoke tests from python"
    config = AppConfig(get_path(config_path))
    tests = SmokeTests(
        get_path(source_path),
        ApiCalls(config.appurl(), config.vars()),
        TestConfig()
    )
    tests.set_verbose(verbose)
    tests.set_filter(filtered_class)
    tests.run()


if __name__ == '__main__':
    cli()
