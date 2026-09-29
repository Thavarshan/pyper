"""Tests for challenges/level06_errors_and_parsing/ex03_validate_password.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level06_errors_and_parsing/test_ex03_validate_password.py -v
"""

import pytest

from challenges.level06_errors_and_parsing.ex03_validate_password import validate_password, is_strong


# TODO: write your tests. Example to get you started:
#
# def test_valid_password_has_no_failures():
#     assert validate_password("Abcdef1!") == []
#
# @pytest.mark.parametrize("pw, expected", [
#     ("Abcde1!", ["too_short"]),
#     ("abcdef1!", ["no_uppercase"]),
# ])
# def test_single_rule_failures(pw, expected):
#     assert validate_password(pw) == expected
