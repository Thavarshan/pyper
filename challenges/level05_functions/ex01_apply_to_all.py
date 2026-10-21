"""
Challenge: Apply To All
Level:     05 - Functions, Deeper
Topics:    functions as values, higher-order functions, lambda
Source:    Re-implementing the built-ins map() and filter()

========================================================================
YOUR TASK
========================================================================
Write two functions that each take ANOTHER FUNCTION as their first
argument:

- `apply_to_all(func, items)` calls `func` on every item and returns a
  new list of the results.
- `keep_if(predicate, items)` returns a new list of only the items
  that `predicate` says "yes" to.

    apply_to_all(str.upper, ["a", "b"])  ->  ['A', 'B']

========================================================================
BACKGROUND: FUNCTIONS ARE VALUES
========================================================================
In Python a function is a value, just like a number or a string. You
can store it in a variable, or pass it to another function, WITHOUT
calling it. You just leave off the parentheses:

    def shout(word):
        return word.upper()

    f = shout          # no (): f now refers to the same function
    f("hi")            # -> 'HI'

    shout              # the function itself, not called
    shout("hi")        # CALLS the function, giving 'HI'

A function that takes another function as an argument is called a
"higher-order function". Both functions you write here are
higher-order functions.

A "predicate" is a function that answers yes or no about one value,
like `str.isdigit` or `lambda n: n > 0`. (A `lambda` is a small,
nameless, one-line function. `lambda n: n > 0` does the same job as a
`def` whose body is `return n > 0`.)

`keep_if` keeps an item when `predicate(item)` is "truthy". Truthy
means Python treats the value as True in an `if`: non-zero numbers,
non-empty strings and lists, and True itself. So a predicate that
returns 1 or "yes" keeps the item. One that returns 0, "" or None
(these are "falsy") drops it.

========================================================================
THE RULES
========================================================================
Your functions must:
1. `apply_to_all`: return a NEW list holding `func(item)` for every
   item, in the same order as `items`. This is what the built-in
   `map()` does.
2. `keep_if`: return a NEW list holding only the items for which
   `predicate(item)` is truthy, in their original order. This is what
   the built-in `filter()` does.
3. Always return a list, whatever kind of iterable `items` is.
4. Not change (mutate) `items`, and loop over it only once.
5. Not use `map()` or `filter()`. Loops and comprehensions are fine.
6. Not catch exceptions raised by `func` or `predicate`. Let them
   propagate (pass through to the caller).

You can assume:
- `func` and `predicate` are callables (things you can call, like
  functions) that take one argument.
- `items` is any iterable (anything you can loop over with `for`): a
  list, tuple, string, range...

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    apply_to_all(str.upper, ["a", "b"])          ->  ['A', 'B']
        str.upper is called on "a", then on "b".

    apply_to_all(lambda x: x * x, range(4))      ->  [0, 1, 4, 9]
        range(4) gives 0, 1, 2, 3, and each one is squared.

    keep_if(lambda n: n % 2 == 0, [1, 2, 3, 4])  ->  [2, 4]
        Only the even numbers make the predicate return True.

    keep_if(str.isdigit, "a1b2")                 ->  ['1', '2']
        Looping over a string gives its characters. Only "1" and "2"
        are digits. The result is a list, not a string.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty input: apply_to_all(len, []) -> [] and keep_if(bool, []) -> []
- A built-in as `func`: apply_to_all(len, ["ab", "c"]) -> [2, 1]
  (try str and abs too)
- A lambda as `func`
- Your own named function, defined inside the test
- A tuple or range as `items`: apply_to_all(abs, (-1, 2)) -> [1, 2]
  (still a list)
- A predicate returning truthy non-bool values:
  keep_if(lambda s: s, ["a", "", "b"]) -> ['a', 'b']
- The original list is unchanged after the call
- An exception inside func propagates:
  apply_to_all(int, ["x"]) raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with an empty list. Loop over items and
   `append(func(item))`.
2. Inside your function, `func` is just a variable that holds a
   function. Call it with `func(item)`.
3. For keep_if: `if predicate(item): result.append(item)`.
4. Once it works, rewrite each one as a one-line list comprehension.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Functions are first-class objects (values like any other)
- Passing `len` vs calling `len(...)`
- lambda expressions: `lambda x: x + 1`
- Truthiness
- Type hints for functions: `Callable[[int], str]` means "takes an int,
  returns a str". `Iterable[T]` means "anything you can loop over".
- Generic type variables with `TypeVar`

========================================================================
STRETCH GOALS
========================================================================
- Write `reduce_all(func, items, initial)`, which folds a list into one
  value (combines the items one at a time into a single result), like
  `functools.reduce`. For example, sum with `lambda acc, x: acc + x`.
- Make lazy versions that `yield` each result when asked for it,
  instead of building a whole list.
- Write an `apply_to_all` that accepts several iterables, like
  `map(func, a, b)`.
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
