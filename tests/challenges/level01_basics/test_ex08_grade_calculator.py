"""Tests for challenges/level01_basics/ex08_grade_calculator.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level01_basics/test_ex08_grade_calculator.py -v
"""

import pytest

from challenges.level01_basics.ex08_grade_calculator import letter_grade, average_grade


# TODO: write your tests. Example to get you started:
#
# def test_exactly_ninety_is_an_a():
#     assert letter_grade(90) == "A"
#
# def test_average_of_empty_list_raises():
#     with pytest.raises(ValueError):
#         average_grade([])
