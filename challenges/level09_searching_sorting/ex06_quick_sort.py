"""
Challenge: Quick Sort
Level:     09 - Searching and Sorting
Topics:    divide and conquer, pivots, partitioning, worst-case analysis
Source:    Classic algorithm (Tony Hoare, 1959)

========================================================================
PROBLEM
========================================================================
QUICK SORT is another divide-and-conquer sort:

    1. Pick one item as the PIVOT.
    2. PARTITION the rest into three groups:
           less    - items smaller than the pivot
           equal   - items equal to the pivot
           greater - items larger than the pivot
    3. Recursively quick-sort `less` and `greater`, then join:
           quick_sort(less) + equal + quick_sort(greater)
    Base case: a list with 0 or 1 items is already sorted.

    [3, 6, 1, 8, 3, 2]  pivot = 3
    less = [1, 2]   equal = [3, 3]   greater = [6, 8]
    -> [1, 2] + [3, 3] + [6, 8] = [1, 2, 3, 3, 6, 8]

Write `quick_sort(items)` that returns a NEW list sorted ascending,
without modifying the input. (This "three lists" version is the
easiest to understand; the classic in-place version is a stretch goal.)

PIVOT CHOICE AND THE WORST CASE:
    Quick sort is fast when the pivot splits the list roughly in HALF
    each time: O(n log n). But if the pivot is always the smallest or
    largest item, one side is empty and the other has n-1 items - that
    gives n levels of recursion and O(n^2) time.
    That's exactly what happens if you always pick the FIRST item and
    the input is already sorted!
    Common fixes:
        - pick the MIDDLE item:  items[len(items) // 2]
        - pick a RANDOM item:    random.choice(items)
        - "median of three": the median of first, middle and last
    Use the middle item or a random one in your solution. Grouping all
    items EQUAL to the pivot together also avoids O(n^2) on lists with
    many duplicates (like [7] * 10_000).

========================================================================
EXAMPLES
========================================================================
    >>> quick_sort([3, 6, 1, 8, 3, 2])
    [1, 2, 3, 3, 6, 8]

    >>> quick_sort([])
    []

    >>> quick_sort(["b", "c", "a"])
    ['a', 'b', 'c']

========================================================================
CONSTRAINTS
========================================================================
- Items are mutually comparable; length 0..10**5.
- Return a NEW list; never modify the input (return a new object even
  for 0 or 1 items).
- Do NOT use sorted(), list.sort() or heapq in the solution. Use
  sorted() in TESTS as the reference.
- Must not hit RecursionError on already-sorted input of 10_000 items
  or on 10_000 equal items (so choose the pivot wisely and group equal
  items).
- Stability is NOT required (quick sort is generally not stable).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n log n) average; O(n^2) worst case with unlucky pivots.
- Space: this version uses O(n) extra for the new lists; recursion
  depth is O(log n) on average.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty and single-item lists
- Two items in either order
- Already sorted and reverse-sorted input of 10_000 items (should not
  raise RecursionError)
- All equal items, e.g. [5] * 10_000
- Many duplicates, negatives, floats
- Strings
- Input unchanged; result is a new object
- Random lists vs sorted() (fixed random seed)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Base case: `if len(items) <= 1: return list(items)`.
2. `pivot = items[len(items) // 2]`.
3. Build the three groups with list comprehensions:
   `less = [x for x in items if x < pivot]` and similarly for == and >.
4. Return `quick_sort(less) + equal + quick_sort(greater)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Divide and conquer with uneven splits
- Best / average / worst case analysis
- List comprehensions with conditions
- Why input order can make an algorithm slow
- `random.choice` and seeding for reproducible tests

========================================================================
STRETCH GOALS
========================================================================
- Implement IN-PLACE quick sort with the Lomuto or Hoare partition
  scheme: quick_sort_inplace(items, low=0, high=None) -> None.
- Implement "median of three" pivot selection.
- Quickselect: find the k-th smallest item in O(n) average time
  (LeetCode #215 "Kth Largest Element in an Array").
- Time first-element pivot vs middle pivot on sorted input of 900 items.
"""

from typing import Any


def quick_sort(items: list[Any]) -> list[Any]:
    """Return a new list with `items` sorted ascending, via quick sort.

    Not required to be stable. The input list is not modified.

    Args:
        items: A list of mutually comparable values.

    Returns:
        A new, sorted list.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
