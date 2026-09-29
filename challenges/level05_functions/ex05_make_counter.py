"""
Challenge: Make Counter
Level:     05 - Functions, Deeper
Topics:    closures, nonlocal, functions that remember state
Source:    Classic closure exercise

========================================================================
PROBLEM
========================================================================
A "closure" is an inner function that remembers variables from the
function it was created in, even after that outer function has
finished running. Each call to the outer function creates a brand-new,
separate set of remembered variables.

To CHANGE (reassign) a remembered variable from inside the inner
function you must declare it with `nonlocal name`. Without it, Python
thinks `count = count + 1` creates a new local variable and raises
`UnboundLocalError`.

Part 1 - `make_counter(start=0, step=1)`

Return a function that takes NO arguments. Each time it is called it
returns the next number in the sequence start, start+step,
start+2*step, ...

    c = make_counter()
    c()  -> 0
    c()  -> 1
    c()  -> 2

- The FIRST call returns `start` itself.
- `step` may be negative (counting down) or zero (always `start`).
- Two counters made by separate calls to make_counter are completely
  independent.

Part 2 - `make_accumulator(initial=0)`

Return a function that takes ONE number, adds it to a running total,
and returns the NEW total.

    acc = make_accumulator(10)
    acc(5)   -> 15
    acc(-3)  -> 12
    acc(0)   -> 12

- Accumulators are independent of each other, like counters.
- Numbers may be int or float (no need to validate types).

========================================================================
EXAMPLES
========================================================================
    >>> c = make_counter(start=10, step=5)
    >>> c(), c(), c()
    (10, 15, 20)

    >>> down = make_counter(3, -1)
    >>> [down() for _ in range(4)]
    [3, 2, 1, 0]

    >>> a = make_counter()
    >>> b = make_counter()
    >>> a(), a(), b()
    (0, 1, 0)

    >>> acc = make_accumulator()
    >>> acc(10), acc(5)
    (10, 15)

========================================================================
CONSTRAINTS
========================================================================
- Use a closure with `nonlocal` - NOT a global variable and NOT a class.
- make_counter's returned function takes no arguments.
- make_accumulator's returned function takes exactly one number.
- Both returned functions must keep working after many calls.

========================================================================
EDGE CASES TO TEST
========================================================================
- Default arguments: make_counter() starts at 0 and steps by 1
- First call returns exactly `start`
- Negative step (count down) and step=0 (always start)
- Two counters don't interfere with each other
- Float step: make_counter(0, 0.5) -> 0, 0.5, 1.0
- Accumulator with negative and float amounts
- Accumulator with no calls yet: first call returns initial + amount
- callable(make_counter()) is True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Inside make_counter, create a variable to hold the "next value to
   return", then define an inner function and return it (no brackets).
2. Inside the inner function, write `nonlocal <that variable>` as the
   first line.
3. Remember the value you're about to return BEFORE adding step, so the
   first call gives `start`.
4. make_accumulator is the same pattern: `nonlocal total`, add, return.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Closures and "enclosing scope"
- The LEGB scope rule: Local, Enclosing, Global, Built-in
- `nonlocal` (and how it differs from `global`)
- UnboundLocalError and why it happens
- Default parameter values
- Inspecting a closure: `c.__closure__` (for curiosity)

========================================================================
STRETCH GOALS
========================================================================
- Give make_counter's function a `reset()` ability: return TWO functions
  `(next_value, reset)` that share the same state.
- Rewrite make_counter as a class with `__call__` and compare.
- Rewrite make_counter using `itertools.count(start, step)` and `next()`.
"""

from collections.abc import Callable


def make_counter(start: int | float = 0, step: int | float = 1) -> Callable[[], int | float]:
    """Return a no-argument function producing start, start+step, ...

    Args:
        start: The value returned by the first call.
        step: How much to add for each subsequent call.

    Returns:
        A function that returns the next value each time it's called.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def make_accumulator(initial: int | float = 0) -> Callable[[int | float], int | float]:
    """Return a function that adds its argument to a running total.

    Args:
        initial: The starting total.

    Returns:
        A one-argument function that adds the amount to the total and
        returns the new total.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
