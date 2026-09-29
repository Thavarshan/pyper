"""Tests for challenges/level11_trees_graphs/ex03_level_order.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level11_trees_graphs/test_ex03_level_order.py -v
"""

import pytest

from challenges.common.structures import build_tree
from challenges.level11_trees_graphs.ex03_level_order import level_order


# TODO: write your tests. Example to get you started:
#
# def test_example_tree():
#     root = build_tree([3, 9, 20, None, None, 15, 7])
#     assert level_order(root) == [[3], [9, 20], [15, 7]]
#
# def test_empty_tree():
#     assert level_order(None) == []
