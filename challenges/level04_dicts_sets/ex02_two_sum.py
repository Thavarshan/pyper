"""
Challenge: Two Sum
Level:     04 - Dictionaries and Sets
Topics:    dicts for fast lookup, enumerate, trading memory for speed
Source:    LeetCode #1 "Two Sum"

========================================================================
PROBLEM
========================================================================
You are given a list of integers `nums` and a single integer `target`.
Find two DIFFERENT positions in the list whose values add up to
`target`, and return those two positions (indices) as a list.

- An "index" is a position in the list, starting from 0. In
  [10, 20, 30], the value 30 is at index 2.
- You may not use the same position twice. With nums = [3] and
  target = 6 there is no answer, because there is only one 3.
  But with nums = [3, 3] the answer is [0, 1] (two different positions
  that happen to hold the same value).
- Return the SMALLER index first: [i, j] with i < j.
- Like LeetCode, assume that when an answer exists it is UNIQUE (only
  one pair of positions works). Write your tests with inputs that have
  exactly one valid pair, so the expected result is unambiguous.
- If no pair adds up to `target`, raise `ValueError`.

The naive approach checks every pair (a loop inside a loop). The goal
here is to do it in ONE pass using a dict that remembers
"value -> index where I saw it".

========================================================================
EXAMPLES
========================================================================
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]

    >>> two_sum([3, 2, 4], 6)
    [1, 2]

    >>> two_sum([3, 3], 6)
    [0, 1]

    >>> two_sum([1, 2, 3], 100)
    Traceback (most recent call last):
    ...
    ValueError: no two numbers add up to 100

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of ints (may be empty, may contain negatives and
  duplicates). Values and target fit comfortably in Python ints.
- Do NOT modify `nums`.
- Raise `ValueError` if there is no valid pair (including when `nums`
  has fewer than 2 elements). The exact message is up to you.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time O(n), space O(n): one pass over the list, and each dict lookup is
  O(1) on average, at the cost of storing up to n entries.

========================================================================
EDGE CASES TO TEST
========================================================================
- The answer uses the first and last elements
- Duplicate values forming the answer: [3, 3], target 6 -> [0, 1]
- A value that is exactly half the target appearing once must NOT pair
  with itself: [3, 4], target 6 -> ValueError
- Negative numbers: [-3, 4, 3, 90], target 0 -> [0, 2]
- Zeros: [0, 4, 3, 0], target 0 -> [0, 3]
- Empty list or single element -> ValueError
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. For each number x, the number you NEED is `target - x` (its
   "complement").
2. `for i, x in enumerate(nums):` gives you both index and value.
3. Keep a dict `seen = {}` mapping value -> index. Before adding x,
   check whether its complement is already in `seen`.
4. Checking BEFORE inserting is what stops a number pairing with itself.
5. If the loop finishes without returning, raise the ValueError.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `enumerate()`
- dict membership (`key in d`) is O(1) on average, list membership is O(n)
- Returning early from inside a loop
- Big-O thinking: O(n^2) nested loops vs O(n) with a hash map

========================================================================
STRETCH GOALS
========================================================================
- Write the O(n^2) brute-force version too, and time both on a list of
  10_000 numbers using the `timeit` module.
- `all_two_sums(nums, target)` returning every index pair.
- Solve "two sum on a SORTED list" with two pointers and O(1) memory.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices of two different elements that sum to target.

    Args:
        nums: The numbers to search. Not modified.
        target: The sum to find.

    Returns:
        A two-element list [i, j] with i < j and nums[i] + nums[j] == target.

    Raises:
        ValueError: If no such pair exists.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
