"""Tests for challenges/level13_concurrency/ex09_async_limited.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex09_async_limited.py -v
"""

import pytest

from challenges.level13_concurrency.ex09_async_limited import async_worker_pool, run_limited


# TODO: write your tests. Example to get you started:
#
# import asyncio
# import time
#
# def make_job(value, delay):
#     async def job():
#         await asyncio.sleep(delay)
#         return value
#     return job
#
# @pytest.mark.timeout(10)  # fail instead of hanging if something gets stuck
# def test_six_jobs_limit_three_take_two_rounds():
#     start = time.perf_counter()
#     result = asyncio.run(run_limited([make_job(i, 0.1) for i in range(6)], 3))
#     elapsed = time.perf_counter() - start
#     assert result == [0, 1, 2, 3, 4, 5]
#     assert elapsed < 0.35  # about 0.2 s; all six one by one would be 0.6 s
#
# def test_pool_never_runs_more_than_num_workers():
#     running = 0
#     max_running = 0
#
#     async def worker(item):
#         nonlocal running, max_running
#         running += 1
#         max_running = max(max_running, running)
#         try:
#             await asyncio.sleep(0.05)
#             return item * 10
#         finally:
#             running -= 1
#
#     result = asyncio.run(async_worker_pool(list(range(10)), worker, 3))
#     assert result == [i * 10 for i in range(10)]
#     assert max_running == 3
#
# def test_limit_zero_raises():
#     with pytest.raises(ValueError):
#         asyncio.run(run_limited([], 0))
