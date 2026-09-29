"""
Challenge: Memoize (your first decorator)
Level:     05 - Functions, Deeper
Topics:    decorators, closures, dict caching, functools.wraps
Source:    Classic decorator exercise (compare functools.lru_cache)

========================================================================
WHAT IS A DECORATOR?
========================================================================
A decorator is simply a function that TAKES a function and RETURNS a
(usually new) function. That's it. Here is the whole idea in plain code:

    def shout(func):                 # takes a function...
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)   # ...calls the original...
            return result.upper()            # ...and adds behaviour
        return wrapper               # returns the new function

    def greet(name):
        return f"hello {name}"

    greet = shout(greet)             # replace greet with the wrapped one
    greet("bob")                     # -> "HELLO BOB"

Writing `greet = shout(greet)` is so common that Python has special
syntax for it. These two are EXACTLY equivalent:

    @shout                           def greet(name): ...
    def greet(name): ...             greet = shout(greet)

`wrapper` is a closure: it remembers `func` from the outer function.
Anything else created in the outer function (like a cache dict) is also
remembered, and shared by every call to the decorated function.

One annoying side effect: after decorating, `greet.__name__` is
"wrapper" and its docstring is gone. `functools.wraps` fixes that:

    import functools
    def shout(func):
        @functools.wraps(func)       # copy name, docstring, etc.
        def wrapper(*args, **kwargs): ...
        return wrapper

Functions are objects, so you can also attach attributes to them:
`wrapper.cache = {}` makes `decorated_func.cache` available to callers.

========================================================================
PROBLEM
========================================================================
"Memoization" means remembering the result of a function call so that
calling it again with the same arguments returns the saved result
instead of recomputing it. It only makes sense for "pure" functions
(same input always gives the same output, no side effects).

Write a decorator `memoize(func)` that returns a wrapped version of
`func` which:

1. Accepts POSITIONAL arguments only (no keyword arguments needed).
2. Uses the tuple of positional arguments `args` as the key into a
   dict. If the key is already in the cache, return the cached value
   WITHOUT calling `func`. Otherwise call `func(*args)`, store the result
   under that key, and return it.
3. Exposes the cache dict as an attribute called `cache` on the
   returned function, so `decorated.cache` is that dict, e.g.
   after `square(3)` then `square.cache == {(3,): 9}`.
4. Uses `functools.wraps` so `__name__` and `__doc__` match the
   original function.
5. Each decorated function has its OWN separate cache.

If `func` raises an exception, nothing is cached and the exception
propagates. Arguments must be hashable (a list argument will cause
Python to raise `TypeError` - that's fine, you don't need to handle it).

========================================================================
EXAMPLES
========================================================================
    >>> @memoize
    ... def square(x):
    ...     "Return x squared."
    ...     return x * x

    >>> square(4)
    16
    >>> square.cache
    {(4,): 16}
    >>> square.__name__, square.__doc__
    ('square', 'Return x squared.')

    >>> @memoize
    ... def slow_fib(n):
    ...     return n if n < 2 else slow_fib(n - 1) + slow_fib(n - 2)
    >>> slow_fib(80)          # instant thanks to the cache
    23416728348467685

========================================================================
CONSTRAINTS
========================================================================
- Only positional arguments; the cache key is exactly the `args` tuple.
- `.cache` must be a plain dict mapping args tuple -> result.
- Do NOT use functools.lru_cache or functools.cache (that's the stretch
  comparison).
- The wrapped function is called at most ONCE per distinct args tuple.

========================================================================
EDGE CASES TO TEST
========================================================================
- The result is correct on first and repeated calls
- The original function runs only once per distinct input (count calls
  with a list or a nonlocal counter inside the test's function)
- Different arguments are cached separately
- Multi-argument functions: key is e.g. (2, 3)
- Zero-argument functions: key is ()
- Two memoized functions don't share a cache
- __name__ and __doc__ are preserved
- If the function raises, the exception propagates and nothing is cached

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Skeleton: `def memoize(func):` -> create `cache = {}` -> define
   `def wrapper(*args):` -> return wrapper.
2. In wrapper: `if args in cache: return cache[args]`.
3. Otherwise compute, store `cache[args] = result`, return result.
4. Before returning wrapper, attach the dict: `wrapper.cache = cache`.
5. Put `@functools.wraps(func)` on the line above `def wrapper`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Decorators and the @ syntax
- Closures holding state (the cache) across calls
- Function attributes
- `functools.wraps` and function metadata (__name__, __doc__)
- Hashable tuples as dict keys
- Recursion + memoization = dynamic programming

========================================================================
STRETCH GOALS
========================================================================
- Support keyword arguments: build a key from args plus
  `tuple(sorted(kwargs.items()))`.
- Add a `cache_clear()` function attribute that empties the cache.
- Time slow_fib(32) with and without @memoize, and compare with
  `@functools.lru_cache(maxsize=None)`.
"""

from collections.abc import Callable
from typing import Any


def memoize(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that caches func's results by positional arguments.

    The returned function has a `.cache` attribute: a dict mapping each
    args tuple to its result. Uses functools.wraps to keep func's name
    and docstring.

    Args:
        func: The function to memoize. Should be pure and take hashable
            positional arguments.

    Returns:
        The wrapped (memoized) function.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
