"""
Challenge: Bubble Sort
Level:     09 - Searching and Sorting
Topics:    nested loops, swapping, copying lists, O(n^2) algorithms
Source:    Classic algorithm

========================================================================
PROBLEM
========================================================================
BUBBLE SORT sorts a list by repeatedly walking through it and swapping
any two NEIGHBOURS that are in the wrong order. After the first full
pass, the largest value has "bubbled up" to the end. After the second
pass the second-largest is in place, and so on.

    [5, 1, 4, 2]
    pass 1: 5>1 swap -> [1,5,4,2]; 5>4 swap -> [1,4,5,2];
            5>2 swap -> [1,4,2,5]           (5 is now in place)
    pass 2: 1<4 ok; 4>2 swap -> [1,2,4,5]   (4 is now in place)
    pass 3: 1<2 ok                           done: [1, 2, 4, 5]

Write `bubble_sort(items)` that returns a NEW list containing the same
values in ascending order. The original list must NOT be changed.

Swapping two list positions in Python:  a[i], a[i+1] = a[i+1], a[i]

========================================================================
EXAMPLES
========================================================================
    >>> bubble_sort([5, 1, 4, 2])
    [1, 2, 4, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort(["pear", "apple", "fig"])
    ['apple', 'fig', 'pear']

    >>> data = [3, 1, 2]
    >>> result = bubble_sort(data)
    >>> data            # unchanged
    [3, 1, 2]

========================================================================
CONSTRAINTS
========================================================================
- `items` is a list of mutually comparable values (all numbers, or all
  strings, etc.), length 0..2000. May contain duplicates.
- Return a NEW list; never modify the input (even when it's already
  sorted, return a different list object).
- Do NOT use sorted(), list.sort(), or heapq in your solution. You
  SHOULD use sorted() in your TESTS as the trusted reference answer:
      assert bubble_sort(data) == sorted(data)
- Only swap when left > right (strictly greater); this keeps the sort
  STABLE (equal items keep their original relative order).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2) worst/average case. With the early-exit stretch goal,
  O(n) best case on already-sorted input.
- Space: O(n) for the copy (the sorting itself uses O(1) extra).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list and single-element list
- Already sorted and reverse sorted input
- Duplicates, e.g. [3, 1, 3, 1]
- Negative numbers and floats
- Strings
- Input list is unchanged and the result is a different object
  (`result is not data`)
- Random lists: compare with sorted() for many random inputs (use the
  `random` module with a fixed seed so the test is repeatable)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with `result = list(items)` (or `items[:]`) and sort `result`.
2. Outer loop: n - 1 passes. Inner loop: compare result[j] and
   result[j + 1] for j from 0 up to the unsorted boundary.
3. After pass i, the last i items are already in place, so the inner
   loop can stop at `n - 1 - i`.
4. Be careful with range bounds: `result[j + 1]` must never go past the
   end of the list.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Nested loops and their O(n^2) cost
- Tuple-unpacking swap: a, b = b, a
- Shallow copies: list(x), x[:], x.copy()
- Stability in sorting
- Property-style testing with random inputs vs a reference

========================================================================
STRETCH GOALS
========================================================================
- EARLY EXIT: track whether a pass made any swaps; if none, the list is
  sorted - stop. Test that a sorted input finishes after one pass (e.g.
  by counting comparisons with a small wrapper).
- Add `reverse: bool = False` to sort in descending order.
- Add a `key` function parameter like sorted() has.
"""

from typing import Any


def bubble_sort(items: list[Any]) -> list[Any]:
    """Return a new list with the items in ascending order (bubble sort).

    The sort is stable. The input list is not modified.

    Args:
        items: A list of mutually comparable values.

    Returns:
        A new, sorted list.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
