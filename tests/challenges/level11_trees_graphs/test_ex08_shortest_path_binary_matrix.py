"""Tests for challenges/level11_trees_graphs/ex08_shortest_path_binary_matrix.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level11_trees_graphs/test_ex08_shortest_path_binary_matrix.py -v
"""

import pytest

from challenges.level11_trees_graphs.ex08_shortest_path_binary_matrix import (
    shortest_path_binary_matrix,
)


# TODO: write your tests. Example to get you started:
#
# def test_diagonal_path():
#     assert shortest_path_binary_matrix([[0, 1], [1, 0]]) == 2
#
# def test_blocked_start_returns_minus_one():
#     assert shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
