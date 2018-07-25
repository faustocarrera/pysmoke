#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Pysmoke
Test your API endpoints from the command line
"""

from smoke import utils
from smoke import SmokeTests
import click


@click.command()
@click.option('-c', '--config', 'config_path', default='config/app.conf', help='Config file path')
@click.option('-s', '--source', 'source_path', default='tests', help='Tests folder path')
@click.option('-f', '--filter', 'filtered_class', default=None, help='Run just this test')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Verbose mode')
def cli(config_path, source_path, filtered_class, verbose):
    "Pysmoke entry point"
    smoke = SmokeTests(
        utils.get_path(__file__, config_path),
        utils.get_path(__file__, source_path)
    )
    smoke.set_filter(filtered_class)
    smoke.set_verbose(verbose)
    smoke.run()


if __name__ == '__main__':
    cli()
