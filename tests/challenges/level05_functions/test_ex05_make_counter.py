"""Tests for challenges/level05_functions/ex05_make_counter.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level05_functions/test_ex05_make_counter.py -v
"""

import pytest

from challenges.level05_functions.ex05_make_counter import make_counter, make_accumulator


# TODO: write your tests. Example to get you started:
#
# def test_counter_starts_at_start():
#     c = make_counter(start=10, step=5)
#     assert [c(), c(), c()] == [10, 15, 20]
#
# def test_counters_are_independent():
#     a, b = make_counter(), make_counter()
#     a(); a()
#     assert b() == 0
