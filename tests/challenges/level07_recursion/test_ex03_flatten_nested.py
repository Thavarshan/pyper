"""Tests for challenges/level07_recursion/ex03_flatten_nested.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level07_recursion/test_ex03_flatten_nested.py -v
"""

import pytest

from challenges.level07_recursion.ex03_flatten_nested import depth, flatten


# TODO: write your tests. Example to get you started:
#
# def test_flatten_deeply_nested():
#     assert flatten([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]
#
# def test_depth_of_empty_list_is_one():
#     assert depth([]) == 1
