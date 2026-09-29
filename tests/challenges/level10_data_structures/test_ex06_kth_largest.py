"""Tests for challenges/level10_data_structures/ex06_kth_largest.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level10_data_structures/test_ex06_kth_largest.py -v
"""

import pytest

from challenges.level10_data_structures.ex06_kth_largest import find_kth_largest


# TODO: write your tests. Example to get you started:
#
# def test_duplicates_count():
#     assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
#
# @pytest.mark.parametrize("nums, k", [([1, 2], 0), ([1, 2], 3), ([], 1)])
# def test_invalid_k_raises(nums, k):
#     with pytest.raises(ValueError):
#         find_kth_largest(nums, k)
