"""Tests for challenges/level09_searching_sorting/ex02_binary_search.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level09_searching_sorting/test_ex02_binary_search.py -v
"""

import pytest

from challenges.level09_searching_sorting.ex02_binary_search import binary_search, binary_search_recursive


# TODO: write your tests. Example to get you started:
#
# @pytest.mark.parametrize("search", [binary_search, binary_search_recursive])
# def test_found(search):
#     assert search([-1, 0, 3, 5, 9, 12], 9) == 4
#
# @pytest.mark.parametrize("search", [binary_search, binary_search_recursive])
# def test_empty_list(search):
#     assert search([], 1) == -1
