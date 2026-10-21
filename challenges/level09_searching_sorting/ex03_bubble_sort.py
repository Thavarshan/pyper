"""
Challenge: Bubble Sort
Level:     09 - Searching and Sorting
Topics:    nested loops, swapping, copying lists, O(n^2) algorithms
Source:    Classic algorithm

========================================================================
YOUR TASK
========================================================================
Write `bubble_sort(items)`. It RETURNS a NEW list with the same values
in ascending (smallest first) order, using the bubble sort algorithm.
The original list stays as it was.

    bubble_sort([5, 1, 4, 2])  ->  [1, 2, 4, 5]

========================================================================
HOW BUBBLE SORT WORKS
========================================================================
Bubble sort walks through the list again and again. On each walk (a
"pass") it compares every pair of NEIGHBOURS and swaps them if they
are in the wrong order. After the first pass, the largest value has
"bubbled up" to the end. After the second pass, the second-largest is
in place, and so on.

    [5, 1, 4, 2]
    pass 1: 5>1 swap -> [1, 5, 4, 2]
            5>4 swap -> [1, 4, 5, 2]
            5>2 swap -> [1, 4, 2, 5]     (5 is now in place)
    pass 2: 1<4 ok
            4>2 swap -> [1, 2, 4, 5]     (4 is now in place)
    pass 3: 1<2 ok                       done: [1, 2, 4, 5]

Swapping two list positions in Python:  a[i], a[i+1] = a[i+1], a[i]

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a NEW list with the values in ascending order.
2. Never change (mutate) the input. Even when the input is already
   sorted, return a different list object.
3. Swap only when left > right (strictly greater). This keeps the sort
   STABLE: items that compare equal keep their original order.
4. Not use sorted(), list.sort() or heapq in the solution. You SHOULD
   use sorted() in your TESTS as the trusted reference answer:
       assert bubble_sort(data) == sorted(data)

You can assume:
- `items` holds values that can all be compared with each other (all
  numbers, or all strings, and so on).
- `items` may contain duplicates.
- len(items) is between 0 and 2000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    bubble_sort([5, 1, 4, 2])              ->  [1, 2, 4, 5]
        See the walk-through above.

    bubble_sort([])                        ->  []
        Nothing to sort, but still a new list.

    bubble_sort(["pear", "apple", "fig"])  ->  ['apple', 'fig', 'pear']
        Strings sort alphabetically.

The input is not changed:

    data = [3, 1, 2]
    result = bubble_sort(data)
    data      # -> [3, 1, 2]   (unchanged)
    result    # -> [1, 2, 3]

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2) worst and average case: a loop inside a loop, so
  doubling the list makes it about four times slower. With the
  early-exit stretch goal, the best case is O(n) on already-sorted
  input: one pass with no swaps, then stop.
- Space: O(n) for the copy. The sorting itself uses only O(1) extra
  (a few variables).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: bubble_sort([]) -> []
- One item: bubble_sort([7]) -> [7]
- Already sorted: bubble_sort([1, 2, 3]) -> [1, 2, 3]
- Reverse sorted: bubble_sort([3, 2, 1]) -> [1, 2, 3]
- Duplicates: bubble_sort([3, 1, 3, 1]) -> [1, 1, 3, 3]
- Negative numbers and floats: bubble_sort([2.5, -1, 0]) -> [-1, 0, 2.5]
- Strings, as in the examples
- The input list is unchanged, and the result is a different object
  (`result is not data`)
- Random lists: compare with sorted() for many random inputs. Use the
  `random` module with a fixed seed (random.seed(0)) so the test gives
  the same lists every run.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with `result = list(items)` (or `items[:]`) and sort
   `result`.
2. Outer loop: n - 1 passes. Inner loop: compare result[j] and
   result[j + 1] for j from 0 up to the unsorted boundary.
3. With `for i in range(n - 1):`, the last i items are already in
   place when pass i starts. So the inner loop can be
   `for j in range(n - 1 - i):`.
4. Be careful with range bounds: `result[j + 1]` must never go past
   the end of the list.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Nested loops and their O(n^2) cost
- Tuple-unpacking swap: a, b = b, a
- Shallow copies: list(x), x[:], x.copy()
- Stability in sorting
- Property-style testing: check a rule against a trusted reference
  for many random inputs

========================================================================
STRETCH GOALS
========================================================================
- EARLY EXIT: track whether a pass made any swaps. If none did, the
  list is sorted, so stop. Test that a sorted input finishes after one
  pass (for example, by counting comparisons with a small wrapper).
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
