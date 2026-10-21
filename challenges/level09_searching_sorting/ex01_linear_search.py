"""
Challenge: Linear Search
Level:     09 - Searching and Sorting
Topics:    loops, enumerate(), returning indices, Big-O notation
Source:    Classic algorithm

========================================================================
YOUR TASK
========================================================================
Write two functions that look for `target` in a list by checking the
items one by one, from the start:

    linear_search(items, target)  gives back the index of the FIRST
                                  match, or -1 if there is none.
    find_all(items, target)       gives back a list of EVERY index
                                  where `target` appears.

    linear_search([4, 2, 7, 2], 2)  ->  1

========================================================================
WHAT IS BIG-O NOTATION? (read this first)
========================================================================
Big-O describes how the running time (or memory) of an algorithm GROWS
as the input size `n` grows. It ignores small details and keeps only
the main trend: "roughly how much slower does it get if I double the
input?"

    O(1)        constant      same time no matter how big n is
                              (items[0], len(items), a dict lookup)
    O(log n)    logarithmic   each step halves the work, so 1 million
                              items needs only about 20 steps
                              (binary search)
    O(n)        linear        look at each item once: double n, double
                              the time (this challenge!)
    O(n log n)  linearithmic  good general sorting (merge sort)
    O(n^2)      quadratic     a loop inside a loop over the data:
                              double n, FOUR times the time
                              (bubble sort)

We usually describe the WORST case (the unluckiest input), and
sometimes also the best and average case. "Space complexity" is the
same idea for the extra memory used.

For linear search, the best case is O(1) (the target is the first
item). The worst case is O(n) (the target is last, or missing).

Linear search works on ANY list, sorted or not.

========================================================================
THE RULES
========================================================================
Your functions must:
1. linear_search: return the index of the FIRST item equal to
   `target`, or -1 if no item is equal to it.
2. find_all: return a list of every index where `target` appears, in
   increasing order. Return [] if there are none.
3. Treat "equal" as `==`. So 1 == 1.0 counts as a match.
4. Not change (mutate) `items`.
5. Write the loop yourself. Do NOT use `items.index()`, the
   `x in items` membership test, or `items.count()`.

You can assume:
- `items` is a list of any values that support `==`.
- `items` may be empty and may be unsorted.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    linear_search([4, 2, 7, 2], 2)  ->  1
        2 is at index 1 and index 3. The FIRST one wins.

    linear_search([4, 2, 7], 9)     ->  -1
        9 is not in the list.

    find_all([4, 2, 7, 2], 2)       ->  [1, 3]
        Every index where 2 appears, smallest first.

    find_all(["a", "b"], "z")       ->  []
        No matches, so an empty list.

========================================================================
COMPLEXITY TARGET
========================================================================
linear_search:
- Time O(n) worst case: one pass, checking each item once.
- Time O(1) best case: the first item matches, so you stop at once.
- Space O(1): only a few variables, no new list.

find_all:
- Time O(n) always: it must check every item, even after a match.
- Space O(k) for the k indices returned: the result list grows by
  one for each match.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: linear_search([], 1) -> -1 and find_all([], 1) -> []
- Target at index 0: linear_search([5, 6, 7], 5) -> 0
- Target at the last index: linear_search([5, 6, 7], 7) -> 2
- Target missing -> -1 (and [] from find_all)
- Duplicates: linear_search([4, 2, 7, 2], 2) -> 1 (the FIRST),
  find_all([4, 2, 7, 2], 2) -> [1, 3] (all, increasing)
- Strings and mixed types: linear_search([1, "1", None], None) -> 2
  and find_all([1, "1", None], None) -> [2]
- 1 == 1.0 is a match: linear_search([1.0], 1) -> 0
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `for i, value in enumerate(items):` gives you both the index and
   the value.
2. `return i` as soon as you find a match. That early stop is the O(1)
   best case.
3. Only `return -1` AFTER the loop finishes.
4. find_all: collect the indices in a list (or use a list
   comprehension with `if`).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- enumerate()
- Early return from inside a loop
- Sentinel values (special stand-in values) like -1 for "not found"
- Big-O notation: best vs worst case
- Type hints with `Any`

========================================================================
STRETCH GOALS
========================================================================
- Add a `key` parameter, a function that picks what to compare:
  linear_search(people, "Bob", key=lambda p: p.name).
- Write `find_last(items, target)` that scans from the end.
- Time linear_search on lists of 1_000, 10_000 and 100_000 items with
  `timeit` and check the time grows roughly linearly (10 times the
  items, about 10 times the time).
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
