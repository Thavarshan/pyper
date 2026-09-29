"""
Challenge: Remove Duplicates (Keep Order)
Level:     03 - Lists
Topics:    sets, membership tests, building new lists, preserving order
Source:    Classic exercise (a common real-world task)

========================================================================
PROBLEM
========================================================================
Write `remove_duplicates(items)` that returns a NEW list containing each
distinct item only once, in the order in which each item FIRST appears.

    [3, 1, 3, 2, 1] -> [3, 1, 2]

"First occurrence order" means: walk through the list from left to
right; the first time you see a value, keep it; every later copy is
dropped.

The original list must NOT be changed.

Note: `list(set(items))` removes duplicates but does NOT keep the
original order (sets are unordered), so it is not a correct solution.

========================================================================
EXAMPLES
========================================================================
    >>> remove_duplicates([3, 1, 3, 2, 1])
    [3, 1, 2]

    >>> remove_duplicates(["b", "a", "b", "c"])
    ['b', 'a', 'c']

    >>> remove_duplicates([])
    []

========================================================================
CONSTRAINTS
========================================================================
- `items` is a list of HASHABLE values (ints, strs, tuples, ... - things
  that can go in a set). You don't need to support lists of lists.
- Two items are duplicates if they are equal with ==. Note that in
  Python 1 == 1.0 == True, so [1, 1.0, True] -> [1] (the first one wins).
  You don't need to test that, just be aware of it.
- Return a new list; the input list must be unchanged.
- Aim for a solution that stays fast for 100_000 items (see hint 3).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> []
- No duplicates -> same items, same order (but a different list object:
  `result is not items`)
- All the same value -> a one-item list
- Duplicates that are far apart
- Strings as items
- The input list is unchanged after the call
- Order is preserved (compare with a specific expected list, not a set)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Make an empty result list and loop over the items.
2. Only append an item if it is not already in the result.
3. `x in some_list` has to scan the whole list, which gets slow for big
   lists. `x in some_set` is (almost) instant. Keep a `seen` set
   alongside the result list.
4. Bonus trick: dicts remember insertion order, so
   list(dict.fromkeys(items)) is a famous one-liner. Try it AFTER
   writing the loop version.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Sets: `set()`, `.add()`, fast `in`
- Hashable vs unhashable objects
- Returning a new list vs mutating the input
- `is` (same object) vs `==` (equal value)
- Dicts preserve insertion order (Python 3.7+)

========================================================================
STRETCH GOALS
========================================================================
- Write `remove_duplicates_keep_last(items)` which keeps the LAST
  occurrence of each item instead of the first.
- Write `find_duplicates(items) -> list` returning the values that
  appear more than once, in first-occurrence order.
"""

from collections.abc import Hashable
from typing import TypeVar

T = TypeVar("T", bound=Hashable)


def remove_duplicates(items: list[T]) -> list[T]:
    """Return a new list with duplicates removed, keeping first occurrences.

    Args:
        items: A list of hashable values. It is not modified.

    Returns:
        A new list with each distinct value once, in first-seen order.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
