"""Tests for challenges/level04_dicts_sets/ex01_word_frequency.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level04_dicts_sets/test_ex01_word_frequency.py -v
"""

import pytest

from challenges.level04_dicts_sets.ex01_word_frequency import word_frequency, most_common_words


# TODO: write your tests. Example to get you started:
#
# def test_counts_are_case_insensitive():
#     assert word_frequency("Go go GO") == {"go": 3}
#
# def test_most_common_breaks_ties_alphabetically():
#     assert most_common_words("pear apple fig", 2) == [("apple", 1), ("fig", 1)]
#
# def test_negative_n_raises_value_error():
#     with pytest.raises(ValueError):
#         most_common_words("a b", -1)
