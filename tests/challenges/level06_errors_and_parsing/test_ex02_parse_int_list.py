"""Tests for challenges/level06_errors_and_parsing/ex02_parse_int_list.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level06_errors_and_parsing/test_ex02_parse_int_list.py -v
"""

import pytest

from challenges.level06_errors_and_parsing.ex02_parse_int_list import parse_int_list


# TODO: write your tests. Example to get you started:
#
# import re
#
# def test_whitespace_is_tolerated():
#     assert parse_int_list(" 1 ,2,   3 ") == [1, 2, 3]
#
# def test_error_names_token_and_position():
#     expected = "invalid integer '2.5' at position 1"
#     with pytest.raises(ValueError, match=re.escape(expected)):
#         parse_int_list("10, 2.5, 3")
