"""Tests for challenges/level12_algorithms/ex04_longest_substring_without_repeating.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level12_algorithms/test_ex04_longest_substring_without_repeating.py -v
"""

import pytest

from challenges.level12_algorithms.ex04_longest_substring_without_repeating import (
    length_of_longest_substring,
)


# TODO: write your tests. Example to get you started:
#
# @pytest.mark.parametrize("s, expected", [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)])
# def test_examples(s, expected):
#     assert length_of_longest_substring(s) == expected
#
# def test_left_pointer_never_moves_backwards():
#     assert length_of_longest_substring("abba") == 2
