"""
Challenge: Fibonacci Generator
Level:     05 - Functions, Deeper
Topics:    generators, yield, laziness, infinite sequences, iterators
Source:    Classic generator exercise

========================================================================
YOUR TASK
========================================================================
Write three functions:

- `fibonacci()`: a generator that yields the Fibonacci numbers
  0, 1, 1, 2, 3, 5, ... forever.
- `take(n, iterable)`: returns a list of the first `n` items of any
  iterable, even an endless one.
- `fibonacci_up_to(limit)`: a generator that yields the Fibonacci
  numbers up to `limit`, then stops.

    take(10, fibonacci())  ->  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

========================================================================
BACKGROUND: FIBONACCI, GENERATORS AND YIELD
========================================================================
The Fibonacci sequence starts with 0 and 1. Each next number is the
sum of the previous two (0 + 1 = 1, 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5,
and so on):

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

A "generator function" is a function that contains `yield`. It
behaves very differently from a normal function:

    def count_to_three():
        print("starting")
        yield 1
        yield 2
        yield 3

    gen = count_to_three()   # prints NOTHING: the body hasn't run yet
    next(gen)                # prints "starting", then gives 1
    next(gen)                # -> 2   (carries on from where it paused)
    next(gen)                # -> 3
    next(gen)                # raises StopIteration: the body finished

- Calling a generator function does NOT run its body. It returns a
  "generator object".
- Each `next(gen)` runs the body until the next `yield`, hands that
  value back, and PAUSES there. All the local variables are remembered
  until you ask again.
- When the body finishes (or hits `return`), the generator is done.
  `next()` then raises StopIteration, and a `for` loop simply stops.
- A `for` loop calls next() for you: `for x in count_to_three():`
  gives 1, 2, 3.

This is called "lazy" evaluation: values are made only when they are
asked for. So a generator can even be infinite (loop forever) without
using infinite memory, as long as you only ask for some of its values.

A generator is one kind of "iterator": an object that remembers its
position as you loop over it. Any item you pull out of an iterator is
gone. The next reader starts after it.

========================================================================
THE RULES
========================================================================
For `fibonacci`, your function must:
1. Be a generator function (use `yield`), not a function that builds
   and returns a list.
2. Yield 0, 1, 1, 2, 3, 5, ... forever. It never stops, so never call
   `list(fibonacci())`: it would never finish!

For `take`, your function must:
3. Return a list of the first `n` items of `iterable`, in order.
4. Return all the items if the iterable has fewer than `n`.
5. Return [] when `n` is 0.
6. Raise `ValueError` when `n` is negative.
7. Pull out no more than `n` items. This is what lets
   `take(5, fibonacci())` finish instantly, and it leaves the rest of
   an iterator untouched for the next reader.
8. Not use `itertools.islice` (that's the tool you're re-creating).
   Use `iter()` and `next()`, or a `for` loop with a counter.

For `fibonacci_up_to`, your function must:
9. Be a generator function (use `yield`).
10. Yield the Fibonacci numbers that are <= `limit`, in order, then
    stop. Include `limit` itself if it is a Fibonacci number.
11. Yield nothing if `limit` is negative.

Note: 1 appears twice in the sequence, so fibonacci_up_to(1) yields
0, 1, 1.

You can assume:
- `n` and `limit` are ints.
- `iterable` is any iterable (anything you can loop over): a list, a
  string, or even an infinite generator.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    take(10, fibonacci())       ->  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        Only 10 values are pulled from the endless generator.

    take(3, "hello")            ->  ['h', 'e', 'l']
        A string is iterable too. The result is a list.

    take(10, [1, 2])            ->  [1, 2]
        Only 2 items exist, so you get both.

    list(fibonacci_up_to(20))   ->  [0, 1, 1, 2, 3, 5, 8, 13]
        The next number, 21, is bigger than 20, so it stops.

You can also step through a generator by hand with next():

    gen = fibonacci()
    next(gen)    # -> 0
    next(gen)    # -> 1
    next(gen)    # -> 1
    next(gen)    # -> 2

========================================================================
EDGE CASES TO TEST
========================================================================
- The first few values of fibonacci() via next(): 0, 1, 1, 2
- The 50th Fibonacci number is correct (Python ints never overflow, so
  big numbers are fine): take(51, fibonacci())[-1] == 12586269025
- Two separate fibonacci() generators are independent: advancing one
  doesn't move the other
- take(0, [1, 2]) -> [], take(-1, [1, 2]) -> ValueError
- take on a short list: take(5, [1, 2]) -> [1, 2]. On an empty list:
  take(3, []) -> []
- take does not over-consume (pull out extra items): after
  `g = iter([1, 2, 3, 4])` (iter() turns the list into an iterator)
  and `take(2, g)`, `next(g)` should be 3
- fibonacci_up_to(0) -> [0], fibonacci_up_to(1) -> [0, 1, 1],
  fibonacci_up_to(-5) -> [] (wrap each call in list() to compare)
- inspect.isgeneratorfunction(fibonacci) is True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Keep two variables, `a, b = 0, 1`. Loop forever with `while True:`.
   Inside, `yield a`, then update with `a, b = b, a + b`.
2. `for` loops call `next()` for you and stop at the end
   automatically.
3. For take: loop over the iterable with a counter, and stop (`break`)
   as soon as you have n items. Check "do I have n yet?" right AFTER
   appending, not at the start of the next loop turn, which would pull
   one extra item first. For the same reason, check n == 0 BEFORE
   pulling anything at all.
4. For fibonacci_up_to: use the same loop as fibonacci, but stop when
   a > limit. Or, more cleverly: loop over `fibonacci()` and `return`
   when a number is too big.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `yield` and generator functions
- Generator objects, `next()`, and `StopIteration`
- Iterables vs iterators, and `iter()`
- Lazy evaluation and infinite sequences
- Tuple assignment `a, b = b, a + b`
- `itertools.islice` and `itertools.takewhile` (stretch)
- `Iterator[int]` / `Iterable[T]` type hints

========================================================================
STRETCH GOALS
========================================================================
- Re-implement fibonacci_up_to in one line with `itertools.takewhile`
  (which yields items for as long as a condition stays true).
- Write `evens(iterable)` as a generator EXPRESSION:
  (x for x in ... if ...). It looks like a list comprehension in round
  brackets, but it is lazy.
- Write a generator `chunked(iterable, size)` that yields lists of
  `size` items.
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
