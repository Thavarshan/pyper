"""
Challenge: Even or Odd
Level:     01 - Basics
Topics:    the modulo operator (%), booleans, conditionals, reusing functions
Source:    Classic beginner exercise

========================================================================
YOUR TASK
========================================================================
Write two small functions:

    is_even(n)      returns True if `n` is even, False if it is odd.
    even_or_odd(n)  returns the string "even" or "odd".

    is_even(4)  ->  True

========================================================================
WHAT "EVEN" MEANS
========================================================================
A whole number is EVEN when it divides by 2 with nothing left over
(the remainder is 0). Otherwise it is ODD.

    8 / 2 = 4, remainder 0   ->  even
    7 / 2 = 3, remainder 1   ->  odd

Zero is even: 0 / 2 = 0, remainder 0. Negative numbers follow the same
rule: -4 is even and -3 is odd.

========================================================================
THE RULES
========================================================================
Your functions must:
1. `is_even(n)` returns a real bool: True or False. Not 0 or 1, and
   not a string.
2. `even_or_odd(n)` returns exactly "even" or "odd", all lower-case.
3. Both work for positive numbers, negative numbers and zero.
4. Both work for huge numbers such as 10**100 (10 to the power 100).
   Python ints have no size limit.

Try to make `even_or_odd` CALL `is_even` instead of repeating the logic.

You can assume:
- `n` is an int.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    is_even(4)       ->  True
        4 / 2 = 2 with remainder 0.

    is_even(7)       ->  False
        7 / 2 = 3 with remainder 1.

    even_or_odd(0)   ->  'even'
        Zero divides by 2 with nothing left over.

    even_or_odd(-3)  ->  'odd'
        Negative numbers follow the same rule.

========================================================================
EDGE CASES TO TEST
========================================================================
- even_or_odd(0)   -> 'even'
- even_or_odd(1)   -> 'odd'    and even_or_odd(2)  -> 'even'
- even_or_odd(-1)  -> 'odd'    and even_or_odd(-2) -> 'even'
- even_or_odd(10**100) -> 'even' and even_or_odd(10**100 + 1) -> 'odd'
- `is_even` returns a real bool: `assert is_even(2) is True` and
  `assert is_even(3) is False`

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `n % 2` gives the remainder after dividing by 2. It is either 0 or 1.
2. In Python, `-3 % 2` is 1 (not -1), so the same check works for
   negative numbers.
3. A comparison like `n % 2 == 0` already IS a bool. You can return it
   directly, no `if` needed.
4. `even_or_odd` can use a conditional expression (a one-line
   if/else): "even" if is_even(n) else "odd".

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The `%` (modulo, the remainder) operator, including with negative
  numbers
- Comparison operators return bools
- Returning a bool expression directly instead of `if ...: return True`
- Conditional (ternary) expressions: `a if condition else b`
- Calling one of your own functions from another

========================================================================
STRETCH GOALS
========================================================================
- Write `is_even_bitwise(n)` using the bitwise AND operator: `n & 1`.
  It looks at the last binary digit of `n`, which is 1 for odd numbers
  and 0 for even ones.
- Write `split_even_odd(nums: list[int]) -> tuple[list[int], list[int]]`
  that returns (evens, odds), keeping the original order.
- Use `@pytest.mark.parametrize` (a pytest feature that runs one test
  once for each input you list) to test many numbers with one test.
"""


def is_even(n: int) -> bool:
    """Return True if `n` is even, False if it is odd.

    Args:
        n: Any integer (may be negative or zero).

    Returns:
        True when `n` is divisible by 2, otherwise False.
    """
    return n % 2 == 0



def even_or_odd(n: int) -> str:
    """Describe `n` as "even" or "odd".

    Args:
        n: Any integer (may be negative or zero).

    Returns:
        The string "even" or "odd".
    """
    return "even" if is_even(n) else "odd"


def split_even_odd(nums: list[int]) -> tuple[list[int], list[int]]:
    evens: list[int] = []
    odds: list[int] = []

    for num in nums:
        if is_even(num):
            evens.append(num)
        else:
            odds.append(num)

    return (evens, odds)


def is_even_bitwise(num: int) -> bool:
    return (num & 1) == 0
