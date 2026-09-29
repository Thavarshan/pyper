"""
Challenge: Grade Calculator
Level:     01 - Basics
Topics:    if / elif / else chains, range checks, lists, averages
Source:    Classic beginner exercise

========================================================================
PROBLEM
========================================================================
Write two functions for a teacher's grade book.

1. `letter_grade(score)` turns a numeric score from 0 to 100 into a
   letter grade:

       score >= 90   -> "A"
       score >= 80   -> "B"
       score >= 70   -> "C"
       score >= 60   -> "D"
       below 60      -> "F"

   The boundaries are INCLUSIVE at the bottom: exactly 90 is an "A",
   89.99 is a "B".

2. `average_grade(scores)` takes a list of scores, computes their
   average (mean = sum divided by how many there are), and returns the
   letter grade of that average. Do not round the average first:
   an average of 89.5 is a "B".

========================================================================
EXAMPLES
========================================================================
    >>> letter_grade(95)
    'A'

    >>> letter_grade(80)
    'B'

    >>> letter_grade(59.9)
    'F'

    >>> average_grade([90, 80, 70])     # average is 80.0
    'B'

========================================================================
CONSTRAINTS
========================================================================
- Scores are ints or floats.
- letter_grade: if score < 0 or score > 100, raise ValueError.
  0 and 100 themselves are valid.
- average_grade:
    - If the list is empty, raise ValueError (you can't average nothing,
      and dividing by zero would crash).
    - If ANY individual score is outside 0-100, raise ValueError.
    - Do not modify the list you were given.
- Both functions return a single upper-case letter as a str.

========================================================================
EDGE CASES TO TEST
========================================================================
- Each boundary exactly: 90, 80, 70, 60 -> A, B, C, D
- Just below each boundary: 89.9, 79.9, 69.9, 59.9
- The extremes 0 -> "F" and 100 -> "A"
- -1 and 100.1 -> ValueError
- average_grade with one score
- average_grade where the average lands on a boundary (e.g. [85, 95])
- average_grade([]) -> ValueError
- average_grade with one invalid score in the list -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Validate first: `if score < 0 or score > 100: raise ValueError(...)`.
   Python also allows chained comparisons: `0 <= score <= 100`.
2. Check the grades from highest to lowest with `elif`; each branch only
   runs if all the previous ones were False, so you don't need upper
   bounds like `score < 90` in the "B" branch.
3. `sum(scores) / len(scores)` is the average.
4. `average_grade` can reuse `letter_grade` - and letter_grade's own
   validation can check each score if you call it on every score.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Ordering `if / elif / else` chains
- Chained comparisons: `0 <= x <= 100`
- Built-ins `sum()` and `len()`
- Checking for an empty list with `if not scores:`
- Reusing a function inside another function

========================================================================
STRETCH GOALS
========================================================================
- Support "+" and "-" grades (e.g. 97+ is "A+", 90-92 is "A-").
- Store the thresholds in a list of (minimum, letter) tuples and loop
  over it instead of writing an elif chain.
- Write `grade_distribution(scores) -> dict[str, int]` counting how many
  of each letter there are.
"""


def letter_grade(score: float) -> str:
    """Convert a numeric score to a letter grade.

    Args:
        score: A number from 0 to 100 inclusive.

    Returns:
        One of "A", "B", "C", "D", "F".

    Raises:
        ValueError: If `score` is below 0 or above 100.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def average_grade(scores: list[float]) -> str:
    """Return the letter grade of the average of `scores`.

    Args:
        scores: A non-empty list of numbers, each from 0 to 100.

    Returns:
        The letter grade (see `letter_grade`) of the mean score.

    Raises:
        ValueError: If `scores` is empty or any score is outside 0-100.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
