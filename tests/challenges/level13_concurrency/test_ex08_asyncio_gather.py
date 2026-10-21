"""Tests for challenges/level13_concurrency/ex08_asyncio_gather.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex08_asyncio_gather.py -v
"""

import pytest

from challenges.level13_concurrency.ex08_asyncio_gather import gather_in_order, with_timeout


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
# def test_jobs_run_at_the_same_time():
#     start = time.perf_counter()
#     result = asyncio.run(gather_in_order([make_job(i, 0.2) for i in range(5)]))
#     elapsed = time.perf_counter() - start
#     assert result == [0, 1, 2, 3, 4]
#     assert elapsed < 0.6  # one after another would take 1.0 s
#
# def test_slow_job_is_cancelled():
#     events = []
#
#     async def slow():
#         try:
#             await asyncio.sleep(5)
#         except asyncio.CancelledError:
#             events.append("cancelled")
#             raise
#
#     assert asyncio.run(with_timeout(slow, 0.1, "late")) == "late"
#     assert events == ["cancelled"]
