"""Tests for challenges/level01_basics/ex04_temperature_conversion.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level01_basics/test_ex04_temperature_conversion.py -v
"""

import pytest

from challenges.level01_basics.ex04_temperature_conversion import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)


@pytest.mark.parametrize(
    "c, expected",
    [(0, 32.0), (100, 212.0), (-40, -40.0), (37, 98.6), (-273.15, -459.67)],
)
def test_celsius_to_fahrenheit(c, expected):
    result = celsius_to_fahrenheit(c)
    assert isinstance(result, float)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    "f, expected",
    [(32, 0.0), (212, 100.0), (-40, -40.0), (98.6, 37.0), (-459.67, -273.15)],
)
def test_fahrenheit_to_celsius(f, expected):
    result = fahrenheit_to_celsius(f)
    assert isinstance(result, float)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize("c", [-273.150001, -273.16, -300])
def test_celsius_below_absolute_zero_raises(c):
    with pytest.raises(ValueError):
        celsius_to_fahrenheit(c)


@pytest.mark.parametrize("f", [-459.670001, -460, -500])
def test_fahrenheit_below_absolute_zero_raises(f):
    with pytest.raises(ValueError):
        fahrenheit_to_celsius(f)


@pytest.mark.parametrize("c", [-100, -40, 0, 20.123456, 37, 100, 1000])
def test_round_trip(c):
    assert fahrenheit_to_celsius(celsius_to_fahrenheit(c)) == pytest.approx(c)


def test_conversion_keeps_precision():
    assert celsius_to_fahrenheit(1.234567) == pytest.approx(34.2222206)
    assert fahrenheit_to_celsius(1) == pytest.approx(-17.22222222222222)
