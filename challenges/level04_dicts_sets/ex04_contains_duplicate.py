"""
Challenge: Contains Duplicate
Level:     04 - Dictionaries and Sets
Topics:    sets, membership testing, early exit
Source:    LeetCode #217 "Contains Duplicate"

========================================================================
PROBLEM
========================================================================
Given a list of integers `nums`, return True if ANY value appears at
least twice in the list, and False if every value is distinct
(different from all the others).

A "set" in Python is a collection that stores each value at most once
and can tell you very quickly whether a value is inside it. That makes
it the perfect tool here.

========================================================================
EXAMPLES
========================================================================
    >>> contains_duplicate([1, 2, 3, 1])
    True

    >>> contains_duplicate([1, 2, 3, 4])
    False

    >>> contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    True

    >>> contains_duplicate([])
    False

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of ints, length 0 to 100_000; values may be negative.
- Do NOT modify `nums` (so no in-place `nums.sort()`).
- Return a real bool (True/False), not 0/1 or a set.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time O(n), space O(n): each set lookup/insert is O(1) on average, and
  the set may grow to hold all n values.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list            -> False
- Single element [7]    -> False
- Two equal [5, 5]      -> True
- Negative numbers and zero [-1, 0, 1, -1] -> True
- Duplicates far apart [1, 2, 3, ..., 1]   -> True
- The result is a bool: `assert contains_duplicate([1]) is False`
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. One-liner idea: a set drops duplicates, so compare `len(set(nums))`
   with `len(nums)`.
2. Loop idea (can stop early!): keep a `seen = set()`; for each number,
   if it's already in `seen` return True, otherwise `seen.add(x)`.
3. If the loop finishes, nothing repeated: return False.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Creating sets: `set()` (NOT `{}` - that's an empty dict!)
- `set.add()` and `x in some_set`
- `len()` of a set vs a list
- Early return from a loop ("short-circuit")

========================================================================
STRETCH GOALS
========================================================================
- Implement both the one-liner and the early-exit loop. Which is faster
  when the duplicate is at the very start of a huge list?
- LeetCode #219: return True if a duplicate exists within distance `k`
  (|i - j| <= k). Hint: a dict of value -> last index.
"""


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears more than once in nums.

    Args:
        nums: The numbers to check. Not modified.

    Returns:
        True if at least one value is repeated, otherwise False.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
