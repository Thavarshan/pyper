"""Tests for challenges/level10_data_structures/ex05_min_stack.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level10_data_structures/test_ex05_min_stack.py -v
"""

import pytest

from challenges.level10_data_structures.ex05_min_stack import MinStack


# TODO: write your tests. Example to get you started:
#
# def test_get_min_after_pops():
#     s = MinStack()
#     s.push(-2)
#     s.push(0)
#     s.push(-3)
#     assert s.get_min() == -3
#     assert s.pop() == -3
#     assert s.get_min() == -2
#
# def test_pop_on_empty_raises_index_error():
#     with pytest.raises(IndexError):
#         MinStack().pop()
