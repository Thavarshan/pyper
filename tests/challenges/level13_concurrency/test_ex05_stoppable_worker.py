"""Tests for challenges/level13_concurrency/ex05_stoppable_worker.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex05_stoppable_worker.py -v
"""

import pytest

from challenges.level13_concurrency.ex05_stoppable_worker import RepeatingWorker


# TODO: write your tests. Example to get you started:
# (add `import time` at the top when you need it)
#
# def wait_until(predicate, timeout=2.0):
#     """Poll until predicate() is True or the timeout runs out."""
#     deadline = time.perf_counter() + timeout
#     while time.perf_counter() < deadline:
#         if predicate():
#             return True
#         time.sleep(0.01)
#     return predicate()
#
# @pytest.mark.timeout(10)  # fail instead of hanging forever
# def test_stop_is_fast_even_with_a_long_interval():
#     w = RepeatingWorker(lambda: None, interval=60)
#     w.start()
#     try:
#         assert wait_until(lambda: w.runs >= 1)   # first run is immediate
#         start = time.perf_counter()
#         w.stop()
#         assert time.perf_counter() - start < 0.5
#         assert not w.is_running
#     finally:
#         w.stop(timeout=5)    # never leave a worker running
#
# def test_bad_interval_raises():
#     with pytest.raises(ValueError):
#         RepeatingWorker(lambda: None, 0)
