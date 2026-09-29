"""
Challenge: Compose and Pipe
Level:     05 - Functions, Deeper
Topics:    returning functions, *args of functions, function composition
Source:    Functional-programming classic

========================================================================
PROBLEM
========================================================================
"Composing" functions means chaining them so the output of one becomes
the input of the next. In maths, (f o g)(x) means f(g(x)): apply g
FIRST, then f. That is, composition reads RIGHT-TO-LEFT.

Part 1 - `compose(*funcs)`

Take any number of one-argument functions and RETURN A NEW FUNCTION
(do not call anything yet!). When that new function is called with a
value x, it applies the functions right-to-left:

    compose(f, g, h)(x)  ==  f(g(h(x)))

- `compose()` with no functions returns the "identity" function: a
  function that returns its argument unchanged (identity(5) == 5).
- `compose(f)` returns a function that behaves like f.
- The returned function takes exactly ONE argument.

Part 2 - `pipe(value, *funcs)`

This one runs immediately and returns a value. It pushes `value`
through the functions LEFT-TO-RIGHT, like a pipeline or a Unix `|`:

    pipe(x, f, g, h)  ==  h(g(f(x)))

- `pipe(x)` with no functions returns x unchanged.

Note: compose and pipe apply the SAME functions in OPPOSITE orders:
    compose(f, g, h)(x) == pipe(x, h, g, f)

========================================================================
EXAMPLES
========================================================================
    >>> add_one = lambda x: x + 1
    >>> double = lambda x: x * 2

    >>> compose(add_one, double)(5)       # add_one(double(5))
    11

    >>> compose(double, add_one)(5)       # double(add_one(5))
    12

    >>> compose()("anything")
    'anything'

    >>> pipe(5, add_one, double)          # double(add_one(5))
    12

    >>> pipe("  Hi ", str.strip, str.lower, len)
    2

========================================================================
CONSTRAINTS
========================================================================
- Every function in `funcs` takes one argument and returns one value.
- `compose` must not call any of the funcs until the returned function
  is called (test this - see edge cases).
- The composed function can be called many times; each call is
  independent.
- Exceptions raised by any function propagate unchanged.

========================================================================
EDGE CASES TO TEST
========================================================================
- compose() is the identity; pipe(x) returns x
- A single function
- Order matters: compose(f, g) differs from compose(g, f)
- Functions that change the type (str -> int, e.g. `len`)
- compose calls nothing until invoked: pass a function that appends to
  a list, check the list is still empty after compose(...), then call
- The composed function can be reused with different inputs
- compose(f, g, h)(x) == pipe(x, h, g, f) for some sample functions

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Define a function INSIDE compose (an "inner function") and
   `return` it - without parentheses.
2. The inner function can see `funcs` from the outer function even
   after compose has returned. That's called a closure.
3. Right-to-left: loop over `reversed(funcs)` and update a running
   value: `result = f(result)`.
4. pipe is the same loop, forwards, but it runs straight away.
5. Stretch thought: `pipe(x, *fs) == compose(*reversed(fs))(x)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Nested (inner) functions and returning a function
- Closures (inner functions remembering outer variables)
- `*funcs` - *args can hold functions, not only numbers
- `reversed()`
- `Callable[[Any], Any]` type hints
- `functools.reduce` (stretch)

========================================================================
STRETCH GOALS
========================================================================
- Implement compose with `functools.reduce` in one expression.
- Allow the RIGHTMOST function in compose to take any arguments:
  compose(str, max)(3, 9, 4) == "9".
- Raise `TypeError` at compose-time if any argument is not callable
  (hint: `callable(obj)`).
"""

from collections.abc import Callable
from typing import Any


def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Return a function that applies funcs right-to-left.

    compose(f, g, h)(x) == f(g(h(x))). With no funcs, returns identity.

    Args:
        *funcs: One-argument functions to chain.

    Returns:
        A new one-argument function.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def pipe(value: Any, *funcs: Callable[[Any], Any]) -> Any:
    """Pass value through funcs left-to-right and return the result.

    pipe(x, f, g, h) == h(g(f(x))). With no funcs, returns value.

    Args:
        value: The starting value.
        *funcs: One-argument functions to apply in order.

    Returns:
        The final result.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
