"""Tests for challenges/level06_errors_and_parsing/ex01_safe_divide.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level06_errors_and_parsing/test_ex01_safe_divide.py -v
"""

import pytest

from challenges.level06_errors_and_parsing.ex01_safe_divide import safe_divide, divide_all


# TODO: write your tests. Example to get you started:
#
# def test_divide_by_zero_returns_default():
#     assert safe_divide(1, 0, default=0) == 0
#
# def test_other_errors_propagate():
#     with pytest.raises(TypeError):
#         safe_divide("6", 2)
