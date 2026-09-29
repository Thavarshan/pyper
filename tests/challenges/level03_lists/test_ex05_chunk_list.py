"""Tests for challenges/level03_lists/ex05_chunk_list.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level03_lists/test_ex05_chunk_list.py -v
"""

import pytest

from challenges.level03_lists.ex05_chunk_list import chunk


# TODO: write your tests. Example to get you started:
#
# def test_last_chunk_may_be_shorter():
#     assert chunk([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
#
# def test_size_zero_raises():
#     with pytest.raises(ValueError):
#         chunk([1, 2], 0)
