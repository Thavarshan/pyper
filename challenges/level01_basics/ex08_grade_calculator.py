"""
Challenge: Grade Calculator
Level:     01 - Basics
Topics:    if / elif / else chains, range checks, lists, averages
Source:    Classic beginner exercise

========================================================================
YOUR TASK
========================================================================
Write two functions for a teacher's grade book:

    letter_grade(score)    turns one score from 0 to 100 into a letter.
    average_grade(scores)  returns the letter for the average of a list.

    letter_grade(95)  ->  'A'

========================================================================
THE RULES
========================================================================
Your functions must:
1. `letter_grade(score)` uses this table:

       score >= 90   -> "A"
       score >= 80   -> "B"
       score >= 70   -> "C"
       score >= 60   -> "D"
       below 60      -> "F"

   Each boundary belongs to the higher grade: exactly 90 is an "A",
   but 89.99 is a "B".
2. `letter_grade` raises ValueError if score < 0 or score > 100. 0 and
   100 themselves are valid.
3. `average_grade(scores)` works out the average (the mean: the sum
   divided by how many scores there are) and returns the letter grade
   of that average.
4. `average_grade` does NOT round the average first: an average of
   89.5 is a "B".
5. `average_grade` raises ValueError if the list is empty. You can't
   average nothing, and dividing by zero would crash.
6. `average_grade` raises ValueError if ANY single score is outside 0
   to 100.
7. `average_grade` does not change (mutate) the list it was given.
8. Both functions return a single upper-case letter as a str.

You can assume:
- Every score is an int or a float.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    letter_grade(95)             ->  'A'
        95 is at least 90.

    letter_grade(80)             ->  'B'
        Exactly on a boundary, so it gets the higher grade.

    letter_grade(59.9)           ->  'F'
        Just below 60.

    average_grade([90, 80, 70])  ->  'B'
        (90 + 80 + 70) / 3 = 80.0, and 80 is a "B".

    letter_grade(101)            ->  raises ValueError
        Scores only go up to 100.

========================================================================
EDGE CASES TO TEST
========================================================================
- Each boundary exactly: 90, 80, 70, 60 -> 'A', 'B', 'C', 'D'
- Just below each boundary: 89.9, 79.9, 69.9, 59.9
  -> 'B', 'C', 'D', 'F'
- The extremes: letter_grade(0) -> 'F' and letter_grade(100) -> 'A'
- letter_grade(-1) and letter_grade(100.1) -> raise ValueError
- One score: average_grade([75]) -> 'C'
- The average lands on a boundary: average_grade([85, 95]) -> 'A'
  (the average is 90.0)
- average_grade([]) -> raises ValueError
- One invalid score in the list: average_grade([90, 101])
  -> raises ValueError
- The list you pass to average_grade is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Validate first: `if score < 0 or score > 100: raise ValueError(...)`.
   Python also allows chained comparisons: `0 <= score <= 100`.
2. Check the grades from highest to lowest with `elif`. Each branch
   only runs if all the previous ones were False, so you don't need
   upper bounds like `score < 90` in the "B" branch.
3. `sum(scores) / len(scores)` is the average.
4. `average_grade` can reuse `letter_grade`. If you call letter_grade
   on every score, its own validation checks each one for you.

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
- Support "+" and "-" grades (for example, 97 and up is "A+", and 90
  to 92 is "A-").
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
