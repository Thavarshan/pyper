"""
Challenge: Insertion Sort (in place)
Level:     09 - Searching and Sorting
Topics:    in-place algorithms, shifting elements, stability, returning None
Source:    Classic algorithm

========================================================================
PROBLEM
========================================================================
INSERTION SORT works the way many people sort a hand of playing cards:
take the cards one at a time and slide each one left into its correct
place among the cards you've already sorted.

    [4, 2, 5, 1]
    take 2: shift 4 right, insert 2      -> [2, 4, 5, 1]
    take 5: already bigger than 4        -> [2, 4, 5, 1]
    take 1: shift 5, 4, 2 right, insert  -> [1, 2, 4, 5]

The left part of the list is always sorted; it grows by one item each
step.

Write `insertion_sort(items)` that sorts the given list IN PLACE and
returns None.

IN PLACE means you rearrange the elements INSIDE the list you were
given, instead of building a new list. The caller sees their own list
become sorted. This is how Python's `list.sort()` behaves - it also
returns None (whereas `sorted()` returns a new list). Returning None
is a deliberate signal that "the object was changed".

The sort must be STABLE: items that compare equal stay in the same
relative order they started in. (Test it with tuples/objects and a
`key`, or see the edge cases.)

========================================================================
EXAMPLES
========================================================================
    >>> data = [4, 2, 5, 1]
    >>> insertion_sort(data)      # returns None, so nothing is printed
    >>> data
    [1, 2, 4, 5]

    >>> empty = []
    >>> insertion_sort(empty) is None
    True

========================================================================
CONSTRAINTS
========================================================================
- `items` is a list of mutually comparable values, length 0..2000.
- Modify `items` itself; do NOT create and return a new list
  (`items = sorted(items)` inside the function would NOT change the
  caller's list - try it and see!).
- Return None.
- Do NOT use sorted(), list.sort() or heapq in the solution. Use
  sorted() in your TESTS as the reference:
      expected = sorted(data)
      insertion_sort(data)
      assert data == expected
- Stable: move an element left only past items STRICTLY greater
  than it.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2) worst/average case (reverse-sorted input);
         O(n) best case (already sorted input).
- Space: O(1) extra - that's the point of in-place.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty and single-element lists
- The return value is None
- The SAME list object is sorted (keep a reference, check `id()` or
  just check the variable you passed)
- Already sorted, reverse sorted, all-equal lists
- Duplicates and negative numbers
- STABILITY: sort a list of objects that compare only by one field and
  check equal ones keep their order. For example, define in your test
  a small class/dataclass with `__lt__` comparing only `.score`, or
  use a list like [(1, "b"), (1, "a")] with a wrapper - equal scores
  must stay in input order.
- Random lists compared against sorted()

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Loop `i` from 1 to len(items) - 1. Save `current = items[i]`.
2. Set `j = i - 1`. While `j >= 0` and `items[j] > current`, shift
   `items[j]` one place right (`items[j + 1] = items[j]`) and do
   `j -= 1`.
3. When the while loop stops, put `current` into `items[j + 1]`.
4. Using `>` (not `>=`) in step 2 is what makes the sort stable.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- In-place mutation vs returning a new object
- Why functions that mutate usually return None (list.sort, list.append)
- Names vs objects: reassigning a parameter doesn't affect the caller
- while loops with compound conditions (short-circuit `and`)
- Stability in sorting

========================================================================
STRETCH GOALS
========================================================================
- Add a `key` parameter (compare key(a) with key(b)).
- Use binary search (bisect-style, written yourself) to find the
  insertion point - does that change the Big-O? (Hint: shifting still
  costs O(n).)
- Count the number of shifts; it equals the number of "inversions"
  in the input.
"""

from typing import Any


def insertion_sort(items: list[Any]) -> None:
    """Sort `items` in place in ascending order using insertion sort.

    The sort is stable.

    Args:
        items: A list of mutually comparable values. Modified in place.

    Returns:
        None. The caller's list is rearranged instead.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
