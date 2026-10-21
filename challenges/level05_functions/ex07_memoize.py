"""
Challenge: Memoize (your first decorator)
Level:     05 - Functions, Deeper
Topics:    decorators, closures, dict caching, functools.wraps
Source:    Classic decorator exercise (compare functools.lru_cache)

========================================================================
YOUR TASK
========================================================================
Write a decorator `memoize(func)`. It returns a new version of `func`
that remembers (caches) the result for each set of arguments. When it
is called again with the same arguments, it returns the saved result
instead of running `func` again.

    @memoize
    def square(x):
        return x * x

    square(4)       # -> 16   runs square and saves the result
    square(4)       # -> 16   comes from the cache: square doesn't run
    square.cache    # -> {(4,): 16}

========================================================================
BACKGROUND: WHAT IS A DECORATOR?
========================================================================
A decorator is a function that TAKES a function and RETURNS a new
function, usually one that adds some behaviour around the original.
That's all. Here is the whole idea in plain code:

    def shout(func):                        # 1. takes a function
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)  # 2. calls the original
            return result.upper()           # 3. adds extra behaviour
        return wrapper                      # 4. returns the new one

    def greet(name):
        return f"hello {name}"

    greet = shout(greet)    # replace greet with the wrapped version
    greet("bob")            # -> 'HELLO BOB'

`*args, **kwargs` in wrapper collect whatever arguments the caller
passes, and `func(*args, **kwargs)` passes them all on, unchanged.

Writing `greet = shout(greet)` is so common that Python has a shortcut
for it: the `@` syntax. These two are EXACTLY the same:

    @shout
    def greet(name): ...

    def greet(name): ...
    greet = shout(greet)

`wrapper` is a closure: an inner function that remembers the variables
of the function it was created in. It remembers `func`. It also
remembers anything else created inside `shout`, such as a cache dict.
That dict is created ONCE, when the decorator is applied, and is then
shared by every call to the decorated function.

There's one annoying side effect. After decorating, `greet.__name__`
is "wrapper" and greet's docstring is gone, because `greet` now IS
wrapper. `functools.wraps` fixes that by copying the name, docstring
and so on from the original:

    import functools

    def shout(func):
        @functools.wraps(func)       # copy name, docstring, etc.
        def wrapper(*args, **kwargs): ...
        return wrapper

Functions are objects, so you can also attach your own attributes to
them: after `wrapper.cache = {}`, callers can read
`decorated_func.cache`.

========================================================================
WHAT "MEMOIZE" MEANS
========================================================================
"Memoization" means remembering the result of a function call. Call
the function again with the same arguments, and you get the saved
result instead of a fresh calculation. This only makes sense for
"pure" functions: the same input always gives the same output, and
calling them has no side effects (they don't print, change lists, and
so on).

The cache is a dict. Its keys are tuples of arguments, and its values
are the results:

    square(3)    cache becomes {(3,): 9}
    square(4)    cache becomes {(3,): 9, (4,): 16}
    square(3)    (3,) is already in the cache: return 9, don't run

A tuple can be a dict key because it is "hashable" (can be used as a
dict key). A list is not.

========================================================================
THE RULES
========================================================================
Your decorator must return a function that:
1. Accepts POSITIONAL arguments only. No keyword arguments are needed.
2. Uses the tuple of positional arguments, `args`, as the cache key,
   exactly as it is.
3. Returns the cached value WITHOUT calling `func` when `args` is
   already in the cache.
4. Otherwise calls `func(*args)`, stores the result under `args`, and
   returns it. So `func` runs at most ONCE for each distinct args
   tuple.
5. Has an attribute called `cache`: a plain dict mapping each args
   tuple to its result. After `square(3)`, `square.cache` is
   {(3,): 9}.
6. Has its OWN separate cache. Two decorated functions never share
   one.
7. Uses `functools.wraps`, so `__name__` and `__doc__` match the
   original function.
8. Caches nothing when `func` raises an exception, and lets the
   exception propagate (pass through to the caller).

Also: do NOT use `functools.lru_cache` or `functools.cache` (comparing
with them is a stretch goal).

You can assume:
- The decorated function is pure.
- Its arguments are hashable. A list argument makes Python raise
  `TypeError` when it is used as a dict key. That's fine: you don't
  need to handle it.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return (after `# ->`).

    @memoize
    def square(x):
        "Return x squared."
        return x * x

    square(4)          # -> 16
    square.cache       # -> {(4,): 16}
    square.__name__    # -> 'square'              thanks to wraps
    square.__doc__     # -> 'Return x squared.'

    @memoize
    def slow_fib(n):
        return n if n < 2 else slow_fib(n - 1) + slow_fib(n - 2)

    slow_fib(80)       # -> 23416728348467685

slow_fib(80) is instant thanks to the cache. The recursive calls go
through the cache too, because the name `slow_fib` now refers to the
wrapper. Without @memoize it would effectively never finish.

========================================================================
EDGE CASES TO TEST
========================================================================
- The result is correct on the first call and on repeated calls
- The original function runs only once per distinct input. Count its
  runs with a list or a nonlocal counter inside the test's function:
  calling square(3) twice -> it ran once
- Different arguments are cached separately: after square(3) and
  square(4), the cache has 2 entries
- Multi-argument functions: the key is the whole tuple, e.g. (2, 3)
- Zero-argument functions: the key is ()
- Two memoized functions don't share a cache
- __name__ and __doc__ are preserved
- If the function raises, the exception propagates and nothing is
  cached (the cache stays {})

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Skeleton: `def memoize(func):` -> create `cache = {}` -> define
   `def wrapper(*args):` -> return wrapper.
2. In wrapper: `if args in cache: return cache[args]`.
3. Otherwise compute the result, store it with
   `cache[args] = result`, and return it.
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
- Recursion + memoization = dynamic programming (solving a big
  problem by reusing the saved answers to smaller ones)

========================================================================
STRETCH GOALS
========================================================================
- Support keyword arguments: build a key from args plus
  `tuple(sorted(kwargs.items()))`.
- Add a `cache_clear()` function attribute that empties the cache.
- Time slow_fib(32) with and without @memoize, and compare with
  `@functools.lru_cache(maxsize=None)` (the standard library's
  ready-made version).
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
