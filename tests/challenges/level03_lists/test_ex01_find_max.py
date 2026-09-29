"""Tests for challenges/level03_lists/ex01_find_max.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level03_lists/test_ex01_find_max.py -v
"""

import pytest

from challenges.level03_lists.ex01_find_max import find_max, find_min_and_max


# TODO: write your tests. Example to get you started:
#
# def test_all_negative_numbers():
#     assert find_max([-5, -2, -9]) == -2
#
# def test_empty_list_raises():
#     with pytest.raises(ValueError):
#         find_max([])
