"""Tests for challenges/level05_functions/ex07_memoize.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level05_functions/test_ex07_memoize.py -v
"""

import pytest

from challenges.level05_functions.ex07_memoize import memoize


# TODO: write your tests. Example to get you started:
#
# def test_function_runs_once_per_argument():
#     calls = []
#
#     @memoize
#     def square(x):
#         calls.append(x)
#         return x * x
#
#     assert square(3) == 9
#     assert square(3) == 9
#     assert calls == [3]            # the real function ran only once
#     assert square.cache == {(3,): 9}
#
# def test_wraps_preserves_name():
#     @memoize
#     def my_func(x):
#         return x
#     assert my_func.__name__ == "my_func"
