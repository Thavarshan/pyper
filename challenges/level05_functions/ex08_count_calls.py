"""
Challenge: Count Calls and Repeat (decorator factories)
Level:     05 - Functions, Deeper
Topics:    decorators, function attributes, decorators with arguments
Source:    Classic decorator exercise

========================================================================
PROBLEM
========================================================================
(If decorators are new to you, do ex07_memoize first - it explains them.)

Part 1 - `count_calls(func)`

A decorator that counts how many times the decorated function has been
called.
- The returned function has an attribute `.calls` (an int) that starts
  at 0 and goes up by 1 on EVERY call, before `func` runs - so it is
  counted even if `func` raises an exception.
- It must forward ALL arguments, positional and keyword, unchanged:
  use `*args, **kwargs`.
- It returns whatever `func` returns.
- It uses `functools.wraps`.
- Each decorated function has its own counter.

Part 2 - `repeat(times)`  -  a "decorator factory"

Sometimes you want to configure a decorator:

    @repeat(3)
    def say(msg): ...

Look closely: `repeat(3)` is CALLED first, and whatever it returns is
used as the decorator. So `repeat` is a function that RETURNS A
DECORATOR, which in turn returns a wrapper. Three levels of functions:

    def repeat(times):               # level 1: takes the configuration
        def decorator(func):         # level 2: takes the function
            def wrapper(*args, **kwargs):   # level 3: runs on each call
                ...
            return wrapper
        return decorator

`@repeat(3)` above `def say` is the same as `say = repeat(3)(say)`.

Behaviour of the wrapper produced by `repeat(times)`:
- Calls `func(*args, **kwargs)` exactly `times` times in a row.
- Returns a LIST of the results of every call, in order.
- `repeat(0)` is valid: func is never called and the result is [].
- If `times` is negative, raise `ValueError` IMMEDIATELY when
  `repeat(times)` is called (i.e. at decoration time, not later).
- If `times` is not an int (or is a bool), raise `TypeError`, also
  immediately.
- Uses `functools.wraps`.

========================================================================
EXAMPLES
========================================================================
    >>> @count_calls
    ... def add(a, b=0):
    ...     return a + b
    >>> add.calls
    0
    >>> add(1, b=2)
    3
    >>> add(5); add(6)
    5
    6
    >>> add.calls
    3

    >>> @repeat(3)
    ... def hello(name):
    ...     return f"hi {name}"
    >>> hello("ann")
    ['hi ann', 'hi ann', 'hi ann']

    >>> repeat(-1)
    Traceback (most recent call last):
    ...
    ValueError: times must be >= 0

========================================================================
CONSTRAINTS
========================================================================
- `.calls` is an int attribute on the returned function, starting at 0.
- Both wrappers forward *args and **kwargs unchanged.
- `repeat` validates `times` when called, before any decorating happens.
- Both use functools.wraps (so __name__ is preserved).

========================================================================
EDGE CASES TO TEST
========================================================================
- count_calls: .calls == 0 before any call
- count_calls: keyword arguments are forwarded correctly
- count_calls: two decorated functions keep separate counts
- count_calls: a call that raises still increments .calls
- repeat: returns a list with `times` results
- repeat: side effects happen `times` times (append to a list in the
  test function and check its length)
- repeat(0) -> [] and func never called
- repeat(-1) -> ValueError; repeat("3") / repeat(2.0) / repeat(True)
  -> TypeError, all without decorating anything
- Stacking: @count_calls on top of @repeat(2) - calls counts outer calls

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. count_calls: define wrapper, set `wrapper.calls = 0` before returning
   it, and inside wrapper do `wrapper.calls += 1`. (The attribute lives
   on the function object, so you don't need `nonlocal`.)
2. repeat: do the validation at the TOP of repeat, before defining
   `decorator`.
3. In repeat's wrapper, a list comprehension over `range(times)` can
   collect the results.
4. `@functools.wraps(func)` goes on the innermost `wrapper`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Function attributes as per-function state
- Forwarding arguments with *args / **kwargs
- Decorator factories (decorators that take arguments)
- Three levels of nested functions and closures
- When code runs: decoration time vs call time
- Stacking multiple decorators (applied bottom-up)

========================================================================
STRETCH GOALS
========================================================================
- Add a `.reset()` function attribute to count_calls.
- Write `retry(times, exceptions=(Exception,))`: call func again if it
  raises one of the given exceptions, up to `times` attempts.
- Write a decorator that works both as `@timer` and `@timer(unit="ms")`.
"""

from collections.abc import Callable
from typing import Any


def count_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that counts calls in a `.calls` attribute.

    Args:
        func: The function to wrap.

    Returns:
        A wrapper that forwards all arguments to func, returns its
        result, and increments `wrapper.calls` on every call.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def repeat(times: int) -> Callable[[Callable[..., Any]], Callable[..., list[Any]]]:
    """Decorator factory: call the decorated function `times` times.

    Args:
        times: How many times to call the function per invocation (>= 0).

    Returns:
        A decorator. Functions decorated with it return a list of the
        results of each of the `times` calls.

    Raises:
        TypeError: If `times` is not an int (bools are rejected too).
        ValueError: If `times` is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
