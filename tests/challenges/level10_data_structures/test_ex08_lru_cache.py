"""Tests for challenges/level10_data_structures/ex08_lru_cache.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level10_data_structures/test_ex08_lru_cache.py -v
"""

import pytest

from challenges.level10_data_structures.ex08_lru_cache import LRUCache


# TODO: write your tests. Example to get you started:
#
# def test_evicts_least_recently_used():
#     cache = LRUCache(2)
#     cache.put(1, 1)
#     cache.put(2, 2)
#     assert cache.get(1) == 1      # 1 is now most recent
#     cache.put(3, 3)               # so 2 is evicted
#     assert cache.get(2) == -1
#     assert cache.get(3) == 3
#
# def test_zero_capacity_raises():
#     with pytest.raises(ValueError):
#         LRUCache(0)
