"""
Challenge: Safe Divide
Level:     06 - Errors and Parsing
Topics:    try / except / else / finally, default values, recovering from errors
Source:    Classic exception-handling exercise

========================================================================
YOUR TASK
========================================================================
Write two functions:

- `safe_divide(a, b, default=None)` returns `a / b`, or `default` if
  `b` is zero.
- `divide_all(pairs, default=None)` does the same for every (a, b)
  pair in a list, and returns a list of the results.

    safe_divide(10, 4)  ->  2.5
    safe_divide(1, 0)   ->  None

========================================================================
BACKGROUND: TRY / EXCEPT / ELSE / FINALLY IN ONE PICTURE
========================================================================
When something goes wrong, Python "raises an exception": it stops
running the current code and looks for an `except` block that handles
that kind of error.

    try:
        risky()                 # code that might raise an exception
    except ZeroDivisionError:
        handle_it()             # runs ONLY if that exception was raised
    else:
        on_success()            # runs ONLY if NO exception was raised
    finally:
        clean_up()              # ALWAYS runs, error or not

- Catch the most SPECIFIC exception you can. A bare `except:` or
  `except Exception:` catches almost everything, so it also hides real
  bugs (like typos). Avoid it.
- An exception you don't catch keeps travelling up to whoever called
  your function. This is called "propagating".
- `else` keeps the try block small: only the risky line goes in `try`.
- `finally` is for cleanup, like closing files. (You'll mostly use
  `with` for that instead.)

========================================================================
THE RULES
========================================================================
For `safe_divide`, your function must:
1. Return `a / b`, using true division `/` (not `//`), so the result
   is a float.
2. Use try/except. Do NOT check `if b == 0` first: the point is to
   practise exceptions.
3. Catch the `ZeroDivisionError` that Python raises when `b` is zero
   (both 0 and 0.0), and return `default` instead.
4. Catch ONLY ZeroDivisionError. Any other error must propagate to the
   caller unchanged. For example, safe_divide("6", 2) raises
   TypeError.
5. Accept any value as `default` (None, 0, float("inf"), "n/a"...).

For `divide_all`, your function must:
6. Return a NEW list with `safe_divide(a, b, default)` for each (a, b)
   pair, in the same order.
7. Keep going after a zero divisor: one bad pair must not stop the
   others from being computed.
8. Not change (mutate) `pairs`.

You can assume:
- For normal use, `a` and `b` are numbers (int or float).
- `pairs` is a list of (a, b) tuples.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    safe_divide(10, 4)               ->  2.5
        Plain division.

    safe_divide(6, 3)                ->  2.0
        `/` always gives a float, even when ints divide evenly.

    safe_divide(1, 0)                ->  None
        Dividing by zero raises ZeroDivisionError, so the default,
        None, is returned instead.

    safe_divide(1, 0, default=0)     ->  0
        The same, with a different default.

    safe_divide("6", 2)              ->  raises TypeError
        Not a ZeroDivisionError, so it is not caught.

    divide_all([(10, 2), (3, 0), (9, 3)], default=-1)
        ->  [5.0, -1, 3.0]
        The middle pair divides by zero and gets -1. The others still
        work.

========================================================================
EDGE CASES TO TEST
========================================================================
- Normal division, including negative numbers:
  safe_divide(-6, 4) -> -1.5
- Integer inputs give a float: safe_divide(6, 3) == 2.0
- Divisor 0 and 0.0 -> default
- Custom default values: safe_divide(1, 0, "n/a") -> 'n/a' (try 0 and
  float("inf") too)
- 0 divided by something: safe_divide(0, 5) -> 0.0
- Wrong types propagate: `pytest.raises(TypeError)` around
  safe_divide("6", 2)
- divide_all([]) -> []
- Several zero divisors in the middle:
  divide_all([(4, 2), (1, 0), (2, 0), (9, 3)], 0) -> [2.0, 0, 0, 3.0]

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Put `return a / b` inside `try:`, and `return default` inside
   `except ZeroDivisionError:`.
2. For divide_all, reuse safe_divide in a loop or a comprehension.
   Unpack each pair with `for a, b in pairs`.
3. To make other errors propagate, just DON'T catch them.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- try / except / else / finally and when each block runs
- Catching specific exceptions vs catching everything
- Exception propagation
- Default parameter values (and why `None` is the usual "no value")
- Tuple unpacking in for loops
- `pytest.raises` as a context manager (used with `with`)

========================================================================
STRETCH GOALS
========================================================================
- Add a `log` list parameter. Append a message to it in `except`, and
  "done" in `finally`. Then write tests that prove the order in which
  the blocks run.
- Write `safe_call(func, *args, default=None, catch=(Exception,))`,
  which generalises safe_divide to any function and any exception
  types.
- Explore what happens if you `return` inside both `try` and
  `finally`.
"""


def safe_divide(a: float, b: float, default: object = None) -> float | object:
    """Return a / b, or `default` if b is zero.

    Args:
        a: The dividend.
        b: The divisor.
        default: The value to return when dividing by zero.

    Returns:
        The float result of a / b, or `default` on ZeroDivisionError.

    Raises:
        TypeError: (propagated, not raised by you) if a or b are not
            numbers.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def divide_all(
    pairs: list[tuple[float, float]], default: object = None
) -> list[float | object]:
    """Divide each (a, b) pair, substituting `default` for zero divisors.

    Args:
        pairs: A list of (dividend, divisor) tuples. Not modified.
        default: The value to use for any pair whose divisor is zero.

    Returns:
        A new list of results in the same order as `pairs`.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
