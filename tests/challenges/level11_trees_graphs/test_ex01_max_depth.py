"""Tests for challenges/level11_trees_graphs/ex01_max_depth.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level11_trees_graphs/test_ex01_max_depth.py -v
"""

import pytest

from challenges.common.structures import build_tree
from challenges.level11_trees_graphs.ex01_max_depth import max_depth


# TODO: write your tests. Example to get you started:
#
# def test_example_tree():
#     root = build_tree([3, 9, 20, None, None, 15, 7])
#     assert max_depth(root) == 3
#
# def test_empty_tree_is_zero():
#     assert max_depth(None) == 0
