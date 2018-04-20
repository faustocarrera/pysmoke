# -*- coding: utf-8 -*-
"""
Tests
env/bin/pytest
"""

import os
import pytest
from helper import AppConfig


@pytest.fixture(scope='module')
def config():
    config_path = os.path.join(os.getcwd(), 'config/app.conf')
    return AppConfig(config_path)