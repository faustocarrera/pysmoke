# -*- coding: utf-8 -*-
"""
Test configuration
"""

import pytest
from . import smoke_utils


@pytest.mark.incremental
class TestParser(object):
    "Test the configuration loader"

    @staticmethod
    def test_load_testcase(smoke_utils):
        "Check if the parser works ok with a string"
        testcase = """http_status: 200\nresult: true\nresult.version: true"""
        tests_to_run = smoke_utils.parse_tests_string(testcase)
        for test in tests_to_run:
            
        
        
        