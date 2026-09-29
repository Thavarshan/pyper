"""
Challenge: Even or Odd
Level:     01 - Basics
Topics:    the modulo operator (%), booleans, conditionals, reusing functions
Source:    Classic beginner exercise

========================================================================
PROBLEM
========================================================================
Write two small functions:

1. `is_even(n)` returns the bool `True` if the whole number `n` is even
   and `False` if it is odd.
2. `even_or_odd(n)` returns the string "even" or "odd" (all lower-case).

A number is EVEN when it divides by 2 with nothing left over (the
remainder is 0). Otherwise it is ODD.

Zero is even (0 / 2 = 0 with remainder 0). Negative numbers follow the
same rule: -4 is even, -3 is odd.

Try to make `even_or_odd` CALL `is_even` instead of repeating the logic.

========================================================================
EXAMPLES
========================================================================
    >>> is_even(4)
    True

    >>> is_even(7)
    False

    >>> even_or_odd(0)
    'even'

    >>> even_or_odd(-3)
    'odd'

========================================================================
CONSTRAINTS
========================================================================
- `n` is an int (positive, negative or zero). Very large ints such as
  10**100 must work too - Python ints have no size limit.
- `is_even` must return an actual bool (True/False), not 0/1 and not a
  string.
- `even_or_odd` must return exactly "even" or "odd".

========================================================================
EDGE CASES TO TEST
========================================================================
- 0                -> even
- 1 and 2          -> odd, even
- -1 and -2        -> odd, even
- A huge number like 10**100 -> even, 10**100 + 1 -> odd
- `is_even(...)` returns something whose type is bool
  (tip: `assert is_even(2) is True`)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `n % 2` gives the remainder after dividing by 2. It is either 0 or 1.
2. In Python, `-3 % 2` is 1 (not -1), so the same check works for
   negatives.
3. A comparison like `n % 2 == 0` already IS a bool - you can return it
   directly, no `if` needed.
4. `even_or_odd` can use a conditional expression:
   "even" if is_even(n) else "odd".

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The `%` (modulo) operator, including with negative numbers
- Comparison operators return bools
- Returning a bool expression directly instead of `if ...: return True`
- Conditional (ternary) expressions: `a if condition else b`
- Calling one of your own functions from another

========================================================================
STRETCH GOALS
========================================================================
- Write `is_even_bitwise(n)` using the bitwise AND operator: `n & 1`.
- Write `split_even_odd(nums: list[int]) -> tuple[list[int], list[int]]`
  that returns (evens, odds), keeping the original order.
- Use `@pytest.mark.parametrize` to test many numbers with one test.
"""


def is_even(n: int) -> bool:
    """Return True if `n` is even, False if it is odd.

    Args:
        n: Any integer (may be negative or zero).

    Returns:
        True when `n` is divisible by 2, otherwise False.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def even_or_odd(n: int) -> str:
    """Describe `n` as "even" or "odd".

    Args:
        n: Any integer (may be negative or zero).

    Returns:
        The string "even" or "odd".
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
