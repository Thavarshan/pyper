"""
Challenge: Factorial
Level:     01 - Basics
Topics:    loops, accumulators, isinstance(), TypeError vs ValueError
Source:    Classic beginner exercise

========================================================================
PROBLEM
========================================================================
The FACTORIAL of a non-negative whole number n, written n!, is the
product of all whole numbers from 1 up to n:

    5! = 5 * 4 * 3 * 2 * 1 = 120
    1! = 1
    0! = 1      (by definition - the "empty product" is 1)

Write `factorial(n)` that computes n! using a LOOP (an iterative
solution). Do not use `math.factorial` and do not use recursion here
(recursion comes in a later level).

Input validation - two different kinds of "wrong":

    - Wrong TYPE  (e.g. 5.0, "5", None)   -> raise TypeError
    - Wrong VALUE (a negative int like -3) -> raise ValueError

About bools: in Python `bool` is a subclass of `int`, so
`isinstance(True, int)` is True and `True + True == 2`. Passing a bool
to factorial is almost certainly a bug, so in this challenge we DECIDE:
bools are REJECTED with TypeError. (factorial(True) raises TypeError.)

========================================================================
EXAMPLES
========================================================================
    >>> factorial(5)
    120

    >>> factorial(0)
    1

    >>> factorial(10)
    3628800

========================================================================
CONSTRAINTS
========================================================================
- `n` must be an int (but not a bool); otherwise raise TypeError.
  Note: 5.0 is a float, so it raises TypeError even though it is "whole".
- If n < 0, raise ValueError.
- Check the type BEFORE the value (so factorial("x") raises TypeError,
  not some confusing comparison error).
- Return an int. Python ints grow without limit, so factorial(100) works.

========================================================================
EDGE CASES TO TEST
========================================================================
- 0 -> 1 and 1 -> 1
- A small value, 5 -> 120
- A larger value such as 20 -> 2432902008176640000
- Compare to math.factorial for n in range(30) (fine to use in TESTS)
- Negative number -> ValueError
- Float (5.0), string ("5"), None -> TypeError
- True / False -> TypeError (our decision about bools)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with `result = 1` (not 0 - multiplying by 0 ruins everything).
2. Loop `for i in range(2, n + 1):` and do `result *= i`.
3. `isinstance(n, int)` checks the type; because bool is a subclass of
   int you ALSO need `isinstance(n, bool)` to reject bools.
4. Order your checks: bool/type first, then negative, then compute.
5. Notice that 0 and 1 need no special case if your loop starts at 2.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The accumulator pattern with multiplication (`*=`)
- `isinstance()` and class inheritance (bool is an int!)
- TypeError vs ValueError: which one describes the problem?
- Python's arbitrary-precision integers
- Using `pytest.raises` to check exceptions

========================================================================
STRETCH GOALS
========================================================================
- Rewrite it with a `while` loop.
- Write it using `functools.reduce` and `operator.mul`.
- Write `count_trailing_zeros(n)` - how many zeros end n!? (Hint: count
  factors of 5, without computing n!.)
"""


def factorial(n: int) -> int:
    """Return n! computed iteratively.

    Args:
        n: A non-negative integer (bools are not accepted).

    Returns:
        The product 1 * 2 * ... * n, with factorial(0) == 1.

    Raises:
        TypeError: If `n` is not an int, or is a bool.
        ValueError: If `n` is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
