"""Tests for challenges/level13_concurrency/ex04_producer_consumer.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex04_producer_consumer.py -v
"""

import pytest

from challenges.level13_concurrency.ex04_producer_consumer import process_with_workers


# TODO: write your tests. Example to get you started:
# (add `import threading` and `import time` at the top when you need them)
#
# def test_example():
#     assert process_with_workers([1, 2, 3, 4], lambda x: x * 10, num_workers=2) == [10, 20, 30, 40]
#
# @pytest.mark.timeout(10)  # fail instead of hanging if a worker never stops
# def test_runs_at_the_same_time():
#     def slow_double(x):
#         time.sleep(0.2)
#         return x * 2
#     start = time.perf_counter()
#     result = process_with_workers(list(range(8)), slow_double, num_workers=4)
#     elapsed = time.perf_counter() - start
#     assert result == [0, 2, 4, 6, 8, 10, 12, 14]
#     assert elapsed < 0.8      # one at a time would take 1.6 s
#
# @pytest.mark.timeout(10)
# def test_never_more_than_num_workers_at_once():
#     lock = threading.Lock()
#     running = 0
#     highest = 0
#
#     def work(x):
#         nonlocal running, highest
#         with lock:
#             running += 1
#             highest = max(highest, running)
#         time.sleep(0.05)
#         with lock:
#             running -= 1
#         return x
#
#     process_with_workers(list(range(12)), work, num_workers=3)
#     assert highest == 3
