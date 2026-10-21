"""Tests for challenges/level13_concurrency/ex06_thread_pool.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex06_thread_pool.py -v
"""

import pytest

from challenges.level13_concurrency.ex06_thread_pool import fastest, parallel_map


# TODO: write your tests. Example to get you started:
# (add `import time` at the top when you need it)
#
# def sleeper(seconds, value):
#     """Return a no-argument function that sleeps, then returns value."""
#     def f():
#         time.sleep(seconds)
#         return value
#     return f
#
# def test_parallel_map_keeps_order():
#     assert parallel_map(lambda x: x * x, [1, 2, 3]) == [1, 4, 9]
#
# @pytest.mark.timeout(10)  # fail instead of hanging forever
# def test_fastest_does_not_wait_for_the_slow_one():
#     start = time.perf_counter()
#     assert fastest([sleeper(1.0, "slow"), sleeper(0.05, "fast")]) == "fast"
#     assert time.perf_counter() - start < 0.5
