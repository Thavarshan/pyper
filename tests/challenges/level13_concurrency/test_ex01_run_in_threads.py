"""Tests for challenges/level13_concurrency/ex01_run_in_threads.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex01_run_in_threads.py -v
"""

import pytest

from challenges.level13_concurrency.ex01_run_in_threads import run_in_threads


# TODO: write your tests. Example to get you started:
#
# import time
#
# def test_example():
#     assert run_in_threads(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
#
# @pytest.mark.timeout(10)  # fail instead of hanging forever
# def test_calls_run_at_the_same_time():
#     def slow_double(x):
#         time.sleep(0.2)
#         return x * 2
#
#     start = time.perf_counter()
#     result = run_in_threads(slow_double, [1, 2, 3, 4, 5])
#     elapsed = time.perf_counter() - start
#     assert result == [2, 4, 6, 8, 10]
#     assert elapsed < 0.6  # one at a time would take 1.0 s
#
# def test_earliest_error_is_raised():
#     def check(x):
#         if x < 0:
#             raise ValueError(f"negative: {x}")
#         return x
#
#     with pytest.raises(ValueError, match="negative: -1"):
#         run_in_threads(check, [5, -1, -2])
