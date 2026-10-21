"""
Challenge: Merge Sort
Level:     09 - Searching and Sorting
Topics:    divide and conquer, recursion, merging sorted lists, stability
Source:    Classic algorithm (John von Neumann, 1945)

========================================================================
YOUR TASK
========================================================================
Write two functions:

    merge(left, right)  takes two lists that are already sorted and
                        RETURNS one NEW sorted list with all their
                        items.
    merge_sort(items)   RETURNS a NEW sorted copy of `items`, using
                        merge sort (and your merge()).

    merge_sort([5, 2, 4, 1, 3])  ->  [1, 2, 3, 4, 5]

========================================================================
HOW MERGE SORT WORKS
========================================================================
DIVIDE AND CONQUER is a strategy with three steps:

    1. DIVIDE   split the problem into smaller sub-problems
    2. CONQUER  solve each sub-problem (usually recursively, meaning
                the function calls itself)
    3. COMBINE  join the sub-answers into the full answer

Merge sort applies it to sorting:

    1. Split the list into two halves.
    2. Merge-sort each half (recursively). A list of 0 or 1 items is
       already sorted. That's the base case, where the recursion stops.
    3. MERGE the two sorted halves into one sorted list.

    [5, 2, 4, 1]
    split  -> [5, 2]        [4, 1]
    split  -> [5] [2]       [4] [1]
    merge  -> [2, 5]        [1, 4]
    merge  -> [1, 2, 4, 5]

Merging two lists that are already sorted is easy and fast. Look at
the front item of each, take the smaller one, and repeat. When one
list runs out, add whatever is left of the other.

========================================================================
THE RULES
========================================================================
Your functions must:
1. merge: return a NEW list, sorted ascending, holding every item from
   `left` and `right`.
2. merge: when an item in `left` equals an item in `right`, take the
   one from LEFT first. This makes merge sort STABLE: equal items keep
   their original order.
3. merge_sort: return a NEW list, sorted ascending, built with the
   recursive algorithm above and your merge(). Return a new list
   object even for 0 or 1 items.
4. Never change (mutate) the inputs of either function.
5. Not use sorted(), list.sort(), heapq or heapq.merge in the
   solution. Use sorted() in your TESTS as the reference.

You can assume:
- All items can be compared with each other.
- merge's `left` and `right` are each sorted ascending.
- Lists have 0 to 10**5 items. Recursion goes only about log2(n)
  levels deep (about 17 for 10**5 items), so it's safe.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    merge([1, 4, 9], [2, 3, 10])  ->  [1, 2, 3, 4, 9, 10]
        Take the smaller front item each time: 1, 2, 3, 4, 9, then
        the leftover 10.

    merge([], [1, 2])             ->  [1, 2]
        Left is empty, so the result is just the right side.

    merge_sort([5, 2, 4, 1, 3])   ->  [1, 2, 3, 4, 5]
        Split, sort each half, merge.

    merge_sort([])                ->  []
        Nothing to sort, but still a new list.

========================================================================
COMPLEXITY TARGET
========================================================================
- merge:      Time O(len(left) + len(right)): each item is looked at
              once. Space O(same): the new list holds every item.
- merge_sort: Time O(n log n) in EVERY case (best, average, worst).
              There are about log n levels of splitting, and each
              level does O(n) merging work. Space O(n) extra for the
              new lists.

========================================================================
EDGE CASES TO TEST
========================================================================
- merge with one or both inputs empty: merge([], []) -> []
- All of left smaller than all of right:
  merge([1, 2], [3, 4]) -> [1, 2, 3, 4] (and the other way round)
- Equal items: merge([1, 2], [2, 3]) -> [1, 2, 2, 3]
- merge_sort on empty, one item and two items:
  merge_sort([2, 1]) -> [1, 2]
- Already sorted, reverse sorted, all equal, duplicates, negatives
- The input is unchanged, and the result is a new object
- STABILITY: sort objects that compare only by one field (see the
  insertion sort challenge for ideas). Equal ones must keep their
  order.
- Random lists vs sorted(), with a fixed random seed
- A large list (for example 50_000 random ints) runs quickly

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. merge: use two indices, i and j, starting at 0. While both lists
   have items left, append the smaller of left[i] and right[j] and
   move that index on. Use `<=` so that ties come from left.
2. After the loop, `result.extend(left[i:])` and
   `result.extend(right[j:])`. One of them will be empty.
3. merge_sort base case: `if len(items) <= 1: return list(items)`
   (a copy, not `items` itself).
4. `mid = len(items) // 2`, then recurse on `items[:mid]` and
   `items[mid:]` and merge the results.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Divide and conquer
- Recursion on halves, with a recursion depth of O(log n)
- Two-pointer technique
- Slicing creates copies
- Stability and why `<=` vs `<` matters
- Why O(n log n) beats O(n^2) (compare timings with bubble sort!)

========================================================================
STRETCH GOALS
========================================================================
- Write a bottom-up (iterative) merge sort with no recursion: merge
  pairs of 1-item lists, then pairs of 2-item lists, and so on.
- Count INVERSIONS (pairs of positions i < j with a[i] > a[j]) during
  the merge step, in O(n log n).
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
