"""
Challenge: Sum of Digits and Digital Root
Level:     07 - Recursion
Topics:    recursion basics, base case, recursive case, // and %, abs()
Source:    Classic recursion exercise (digital root is also LeetCode #258
           "Add Digits")

========================================================================
YOUR TASK
========================================================================
Write two functions, both RECURSIVE (they call themselves):

- `sum_digits(n)` adds up the digits of the integer `n`.
- `digital_root(n)` keeps adding up the digits until only one digit
  is left, and returns that digit.

    sum_digits(1234)    ->  10    (1 + 2 + 3 + 4)
    digital_root(9875)  ->  2     (9875 -> 29 -> 11 -> 2)

========================================================================
WHAT IS RECURSION? (read this first)
========================================================================
A function is RECURSIVE when it calls itself. Instead of looping, it
solves a small piece of the problem. Then it hands the smaller rest of
the problem to another call of itself.

Every recursive function needs two parts:

    1. BASE CASE: an input so small that the answer is obvious. The
       function returns straight away, WITHOUT calling itself.
       Without a base case the function would call itself forever.
    2. RECURSIVE CASE: the function does a little work, then calls
       itself on a SMALLER input and uses that result. "Smaller" must
       always move towards the base case.

Example, counting down:

    def countdown(n):
        if n == 0:                      # base case
            return [0]
        return [n] + countdown(n - 1)   # recursive case (n shrinks)

    countdown(3)  ->  [3, 2, 1, 0]

THE CALL STACK: each time a function is called, Python stores that
call's local variables in a "frame". It puts the frame on top of a pile
called the call stack. countdown(3) calls countdown(2), which calls
countdown(1), which calls countdown(0). Now four frames are waiting on
the stack. countdown(0) returns first. Then each waiting frame finishes,
in reverse order.

RecursionError: Python limits how tall the stack may grow (about 1000
frames by default, see `sys.getrecursionlimit()`). If you forget the
base case, or your input never gets smaller, Python stops you with
`RecursionError: maximum recursion depth exceeded`. If you see this
error, check that (a) the base case exists and (b) every recursive call
moves closer to it.

WHAT "DIGITAL ROOT" MEANS: sum the digits, then sum the digits of that
answer, and so on, until a single digit (0 to 9) remains:

    9875  ->  9+8+7+5 = 29  ->  2+9 = 11  ->  1+1 = 2

So digital_root(9875) is 2.

Two bits of arithmetic do most of the work:

    n % 10   ->  the LAST digit of n            (1234 % 10  == 4)
    n // 10  ->  n with its last digit removed  (1234 // 10 == 123)

========================================================================
THE RULES
========================================================================
Your functions must:
1. `sum_digits(n)`: return the sum of the decimal digits of `n`.
2. `digital_root(n)`: return the single digit (0 to 9) you reach by
   summing the digits again and again.
3. Ignore the sign of a negative `n` (use its absolute value), so
   sum_digits(-1234) is 10, the same as sum_digits(1234). This applies
   to both functions.
4. Raise `TypeError` if `n` is not an int.
5. Be recursive. No `for` or `while` loops, and no turning `n` into a
   `str` and adding up the characters (that skips the lesson).
6. Make the recursion depth (how many calls are waiting on the stack at
   once) grow with the NUMBER OF DIGITS, not with the size of the
   number. A 300-digit number should need about 300 calls, not
   anything like 10**300.

You may (and should) call sum_digits from inside digital_root.

You can assume:
- `n` can be negative, zero or positive, with up to about 300 digits.
- `bool` counts as a kind of int in Python. You may treat True and
  False as 1 and 0. This is not tested.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    sum_digits(1234)    ->  10
        1 + 2 + 3 + 4 = 10.

    sum_digits(-907)    ->  16
        The minus sign is ignored: 9 + 0 + 7 = 16.

    sum_digits(0)       ->  0
        0 has one digit, and it is 0.

    digital_root(9875)  ->  2
        9875 -> 29 -> 11 -> 2.

    digital_root(7)     ->  7
        Already a single digit, so nothing to do.

========================================================================
COMPLEXITY TARGET
========================================================================
d is the number of digits in n. "O(d)" means the work grows in step
with d: twice as many digits, about twice as much work.

- Time:  O(d). Each call peels off one digit, so there are about d
  calls.
- Space: O(d) for the call stack. All d calls are waiting on the stack
  at the deepest point, one frame per digit.
- digital_root: O(d) overall. After the first digit sum the number is
  tiny (a 300-digit number sums to at most 2700), so the later rounds
  cost almost nothing.

========================================================================
EDGE CASES TO TEST
========================================================================
- sum_digits(0)          -> 0
- A single digit: sum_digits(7) -> 7
- A negative number: sum_digits(-1234) -> 10
- Zeros inside the number: sum_digits(1005) -> 6
- A big number: sum_digits(10**100) -> 1
- digital_root(0) -> 0, digital_root(9) -> 9, digital_root(10) -> 1
- A negative number: digital_root(-38) -> 2   (38 -> 11 -> 2)
- Not an int: sum_digits("12") and sum_digits(1.5) -> raise TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Deal with the sign once, at the start: `n = abs(n)`. You can do this
   in the public function and put the recursion in a private helper,
   or just recurse on abs(n). Both are fine.
2. Base case for sum_digits: if n < 10, the answer is n itself.
3. Recursive case: the last digit plus the sum of the other digits,
   written `n % 10 + sum_digits(n // 10)`.
4. digital_root: if n < 10 you are done. Otherwise return
   digital_root(sum_digits(n)).
5. Use `isinstance(n, int)` to check the type.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Recursion: base case, recursive case, call stack
- `RecursionError` and `sys.getrecursionlimit()`
- Integer division `//` and modulo `%` (the remainder)
- `abs()` for absolute value
- `isinstance()` for type checking, and `raise TypeError(...)`

========================================================================
STRETCH GOALS
========================================================================
- digital_root has a famous O(1) formula (constant time: the same work
  whatever the size of n). For n > 0 it is `1 + (n - 1) % 9`. Write a
  test that checks your recursive version agrees with the formula for
  every n in range(1, 10_000).
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
