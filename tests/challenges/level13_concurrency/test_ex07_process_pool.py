"""Tests for challenges/level13_concurrency/ex07_process_pool.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex07_process_pool.py -v
"""

import pytest

from challenges.level13_concurrency.ex07_process_pool import (
    count_primes,
    count_primes_parallel,
)


# TODO: write your tests. Example to get you started:
#
# def test_count_primes_below_ten():
#     assert count_primes(0, 10) == 4
#
# @pytest.mark.timeout(30)  # fail instead of hanging if processes get stuck
# def test_parallel_matches_plain_version():
#     # Compare answers, never timings: speed depends on the machine.
#     for workers in [1, 2, 3, 8]:
#         assert count_primes_parallel(1_000, workers) == count_primes(0, 1_000)
#
# def test_negative_limit_raises():
#     with pytest.raises(ValueError):
#         count_primes_parallel(-1)
