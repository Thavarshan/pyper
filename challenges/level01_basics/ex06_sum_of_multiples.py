"""
Challenge: Sum of Multiples
Level:     01 - Basics
Topics:    loops, accumulators, any(), default arguments, tuples
Source:    Project Euler #1 "Multiples of 3 or 5"

========================================================================
YOUR TASK
========================================================================
Write `sum_of_multiples(limit, divisors=(3, 5))`. It adds up every
number from 1 up to, but NOT including, `limit` that is a multiple of
at least one of the `divisors`, and returns the total.

    sum_of_multiples(10)  ->  23

========================================================================
A WORKED EXAMPLE
========================================================================
Take limit 10 and the divisors 3 and 5. The numbers below 10 are 1 to
9. The ones that are multiples of 3 or 5 are 3, 5, 6 and 9:

    3 + 5 + 6 + 9 = 23

A number can be a multiple of several divisors. 15 is a multiple of
both 3 and 5, but it is still added only ONCE.

`divisors=(3, 5)` is a "default argument": the value used when the
caller leaves that argument out. So sum_of_multiples(10) is the same as
sum_of_multiples(10, (3, 5)).

========================================================================
THE RULES
========================================================================
Your function must:
1. Add up the natural numbers 1, 2, 3, ... that are STRICTLY BELOW
   `limit` (`limit` itself is NOT included) and divisible by at least
   one number in `divisors`.
2. Count each number ONCE, even when several divisors divide it.
3. Return an int.
4. Return 0 when `limit` <= 1, because there are no numbers to add.
   This includes 0 and negative limits. They are not an error.
5. Return 0 when `divisors` is empty (no number is a multiple of
   "nothing").
6. Raise ValueError if any divisor is 0 or negative. You cannot have
   multiples of zero, and dividing by zero would crash anyway.
7. Check the divisors FIRST. A bad divisor raises ValueError even when
   `limit` <= 1: sum_of_multiples(0, (0,)) raises ValueError.

You can assume:
- `limit` is an int.
- `divisors` is a tuple (or any other iterable, meaning anything you can
  loop over with `for`) of ints.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    sum_of_multiples(10)          ->  23
        3 + 5 + 6 + 9, using the default divisors (3, 5).

    sum_of_multiples(16)          ->  60
        3 + 5 + 6 + 9 + 10 + 12 + 15. 15 is a multiple of 3 AND 5,
        but it is added only once.

    sum_of_multiples(20, (7,))    ->  21
        7 + 14. `(7,)` is a tuple with one item: the comma makes it a
        tuple.

    sum_of_multiples(1)           ->  0
        There are no natural numbers below 1.

    sum_of_multiples(10, (0,))    ->  raises ValueError
        Zero is not a valid divisor.

========================================================================
EDGE CASES TO TEST
========================================================================
- The default divisors: sum_of_multiples(10) -> 23
- Multiples of both divisors count once: sum_of_multiples(16) -> 60
  (not 75, which you get if 15 is added twice)
- `limit` itself is excluded: sum_of_multiples(6) -> 8
  (3 + 5, not 3 + 5 + 6 = 14)
- sum_of_multiples(0), sum_of_multiples(1) and sum_of_multiples(-5)
  -> 0
- A single divisor: sum_of_multiples(20, (7,)) -> 21
- Empty divisors: sum_of_multiples(10, ()) -> 0
- A divisor of 1 means every number counts:
  sum_of_multiples(5, (1,)) -> 10 (1 + 2 + 3 + 4)
- A zero or negative divisor: sum_of_multiples(10, (0,)) and
  sum_of_multiples(10, (-3,)) -> raise ValueError
- A bad divisor is caught even with a small limit:
  sum_of_multiples(0, (0,)) -> raises ValueError
- The real Project Euler answer: sum_of_multiples(1000) -> 233168

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Loop over `range(1, limit)`. range already stops before `limit`.
2. Keep a running total in a variable that starts at 0 (an
   "accumulator") and add to it inside the loop.
3. To avoid double counting, ask ONE question for each number: "is it
   divisible by any divisor?" Then add it at most once.
4. `any(n % d == 0 for d in divisors)` answers that question in one
   line. `any(...)` is True when at least one of the checks is True.
5. Validate the divisors BEFORE the main loop.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Default parameter values (and why a tuple is a safe default, while
  a list would be a classic bug: look up "mutable default argument",
  where mutable means "can be changed in place")
- Tuples, including the one-item tuple syntax `(7,)`
- The accumulator pattern
- The built-ins `any()`, `all()` and `sum()`
- Generator expressions (like a list comprehension in round brackets,
  which produces items one at a time instead of building a list)

========================================================================
STRETCH GOALS
========================================================================
- Solve it as a single `return sum(...)` line.
- For huge limits (10**12) looping is too slow. For a single divisor d
  there is a formula: d * k * (k + 1) // 2 where k = (limit - 1) // d
  (k is how many multiples of d are below the limit). Use it with the
  inclusion-exclusion principle for (3, 5): add the multiples of 3,
  add the multiples of 5, then subtract the multiples of 15, because
  those were counted twice.
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
