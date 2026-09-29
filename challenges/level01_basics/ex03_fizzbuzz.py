"""
Challenge: FizzBuzz
Level:     01 - Basics
Topics:    loops, conditionals, the modulo operator (%), building lists
Source:    Classic interview warm-up (also LeetCode #412 "Fizz Buzz")

========================================================================
PROBLEM
========================================================================
Write a function that takes a whole number `n` and returns a list of
strings for every number from 1 up to and including `n`, following
these rules:

    - If the number is divisible by 3 AND by 5  -> "FizzBuzz"
    - If the number is divisible by 3 only      -> "Fizz"
    - If the number is divisible by 5 only      -> "Buzz"
    - Otherwise                                 -> the number as a string,
                                                   e.g. 7 -> "7"

"Divisible by" means the remainder is zero. In Python the remainder
operator is `%`, so `9 % 3 == 0` is True and `10 % 3 == 0` is False.

========================================================================
EXAMPLES
========================================================================
    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> fizzbuzz(15)[-1]
    'FizzBuzz'

    >>> fizzbuzz(1)
    ['1']

========================================================================
CONSTRAINTS
========================================================================
- `n` is an int.
- 0 <= n <= 10_000 for normal input.
- If `n` is negative, raise a `ValueError` (it makes no sense to count
  up to a negative number).

========================================================================
EDGE CASES TO TEST
========================================================================
- n = 0         -> an empty list []
- n = 1         -> ['1']
- n = 3, 5, 15  -> the last element is 'Fizz', 'Buzz', 'FizzBuzz'
- The length of the result always equals n
- Every element is a str (not an int!)
- n = -1        -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `range(1, n + 1)` gives you 1, 2, ..., n. `range` stops BEFORE its
   second argument, which is why you need `n + 1`.
2. Order matters: check "divisible by both" FIRST. If you check "by 3"
   first, 15 will return "Fizz" and never reach the "FizzBuzz" branch.
3. "Divisible by 3 and 5" is the same as "divisible by 15".
4. `str(7)` turns the int 7 into the string "7".

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `for x in range(...)` loops
- `if / elif / else` chains and why their order matters
- The `%` (modulo) operator
- Creating a list with `[]` and adding to it with `.append()`
- Raising exceptions: `raise ValueError("message")`
- Type hints: `list[str]` means "a list whose items are strings"

========================================================================
STRETCH GOALS
========================================================================
- Rewrite your solution as a single list comprehension.
- Generalise it: `fizzbuzz_custom(n, rules)` where `rules` is a dict like
  {3: "Fizz", 5: "Buzz", 7: "Bazz"} so 105 -> "FizzBuzzBazz".
"""


def fizzbuzz(n: int) -> list[str]:
    """Return the FizzBuzz sequence for the numbers 1..n.

    Args:
        n: How many numbers to generate. Must be >= 0.

    Returns:
        A list of length `n` where each item is "Fizz", "Buzz",
        "FizzBuzz", or the number itself as a string.

    Raises:
        ValueError: If `n` is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
