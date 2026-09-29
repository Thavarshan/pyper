"""
Challenge: Maximum Subarray
Level:     12 - Algorithms
Topics:    Kadane's algorithm, greedy / dynamic programming, running totals
Source:    LeetCode #53 "Maximum Subarray"

========================================================================
PROBLEM
========================================================================
Given a non-empty list of ints `nums`, find the contiguous SUBARRAY
(a run of one or more neighbouring elements) with the largest sum, and
return that SUM.

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                       [--------------]
                        4 + -1 + 2 + 1 = 6      -> 6

The subarray must contain AT LEAST ONE element, so for an all-negative
list the answer is the largest (least negative) single element, not 0.

KADANE'S ALGORITHM: walk through the list once, keeping
    current = the best sum of a subarray that ENDS at this position
    best    = the best sum seen anywhere so far

At each element x you have exactly two choices for `current`:
    - extend the previous subarray:  current + x
    - start fresh at x:              x
Take whichever is larger. Intuition: if the running sum so far is
negative, it can only drag x down, so throw it away and restart.

    x:        -2   1  -3   4  -1   2   1  -5   4
    current:  -2   1  -2   4   3   5   6   1   5
    best:     -2   1   1   4   4   5   6   6   6     -> 6

(This is actually a tiny dynamic programming solution: current is "dp[i]
= best sum ending at i", and dp[i] = max(nums[i], dp[i-1] + nums[i]).)

========================================================================
EXAMPLES
========================================================================
    >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6

    >>> max_subarray([1])
    1

    >>> max_subarray([5, 4, -1, 7, 8])
    23

    >>> max_subarray([-3, -1, -2])
    -1

========================================================================
CONSTRAINTS
========================================================================
- 1 <= len(nums) <= 100_000 for valid input.
- -10_000 <= nums[i] <= 10_000.
- An empty list raises `ValueError` (there is no non-empty subarray).
- Do not mutate `nums`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n) - one pass.
- Space: O(1).

========================================================================
EDGE CASES TO TEST
========================================================================
- Single element (positive, negative, zero)
- All negative -> the maximum single element (NOT 0)
- All positive -> sum of the whole list
- The best subarray is at the very start or very end
- Zeros mixed with negatives: [-1, 0, -2] -> 0
- [] -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Brute force: try every (start, end) pair and sum - O(n^2) with a
   running sum. Handy as a test reference.
2. Initialise both current and best to nums[0] (NOT 0 - think about the
   all-negative case).
3. Loop over nums[1:]: current = max(x, current + x); best = max(best,
   current).
4. Check for the empty list before touching nums[0].

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Iterating over a slice `nums[1:]` (or using an index loop)
- Why initialising to 0 is a classic bug here
- Recognising a DP recurrence hidden inside a greedy loop

========================================================================
STRETCH GOALS
========================================================================
- Also return the (start, end) indexes of the best subarray.
- Divide and conquer version in O(n log n).
- Maximum Product Subarray (LeetCode #152) - negatives make it trickier.
"""


def max_subarray(nums: list[int]) -> int:
    """Return the largest sum of any non-empty contiguous subarray.

    Args:
        nums: The numbers to search. Must be non-empty. Not modified.

    Returns:
        The maximum subarray sum.

    Raises:
        ValueError: If `nums` is empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
