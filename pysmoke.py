#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Pysmoke
Test your API endpoints from the command line
"""

import click


@click.command()
@click.option('-c', '--config', 'config_path', default='config/app.conf', help='Config file path')
@click.option('-s', '--source', 'source_path', default='tests', help='Tests folder path')
@click.option('-f', '--filter', 'filtered_class', default=None, help='Run just this test')
@click.option('-v', '--verbose', is_flag=True, default=False, help='Verbose mode')
def cli(config_path, source_path, filtered_class, verbose):
    "Pysmoke entry point"
    print(config_path)
    print(source_path)
    print(filtered_class)
    print(verbose)


if __name__ == '__main__':
    cli()
