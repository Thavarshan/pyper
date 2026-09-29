"""Tests for challenges/level12_algorithms/ex06_climbing_stairs.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level12_algorithms/test_ex06_climbing_stairs.py -v
"""

import pytest

from challenges.level12_algorithms.ex06_climbing_stairs import climb_stairs


# TODO: write your tests. Example to get you started:
#
# @pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (2, 2), (3, 3), (5, 8)])
# def test_small_values(n, expected):
#     assert climb_stairs(n) == expected
#
# def test_negative_raises_value_error():
#     with pytest.raises(ValueError):
#         climb_stairs(-1)
