"""Tests for challenges/level01_basics/ex04_temperature_conversion.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level01_basics/test_ex04_temperature_conversion.py -v
"""

import pytest

from challenges.level01_basics.ex04_temperature_conversion import celsius_to_fahrenheit, fahrenheit_to_celsius


# TODO: write your tests. Example to get you started:
#
# def test_body_temperature():
#     assert celsius_to_fahrenheit(37) == pytest.approx(98.6)
#
# def test_below_absolute_zero_raises():
#     with pytest.raises(ValueError):
#         celsius_to_fahrenheit(-300)
