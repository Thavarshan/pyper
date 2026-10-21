"""
Challenge: Maximum Subarray
Level:     12 - Algorithms
Topics:    Kadane's algorithm, greedy / dynamic programming, running totals
Source:    LeetCode #53 "Maximum Subarray"

========================================================================
YOUR TASK
========================================================================
Write `max_subarray(nums)`. A subarray is a run of one or more
neighbouring items. RETURN the largest SUM any subarray of `nums` can
have.

    max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  ->  6

========================================================================
KADANE'S ALGORITHM
========================================================================
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                       [--------------]
                        4 + -1 + 2 + 1 = 6      -> 6

The subarray must contain AT LEAST ONE item. So for an all-negative
list the answer is the largest (least negative) single item, not 0.

Kadane's algorithm walks through the list once, keeping two numbers:
    current = the best sum of a subarray that ENDS at this position
    best    = the best sum seen anywhere so far

At each item x you have exactly two choices for `current`:
    - extend the previous subarray:  current + x
    - start fresh at x:              x
Take whichever is larger. The intuition: if the running sum so far is
negative, it can only drag x down, so throw it away and restart.

    x:        -2   1  -3   4  -1   2   1  -5   4
    current:  -2   1  -2   4   3   5   6   1   5
    best:     -2   1   1   4   4   5   6   6   6     -> 6

    At x = 1: current was -2, and -2 + 1 = -1 is worse than just 1,
    so start fresh. At x = 4: current was -2, so start fresh again.

This is really a tiny dynamic programming solution. (Dynamic
programming builds each answer from answers to smaller versions of the
same problem.) `current` is dp[i], "the best sum ending at index i",
and dp[i] = max(nums[i], dp[i-1] + nums[i]).

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the largest sum of any non-empty run of neighbouring items.
2. For an all-negative list, return the largest single item (NOT 0).
3. Raise ValueError if `nums` is empty (there is no non-empty
   subarray).
4. Not change (mutate) `nums`.

You can assume:
- `nums` is a list of ints. When it is not empty, it has up to 100_000
  items.
- Each number is from -10_000 to 10_000.
- With up to 100_000 items, trying every (start, end) pair is too slow
  for big inputs: aim for one pass.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])  ->  6
        The run 4, -1, 2, 1. See the table above.

    max_subarray([1])                              ->  1
        The only subarray is [1].

    max_subarray([5, 4, -1, 7, 8])                 ->  23
        The whole list. The -1 is worth keeping to reach 7 and 8.

    max_subarray([-3, -1, -2])                     ->  -1
        All negative, so pick the single largest item.

    max_subarray([])                               ->  raises ValueError

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). One pass over the list, no loop inside a loop.
- Space: O(1). Just two variables, however long the list is.

========================================================================
EDGE CASES TO TEST
========================================================================
- Single item: [5] -> 5, [-7] -> -7, [0] -> 0
- All negative: [-3, -1, -2] -> -1 (the largest single item, NOT 0)
- All positive: [1, 2, 3] -> 6 (the sum of the whole list)
- The best subarray is at the very start: [5, -10, 1] -> 5
- The best subarray is at the very end: [1, -10, 5] -> 5
- Zeros mixed with negatives: [-1, 0, -2] -> 0
- [] -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Brute force: try every (start, end) pair and keep a running sum.
   That is O(n^2), but handy as a test reference.
2. Start both current and best at nums[0] (NOT 0: think about the
   all-negative case, where starting at 0 would wrongly return 0).
3. Loop over nums[1:]: current = max(x, current + x), then
   best = max(best, current).
4. Check for the empty list before touching nums[0].

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Iterating over a slice `nums[1:]` (or using an index loop)
- Why initialising to 0 is a classic bug here
- Recognising a DP recurrence (a formula that builds each answer from
  earlier ones) hidden inside a greedy loop

========================================================================
STRETCH GOALS
========================================================================
- Also return the (start, end) indexes of the best subarray.
- Divide and conquer version in O(n log n): split the list in half,
  solve each half, and also check runs that cross the middle.
- Maximum Product Subarray (LeetCode #152). Negatives make it trickier.
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
