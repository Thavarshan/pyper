"""Tests for challenges/level10_data_structures/ex02_reverse_linked_list.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Tip: use @pytest.mark.parametrize over the function objects themselves so
the same tests check both reverse_list and reverse_list_recursive.

Run just this file:
    pytest tests/challenges/level10_data_structures/test_ex02_reverse_linked_list.py -v
"""

import pytest

from challenges.common.structures import linked_to_list, list_to_linked
from challenges.level10_data_structures.ex02_reverse_linked_list import (
    reverse_list,
    reverse_list_recursive,
)


# TODO: write your tests. Example to get you started:
#
# @pytest.mark.parametrize("reverse", [reverse_list, reverse_list_recursive])
# def test_reverses_four_nodes(reverse):
#     head = list_to_linked([1, 2, 3, 4])
#     assert linked_to_list(reverse(head)) == [4, 3, 2, 1]
#
# @pytest.mark.parametrize("reverse", [reverse_list, reverse_list_recursive])
# def test_empty_list_returns_none(reverse):
#     assert reverse(None) is None
