"""
Challenge: Safe Divide
Level:     06 - Errors and Parsing
Topics:    try / except / else / finally, default values, recovering from errors
Source:    Classic exception-handling exercise

========================================================================
TRY / EXCEPT / ELSE / FINALLY IN ONE PICTURE
========================================================================
    try:
        risky()                 # code that might raise an exception
    except ZeroDivisionError:
        handle_it()             # runs ONLY if that exception was raised
    else:
        on_success()            # runs ONLY if NO exception was raised
    finally:
        clean_up()              # ALWAYS runs, error or not

- Catch the most SPECIFIC exception you can. A bare `except:` or
  `except Exception:` hides real bugs (like typos) - avoid it.
- An exception you don't catch keeps travelling up to the caller
  ("propagates").
- `else` keeps the try block small: only the risky line goes in `try`.
- `finally` is for cleanup like closing files (you'll mostly use `with`
  for that instead).

========================================================================
PROBLEM
========================================================================
Part 1 - `safe_divide(a, b, default=None)`

Return `a / b` (true division, so the result is a float). If `b` is
zero, Python raises `ZeroDivisionError`; catch it and return `default`
instead.
- ONLY ZeroDivisionError is handled. Any other error - for example
  `safe_divide("6", 2)` which raises TypeError - must propagate to the
  caller unchanged.
- `default` can be any value (None, 0, float("inf"), "n/a"...).

Part 2 - `divide_all(pairs, default=None)`

Given a list of (a, b) tuples, return a list with `safe_divide(a, b,
default)` for each pair, in the same order. A zero divisor in one pair
must not stop the others from being computed.

========================================================================
EXAMPLES
========================================================================
    >>> safe_divide(10, 4)
    2.5

    >>> safe_divide(1, 0) is None
    True

    >>> safe_divide(1, 0, default=0)
    0

    >>> divide_all([(10, 2), (3, 0), (9, 3)], default=-1)
    [5.0, -1, 3.0]

========================================================================
CONSTRAINTS
========================================================================
- a and b are numbers (int or float) for normal use.
- Use `/` (true division), not `//`.
- Use try/except - do NOT check `if b == 0` first. (The point is to
  practise exceptions. Note that 0.0 also raises ZeroDivisionError.)
- Only catch ZeroDivisionError.
- divide_all returns a new list and does not modify `pairs`.

========================================================================
EDGE CASES TO TEST
========================================================================
- Normal division, including negative numbers
- Integer inputs give a float: safe_divide(6, 3) == 2.0
- Divisor 0 and 0.0 -> default
- Custom default values (0, "n/a", float("inf"))
- 0 divided by something -> 0.0
- Wrong types propagate: `pytest.raises(TypeError)` for safe_divide("6", 2)
- divide_all([]) -> []
- divide_all with several zero divisors in the middle

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Put `return a / b` inside `try:`, and `return default` inside
   `except ZeroDivisionError:`.
2. For divide_all, reuse safe_divide in a loop or comprehension -
   unpack each pair with `for a, b in pairs`.
3. To see that other errors propagate, just DON'T catch them.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- try / except / else / finally and when each block runs
- Catching specific exceptions vs catching everything
- Exception propagation
- Default parameter values (and why `None` is the usual "no value")
- Tuple unpacking in for loops
- `pytest.raises` as a context manager

========================================================================
STRETCH GOALS
========================================================================
- Add a `log` list parameter: append a message in `except`, and
  "done" in `finally`, then write tests proving the order of execution.
- `safe_call(func, *args, default=None, catch=(Exception,))` that
  generalises safe_divide to any function and exception types.
- Explore what happens if you `return` inside both `try` and `finally`.
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
