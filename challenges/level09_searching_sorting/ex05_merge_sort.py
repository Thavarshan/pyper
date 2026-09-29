"""
Challenge: Merge Sort
Level:     09 - Searching and Sorting
Topics:    divide and conquer, recursion, merging sorted lists, stability
Source:    Classic algorithm (John von Neumann, 1945)

========================================================================
PROBLEM
========================================================================
DIVIDE AND CONQUER is a strategy with three steps:

    1. DIVIDE   - split the problem into smaller sub-problems
    2. CONQUER  - solve each sub-problem (usually recursively)
    3. COMBINE  - join the sub-answers into the full answer

MERGE SORT applies it to sorting:

    1. Split the list into two halves.
    2. Merge-sort each half (recursively). A list of 0 or 1 items is
       already sorted - that's the base case.
    3. MERGE the two sorted halves into one sorted list.

    [5, 2, 4, 1]
    split  -> [5, 2]        [4, 1]
    split  -> [5] [2]       [4] [1]
    merge  -> [2, 5]        [1, 4]
    merge  -> [1, 2, 4, 5]

Merging two already-sorted lists is easy and fast: look at the front
item of each, take the smaller one, repeat. When one list runs out,
append whatever is left of the other.

Write two functions:

    merge(left, right)
        Both inputs are sorted ascending. Return a NEW sorted list with
        all items from both. When left and right have equal items, take
        from LEFT first - this is what makes merge sort STABLE.
        Do not modify the inputs.

    merge_sort(items)
        Return a NEW sorted list (ascending), built with the recursive
        algorithm above and your merge(). Do not modify `items`.

STABLE means equal items keep their original relative order.

========================================================================
EXAMPLES
========================================================================
    >>> merge([1, 4, 9], [2, 3, 10])
    [1, 2, 3, 4, 9, 10]

    >>> merge([], [1, 2])
    [1, 2]

    >>> merge_sort([5, 2, 4, 1, 3])
    [1, 2, 3, 4, 5]

    >>> merge_sort([])
    []

========================================================================
CONSTRAINTS
========================================================================
- Items are mutually comparable; length 0..10**5 (recursion depth is
  only ~log2(n), so that's safe).
- Return new lists; never modify inputs. merge_sort must return a new
  list object even for 0 or 1 items.
- Do NOT use sorted(), list.sort(), heapq or heapq.merge in the
  solution. Use sorted() in TESTS as the reference.
- Stable (see merge tie rule).

========================================================================
COMPLEXITY TARGET
========================================================================
- merge:      Time O(len(left) + len(right)), Space O(same).
- merge_sort: Time O(n log n) in EVERY case (best, average, worst) -
              there are log n levels of splitting and each level does
              O(n) merging work. Space O(n) extra.

========================================================================
EDGE CASES TO TEST
========================================================================
- merge with one or both inputs empty
- merge where all of left < all of right (and vice versa)
- merge with equal items (e.g. [1, 2] and [2, 3])
- merge_sort on empty, single item, two items
- Already sorted, reverse sorted, all equal, duplicates, negatives
- Input unchanged, result is a new object
- STABILITY: sort objects that compare only by a key (see the
  insertion sort challenge for ideas) and check equal ones keep order
- Random lists vs sorted() (fixed random seed)
- A large list (e.g. 50_000 random ints) runs quickly

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. merge: use two indices i and j starting at 0. While both have items
   left, append the smaller of left[i] / right[j] (use `<=` so ties
   come from left) and advance that index.
2. After the loop, `result.extend(left[i:])` and
   `result.extend(right[j:])` - one of them will be empty.
3. merge_sort base case: `if len(items) <= 1: return list(items)`
   (a copy, not `items` itself).
4. `mid = len(items) // 2`, then recurse on `items[:mid]` and
   `items[mid:]` and merge the results.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Divide and conquer
- Recursion on halves; recursion depth O(log n)
- Two-pointer technique
- Slicing creates copies
- Stability and why `<=` vs `<` matters
- Why O(n log n) beats O(n^2) (compare timings with bubble sort!)

========================================================================
STRETCH GOALS
========================================================================
- Write a bottom-up (iterative) merge sort with no recursion.
- Count INVERSIONS (pairs i < j with a[i] > a[j]) during the merge step
  in O(n log n).
- Use `timeit` to compare merge_sort with bubble_sort on 2_000 items.
- LeetCode #88 "Merge Sorted Array" and #21 "Merge Two Sorted Lists".
"""

from typing import Any


def merge(left: list[Any], right: list[Any]) -> list[Any]:
    """Merge two ascending lists into one new ascending list.

    On ties, items from `left` come first (stability).

    Args:
        left: A sorted list. Not modified.
        right: A sorted list. Not modified.

    Returns:
        A new sorted list containing every item of both inputs.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def merge_sort(items: list[Any]) -> list[Any]:
    """Return a new list with `items` sorted ascending, via merge sort.

    The sort is stable. The input list is not modified.

    Args:
        items: A list of mutually comparable values.

    Returns:
        A new, sorted list.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
