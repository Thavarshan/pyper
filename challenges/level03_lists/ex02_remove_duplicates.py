"""
Challenge: Remove Duplicates (Keep Order)
Level:     03 - Lists
Topics:    sets, membership tests, building new lists, preserving order
Source:    Classic exercise (a common real-world task)

========================================================================
YOUR TASK
========================================================================
Write `remove_duplicates(items)`. It returns a NEW list that holds each
value only once, in the order in which each value FIRST appears.

    remove_duplicates([3, 1, 3, 2, 1])  ->  [3, 1, 2]

========================================================================
WHAT "FIRST-OCCURRENCE ORDER" MEANS
========================================================================
Walk through the list from left to right. The first time you see a
value, keep it. Every later copy of that value is dropped:

    [3, 1, 3, 2, 1]
     3                  keep (the first 3)
        1               keep (the first 1)
           3            drop (already have a 3)
              2         keep (the first 2)
                 1      drop (already have a 1)

    result: [3, 1, 2]

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a NEW list, even when there are no duplicates. Do not change
   (mutate) `items`.
2. Keep only the first copy of each value, in first-occurrence order.
3. Treat two items as duplicates when they are equal with `==`.
4. Stay fast for a list of 100_000 items (see hint 3).

You can assume:
- `items` is a list of HASHABLE values: values that can go in a set,
  such as ints, strs and tuples. You don't need to support lists of
  lists.

Note: `list(set(items))` removes duplicates but does NOT keep the
original order (a set has no fixed order), so it is not a correct
solution.

Note: in Python, 1 == 1.0 == True. So [1, 1.0, True] -> [1] (the first
one wins). You don't need to test that, just be aware of it.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    remove_duplicates([3, 1, 3, 2, 1])       ->  [3, 1, 2]
        The second 3 and the second 1 are dropped.

    remove_duplicates(["b", "a", "b", "c"])  ->  ['b', 'a', 'c']
        Works with strings too. The second "b" is dropped.

    remove_duplicates([])                    ->  []
        Nothing to remove.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> []
- No duplicates: [1, 2, 3] -> [1, 2, 3], but a NEW list
  (check `result is not items`)
- All the same value: [7, 7, 7] -> [7]
- Duplicates that are far apart: [1, 2, 3, 4, 1] -> [1, 2, 3, 4]
- Strings as items: ["x", "y", "x"] -> ['x', 'y']
- The input list is unchanged after the call
- Order is kept: compare with an exact expected list, not a set
  ([3, 1, 2] == [1, 2, 3] is False, but {3, 1, 2} == {1, 2, 3} is True)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Make an empty result list and loop over the items.
2. Only append an item if it is not already in the result.
3. `x in some_list` has to scan the whole list, which gets slow for big
   lists. `x in some_set` is (almost) instant. Keep a `seen` set
   alongside the result list.
4. Bonus trick: dicts remember the order keys were added, so
   list(dict.fromkeys(items)) is a famous one-liner. Try it AFTER
   writing the loop version.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Sets: `set()`, `.add()`, fast `in`
- Hashable (can go in a set or be a dict key) vs unhashable objects
- Returning a new list vs mutating the input
- `is` (same object) vs `==` (equal value)
- Dicts keep insertion order (Python 3.7+)

========================================================================
STRETCH GOALS
========================================================================
- Write `remove_duplicates_keep_last(items)`, which keeps the LAST
  occurrence of each item instead of the first.
- Write `find_duplicates(items) -> list`, which returns the values that
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
