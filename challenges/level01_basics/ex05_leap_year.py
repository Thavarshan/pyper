"""
Challenge: Leap Year
Level:     01 - Basics
Topics:    boolean logic (and / or / not), modulo, nested conditions
Source:    Classic beginner exercise (Gregorian calendar rules)

========================================================================
PROBLEM
========================================================================
A LEAP YEAR has 366 days instead of 365 (February gets a 29th day).
Write `is_leap_year(year)` that returns True if `year` is a leap year
in the Gregorian calendar (the calendar most of the world uses), and
False otherwise.

The Gregorian rules are:

    1. A year divisible by 4 is a leap year...
    2. ...EXCEPT a year divisible by 100 is NOT a leap year...
    3. ...EXCEPT a year divisible by 400 IS a leap year after all.

So 2024 is a leap year (rule 1), 1900 is not (rule 2), and 2000 is
(rule 3). 2023 is not (not divisible by 4 at all).

We apply these rules to every year from 1 onwards, even though the
calendar was actually introduced in 1582 (this is called the
"proleptic" Gregorian calendar - you don't need to worry about history).

========================================================================
EXAMPLES
========================================================================
    >>> is_leap_year(2024)
    True

    >>> is_leap_year(1900)
    False

    >>> is_leap_year(2000)
    True

    >>> is_leap_year(2023)
    False

========================================================================
CONSTRAINTS
========================================================================
- `year` is an int.
- If `year < 1`, raise ValueError (there is no year 0 in this calendar).
- Return a real bool.

========================================================================
EDGE CASES TO TEST
========================================================================
- Divisible by 4 but not 100 (e.g. 1996, 2024)     -> True
- Divisible by 100 but not 400 (e.g. 1900, 2100)   -> False
- Divisible by 400 (e.g. 1600, 2000)               -> True
- Not divisible by 4 (e.g. 2019, 2023)             -> False
- Year 1 -> False; year 4 -> True
- Year 0 and negative years                         -> ValueError
- Bonus: compare against the stdlib `calendar.isleap` for a range of
  years in a loop

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. "Divisible by 4" in code is `year % 4 == 0`.
2. Check the most specific rule first: is it divisible by 400? Then by
   100? Then by 4?
3. The whole rule fits in one boolean expression:
   (divisible by 4 AND not by 100) OR (divisible by 400).
4. The standard library has `calendar.isleap(year)` - don't use it in
   your solution, but it's a great "oracle" to test against!

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Combining conditions with `and`, `or`, `not`
- Parentheses to make the grouping of boolean logic explicit
- if / elif / else ordering from most specific to most general
- Using a trusted stdlib function as a test oracle

========================================================================
STRETCH GOALS
========================================================================
- Write `days_in_year(year) -> int` returning 365 or 366.
- Write `days_in_month(year, month) -> int` (ValueError for month
  outside 1-12).
- Write `leap_years_between(start, end) -> list[int]` (inclusive).
"""


def is_leap_year(year: int) -> bool:
    """Return True if `year` is a Gregorian leap year.

    Args:
        year: A calendar year, 1 or greater.

    Returns:
        True if the year has 366 days, otherwise False.

    Raises:
        ValueError: If `year` is less than 1.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
