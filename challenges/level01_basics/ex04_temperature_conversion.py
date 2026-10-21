"""
Challenge: Temperature Conversion
Level:     01 - Basics
Topics:    arithmetic, floats, formulas, raising exceptions, comparing floats
Source:    Classic beginner exercise

========================================================================
YOUR TASK
========================================================================
Write two functions that convert temperatures between the Celsius and
Fahrenheit scales. Each returns the answer as a float:

    celsius_to_fahrenheit(c)   uses   F = C * 9 / 5 + 32
    fahrenheit_to_celsius(f)   uses   C = (F - 32) * 5 / 9

    celsius_to_fahrenheit(100)  ->  212.0

========================================================================
BACKGROUND: ABSOLUTE ZERO AND FLOATS
========================================================================
ABSOLUTE ZERO is the coldest temperature physically possible: -273.15
degrees Celsius, which equals -459.67 degrees Fahrenheit. Nothing can
be colder, so a temperature BELOW it is an error.

Floats (numbers with a decimal point) are stored in binary, so tiny
rounding errors appear. For example, `0.1 + 0.2 == 0.3` is False in
Python, because 0.1 + 0.2 gives 0.30000000000000004. So when you test
a float result, never rely on `==` for "messy" numbers. Use one of:

    assert result == pytest.approx(98.6)       # recommended in tests
    assert round(result, 2) == 98.6            # round to 2 decimals

`pytest.approx(98.6)` means "98.6, give or take a tiny rounding error".

========================================================================
THE RULES
========================================================================
Your functions must:
1. `celsius_to_fahrenheit(c)` returns C * 9 / 5 + 32.
2. `fahrenheit_to_celsius(f)` returns (F - 32) * 5 / 9.
3. Always return a float, even for "round" answers and int input:
   celsius_to_fahrenheit(100) returns 212.0, not 212.
4. Return the full-precision result. Do NOT round it inside the
   function.
5. `celsius_to_fahrenheit` raises ValueError if c < -273.15.
6. `fahrenheit_to_celsius` raises ValueError if f < -459.67.
7. Accept exactly absolute zero (-273.15 C or -459.67 F) without an
   error.

You can assume:
- The input is an int or a float.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    celsius_to_fahrenheit(0)               ->  32.0
        Water freezes at 0 C: 0 * 9 / 5 + 32 = 32.

    celsius_to_fahrenheit(100)             ->  212.0
        Water boils at 100 C. The answer is a float, so 212.0.

    fahrenheit_to_celsius(-40)             ->  -40.0
        -40 is the one temperature that is the same on both scales.

    round(fahrenheit_to_celsius(98.6), 2)  ->  37.0
        98.6 F is body temperature. round() hides any tiny float
        error.

    celsius_to_fahrenheit(-300)            ->  raises ValueError
        That is colder than absolute zero.

========================================================================
EDGE CASES TO TEST
========================================================================
- Freezing point: celsius_to_fahrenheit(0) -> 32.0 and
  fahrenheit_to_celsius(32) -> 0.0
- Boiling point: celsius_to_fahrenheit(100) -> 212.0 and
  fahrenheit_to_celsius(212) -> 100.0
- -40 is the same on both scales: both functions turn -40 into -40.0
- Body temperature: celsius_to_fahrenheit(37) == pytest.approx(98.6)
- Exactly absolute zero is allowed: celsius_to_fahrenheit(-273.15) and
  fahrenheit_to_celsius(-459.67) do NOT raise
- Just below absolute zero: celsius_to_fahrenheit(-273.16) and
  fahrenheit_to_celsius(-460) -> raise ValueError
- Round trip: fahrenheit_to_celsius(celsius_to_fahrenheit(x)) ==
  pytest.approx(x), for example with x = 25.5
- The return type is float even for int input:
  isinstance(celsius_to_fahrenheit(0), float) -> True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. The `/` operator ALWAYS returns a float in Python 3, even 10 / 2
   gives 5.0. (Use `//` if you ever want integer "floor" division,
   which drops the remainder.)
2. Check the absolute-zero rule FIRST, before doing the maths.
3. Store the limits in module-level constants (names defined at the top
   of the file, outside any function), such as ABSOLUTE_ZERO_C =
   -273.15, so they have a name and are easy to reuse.
4. For the round-trip test, `pytest.approx` handles the tiny errors.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- int vs float and how `/` behaves
- Operator precedence (which operator Python works out first): why
  (F - 32) needs parentheses
- Floating-point imprecision and `pytest.approx` / `round()`
- Raising exceptions with a helpful message: raise ValueError("...")
- Module-level constants (UPPER_CASE names by convention)

========================================================================
STRETCH GOALS
========================================================================
- Add `celsius_to_kelvin` and `kelvin_to_celsius` (K = C + 273.15.
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
    if c < -273.15:
        raise ValueError("Nothing can be colder")
    return ((c * 9) / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    """Convert a Fahrenheit temperature to Celsius.

    Args:
        f: Temperature in degrees Fahrenheit.

    Returns:
        The temperature in degrees Celsius, as a float.

    Raises:
        ValueError: If `f` is below absolute zero (-459.67).
    """
    if f < -459.67:
        raise ValueError("Nothing can be colder")
    return (f - 32) * 5 / 9
