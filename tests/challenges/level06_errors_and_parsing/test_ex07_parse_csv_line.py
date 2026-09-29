"""Tests for challenges/level06_errors_and_parsing/ex07_parse_csv_line.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level06_errors_and_parsing/test_ex07_parse_csv_line.py -v
"""

import pytest

from challenges.level06_errors_and_parsing.ex07_parse_csv_line import parse_csv_line


# TODO: write your tests. Example to get you started:
#
# def test_quoted_field_with_comma():
#     assert parse_csv_line('"Smith, John",42') == ["Smith, John", "42"]
#
# def test_unterminated_quote_raises():
#     with pytest.raises(ValueError):
#         parse_csv_line('"oops,1')
