"""Tests for challenges/level05_functions/ex06_fibonacci_generator.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level05_functions/test_ex06_fibonacci_generator.py -v
"""

import pytest

from challenges.level05_functions.ex06_fibonacci_generator import fibonacci, take, fibonacci_up_to


# TODO: write your tests. Example to get you started:
#
# import itertools
#
# def test_first_values_with_next():
#     gen = fibonacci()
#     assert [next(gen) for _ in range(5)] == [0, 1, 1, 2, 3]
#
# def test_islice_on_infinite_generator():
#     assert list(itertools.islice(fibonacci(), 7)) == [0, 1, 1, 2, 3, 5, 8]
#
# def test_take_does_not_over_consume():
#     it = iter([1, 2, 3, 4])
#     assert take(2, it) == [1, 2]
#     assert next(it) == 3
