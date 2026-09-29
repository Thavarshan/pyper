"""Tests for challenges/level10_data_structures/ex03_merge_two_sorted_lists.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level10_data_structures/test_ex03_merge_two_sorted_lists.py -v
"""

import pytest

from challenges.common.structures import linked_to_list, list_to_linked
from challenges.level10_data_structures.ex03_merge_two_sorted_lists import merge_two_lists


# TODO: write your tests. Example to get you started:
#
# def test_merges_two_lists():
#     a = list_to_linked([1, 2, 4])
#     b = list_to_linked([1, 3, 4])
#     assert linked_to_list(merge_two_lists(a, b)) == [1, 1, 2, 3, 4, 4]
#
# def test_both_empty_returns_none():
#     assert merge_two_lists(None, None) is None
