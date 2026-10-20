"""Tests for challenges/level01_basics/ex01_greet.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level01_basics/test_ex01_greet.py -v
"""

import pytest

from challenges.level01_basics.ex01_greet import greet, greet_all


def test_greets_by_name():
    assert greet("Ada") == "Hello, Ada!"


@pytest.mark.parametrize(
    "name, expected",
    [
        ("   Grace  ", "Hello, Grace!"),
        ("\tAda\n", "Hello, Ada!"),
        ("\n\n Linus \t", "Hello, Linus!"),
        ("  Ada", "Hello, Ada!"),
        ("Ada  ", "Hello, Ada!"),
    ],
)
def test_strips_surrounding_whitespace(name, expected):
    assert greet(name) == expected


@pytest.mark.parametrize("name", ["", " ", "    ", "\t", "\n", " \t\n "])
def test_blank_name_greets_world(name):
    assert greet(name) == "Hello, World!"


def test_inner_whitespace_is_preserved():
    assert greet("  Ada Lovelace  ") == "Hello, Ada Lovelace!"
    assert greet("Mary  Jane") == "Hello, Mary  Jane!"


def test_capitalisation_is_unchanged():
    assert greet("bob") == "Hello, bob!"
    assert greet("ADA") == "Hello, ADA!"


def test_returns_string_and_does_not_print(capsys):
    result = greet("Ada")
    assert isinstance(result, str)
    assert capsys.readouterr().out == ""


# ---------------------------------------------------------------------------
# Stretch goals
# ---------------------------------------------------------------------------
# Imports live inside the tests so the core tests above still run before
# you've added `greet_all`.


def test_custom_greeting():
    assert greet("Ada", greeting="Hi") == "Hi, Ada!"
    assert greet("  Ada  ", greeting="Welcome") == "Welcome, Ada!"


def test_custom_greeting_with_blank_name():
    assert greet("", greeting="Hi") == "Hi, World!"


def test_default_greeting_is_hello():
    assert greet("Ada", greeting="Hello") == greet("Ada")


def test_greet_all_greets_everyone_in_order():
    from challenges.level01_basics.ex01_greet import greet_all

    assert greet_all(["Ada", "Grace"]) == ["Hello, Ada!", "Hello, Grace!"]


def test_greet_all_applies_stripping_and_blank_rules():
    from challenges.level01_basics.ex01_greet import greet_all

    assert greet_all(["  Ada ", "", "\t"]) == [
        "Hello, Ada!",
        "Hello, World!",
        "Hello, World!",
    ]


def test_greet_all_empty_list():
    from challenges.level01_basics.ex01_greet import greet_all

    assert greet_all([]) == []


def test_greet_all_does_not_modify_input():
    from challenges.level01_basics.ex01_greet import greet_all

    names = ["  Ada ", "Grace"]
    greet_all(names)
    assert names == ["  Ada ", "Grace"]
