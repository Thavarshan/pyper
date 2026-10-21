"""Tests for challenges/level13_concurrency/ex02_safe_counter.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex02_safe_counter.py -v
"""

import pytest

from challenges.level13_concurrency.ex02_safe_counter import SafeCounter, increment_many


# TODO: write your tests. Example to get you started:
#
# import sys
#
# def test_increment_and_decrement():
#     c = SafeCounter(10)
#     c.increment(5)
#     c.decrement(2)
#     assert c.value == 13
#
# def test_negative_amount_raises():
#     c = SafeCounter()
#     with pytest.raises(ValueError):
#         c.increment(-1)
#     assert c.value == 0
#
# @pytest.mark.timeout(10)  # fail instead of hanging forever
# def test_many_threads_lose_no_updates():
#     old = sys.getswitchinterval()
#     sys.setswitchinterval(1e-6)  # switch threads very often
#     try:
#         c = SafeCounter()
#         increment_many(c, 8, 10_000)
#     finally:
#         sys.setswitchinterval(old)  # always put it back
#     assert c.value == 80_000
