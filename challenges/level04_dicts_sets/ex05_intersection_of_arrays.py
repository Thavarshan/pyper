"""
Challenge: Intersection of Two Arrays
Level:     04 - Dictionaries and Sets
Topics:    set operations, converting between list and set, sorting
Source:    LeetCode #349 "Intersection of Two Arrays"

========================================================================
PROBLEM
========================================================================
Given two lists of integers, return the values that appear in BOTH
lists. This is called the "intersection" (think of the overlapping
middle of a Venn diagram).

Rules:
- Each value appears in the result at most ONCE, even if it is repeated
  in the inputs. ([1, 2, 2, 1] and [2, 2] -> [2], not [2, 2].)
- LeetCode allows any order; to make tests deterministic (predictable),
  YOUR function must return the values sorted in ascending order.
- Do not modify either input list.

========================================================================
EXAMPLES
========================================================================
    >>> intersection([1, 2, 2, 1], [2, 2])
    [2]

    >>> intersection([4, 9, 5], [9, 4, 9, 8, 4])
    [4, 9]

    >>> intersection([1, 2, 3], [4, 5, 6])
    []

========================================================================
CONSTRAINTS
========================================================================
- `nums1` and `nums2` are lists of ints (either may be empty); values
  may be negative.
- Return a `list[int]` (NOT a set), sorted ascending, with no duplicates.
- Neither input is modified.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time O(n + m + k log k), space O(n + m): building two sets is linear,
  and only the k common values need sorting.

========================================================================
EDGE CASES TO TEST
========================================================================
- One or both lists empty      -> []
- No common values             -> []
- Identical lists              -> sorted unique values of that list
- Heavy duplication on both sides -> each common value once
- Negative numbers [-1, -2, 3] & [-2, 3, 3] -> [-2, 3]
- Result is a list, not a set: `assert isinstance(result, list)`
- Inputs unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `set(nums1)` removes duplicates from the first list.
2. Sets support `&` for intersection: `{1, 2, 3} & {2, 3, 4} == {2, 3}`.
   (Or the method form: `a.intersection(b)`.)
3. `sorted(some_set)` returns a NEW sorted list.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Set operators: `&` (intersection), `|` (union), `-` (difference),
  `^` (symmetric difference)
- `sorted()` returns a list from any iterable
- Why sets have no guaranteed order (and why we sort for tests)

========================================================================
STRETCH GOALS
========================================================================
- Solve it without the `&` operator, using a loop and one set.
- LeetCode #350 "Intersection of Two Arrays II": keep duplicates as many
  times as they appear in both (hint: `collections.Counter` supports `&`).
- `union(nums1, nums2)` and `difference(nums1, nums2)` with the same
  sorted-unique rules.
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
