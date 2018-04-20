# -*- coding: utf-8 -*-
"""
Test configuration
"""

import pytest
from . import config


@pytest.mark.incremental
class TestConfig(object):
    "Test the configuration loader"

    @staticmethod
    def test_load_config(config):
        "Check if the test load correctly"
        assert config.get('app', 'url') is not None