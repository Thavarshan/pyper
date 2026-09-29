"""
Challenge: Sum of Multiples
Level:     01 - Basics
Topics:    loops, accumulators, any(), default arguments, tuples
Source:    Project Euler #1 "Multiples of 3 or 5"

========================================================================
PROBLEM
========================================================================
The natural numbers below 10 that are multiples of 3 or 5 are
3, 5, 6 and 9. Their sum is 23.

Write `sum_of_multiples(limit, divisors=(3, 5))` that returns the sum of
all natural numbers STRICTLY BELOW `limit` that are divisible by AT LEAST
ONE of the numbers in `divisors`.

- "Natural numbers" here means 1, 2, 3, ... (we start at 1).
- "Strictly below" means `limit` itself is NOT included.
- A number that is a multiple of several divisors (like 15, which is a
  multiple of both 3 and 5) is counted ONCE, not twice.
- A "default argument" is a value used when the caller leaves that
  argument out, so sum_of_multiples(10) is the same as
  sum_of_multiples(10, (3, 5)).

========================================================================
EXAMPLES
========================================================================
    >>> sum_of_multiples(10)
    23

    >>> sum_of_multiples(16)          # 3+5+6+9+10+12+15 (15 once!)
    60

    >>> sum_of_multiples(20, (7,))    # 7 + 14
    21

    >>> sum_of_multiples(1)
    0

========================================================================
CONSTRAINTS
========================================================================
- `limit` is an int. If `limit <= 1` there are no numbers to add, so
  return 0 (this includes 0 and negative limits - no error).
- `divisors` is a tuple (or any iterable) of positive ints.
- If any divisor is 0 or negative, raise ValueError (you cannot have
  multiples of zero, and dividing by zero would crash anyway).
  Check this FIRST: a bad divisor raises ValueError even when `limit <= 1`,
  e.g. sum_of_multiples(0, (0,)) -> ValueError.
- If `divisors` is empty, return 0 (no number is a multiple of "nothing").
- Return an int.

========================================================================
EDGE CASES TO TEST
========================================================================
- The default divisors: limit 10 -> 23
- Numbers that are multiples of both divisors are only counted once
- `limit` itself is excluded: sum_of_multiples(6) is 3 + 5 = 8 (not 14)
- limit 0, 1, and negative -> 0
- A single divisor, e.g. (7,)
- Empty divisors () -> 0
- A divisor of 1 means every number counts: sum_of_multiples(5, (1,)) = 10
- A zero or negative divisor -> ValueError
- The real Project Euler answer: sum_of_multiples(1000) == 233168

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Loop over `range(1, limit)` - range already stops before `limit`.
2. Keep a running total in a variable that starts at 0 (an
   "accumulator") and add to it inside the loop.
3. To avoid double counting, for each number ask ONE question: "is it
   divisible by any divisor?" - then add it at most once.
4. `any(n % d == 0 for d in divisors)` answers that question in one line.
5. Validate the divisors BEFORE the main loop.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Default parameter values (and why a tuple is a safe default, while
  a list would be a classic bug - look up "mutable default argument")
- Tuples, including the one-item tuple syntax `(7,)`
- The accumulator pattern
- The built-ins `any()`, `all()` and `sum()`
- Generator expressions

========================================================================
STRETCH GOALS
========================================================================
- Solve it as a single `return sum(...)` line.
- For huge limits (10**12) looping is too slow. For a single divisor d
  there is a formula: d * k * (k + 1) // 2 where k = (limit - 1) // d.
  Use it with the inclusion-exclusion principle for (3, 5).
"""


def sum_of_multiples(limit: int, divisors: tuple[int, ...] = (3, 5)) -> int:
    """Sum the natural numbers below `limit` divisible by any divisor.

    Args:
        limit: Upper bound (exclusive). Values <= 1 give 0.
        divisors: Positive integers to test divisibility against.

    Returns:
        The sum of every n with 1 <= n < limit where n is divisible by at
        least one divisor. Each qualifying n is counted once.

    Raises:
        ValueError: If any divisor is zero or negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
