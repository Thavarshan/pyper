"""Tests for challenges/level06_errors_and_parsing/ex04_parse_config.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level06_errors_and_parsing/test_ex04_parse_config.py -v
"""

import pytest

from challenges.level06_errors_and_parsing.ex04_parse_config import ConfigError, parse_config


# TODO: write your tests. Example to get you started:
#
# def test_basic_parsing():
#     assert parse_config("host = localhost\nport=5432") == {"host": "localhost", "port": "5432"}
#
# def test_missing_equals_reports_line_number():
#     with pytest.raises(ConfigError) as excinfo:
#         parse_config("# comment\na = 1\njunk")
#     assert excinfo.value.line_number == 3
