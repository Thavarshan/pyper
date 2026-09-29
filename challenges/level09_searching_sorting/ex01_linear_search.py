"""
Challenge: Linear Search
Level:     09 - Searching and Sorting
Topics:    loops, enumerate(), returning indices, Big-O notation
Source:    Classic algorithm

========================================================================
WHAT IS BIG-O NOTATION? (read this first)
========================================================================
Big-O describes how the running time (or memory) of an algorithm GROWS
as the input size `n` grows. It ignores constant factors and small
details and keeps only the dominant trend - "roughly how much slower
does it get if I double the input?"

    O(1)        constant      - same time no matter how big n is
                                (e.g. items[0], len(items), dict lookup)
    O(log n)    logarithmic   - each step halves the work; 1 million
                                items needs only ~20 steps (binary search)
    O(n)        linear        - look at each item once; double n, double
                                the time (this challenge!)
    O(n log n)  linearithmic  - good general sorting (merge sort)
    O(n^2)      quadratic     - a loop inside a loop over the data;
                                double n, FOUR times the time (bubble sort)

We usually describe the WORST case (the unluckiest input), sometimes
also the best and average case. "Space complexity" is the same idea for
extra memory used.

For linear search: best case O(1) (target is first), worst case O(n)
(target is last or missing).

========================================================================
PROBLEM
========================================================================
LINEAR SEARCH checks items one by one, from the start, until it finds
what it's looking for. It works on ANY list - sorted or not.

Part 1 - linear_search(items, target):
    Return the index of the FIRST occurrence of `target` in `items`,
    or -1 if it isn't there.

Part 2 - find_all(items, target):
    Return a list of EVERY index where `target` appears, in increasing
    order. Return [] if there are none.

"Equal" means `==`, so 1 == 1.0 counts as a match.

========================================================================
EXAMPLES
========================================================================
    >>> linear_search([4, 2, 7, 2], 2)
    1

    >>> linear_search([4, 2, 7], 9)
    -1

    >>> find_all([4, 2, 7, 2], 2)
    [1, 3]

    >>> find_all(["a", "b"], "z")
    []

========================================================================
CONSTRAINTS
========================================================================
- `items` is a list of any values that support `==`; it may be empty
  and may be unsorted.
- Do NOT use `items.index()`, the `x in items` membership test, or `items.count()` - write the loop
  yourself.
- Do not modify `items`.

========================================================================
COMPLEXITY TARGET
========================================================================
- linear_search: Time O(n) worst case, O(1) best case. Space O(1).
- find_all:      Time O(n) always (must check every item).
                 Space O(k) for the k indices returned.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> -1 and []
- Target at index 0 and at the last index
- Target missing -> -1
- Duplicates: linear_search returns the FIRST index; find_all returns
  all of them in increasing order
- Works with strings and mixed types (e.g. [1, "1", None], target None)
- 1 == 1.0 is a match: linear_search([1.0], 1) == 0
- The input list is unchanged

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `for i, value in enumerate(items):` gives you both the index and
   the value.
2. `return i` as soon as you find a match - that's the O(1) best case.
3. Only `return -1` AFTER the loop finishes.
4. find_all: collect indices in a list (or use a list comprehension
   with `if`).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- enumerate()
- Early return from inside a loop
- Sentinel values like -1 for "not found"
- Big-O notation: best vs worst case
- Type hints with `Any`

========================================================================
STRETCH GOALS
========================================================================
- Add a `key` parameter: linear_search(people, "Bob", key=lambda p: p.name).
- Write `find_last(items, target)` that scans from the end.
- Time linear_search on lists of 1_000, 10_000 and 100_000 items with
  `timeit` and check the time grows roughly linearly.
"""

from typing import Any


def linear_search(items: list[Any], target: Any) -> int:
    """Return the index of the first item equal to `target`, or -1.

    Args:
        items: The list to search (any order). Not modified.
        target: The value to look for.

    Returns:
        The smallest index i with items[i] == target, or -1 if none.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def find_all(items: list[Any], target: Any) -> list[int]:
    """Return every index where `target` appears, in increasing order.

    Args:
        items: The list to search (any order). Not modified.
        target: The value to look for.

    Returns:
        A list of indices (possibly empty), smallest first.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
