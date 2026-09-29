"""Tests for challenges/level04_dicts_sets/ex06_invert_dictionary.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level04_dicts_sets/test_ex06_invert_dictionary.py -v
"""

import pytest

from challenges.level04_dicts_sets.ex06_invert_dictionary import invert, invert_grouped


# TODO: write your tests. Example to get you started:
#
# def test_invert_swaps_keys_and_values():
#     assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
#
# def test_invert_duplicate_values_raises():
#     with pytest.raises(ValueError):
#         invert({"x": 1, "y": 1})
#
# def test_invert_grouped_keeps_order():
#     result = invert_grouped({"a": "v", "b": "w", "c": "v"})
#     assert result == {"v": ["a", "c"], "w": ["b"]}
#     assert list(result) == ["v", "w"]  # == on dicts ignores order, so check it
