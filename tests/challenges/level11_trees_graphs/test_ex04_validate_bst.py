"""Tests for challenges/level11_trees_graphs/ex04_validate_bst.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level11_trees_graphs/test_ex04_validate_bst.py -v
"""

import pytest

from challenges.common.structures import build_tree
from challenges.level11_trees_graphs.ex04_validate_bst import is_valid_bst


# TODO: write your tests. Example to get you started:
#
# def test_simple_valid_bst():
#     assert is_valid_bst(build_tree([2, 1, 3])) is True
#
# @pytest.mark.parametrize("values", [[5, 3, 8, 1, 6], [2, 2], [2, None, 2]])
# def test_invalid_bsts(values):
#     assert is_valid_bst(build_tree(values)) is False
