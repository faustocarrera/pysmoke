#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Utils
"""

import os

def get_path(filename):
    "Return file real path"
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)