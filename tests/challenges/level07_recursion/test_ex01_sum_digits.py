"""Tests for challenges/level07_recursion/ex01_sum_digits.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level07_recursion/test_ex01_sum_digits.py -v
"""

import pytest

from challenges.level07_recursion.ex01_sum_digits import sum_digits, digital_root


# TODO: write your tests. Example to get you started:
#
# def test_sum_digits_basic():
#     assert sum_digits(1234) == 10
#
# def test_non_int_raises_type_error():
#     with pytest.raises(TypeError):
#         sum_digits("12")
