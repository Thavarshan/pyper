"""Tests for challenges/level11_trees_graphs/ex02_invert_tree.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level11_trees_graphs/test_ex02_invert_tree.py -v
"""

import pytest

from challenges.common.structures import build_tree, tree_to_list
from challenges.level11_trees_graphs.ex02_invert_tree import invert_tree


# TODO: write your tests. Example to get you started:
#
# def test_inverts_perfect_tree():
#     root = build_tree([4, 2, 7, 1, 3, 6, 9])
#     assert tree_to_list(invert_tree(root)) == [4, 7, 2, 9, 6, 3, 1]
#
# def test_returns_same_root_object():
#     root = build_tree([2, 1, 3])
#     assert invert_tree(root) is root
