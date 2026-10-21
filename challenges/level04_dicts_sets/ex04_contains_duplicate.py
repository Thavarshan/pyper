"""
Challenge: Contains Duplicate
Level:     04 - Dictionaries and Sets
Topics:    sets, membership testing, early exit
Source:    LeetCode #217 "Contains Duplicate"

========================================================================
YOUR TASK
========================================================================
Write `contains_duplicate(nums)`. Return True if ANY value appears at
least twice in the list, and False if every value is distinct
(different from all the others).

    contains_duplicate([1, 2, 3, 1])  ->  True

A "set" in Python is a collection that stores each value at most once,
and can tell you very quickly whether a value is inside it. That makes
it the perfect tool here.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a real bool, True or False. Not 0/1, and not a set.
2. Not change (mutate) `nums`. So no `nums.sort()`, which reorders the
   caller's list in place.

You can assume:
- `nums` is a list of ints with 0 to 100_000 elements. Values may be
  negative.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    contains_duplicate([1, 2, 3, 1])                    ->  True
        1 appears twice.

    contains_duplicate([1, 2, 3, 4])                    ->  False
        All four values are different.

    contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  ->  True
        Several values repeat. One repeat is enough for True.

    contains_duplicate([])                              ->  False
        No values, so nothing can repeat.

========================================================================
COMPLEXITY TARGET
========================================================================
- O(n) time: one pass over the list. Each set lookup or insert takes
  about the same tiny time however big the set is (O(1) on average).
- O(n) space: the set may grow to hold all n values.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: [] -> False
- Single element: [7] -> False
- Two equal: [5, 5] -> True
- Negative numbers and zero: [-1, 0, 1, -1] -> True
- Duplicates far apart: [1, 2, 3, 4, 5, 6, 7, 8, 9, 1] -> True
- The result is a bool: `assert contains_duplicate([1]) is False`
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. One-liner idea: a set drops duplicates, so compare `len(set(nums))`
   with `len(nums)`.
2. Loop idea (it can stop early!): keep a `seen = set()`. For each
   number, if it's already in `seen` return True, otherwise
   `seen.add(x)`.
3. If the loop finishes, nothing repeated: return False.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Creating sets: `set()` (NOT `{}`, which is an empty dict!)
- `set.add()` and `x in some_set`
- `len()` of a set vs a list
- Returning early from a loop ("short-circuit": stop as soon as you
  know the answer)

========================================================================
STRETCH GOALS
========================================================================
- Implement both the one-liner and the early-exit loop. Which is faster
  when the duplicate is at the very start of a huge list?
- LeetCode #219: return True if two equal values sit at most `k`
  positions apart (|i - j| <= k). Hint: a dict of value -> last index.
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
