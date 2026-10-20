"""Tests for challenges/level01_basics/ex03_fizzbuzz.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level01_basics/test_ex03_fizzbuzz.py -v
"""

import pytest

from challenges.level01_basics.ex03_fizzbuzz import fizzbuzz


def test_zero_returns_empty_list():
    assert fizzbuzz(0) == []


def test_one_returns_single_string():
    assert fizzbuzz(1) == ["1"]


def test_first_five():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]


def test_first_fifteen():
    assert fizzbuzz(15) == [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz",
        "11", "Fizz", "13", "14", "FizzBuzz",
    ]


@pytest.mark.parametrize(
    "n, expected_last",
    [(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (30, "FizzBuzz"), (7, "7")],
)
def test_last_element(n, expected_last):
    assert fizzbuzz(n)[-1] == expected_last


@pytest.mark.parametrize("n", [0, 1, 2, 14, 15, 100])
def test_length_equals_n(n):
    assert len(fizzbuzz(n)) == n


def test_every_element_is_a_string():
    assert all(isinstance(item, str) for item in fizzbuzz(30))


def test_multiples_of_fifteen_are_fizzbuzz_not_fizz():
    result = fizzbuzz(45)
    assert result[14] == "FizzBuzz"
    assert result[29] == "FizzBuzz"
    assert result[44] == "FizzBuzz"


def test_counts_for_larger_input():
    result = fizzbuzz(100)
    assert result.count("FizzBuzz") == 6
    assert result.count("Fizz") == 27
    assert result.count("Buzz") == 14


def test_largest_normal_input():
    result = fizzbuzz(10_000)
    assert len(result) == 10_000
    assert result[-1] == "Buzz"


@pytest.mark.parametrize("n", [-1, -15, -10_000])
def test_negative_raises_value_error(n):
    with pytest.raises(ValueError):
        fizzbuzz(n)


# ---------------------------------------------------------------------------
# Stretch goals
# ---------------------------------------------------------------------------
# Imports live inside the tests so the core tests above still run before
# you've added `fizzbuzz_custom`.


def test_custom_matches_classic_fizzbuzz():
    from challenges.level01_basics.ex03_fizzbuzz import fizzbuzz_custom

    assert fizzbuzz_custom(30, {3: "Fizz", 5: "Buzz"}) == fizzbuzz(30)


def test_custom_three_rules_combine_in_order():
    from challenges.level01_basics.ex03_fizzbuzz import fizzbuzz_custom

    rules = {3: "Fizz", 5: "Buzz", 7: "Bazz"}
    result = fizzbuzz_custom(105, rules)
    assert result[104] == "FizzBuzzBazz"
    assert result[20] == "FizzBazz"  # 21
    assert result[34] == "BuzzBazz"  # 35
    assert result[6] == "Bazz"  # 7
    assert result[0] == "1"


def test_custom_single_rule():
    from challenges.level01_basics.ex03_fizzbuzz import fizzbuzz_custom

    assert fizzbuzz_custom(6, {2: "Even"}) == ["1", "Even", "3", "Even", "5", "Even"]


def test_custom_empty_rules_returns_numbers():
    from challenges.level01_basics.ex03_fizzbuzz import fizzbuzz_custom

    assert fizzbuzz_custom(3, {}) == ["1", "2", "3"]


def test_custom_zero_returns_empty_list():
    from challenges.level01_basics.ex03_fizzbuzz import fizzbuzz_custom

    assert fizzbuzz_custom(0, {3: "Fizz"}) == []


def test_custom_negative_raises_value_error():
    from challenges.level01_basics.ex03_fizzbuzz import fizzbuzz_custom

    with pytest.raises(ValueError):
        fizzbuzz_custom(-1, {3: "Fizz"})


def test_custom_does_not_modify_rules():
    from challenges.level01_basics.ex03_fizzbuzz import fizzbuzz_custom

    rules = {3: "Fizz", 5: "Buzz"}
    fizzbuzz_custom(15, rules)
    assert rules == {3: "Fizz", 5: "Buzz"}
