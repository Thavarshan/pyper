"""
Challenge: Two Sum
Level:     04 - Dictionaries and Sets
Topics:    dicts for fast lookup, enumerate, trading memory for speed
Source:    LeetCode #1 "Two Sum"

========================================================================
YOUR TASK
========================================================================
Write `two_sum(nums, target)`. Find two DIFFERENT positions in the list
whose values add up to `target`, and return those two positions
(indices) as a list, smaller index first.

    two_sum([2, 7, 11, 15], 9)  ->  [0, 1]

An "index" is a position in the list, counting from 0. In [10, 20, 30],
the value 30 is at index 2.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a list [i, j] with i < j and nums[i] + nums[j] == target.
2. Use two DIFFERENT positions, never the same position twice. With
   nums = [3] and target = 6 there is no answer, because there is only
   one 3. But with nums = [3, 3] the answer is [0, 1]: two different
   positions that happen to hold the same value.
3. Raise ValueError if no pair adds up to `target`, including when
   `nums` has fewer than 2 elements. The exact message is up to you.
4. Not change (mutate) `nums`.

You can assume:
- `nums` is a list of ints. It may be empty, and may contain negatives
  and duplicates.
- `target` is an int.
- When an answer exists, it is UNIQUE (only one pair of positions
  works), as on LeetCode. Write your tests with inputs that have
  exactly one valid pair, so the expected result is clear.

The simple approach checks every pair (a loop inside a loop). The goal
here is to do it in ONE pass, using a dict that remembers
"value -> index where I saw it".

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    two_sum([2, 7, 11, 15], 9)  ->  [0, 1]
        nums[0] + nums[1] is 2 + 7, which is 9.

    two_sum([3, 2, 4], 6)       ->  [1, 2]
        2 + 4 is 6. The 3 can't be used twice to make 6.

    two_sum([3, 3], 6)          ->  [0, 1]
        Two different positions that hold the same value.

    two_sum([1, 2, 3], 100)     ->  raises ValueError
        No pair adds up to 100. A message such as
        "no two numbers add up to 100" is helpful.

========================================================================
COMPLEXITY TARGET
========================================================================
- O(n) time: one pass over the list, with no loop inside a loop.
  Checking whether a key is in a dict takes about the same tiny time
  however big the dict is (O(1) on average).
- O(n) space: the dict may end up storing up to n entries, one per
  element. You trade memory for speed.

========================================================================
EDGE CASES TO TEST
========================================================================
- The answer uses the first and last elements:
  two_sum([1, 5, 9, 4], 5) -> [0, 3]
- Duplicate values forming the answer: two_sum([3, 3], 6) -> [0, 1]
- A value that is exactly half the target, appearing once, must NOT
  pair with itself: two_sum([3, 4], 6) -> raises ValueError
- Negative numbers: two_sum([-3, 4, 3, 90], 0) -> [0, 2]
- Zeros: two_sum([0, 4, 3, 0], 0) -> [0, 3]
- Empty list or a single element: two_sum([], 5) and
  two_sum([5], 10) -> raises ValueError
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. For each number x, the number you NEED is `target - x` (its
   "complement").
2. `for i, x in enumerate(nums):` gives you both the index and the
   value.
3. Keep a dict `seen = {}` mapping value -> index. Before adding x,
   check whether its complement is already in `seen`.
4. Checking BEFORE inserting is what stops a number pairing with
   itself.
5. If the loop finishes without returning, raise the ValueError.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `enumerate()`
- dict membership (`key in d`) is O(1) on average, list membership is
  O(n) (it scans the whole list)
- Returning early from inside a loop
- Big-O thinking: O(n^2) nested loops vs O(n) with a hash map (the
  general name for a dict)

========================================================================
STRETCH GOALS
========================================================================
- Write the O(n^2) brute-force version too (check every pair), and
  time both on a list of 10_000 numbers using the `timeit` module.
- `all_two_sums(nums, target)`, which returns every index pair.
- Solve "two sum on a SORTED list" with two pointers and O(1) memory
  (only a few variables, no dict).
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
