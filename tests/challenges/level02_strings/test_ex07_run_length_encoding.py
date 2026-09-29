"""Tests for challenges/level02_strings/ex07_run_length_encoding.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level02_strings/test_ex07_run_length_encoding.py -v
"""

import pytest

from challenges.level02_strings.ex07_run_length_encoding import encode, decode


# TODO: write your tests. Example to get you started:
#
# def test_encode_always_writes_counts():
#     assert encode("aaabcc") == "a3b1c2"
#
# def test_decode_missing_count_raises():
#     with pytest.raises(ValueError):
#         decode("a3b")
