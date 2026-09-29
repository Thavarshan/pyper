"""Tests for challenges/level05_functions/ex04_compose.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level05_functions/test_ex04_compose.py -v
"""

import pytest

from challenges.level05_functions.ex04_compose import compose, pipe


# TODO: write your tests. Example to get you started:
#
# def test_compose_applies_right_to_left():
#     add_one = lambda x: x + 1
#     double = lambda x: x * 2
#     assert compose(add_one, double)(5) == 11
#
# def test_compose_is_lazy():
#     calls = []
#     def record(x):
#         calls.append(x)
#         return x
#     f = compose(record)
#     assert calls == []   # nothing called yet
#     f(1)
#     assert calls == [1]
