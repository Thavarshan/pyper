"""Tests for challenges/level05_functions/ex02_comprehensions.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level05_functions/test_ex02_comprehensions.py -v
"""

import pytest

from challenges.level05_functions.ex02_comprehensions import (
    squares_of_evens,
    word_lengths,
    unique_first_letters,
    flatten_matrix,
    transpose,
)


# TODO: write your tests. Example to get you started:
#
# def test_squares_of_evens():
#     assert squares_of_evens([1, 2, 3, 4]) == [4, 16]
#
# def test_transpose_ragged_raises():
#     with pytest.raises(ValueError):
#         transpose([[1, 2], [3]])
