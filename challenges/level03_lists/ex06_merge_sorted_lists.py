"""
Challenge: Merge Two Sorted Lists
Level:     03 - Lists
Topics:    two pointers, while loops, index arithmetic
Source:    Classic (the "merge" step of merge sort; cf. LeetCode #88 / #21)

========================================================================
PROBLEM
========================================================================
You are given two lists, `a` and `b`, that are each already SORTED in
ascending (smallest-to-largest) order. Write `merge_sorted(a, b)` that
returns ONE new list containing every element of both, also in ascending
order.

    merge_sorted([1, 4, 7], [2, 3, 8]) -> [1, 2, 3, 4, 7, 8]

You must NOT use sorted(), list.sort(), or heapq. The point is to take
advantage of the fact that both inputs are already sorted: you never
need to look backwards.

Duplicates are kept: merging [1, 2] and [2, 3] gives [1, 2, 2, 3].

========================================================================
EXAMPLES
========================================================================
    >>> merge_sorted([1, 4, 7], [2, 3, 8])
    [1, 2, 3, 4, 7, 8]

    >>> merge_sorted([1, 2, 2], [2, 5])
    [1, 2, 2, 2, 5]

    >>> merge_sorted([], [1, 2])
    [1, 2]

    >>> merge_sorted([5, 6], [1, 2])
    [1, 2, 5, 6]

========================================================================
CONSTRAINTS
========================================================================
- `a` and `b` are lists of numbers, each sorted ascending. You may
  assume they really are sorted (you don't need to check).
- Either or both may be empty.
- len(result) == len(a) + len(b).
- Return a new list; do not modify `a` or `b`.
- No sorted(), .sort(), or heapq.

========================================================================
EDGE CASES TO TEST
========================================================================
- Both empty -> []
- One empty -> a copy of the other (and a different object!)
- Interleaved values
- All of `a` smaller than all of `b` (and vice versa)
- Duplicates within a list and across both lists
- Negative numbers
- Lists of very different lengths
- Inputs unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Use two index variables, i for `a` and j for `b`, both starting at 0.
2. While BOTH lists still have elements left, compare a[i] and b[j],
   append the smaller one to the result, and advance only that index.
3. When one list runs out, everything left in the other list is already
   sorted and larger - append the rest in one go with extend() and a
   slice: result.extend(a[i:]).
4. Using `<=` when comparing keeps equal elements from `a` before those
   from `b` (this property is called "stable").

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The two-pointer technique
- `while` loops with compound conditions (and)
- `list.append()` vs `list.extend()`
- Why this is faster than joining the lists and sorting (you'll learn
  Big-O notation in later levels: this is O(n + m))

========================================================================
STRETCH GOALS
========================================================================
- Write `merge_k_sorted(lists: list[list[int]]) -> list[int]` for any
  number of lists.
- Use merge_sorted to implement merge sort: split a list in half,
  sort each half recursively, then merge.
- Compare your output with `heapq.merge` (in your tests only).
"""


def merge_sorted(a: list[float], b: list[float]) -> list[float]:
    """Merge two ascending lists into one ascending list.

    Args:
        a: A list sorted in ascending order. Not modified.
        b: A list sorted in ascending order. Not modified.

    Returns:
        A new ascending list containing all elements of `a` and `b`.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
