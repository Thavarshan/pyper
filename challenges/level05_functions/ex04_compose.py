"""
Challenge: Compose and Pipe
Level:     05 - Functions, Deeper
Topics:    returning functions, *args of functions, function composition
Source:    Functional-programming classic

========================================================================
YOUR TASK
========================================================================
Write two functions that chain other functions together, so the
output of one becomes the input of the next:

- `compose(*funcs)` RETURNS A NEW FUNCTION that applies `funcs` from
  right to left.
- `pipe(value, *funcs)` pushes `value` through `funcs` from left to
  right and returns the result straight away.

    compose(len, str.strip)("  hi ")  ->  2     (strip first, then len)

========================================================================
BACKGROUND: COMPOSING FUNCTIONS
========================================================================
"Composing" functions means chaining them. In maths, (f o g)(x) means
f(g(x)): apply g FIRST, then f. So composition reads RIGHT TO LEFT:

    compose(f, g, h)(x)  ==  f(g(h(x)))     h runs first, f runs last

A pipeline reads LEFT TO RIGHT, like a Unix `|`:

    pipe(x, f, g, h)     ==  h(g(f(x)))     f runs first, h runs last

So compose and pipe apply the same functions in OPPOSITE orders:

    compose(f, g, h)(x)  ==  pipe(x, h, g, f)

The other big difference: `pipe` gives you a value right away.
`compose` gives you a FUNCTION, and nothing runs until you call that
function. A function can return a function, just as it can return a
number:

    def make_adder(n):
        def add(x):           # an "inner function", defined inside
            return x + n
        return add            # return the function itself: no ()

    add_ten = make_adder(10)  # nothing is added yet
    add_ten(5)                # -> 15

The inner function `add` still remembers `n` after make_adder has
returned. An inner function that remembers outer variables like this
is called a "closure".

========================================================================
THE RULES
========================================================================
For `compose`, your function must:
1. Return a NEW function. Do not call any of `funcs` inside compose
   itself. They run only when the returned function is called (test
   this: see the edge cases).
2. Make the returned function take exactly ONE argument x and apply
   the functions right to left: compose(f, g, h)(x) == f(g(h(x))).
3. With no functions, return the "identity" function: a function that
   returns its argument unchanged, so compose()(5) == 5.
4. With one function, return a function that behaves like that
   function.
5. Make the returned function reusable: it can be called many times,
   and each call is independent.

For `pipe`, your function must:
6. Run straight away and return a value: pipe(x, f, g, h) ==
   h(g(f(x))).
7. With no functions, return `value` unchanged: pipe(x) == x.

For both:
8. Let exceptions raised by any function propagate (pass through to
   the caller) unchanged.

You can assume:
- Every function in `funcs` takes one argument and returns one value.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return. The examples use
two small helper functions:

    add_one = lambda x: x + 1
    double = lambda x: x * 2

    compose(add_one, double)(5)    ->  11
        Right to left: double(5) is 10, then add_one(10) is 11.

    compose(double, add_one)(5)    ->  12
        add_one(5) is 6, then double(6) is 12. Order matters!

    compose()("anything")          ->  'anything'
        No functions, so you get the identity function.

    pipe(5, add_one, double)       ->  12
        Left to right: add_one(5) is 6, then double(6) is 12.

    pipe("  Hi ", str.strip, str.lower, len)  ->  2
        "  Hi " -> "Hi" -> "hi" -> 2. The last step changes the type
        from str to int.

========================================================================
EDGE CASES TO TEST
========================================================================
- compose() is the identity: compose()(5) -> 5. And pipe(7) -> 7
- A single function: compose(abs)(-3) -> 3, pipe(-3, abs) -> 3
- Order matters: compose(add_one, double)(5) -> 11, but
  compose(double, add_one)(5) -> 12
- Functions that change the type: compose(len, str.strip)("  hi ")
  -> 2
- compose calls nothing until invoked: pass a function that appends
  to a list. Check the list is still empty after compose(...), then
  call the result and check that the list has grown
- The composed function can be reused: call it with 1, then with 2,
  and check both answers
- compose(f, g, h)(x) == pipe(x, h, g, f) for some sample functions

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Define a function INSIDE compose (an "inner function") and `return`
   it without parentheses.
2. The inner function can see `funcs` from the outer function, even
   after compose has returned. That's a closure.
3. Right to left: loop over `reversed(funcs)` and update a running
   value: `result = f(result)`.
4. pipe is the same loop, forwards, but it runs straight away.
5. Stretch thought: `pipe(x, *fs) == compose(*reversed(fs))(x)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Nested (inner) functions and returning a function
- Closures (inner functions remembering outer variables)
- `*funcs`: *args can hold functions, not only numbers
- `reversed()`
- `Callable[[Any], Any]` type hints
- `functools.reduce` (stretch)

========================================================================
STRETCH GOALS
========================================================================
- Implement compose with `functools.reduce` (which combines a list of
  things into one, two at a time) in one expression.
- Allow the RIGHTMOST function in compose to take any arguments:
  compose(str, max)(3, 9, 4) == "9".
- Raise `TypeError` at compose time (when compose is called, not
  later) if any argument is not callable (hint: `callable(obj)`).
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
