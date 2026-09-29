"""Tests for challenges/level07_recursion/ex07_generate_parentheses.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level07_recursion/test_ex07_generate_parentheses.py -v
"""

import pytest

from challenges.level07_recursion.ex07_generate_parentheses import generate_parentheses


# TODO: write your tests. Example to get you started:
#
# def test_n_equals_2():
#     assert generate_parentheses(2) == ["(())", "()()"]
#
# def test_negative_raises_value_error():
#     with pytest.raises(ValueError):
#         generate_parentheses(-1)
