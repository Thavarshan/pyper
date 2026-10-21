"""
Challenge: Insertion Sort (in place)
Level:     09 - Searching and Sorting
Topics:    in-place algorithms, shifting elements, stability, returning None
Source:    Classic algorithm

========================================================================
YOUR TASK
========================================================================
Write `insertion_sort(items)`. It sorts the list you are given IN
PLACE (it rearranges that same list) into ascending order, and returns
None.

    data = [4, 2, 5, 1]
    insertion_sort(data)    # -> None
    data                    # -> [1, 2, 4, 5]

========================================================================
HOW INSERTION SORT WORKS
========================================================================
Insertion sort works the way many people sort a hand of playing cards.
Take the cards one at a time and slide each one left into its correct
place among the cards you have already sorted.

    [4, 2, 5, 1]
    take 2: shift 4 right, insert 2      -> [2, 4, 5, 1]
    take 5: already bigger than 4        -> [2, 4, 5, 1]
    take 1: shift 5, 4, 2 right, insert  -> [1, 2, 4, 5]

The left part of the list is always sorted. It grows by one item each
step.

========================================================================
WHAT "IN PLACE" MEANS
========================================================================
IN PLACE means you rearrange the items INSIDE the list you were given,
instead of building a new list. The caller sees their own list become
sorted.

Python's `list.sort()` works this way, and it also returns None.
`sorted()` is the other kind: it returns a new list. Returning None is
a deliberate signal that says "I changed the object you gave me".

Watch out: `items = sorted(items)` inside your function would NOT
change the caller's list. It only points your local name `items` at a
new list. Try it and see!

========================================================================
THE RULES
========================================================================
Your function must:
1. Sort `items` itself into ascending order. Do NOT create and return
   a new list.
2. Return None.
3. Be STABLE: items that compare equal stay in the same order they
   started in. To do that, move an item left only past items that are
   STRICTLY greater than it.
4. Not use sorted(), list.sort() or heapq in the solution. Use
   sorted() in your TESTS as the reference:
       expected = sorted(data)
       insertion_sort(data)
       assert data == expected

You can assume:
- `items` holds values that can all be compared with each other.
- len(items) is between 0 and 2000.

========================================================================
EXAMPLES
========================================================================
Each example shows the calls, then the values with `# ->`.

    data = [4, 2, 5, 1]
    insertion_sort(data)    # -> None (so nothing is printed)
    data                    # -> [1, 2, 4, 5]

    empty = []
    insertion_sort(empty)   # -> None
    empty                   # -> []

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2) worst and average case (reverse-sorted input): every
         new item may shift past all the sorted ones, a loop inside a
         loop.
         O(n) best case (already sorted input): each item is already
         in place, so one pass with no shifting.
- Space: O(1) extra: only a few variables. That's the point of in
         place.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: [] stays [], and the call returns None
- One item: [7] stays [7]
- The return value is None
- The SAME list object is sorted: keep a reference to the list you
  passed in and check that it is now sorted
- Already sorted: [1, 2, 3] stays [1, 2, 3]
- Reverse sorted: [3, 2, 1] becomes [1, 2, 3]
- All equal: [5, 5, 5] stays [5, 5, 5]
- Duplicates and negative numbers: [2, -1, 2, 0] becomes [-1, 0, 2, 2]
- STABILITY: sort a list of objects that compare only by one field,
  and check that equal ones keep their order. For example, define in
  your test a small class or dataclass whose `__lt__` compares only
  `.score`. Note that plain tuples like (1, "b") and
  (1, "a") compare ALL their parts, so they need a wrapper like this.
  Items with equal scores must stay in input order.
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
- In-place mutation (changing an object) vs returning a new object
- Why functions that mutate usually return None (list.sort,
  list.append)
- Names vs objects: reassigning a parameter doesn't affect the caller
- while loops with compound conditions (short-circuit `and`: the right
  side is only checked when the left side is True)
- Stability in sorting

========================================================================
STRETCH GOALS
========================================================================
- Add a `key` parameter (compare key(a) with key(b)).
- Use binary search (bisect-style, written yourself) to find the
  insertion point. Does that change the Big-O? (Hint: shifting still
  costs O(n).)
- Count the number of shifts. It equals the number of "inversions" in
  the input: pairs of positions i < j where items[i] > items[j].
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
