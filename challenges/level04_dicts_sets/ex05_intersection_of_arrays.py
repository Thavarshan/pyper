"""
Challenge: Intersection of Two Arrays
Level:     04 - Dictionaries and Sets
Topics:    set operations, converting between list and set, sorting
Source:    LeetCode #349 "Intersection of Two Arrays"

========================================================================
YOUR TASK
========================================================================
Write `intersection(nums1, nums2)`. Return the values that appear in
BOTH lists, each value once, sorted from smallest to largest.

    intersection([4, 9, 5], [9, 4, 9, 8, 4])  ->  [4, 9]

The values found in both are called the "intersection". Think of the
overlapping middle of a Venn diagram:

    nums1 has:   4, 9, 5
    nums2 has:   9, 4, 8
    in both:     4, 9

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a `list[int]`, NOT a set.
2. Include each value at most ONCE, even if it is repeated in the
   inputs: [1, 2, 2, 1] and [2, 2] give [2], not [2, 2].
3. Sort the values in ascending order (smallest to largest). LeetCode
   allows any order, but this version sorts so that tests are
   deterministic (they always expect the same exact answer).
4. Not change (mutate) either input list.

You can assume:
- `nums1` and `nums2` are lists of ints. Either may be empty, and
  values may be negative.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    intersection([1, 2, 2, 1], [2, 2])        ->  [2]
        2 is the only value in both lists. It appears once in the
        result.

    intersection([4, 9, 5], [9, 4, 9, 8, 4])  ->  [4, 9]
        4 and 9 are in both lists, sorted smallest first.

    intersection([1, 2, 3], [4, 5, 6])        ->  []
        Nothing in common.

========================================================================
COMPLEXITY TARGET
========================================================================
- O(n + m + k log k) time, where n and m are the two list lengths and k
  is the number of common values. Building the two sets is one pass
  over each list (n + m), and only the k common values need sorting
  (about k log k steps).
- O(n + m) space: the two sets can hold every value from both lists.

========================================================================
EDGE CASES TO TEST
========================================================================
- One or both lists empty: ([], [1, 2]) and ([], []) -> []
- No common values: ([1, 2, 3], [4, 5, 6]) -> []
- Identical lists: ([3, 1, 3, 2], [3, 1, 3, 2]) -> [1, 2, 3]
  (the sorted unique values of that list)
- Heavy duplication on both sides: ([1, 1, 1, 2], [1, 1, 2, 2])
  -> [1, 2] (each common value once)
- Negative numbers: ([-1, -2, 3], [-2, 3, 3]) -> [-2, 3]
- The result is a list, not a set: `assert isinstance(result, list)`
- Both inputs are unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `set(nums1)` removes duplicates from the first list.
2. Sets support `&` for intersection: `{1, 2, 3} & {2, 3, 4} == {2, 3}`.
   (Or use the method form: `a.intersection(b)`.)
3. `sorted(some_set)` returns a NEW sorted list.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Set operators: `&` (intersection: in both), `|` (union: in either),
  `-` (difference: in the first but not the second), `^` (symmetric
  difference: in one or the other, but not both)
- `sorted()` returns a list from any iterable (anything you can loop
  over)
- Why sets have no guaranteed order (and why we sort for tests)

========================================================================
STRETCH GOALS
========================================================================
- Solve it without the `&` operator, using a loop and one set.
- LeetCode #350 "Intersection of Two Arrays II": keep duplicates as
  many times as they appear in both (hint: `collections.Counter`
  supports `&`).
- `union(nums1, nums2)` and `difference(nums1, nums2)` with the same
  sorted, unique rules.
"""


def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """Return the sorted unique values present in both lists.

    Args:
        nums1: First list of ints. Not modified.
        nums2: Second list of ints. Not modified.

    Returns:
        A new list of the distinct values found in both inputs, in
        ascending order.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
