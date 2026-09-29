"""
Challenge: Temperature Conversion
Level:     01 - Basics
Topics:    arithmetic, floats, formulas, raising exceptions, comparing floats
Source:    Classic beginner exercise

========================================================================
PROBLEM
========================================================================
Write two functions that convert temperatures between the Celsius and
Fahrenheit scales:

    celsius_to_fahrenheit(c):  F = C * 9 / 5 + 32
    fahrenheit_to_celsius(f):  C = (F - 32) * 5 / 9

Both functions always return a float (even for "round" answers, so
celsius_to_fahrenheit(100) returns 212.0, not 212).

ABSOLUTE ZERO is the coldest temperature physically possible:
-273.15 degrees Celsius, which equals -459.67 degrees Fahrenheit. Nothing
can be colder, so if the input temperature is BELOW absolute zero, raise
a ValueError. Exactly absolute zero is allowed.

A WORD ABOUT FLOATS: computers store decimals in binary, so tiny
rounding errors appear. For example `0.1 + 0.2 == 0.3` is False in
Python! When testing float results, never rely on `==` for "messy"
numbers. Use one of:

    assert result == pytest.approx(98.6)       # recommended in tests
    assert round(result, 2) == 98.6            # round to 2 decimals

========================================================================
EXAMPLES
========================================================================
    >>> celsius_to_fahrenheit(0)
    32.0

    >>> celsius_to_fahrenheit(100)
    212.0

    >>> fahrenheit_to_celsius(-40)
    -40.0

    >>> round(fahrenheit_to_celsius(98.6), 2)
    37.0

========================================================================
CONSTRAINTS
========================================================================
- Input is an int or a float.
- Return value is always a float. Do NOT round inside the function -
  return the full-precision result.
- celsius_to_fahrenheit: raise ValueError if c < -273.15.
- fahrenheit_to_celsius: raise ValueError if f < -459.67.

========================================================================
EDGE CASES TO TEST
========================================================================
- Freezing point: 0 C <-> 32 F
- Boiling point: 100 C <-> 212 F
- -40 is the same in both scales
- Body temperature 37 C ~ 98.6 F (use pytest.approx)
- Exactly absolute zero is allowed (-273.15 C, -459.67 F)
- Just below absolute zero (e.g. -273.16 C, -460 F) -> ValueError
- Round trip: fahrenheit_to_celsius(celsius_to_fahrenheit(x)) ~ x
- The return type is float even for int input

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. The `/` operator ALWAYS returns a float in Python 3, even 10 / 2.
   (Use `//` if you ever want integer "floor" division.)
2. Check the absolute-zero rule FIRST, before doing the maths.
3. Store the limits in module-level constants such as
   ABSOLUTE_ZERO_C = -273.15 so they have a name and are easy to reuse.
4. For the round-trip test, `pytest.approx` handles the tiny errors.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- int vs float and how `/` behaves
- Operator precedence: why (F - 32) needs parentheses
- Floating-point imprecision and `pytest.approx` / `round()`
- Raising exceptions with a helpful message: raise ValueError("...")
- Module-level constants (UPPER_CASE names by convention)

========================================================================
STRETCH GOALS
========================================================================
- Add `celsius_to_kelvin` and `kelvin_to_celsius` (K = C + 273.15;
  Kelvin can never be negative).
- Write one general function `convert(value, from_unit, to_unit)` that
  accepts "C", "F" or "K" and raises ValueError for unknown units.
"""


def celsius_to_fahrenheit(c: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    Args:
        c: Temperature in degrees Celsius.

    Returns:
        The temperature in degrees Fahrenheit, as a float.

    Raises:
        ValueError: If `c` is below absolute zero (-273.15).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def fahrenheit_to_celsius(f: float) -> float:
    """Convert a Fahrenheit temperature to Celsius.

    Args:
        f: Temperature in degrees Fahrenheit.

    Returns:
        The temperature in degrees Celsius, as a float.

    Raises:
        ValueError: If `f` is below absolute zero (-459.67).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
