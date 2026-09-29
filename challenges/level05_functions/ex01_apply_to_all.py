"""
Challenge: Apply To All
Level:     05 - Functions, Deeper
Topics:    functions as values, higher-order functions, lambda
Source:    Re-implementing the built-ins map() and filter()

========================================================================
PROBLEM
========================================================================
In Python a function is a value, just like a number or a string. You
can store it in a variable and pass it to another function WITHOUT
calling it (no parentheses):

    def shout(word):
        return word.upper()

    f = shout          # f now refers to the same function
    f("hi")            # -> "HI"

A function that takes another function as an argument is called a
"higher-order function". You will write two of them.

Part 1 - `apply_to_all(func, items)`

Call `func` on every item and return a NEW list of the results, in the
same order. This is what the built-in `map()` does - but you must NOT
use `map()`.

Part 2 - `keep_if(predicate, items)`

A "predicate" is a function that returns True or False. Return a NEW
list containing only the items for which `predicate(item)` is truthy,
in their original order. This is what `filter()` does - but you must
NOT use `filter()`.

"Truthy" means Python treats the value as True in an `if`: non-zero
numbers, non-empty strings/lists, True itself. So a predicate returning
1 or "yes" keeps the item; one returning 0, "" or None drops it.

Both functions accept any iterable (list, tuple, string, range...),
always return a list, and never modify the input.

========================================================================
EXAMPLES
========================================================================
    >>> apply_to_all(str.upper, ["a", "b"])
    ['A', 'B']

    >>> apply_to_all(lambda x: x * x, range(4))
    [0, 1, 4, 9]

    >>> keep_if(lambda n: n % 2 == 0, [1, 2, 3, 4])
    [2, 4]

    >>> keep_if(str.isdigit, "a1b2")
    ['1', '2']

========================================================================
CONSTRAINTS
========================================================================
- `func` / `predicate` are callables that take one argument.
- `items` is any iterable. It is consumed once and not modified.
- Do NOT use `map()` or `filter()`. (Loops or comprehensions are fine.)
- If `func` raises an exception, let it propagate (don't catch it).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty input                    -> []
- Passing a built-in (len, str, abs) as `func`
- Passing a lambda
- Passing your own named function (defined inside the test)
- A tuple or range as `items`    -> result is still a list
- Predicate returning truthy non-bool values (e.g. `lambda s: s` keeps
  non-empty strings)
- The original list is unchanged
- An exception inside func propagates: `apply_to_all(int, ["x"])`
  raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with an empty list, loop over items, `append(func(item))`.
2. Inside your function, `func` is just a variable - call it with
   `func(item)`.
3. For keep_if: `if predicate(item): result.append(item)`.
4. Once it works, rewrite each as a one-line list comprehension.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Functions are first-class objects
- Passing `len` vs calling `len(...)`
- lambda expressions: `lambda x: x + 1`
- Truthiness
- Type hints for functions: `Callable[[int], str]` means "takes an int,
  returns a str"; `Iterable[T]` means "anything you can loop over"
- Generic type variables with `TypeVar`

========================================================================
STRETCH GOALS
========================================================================
- `reduce_all(func, items, initial)` that folds a list into one value
  (like `functools.reduce`), e.g. summing with `lambda acc, x: acc + x`.
- Make lazy versions that `yield` results instead of building a list.
- `apply_to_all` that accepts several iterables, like `map(func, a, b)`.
"""

from collections.abc import Callable, Iterable
from typing import Any, TypeVar

T = TypeVar("T")
R = TypeVar("R")


def apply_to_all(func: Callable[[T], R], items: Iterable[T]) -> list[R]:
    """Return a list of func(item) for every item, in order (no map()).

    Args:
        func: A one-argument function to call on each item.
        items: Any iterable. Not modified.

    Returns:
        A new list of results, same length and order as `items`.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def keep_if(predicate: Callable[[T], Any], items: Iterable[T]) -> list[T]:
    """Return the items for which predicate(item) is truthy (no filter()).

    Args:
        predicate: A one-argument function; its result is tested for truth.
        items: Any iterable. Not modified.

    Returns:
        A new list of the kept items, in their original order.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
