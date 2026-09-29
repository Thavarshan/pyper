"""Tests for challenges/level12_algorithms/ex08_longest_increasing_subsequence.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level12_algorithms/test_ex08_longest_increasing_subsequence.py -v
"""

import pytest

from challenges.level12_algorithms.ex08_longest_increasing_subsequence import (
    length_of_lis,
)


# TODO: write your tests. Example to get you started:
#
# def test_example():
#     assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
#
# def test_equal_values_are_not_increasing():
#     assert length_of_lis([7, 7, 7, 7]) == 1
