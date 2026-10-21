"""
Challenge: Leap Year
Level:     01 - Basics
Topics:    boolean logic (and / or / not), modulo, nested conditions
Source:    Classic beginner exercise (Gregorian calendar rules)

========================================================================
YOUR TASK
========================================================================
Write `is_leap_year(year)`. It returns True if `year` is a leap year in
the Gregorian calendar, and False if it is not.

    is_leap_year(2024)  ->  True

========================================================================
WHAT "LEAP YEAR" MEANS
========================================================================
A LEAP YEAR has 366 days instead of 365: February gets a 29th day. The
Gregorian calendar (the one most of the world uses) picks leap years
with three rules. Each rule is an exception to the one before it:

    1. A year divisible by 4 is a leap year...
    2. ...EXCEPT a year divisible by 100 is NOT a leap year...
    3. ...EXCEPT a year divisible by 400 IS a leap year after all.

Walking through some years:

    2024: divisible by 4, not by 100           ->  leap     (rule 1)
    1900: divisible by 4 and 100, not by 400   ->  not leap (rule 2)
    2000: divisible by 4, 100 and 400          ->  leap     (rule 3)
    2023: not divisible by 4 at all            ->  not leap

The calendar was really introduced in 1582, but we apply these rules to
every year from 1 onwards. This is called the "proleptic" Gregorian
calendar. You don't need to worry about the history.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return True for a leap year and False otherwise, using the three
   rules above.
2. Return a real bool: True or False.
3. Raise ValueError if `year` is less than 1 (there is no year 0 in
   this calendar).

You can assume:
- `year` is an int.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    is_leap_year(2024)  ->  True
        Divisible by 4, and not by 100.

    is_leap_year(1900)  ->  False
        Divisible by 100 but not by 400.

    is_leap_year(2000)  ->  True
        Divisible by 400, so it is a leap year after all.

    is_leap_year(2023)  ->  False
        Not divisible by 4.

    is_leap_year(0)     ->  raises ValueError
        Years start at 1.

========================================================================
EDGE CASES TO TEST
========================================================================
- Divisible by 4 but not 100: 1996 and 2024    -> True
- Divisible by 100 but not 400: 1900 and 2100  -> False
- Divisible by 400: 1600 and 2000              -> True
- Not divisible by 4: 2019 and 2023            -> False
- Year 1 -> False, year 4 -> True
- Year 0 and negative years such as -4         -> raise ValueError
- Bonus: in a loop over many years (say 1 to 3000), check that your
  answer matches the standard library's `calendar.isleap(year)`

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. "Divisible by 4" in code is `year % 4 == 0`.
2. Check the most specific rule first: is it divisible by 400? Then by
   100? Then by 4?
3. The whole rule fits in one boolean expression:
   (divisible by 4 AND not by 100) OR (divisible by 400).
4. The standard library has `calendar.isleap(year)`. Don't use it in
   your solution, but it's a great "oracle" (a trusted source of right
   answers) to test against!

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Combining conditions with `and`, `or`, `not`
- Parentheses to make the grouping of boolean logic explicit
- if / elif / else ordering from most specific to most general
- Using a trusted standard-library function as a test oracle

========================================================================
STRETCH GOALS
========================================================================
- Write `days_in_year(year) -> int` returning 365 or 366.
- Write `days_in_month(year, month) -> int` (ValueError for a month
  outside 1-12).
- Write `leap_years_between(start, end) -> list[int]`, including both
  `start` and `end` themselves.
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
