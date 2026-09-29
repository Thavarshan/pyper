"""
Challenge: Sum of Digits and Digital Root
Level:     07 - Recursion
Topics:    recursion basics, base case, recursive case, // and %, abs()
Source:    Classic recursion exercise (digital root is also LeetCode #258
           "Add Digits")

========================================================================
WHAT IS RECURSION? (read this first)
========================================================================
A function is RECURSIVE when it calls itself. Instead of looping, it
solves a small piece of the problem and hands the (smaller) rest of the
problem to another call of itself.

Every recursive function needs two parts:

    1. BASE CASE      - an input so small that the answer is obvious.
                        The function returns immediately WITHOUT calling
                        itself. Without a base case the function would
                        call itself forever.
    2. RECURSIVE CASE - the function does a little work, then calls
                        itself on a SMALLER input, and combines the
                        result. "Smaller" must always move towards the
                        base case.

Example - counting down:

    def countdown(n):
        if n == 0:              # base case
            return [0]
        return [n] + countdown(n - 1)   # recursive case (n gets smaller)

THE CALL STACK: every time a function is called, Python stores that
call's local variables in a "frame" and pushes it onto the call stack.
countdown(3) calls countdown(2), which calls countdown(1), which calls
countdown(0). Now four frames are waiting on the stack. countdown(0)
returns first, then each waiting frame finishes in reverse order.

RecursionError: Python limits how deep the stack may grow (about 1000
frames by default, see `sys.getrecursionlimit()`). If you forget the
base case, or your input never gets smaller, Python stops you with
`RecursionError: maximum recursion depth exceeded`. If you see this
error, check that (a) the base case exists and (b) every recursive call
moves closer to it.

========================================================================
PROBLEM
========================================================================
Part 1 - sum_digits(n):
    Return the sum of the decimal digits of the integer `n`.
    For example 1234 -> 1 + 2 + 3 + 4 = 10.
    If `n` is negative, ignore the sign (use its absolute value), so
    -1234 -> 10 as well.

Part 2 - digital_root(n):
    The DIGITAL ROOT of a number is what you get by summing its digits
    over and over until only a single digit (0-9) remains.
        9875 -> 9+8+7+5 = 29 -> 2+9 = 11 -> 1+1 = 2
    So digital_root(9875) == 2. Negative numbers use their absolute
    value as well.

BOTH functions must be written recursively. You may (and should) call
sum_digits from inside digital_root.

Useful arithmetic:
    n % 10   -> the LAST digit of n      (1234 % 10  == 4)
    n // 10  -> n with the last digit removed (1234 // 10 == 123)

========================================================================
EXAMPLES
========================================================================
    >>> sum_digits(1234)
    10

    >>> sum_digits(-907)
    16

    >>> sum_digits(0)
    0

    >>> digital_root(9875)
    2

    >>> digital_root(7)
    7

========================================================================
CONSTRAINTS
========================================================================
- `n` is an int (it can be negative, zero, or positive).
- |n| can have up to ~300 digits; your recursion depth should grow with
  the number of digits, not with the size of the number.
- If `n` is not an int, raise a `TypeError`. Note: `bool` is a subclass
  of int in Python; you may treat True/False as ints (1/0) - it is not
  tested.
- Solutions must be recursive (no `for`/`while` loops, and no
  converting to `str` and summing characters - that skips the lesson).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(d) where d is the number of digits in n.
- Space: O(d) for the call stack (one frame per digit).
- digital_root: O(d) overall - after the first digit sum the number is
  tiny, so the later rounds cost almost nothing.

========================================================================
EDGE CASES TO TEST
========================================================================
- sum_digits(0)          -> 0
- A single digit, e.g. sum_digits(7) -> 7
- Negative numbers: sum_digits(-1234) -> 10
- Numbers with zeros inside: sum_digits(1005) -> 6
- A big number, e.g. sum_digits(10**100) -> 1
- digital_root(0) -> 0, digital_root(9) -> 9, digital_root(10) -> 1
- digital_root of a negative number, e.g. digital_root(-38) -> 2
- Non-int input like sum_digits("12") or sum_digits(1.5) -> TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Handle the sign once at the start: `n = abs(n)`. (You can do this in
   a public function and put the recursion in a private helper, or just
   recurse on abs(n) - both are fine.)
2. Base case for sum_digits: if n < 10, the answer is n itself.
3. Recursive case: last digit + sum_digits(everything except the last
   digit), i.e. `n % 10 + sum_digits(n // 10)`.
4. digital_root: if n < 10 you are done; otherwise return
   digital_root(sum_digits(n)).
5. Use `isinstance(n, int)` to validate the type.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Recursion: base case, recursive case, call stack
- `RecursionError` and `sys.getrecursionlimit()`
- Integer division `//` and modulo `%`
- `abs()` for absolute value
- `isinstance()` for type checking and `raise TypeError(...)`

========================================================================
STRETCH GOALS
========================================================================
- digital_root has a famous O(1) formula: for n > 0 it is
  `1 + (n - 1) % 9`. Write a test that checks your recursive version
  agrees with the formula for every n in range(1, 10_000).
- Write `count_digits(n)` recursively (0 has 1 digit).
- Write `reverse_number(n)` recursively: 1234 -> 4321.
"""


def sum_digits(n: int) -> int:
    """Return the sum of the decimal digits of `n` (sign ignored).

    Must be implemented recursively.

    Args:
        n: Any integer. Negative values are treated as abs(n).

    Returns:
        The sum of the digits of abs(n). sum_digits(0) == 0.

    Raises:
        TypeError: If `n` is not an int.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def digital_root(n: int) -> int:
    """Repeatedly sum the digits of `n` until a single digit remains.

    Must be implemented recursively.

    Args:
        n: Any integer. Negative values are treated as abs(n).

    Returns:
        A single digit in the range 0..9.

    Raises:
        TypeError: If `n` is not an int.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
