# -*- coding: utf-8 -*-
"""
Tests
env/bin/pytest
"""

import os
import pytest
from helper import AppConfig
from smoke import Utils


@pytest.fixture(scope='module')
def config():
    config_path = os.path.join(os.getcwd(), 'config/app.conf')
    return AppConfig(config_path)

@pytest.fixture(scope='module')
def smoke_utils():
    return Utils()