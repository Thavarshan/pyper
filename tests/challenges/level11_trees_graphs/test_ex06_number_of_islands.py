"""Tests for challenges/level11_trees_graphs/ex06_number_of_islands.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level11_trees_graphs/test_ex06_number_of_islands.py -v
"""

import copy

import pytest

from challenges.level11_trees_graphs.ex06_number_of_islands import num_islands


# TODO: write your tests. Example to get you started:
#
# def test_three_islands():
#     grid = [
#         ["1", "1", "0", "0", "0"],
#         ["1", "1", "0", "0", "0"],
#         ["0", "0", "1", "0", "0"],
#         ["0", "0", "0", "1", "1"],
#     ]
#     assert num_islands(grid) == 3
#
# def test_does_not_mutate_grid():
#     grid = [["1", "0"], ["0", "1"]]
#     original = copy.deepcopy(grid)
#     num_islands(grid)
#     assert grid == original
