"""Tests for challenges/level06_errors_and_parsing/ex05_parse_duration.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level06_errors_and_parsing/test_ex05_parse_duration.py -v
"""

import pytest

from challenges.level06_errors_and_parsing.ex05_parse_duration import parse_duration, format_duration


# TODO: write your tests. Example to get you started:
#
# def test_all_units():
#     assert parse_duration("1h30m15s") == 5415
#
# @pytest.mark.parametrize("bad", ["", "15", "h", "30m1h", "1.5h"])
# def test_invalid_input_raises(bad):
#     with pytest.raises(ValueError):
#         parse_duration(bad)
#
# def test_format_zero():
#     assert format_duration(0) == "0s"
