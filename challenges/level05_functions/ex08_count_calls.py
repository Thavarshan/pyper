"""
Challenge: Count Calls and Repeat (decorator factories)
Level:     05 - Functions, Deeper
Topics:    decorators, function attributes, decorators with arguments
Source:    Classic decorator exercise

========================================================================
YOUR TASK
========================================================================
Write two decorators:

- `count_calls(func)` counts how many times the decorated function has
  been called, in a `.calls` attribute.
- `repeat(times)` is a "decorator factory": `@repeat(3)` makes the
  decorated function run 3 times per call and return a list of the 3
  results.

    @repeat(3)
    def hello(name):
        return f"hi {name}"

    hello("ann")    # -> ['hi ann', 'hi ann', 'hi ann']

(If decorators are new to you, do ex07_memoize first. It explains
them.)

========================================================================
BACKGROUND: DECORATOR FACTORIES
========================================================================
Sometimes you want to configure a decorator, to give it a setting:

    @repeat(3)
    def say(msg): ...

Look closely: `repeat(3)` has parentheses, so it is CALLED first.
Whatever it returns is then used as the decorator. So `repeat` is a
function that RETURNS A DECORATOR, and that decorator returns a
wrapper. That makes three levels of functions:

    def repeat(times):                     # level 1: takes the setting
        def decorator(func):               # level 2: takes the function
            def wrapper(*args, **kwargs):  # level 3: runs on each call
                ...
            return wrapper
        return decorator

`@repeat(3)` above `def say` is the same as `say = repeat(3)(say)`.
Step by step:

    decorator = repeat(3)   # level 1 runs once   ("decoration time")
    say = decorator(say)    # level 2 runs once and returns wrapper
    say("hi")               # level 3, wrapper, runs on EVERY call
                            #                     ("call time")

The difference between decoration time and call time matters below:
`repeat` checks `times` at decoration time, before any call happens.

========================================================================
THE RULES
========================================================================
For `count_calls`, the function it returns must:
1. Have an int attribute `.calls` that starts at 0.
2. Add 1 to `.calls` on EVERY call, BEFORE `func` runs. So a call is
   counted even if `func` raises an exception.
3. Forward (pass on) ALL arguments, positional and keyword, unchanged:
   use `*args, **kwargs`.
4. Return whatever `func` returns.
5. Keep a separate counter for each decorated function.
6. Use `functools.wraps` (so `__name__` is preserved).

For `repeat(times)`:
7. Raise `TypeError` straight away, when `repeat(times)` itself is
   called, if `times` is not an int. A bool counts as "not an int"
   here, even though Python treats True as 1.
8. Raise `ValueError` straight away, when `repeat(times)` itself is
   called, if `times` is negative. Both checks happen at decoration
   time, not later when the decorated function is called.
9. The wrapper it produces calls `func(*args, **kwargs)` exactly
   `times` times in a row, forwarding all arguments unchanged.
10. The wrapper returns a LIST of the results of every call, in order.
11. `repeat(0)` is valid: the wrapper never calls func and returns [].
12. The wrapper uses `functools.wraps`.

You can assume:
- `func` is a function, and it may take any arguments.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return (after `# ->`).

    @count_calls
    def add(a, b=0):
        return a + b

    add.calls       # -> 0     nothing called yet
    add(1, b=2)     # -> 3     the keyword argument is forwarded
    add(5)          # -> 5
    add(6)          # -> 6
    add.calls       # -> 3

    @repeat(3)
    def hello(name):
        return f"hi {name}"

    hello("ann")    # -> ['hi ann', 'hi ann', 'hi ann']

    repeat(-1)      # raises ValueError: times must be >= 0
                    # (the check runs before anything is decorated)

========================================================================
EDGE CASES TO TEST
========================================================================
- count_calls: .calls == 0 before any call
- count_calls: keyword arguments are forwarded: add(1, b=2) -> 3
- count_calls: two decorated functions keep separate counts
- count_calls: a call that raises still increments .calls (0 -> 1)
- repeat: returns a list with `times` results: @repeat(2) gives a
  2-item list
- repeat: side effects happen `times` times (append to a list in the
  test function, then check the list's length)
- repeat(0): the wrapper returns [] and func is never called
- repeat(-1) -> ValueError. repeat("3"), repeat(2.0) and repeat(True)
  -> TypeError. All of these fail without decorating anything
- Stacking: @count_calls on top of @repeat(2). Stacked decorators are
  applied bottom-up, so count_calls wraps the repeat wrapper. One call
  returns a 2-item list, but .calls is 1 (only outer calls count)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. count_calls: define wrapper. Set `wrapper.calls = 0` before
   returning it, and inside wrapper do `wrapper.calls += 1`. The
   attribute lives on the function object, so you don't need
   `nonlocal`. (`nonlocal` is only needed to give a remembered
   variable a NEW value. Changing an attribute of it is fine without.)
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
- Stacking multiple decorators (applied bottom-up: the one nearest
  `def` wraps the function first)

========================================================================
STRETCH GOALS
========================================================================
- Add a `.reset()` function attribute to count_calls that sets .calls
  back to 0.
- Write `retry(times, exceptions=(Exception,))`: call func again if it
  raises one of the given exceptions, up to `times` attempts.
- Write a decorator that works both as `@timer` and as
  `@timer(unit="ms")`, with or without a setting.
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
