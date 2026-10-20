"""Tests for challenges/level01_basics/ex02_even_or_odd.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level01_basics/test_ex02_even_or_odd.py -v
"""

import pytest

from challenges.level01_basics.ex02_even_or_odd import is_even, even_or_odd


def test_zero_is_even():
    assert is_even(0) is True
    assert even_or_odd(0) == "even"


@pytest.mark.parametrize("n", [2, 4, 100, -2, -4, -100])
def test_even_numbers(n):
    assert is_even(n) is True
    assert even_or_odd(n) == "even"


@pytest.mark.parametrize("n", [1, 3, 7, 99, -1, -3, -99])
def test_odd_numbers(n):
    assert is_even(n) is False
    assert even_or_odd(n) == "odd"


def test_huge_numbers():
    assert is_even(10**100) is True
    assert is_even(10**100 + 1) is False
    assert even_or_odd(10**100) == "even"
    assert even_or_odd(10**100 + 1) == "odd"


def test_is_even_returns_a_real_bool():
    assert type(is_even(2)) is bool
    assert type(is_even(3)) is bool


def test_even_or_odd_returns_exact_lowercase_strings():
    assert even_or_odd(2) == "even"
    assert even_or_odd(3) == "odd"


# ---------------------------------------------------------------------------
# Stretch goals
# ---------------------------------------------------------------------------
# Imports live inside the tests so the core tests above still run before
# you've added these functions.


@pytest.mark.parametrize("n", [0, 2, -2, -4, 10**100])
def test_is_even_bitwise_even(n):
    from challenges.level01_basics.ex02_even_or_odd import is_even_bitwise

    assert is_even_bitwise(n) is True


@pytest.mark.parametrize("n", [1, 3, -1, -3, 10**100 + 1])
def test_is_even_bitwise_odd(n):
    from challenges.level01_basics.ex02_even_or_odd import is_even_bitwise

    assert is_even_bitwise(n) is False


def test_split_even_odd_keeps_order():
    from challenges.level01_basics.ex02_even_or_odd import split_even_odd

    assert split_even_odd([5, 2, 8, 1, 4, 3]) == ([2, 8, 4], [5, 1, 3])


def test_split_even_odd_handles_zero_and_negatives():
    from challenges.level01_basics.ex02_even_or_odd import split_even_odd

    assert split_even_odd([0, -1, -2, -3]) == ([0, -2], [-1, -3])


def test_split_even_odd_empty_and_one_sided():
    from challenges.level01_basics.ex02_even_or_odd import split_even_odd

    assert split_even_odd([]) == ([], [])
    assert split_even_odd([2, 4]) == ([2, 4], [])
    assert split_even_odd([1, 3]) == ([], [1, 3])


def test_split_even_odd_does_not_modify_input():
    from challenges.level01_basics.ex02_even_or_odd import split_even_odd

    nums = [3, 2, 1]
    split_even_odd(nums)
    assert nums == [3, 2, 1]
