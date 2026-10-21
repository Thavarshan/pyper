"""
Challenge: Merge Two Sorted Lists
Level:     03 - Lists
Topics:    two pointers, while loops, index arithmetic
Source:    Classic (the "merge" step of merge sort; cf. LeetCode #88 / #21)

========================================================================
YOUR TASK
========================================================================
You get two lists, `a` and `b`, that are each already SORTED in
ascending order (smallest to largest). Write `merge_sorted(a, b)`. It
returns ONE new list with every element of both, also in ascending
order.

    merge_sorted([1, 4, 7], [2, 3, 8])  ->  [1, 2, 3, 4, 7, 8]

========================================================================
HOW MERGING WORKS
========================================================================
Both lists are already sorted, so the smallest element left is always
at the FRONT of one of them. Compare the two front elements, take the
smaller one, and move on. You never need to look backwards:

    a = [1, 4, 7]    b = [2, 3, 8]

    compare 1 and 2  ->  take 1 from a    result: [1]
    compare 4 and 2  ->  take 2 from b    result: [1, 2]
    compare 4 and 3  ->  take 3 from b    result: [1, 2, 3]
    compare 4 and 8  ->  take 4 from a    result: [1, 2, 3, 4]
    compare 7 and 8  ->  take 7 from a    result: [1, 2, 3, 4, 7]
    a is used up     ->  add the rest of b
                                          result: [1, 2, 3, 4, 7, 8]

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a NEW list in ascending order, even when one input is empty.
   Do not change (mutate) `a` or `b`.
2. Keep duplicates: merging [1, 2] and [2, 3] gives [1, 2, 2, 3]. The
   result always has len(a) + len(b) elements.
3. Not use sorted(), list.sort() or the heapq module. The point is to
   take advantage of the fact that both inputs are already sorted.

You can assume:
- `a` and `b` are lists of numbers, each sorted ascending. They really
  are sorted, so you don't need to check.
- Either list, or both, may be empty.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    merge_sorted([1, 4, 7], [2, 3, 8])  ->  [1, 2, 3, 4, 7, 8]
        Elements from both lists, interleaved in order.

    merge_sorted([1, 2, 2], [2, 5])     ->  [1, 2, 2, 2, 5]
        Duplicates are kept: three 2s go in, three 2s come out.

    merge_sorted([], [1, 2])            ->  [1, 2]
        One list is empty, so the result is a copy of the other.

    merge_sorted([5, 6], [1, 2])        ->  [1, 2, 5, 6]
        Everything in b is smaller, so b's elements come first.

========================================================================
EDGE CASES TO TEST
========================================================================
- Both empty: merge_sorted([], []) -> []
- One empty: merge_sorted([], [1, 2]) -> [1, 2], and a different list
  object from b (check `result is not b`)
- Interleaved values: ([1, 4, 7], [2, 3, 8]) -> [1, 2, 3, 4, 7, 8]
- All of a smaller than all of b: ([1, 2], [5, 6]) -> [1, 2, 5, 6]
- And the other way round: ([5, 6], [1, 2]) -> [1, 2, 5, 6]
- Duplicates within a list and across both lists:
  ([1, 2, 2], [2, 5]) -> [1, 2, 2, 2, 5]
- Negative numbers: ([-3, 0], [-5, -1, 2]) -> [-5, -3, -1, 0, 2]
- Lists of very different lengths:
  ([4], [1, 2, 3, 5, 6]) -> [1, 2, 3, 4, 5, 6]
- Both inputs are unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Use two index variables, i for `a` and j for `b`, both starting at
   0.
2. While BOTH lists still have elements left, compare a[i] and b[j],
   append the smaller one to the result, and move forward only that
   index.
3. When one list runs out, everything left in the other list is
   already sorted and larger. Append the rest in one go with extend()
   and a slice: result.extend(a[i:]).
4. Using `<=` when comparing puts equal elements from `a` before those
   from `b`. Keeping equal elements in their original order like this
   is called being "stable".

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The two-pointer technique (two variables that each hold a position)
- `while` loops with compound conditions (and)
- `list.append()` vs `list.extend()`
- Why this is faster than joining the lists and sorting. You'll learn
  Big-O notation in later levels: this is O(n + m), meaning the work
  grows in step with the total number of elements, because each one is
  looked at once.

========================================================================
STRETCH GOALS
========================================================================
- Write `merge_k_sorted(lists: list[list[int]]) -> list[int]` for any
  number of lists.
- Use merge_sorted to build merge sort: split a list in half, sort
  each half recursively (by calling the sort on it), then merge.
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
