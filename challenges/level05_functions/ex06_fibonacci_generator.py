"""
Challenge: Fibonacci Generator
Level:     05 - Functions, Deeper
Topics:    generators, yield, laziness, infinite sequences, iterators
Source:    Classic generator exercise

========================================================================
PROBLEM
========================================================================
The Fibonacci sequence starts 0, 1 and each next number is the sum of
the previous two:

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

A "generator function" is a function that contains `yield` instead of
(or as well as) `return`. Calling it does NOT run its body; instead it
returns a generator object. Each time you ask that object for a value
(with `next(gen)` or a `for` loop), the body runs until the next
`yield`, hands that value back, and PAUSES there - remembering all its
local variables - until you ask again. This is called "lazy"
evaluation: values are produced only when needed, so a generator can
even be infinite without using infinite memory.

Part 1 - `fibonacci()`

An INFINITE generator yielding 0, 1, 1, 2, 3, 5, ... forever. (Never
call `list(fibonacci())` - it would never finish!)

Part 2 - `take(n, iterable)`

Return a list of the first `n` items from ANY iterable (a list, a
string, or an infinite generator). If the iterable has fewer than `n`
items, return all of them. It must only pull the items it needs, so
`take(5, fibonacci())` finishes instantly.
- Do NOT use `itertools.islice` here (that's what you're re-creating);
  use `iter()` and `next()` or a `for` loop with a counter.
- If `n` is negative, raise `ValueError`. `n == 0` returns [].

Part 3 - `fibonacci_up_to(limit)`

A FINITE generator yielding the Fibonacci numbers that are <= `limit`,
then stopping. When a generator function simply finishes (or hits
`return`), iteration stops.
- If `limit` is negative, yield nothing.
- Note: 1 appears twice in the sequence, so fibonacci_up_to(1) yields
  0, 1, 1.

========================================================================
EXAMPLES
========================================================================
    >>> gen = fibonacci()
    >>> next(gen), next(gen), next(gen), next(gen)
    (0, 1, 1, 2)

    >>> take(10, fibonacci())
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    >>> take(3, "hello")
    ['h', 'e', 'l']

    >>> take(10, [1, 2])
    [1, 2]

    >>> list(fibonacci_up_to(20))
    [0, 1, 1, 2, 3, 5, 8, 13]

========================================================================
CONSTRAINTS
========================================================================
- `fibonacci` and `fibonacci_up_to` must be generator functions (use
  `yield`), not functions that build and return a list.
- `take` returns a list and must not consume more than n items.
- `take` raises `ValueError` for negative n.
- `fibonacci_up_to` includes `limit` itself if it is a Fibonacci number.

========================================================================
EDGE CASES TO TEST
========================================================================
- The first few values of fibonacci() via next()
- The 50th Fibonacci number is correct (Python ints never overflow):
  take(51, fibonacci())[-1] == 12586269025
- Two separate fibonacci() generators are independent
- take(0, ...) -> [], take(-1, ...) -> ValueError
- take on a short list / empty list
- take does not over-consume: after `g = iter([1, 2, 3, 4])` and
  `take(2, g)`, `next(g)` should be 3
- fibonacci_up_to(0) -> [0], fibonacci_up_to(1) -> [0, 1, 1],
  fibonacci_up_to(-5) -> []
- inspect.isgeneratorfunction(fibonacci) is True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Keep two variables `a, b = 0, 1`. Loop forever with `while True:`,
   `yield a`, then update with `a, b = b, a + b`.
2. `for` loops call `next()` for you and stop at the end automatically.
3. For take: loop over the iterable with a counter and stop
   (`break`) when you have n items - but check n == 0 BEFORE pulling
   anything, or you'll consume one item too many.
4. For fibonacci_up_to: same loop as fibonacci, but stop when a > limit.
   Or cleverly: loop over `fibonacci()` and `return` when too big.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `yield` and generator functions
- Generator objects, `next()`, and `StopIteration`
- Iterables vs iterators; `iter()`
- Lazy evaluation and infinite sequences
- Tuple assignment `a, b = b, a + b`
- `itertools.islice` and `itertools.takewhile` (stretch)
- `Iterator[int]` / `Iterable[T]` type hints

========================================================================
STRETCH GOALS
========================================================================
- Re-implement fibonacci_up_to in one line with `itertools.takewhile`.
- Write `evens(iterable)` as a generator EXPRESSION: (x for x in ... if ...).
- Write a generator `chunked(iterable, size)` yielding lists of `size`.
- Compare memory: `sys.getsizeof` of a list of a million numbers vs a
  generator.
"""

from collections.abc import Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def fibonacci() -> Iterator[int]:
    """Yield the Fibonacci numbers 0, 1, 1, 2, 3, 5, ... forever.

    Yields:
        The next Fibonacci number.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def take(n: int, iterable: Iterable[T]) -> list[T]:
    """Return the first n items of iterable as a list.

    Args:
        n: How many items to take. Must be >= 0.
        iterable: Any iterable, possibly infinite.

    Returns:
        A list of at most n items. Consumes no more than n items.

    Raises:
        ValueError: If n is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def fibonacci_up_to(limit: int) -> Iterator[int]:
    """Yield Fibonacci numbers that are <= limit, then stop.

    Args:
        limit: The largest value allowed. Negative -> yields nothing.

    Yields:
        Fibonacci numbers in order, each <= limit.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
