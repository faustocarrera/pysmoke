#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = open('README.md').read()

PACKAGE_NAME = 'pysmoke'
VERSION = '2.0.0'

with open('requirements.txt') as file_requirements:
    requirements = file_requirements.read().splitlines()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    install_requires=requirements,
    author='Fausto Carrera',
    author_email='fausto.carrera@gmx.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://faustocarrera.github.io/pysmoke/',
    license='GNU GENERAL PUBLIC LICENSE',
    description='A command line tool to run smoke tests in your REST API using python and just config files.',
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'pysmoke=smoke.standalone:cli'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ]
)
