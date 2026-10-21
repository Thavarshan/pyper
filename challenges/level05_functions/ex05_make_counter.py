"""
Challenge: Make Counter
Level:     05 - Functions, Deeper
Topics:    closures, nonlocal, functions that remember state
Source:    Classic closure exercise

========================================================================
YOUR TASK
========================================================================
Write two functions that each RETURN A NEW FUNCTION, one that
remembers a number between calls:

- `make_counter(start=0, step=1)` returns a no-argument function that
  gives start, start+step, start+2*step, ..., one value per call.
- `make_accumulator(initial=0)` returns a one-argument function that
  adds its argument to a running total and returns the new total.

    c = make_counter()
    c()    # -> 0
    c()    # -> 1
    c()    # -> 2

========================================================================
BACKGROUND: CLOSURES AND NONLOCAL
========================================================================
A "closure" is an inner function that remembers the variables of the
function it was created in, even after that outer function has
finished running:

    def make_greeter(name):
        def greet():
            return f"hi {name}"   # uses `name` from the outer function
        return greet

    g = make_greeter("ann")       # make_greeter has finished...
    g()                           # -> 'hi ann'  ...but greet remembers

Each call to the outer function creates a brand-new, separate set of
remembered variables. make_greeter("bob") makes a second function that
remembers "bob", and the two don't affect each other.

READING a remembered variable just works. CHANGING it (giving it a new
value) needs one extra line. Without it, this breaks:

    def make_toggle():
        on = False
        def toggle():
            on = not on       # UnboundLocalError when toggle() runs!
            return on
        return toggle

Because `toggle` assigns to `on`, Python decides that `on` is a
brand-new local variable of `toggle`. Then `not on` tries to read that
local before it has a value. The fix is to say "I mean the outer one"
with `nonlocal`:

        def toggle():
            nonlocal on       # use make_toggle's `on`
            on = not on
            return on

========================================================================
THE RULES
========================================================================
Your functions must:
1. Use a closure with `nonlocal`. Do NOT use a global variable or a
   class.
2. `make_counter`: return a function that takes NO arguments.
3. Make the counter's FIRST call return `start` itself. Each later call
   returns the previous value plus `step`.
4. Allow `step` to be negative (counting down) or zero (always
   returning `start`).
5. `make_accumulator`: return a function that takes exactly ONE
   number, adds it to the running total, and returns the NEW total.
   The total starts at `initial`.
6. Keep every counter and accumulator independent. Two made by
   separate calls must not affect each other.
7. Make both returned functions keep working after many calls.

You can assume:
- `start`, `step`, `initial` and the numbers passed to the accumulator
  are ints or floats. You don't need to check their types.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return (after `# ->`).

    c = make_counter(start=10, step=5)
    c()    # -> 10    the first call gives start
    c()    # -> 15
    c()    # -> 20

    down = make_counter(3, -1)
    [down() for _ in range(4)]    # -> [3, 2, 1, 0]   counts down

    a = make_counter()
    b = make_counter()
    a()    # -> 0
    a()    # -> 1
    b()    # -> 0     b has its own count, untouched by a

    acc = make_accumulator(10)
    acc(5)     # -> 15    10 + 5
    acc(-3)    # -> 12    15 - 3
    acc(0)     # -> 12

    acc2 = make_accumulator()
    acc2(10)   # -> 10    the total starts at 0
    acc2(5)    # -> 15

========================================================================
EDGE CASES TO TEST
========================================================================
- Default arguments: make_counter() gives 0, 1, 2, ...
- The first call returns exactly `start`: make_counter(7)() -> 7
- Negative step: make_counter(3, -1) gives 3, 2, 1, 0
- Zero step: make_counter(4, 0) gives 4, 4, 4, ...
- Two counters don't interfere with each other
- Float step: make_counter(0, 0.5) gives 0, 0.5, 1.0
- Accumulator with negative and float amounts:
  make_accumulator()(-1.5) -> -1.5
- The first accumulator call returns initial + amount:
  make_accumulator(10)(5) -> 15
- callable(make_counter()) is True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Inside make_counter, create a variable to hold the "next value to
   return". Then define an inner function and return it (without
   parentheses).
2. Inside the inner function, write `nonlocal <that variable>` as the
   first line.
3. Save the value you're about to return BEFORE adding step, so the
   first call gives `start`.
4. make_accumulator is the same pattern: `nonlocal total`, add,
   return.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Closures and the "enclosing scope" (the outer function's variables)
- The LEGB scope rule: Python looks a name up in the Local, then
  Enclosing, then Global, then Built-in scope
- `nonlocal` (and how it differs from `global`)
- UnboundLocalError and why it happens
- Default parameter values
- Inspecting a closure: `c.__closure__` (for curiosity)

========================================================================
STRETCH GOALS
========================================================================
- Give make_counter a reset ability: return TWO functions
  `(next_value, reset)` that share the same state.
- Rewrite make_counter as a class with `__call__` (the method that
  lets an object be called like a function), and compare.
- Rewrite make_counter using `itertools.count(start, step)` and
  `next()`.
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
