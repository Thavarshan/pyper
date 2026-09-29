"""Tests for challenges/level11_trees_graphs/ex05_lowest_common_ancestor_bst.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level11_trees_graphs/test_ex05_lowest_common_ancestor_bst.py -v
"""

import pytest

from challenges.common.structures import build_tree
from challenges.level11_trees_graphs.ex05_lowest_common_ancestor_bst import (
    lowest_common_ancestor,
)


# TODO: write your tests. Example to get you started:
#
# @pytest.fixture
# def root():
#     return build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
#
# @pytest.mark.parametrize("p, q, expected", [(2, 8, 6), (2, 4, 2), (3, 5, 4)])
# def test_lca(root, p, q, expected):
#     assert lowest_common_ancestor(root, p, q) == expected
