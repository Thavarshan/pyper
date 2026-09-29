"""Tests for challenges/level07_recursion/ex04_tower_of_hanoi.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level07_recursion/test_ex04_tower_of_hanoi.py -v
"""

import pytest

from challenges.level07_recursion.ex04_tower_of_hanoi import hanoi


# TODO: write your tests. Example to get you started:
#
# def test_two_discs():
#     assert hanoi(2) == [("A", "B"), ("A", "C"), ("B", "C")]
#
# @pytest.mark.parametrize("n", range(0, 8))
# def test_move_count(n):
#     assert len(hanoi(n)) == 2**n - 1
