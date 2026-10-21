"""
Challenge: Longest Increasing Subsequence
Level:     12 - Algorithms
Topics:    dynamic programming O(n^2), binary search with bisect (stretch)
Source:    LeetCode #300 "Longest Increasing Subsequence"

========================================================================
YOUR TASK
========================================================================
Write `length_of_lis(nums)`. It RETURNS the length of the longest
STRICTLY increasing subsequence of `nums`.

    length_of_lis([10, 9, 2, 5, 3, 7, 101, 18])  ->  4    (2, 5, 7, 101)

========================================================================
SUBSEQUENCES, AND A DYNAMIC PROGRAMMING TABLE
========================================================================
A SUBSEQUENCE keeps the original order but may SKIP items. (A
substring or subarray may not skip: its items must sit next to each
other.) "Strictly increasing" means each item is greater than the one
before it. Equal values do not count.

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
                  2  5     7  101          -> length 4
                  2     3  7       18      -> also length 4

DYNAMIC PROGRAMMING (DP) builds the answer from answers to smaller
versions of the same problem, stored in a table. Here:

    Let dp[i] = the length of the longest increasing subsequence that
    ENDS exactly at index i (so nums[i] is its last item).
    - Every item alone is a subsequence of length 1, so start each
      dp[i] at 1.
    - To end at i, the item before it must be at some j < i with
      nums[j] < nums[i]. Then dp[i] = max(dp[i], dp[j] + 1).
    - The answer is max(dp): the best subsequence can end anywhere.

    i:        0   1   2   3   4   5   6    7
    nums[i]:  10  9   2   5   3   7   101  18
    dp[i]:    1   1   1   2   2   3   4    4      -> max = 4

    How dp[5] = 3 is found (nums[5] is 7): the earlier items smaller
    than 7 are 2 (dp 1), 5 (dp 2) and 3 (dp 2). The best is 2, so
    dp[5] = 2 + 1 = 3. That is 2, 5, 7 (or 2, 3, 7).

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the length of the longest subsequence whose values strictly
   increase (equal values do not count as increasing).
2. Return 0 for an empty list.
3. Not change (mutate) `nums`.

You can assume:
- `nums` is a list of 0 to 2_500 ints.
- Each number is from -10_000 to 10_000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    length_of_lis([10, 9, 2, 5, 3, 7, 101, 18])  ->  4
        2, 5, 7, 101 (or 2, 3, 7, 18). See the table above.

    length_of_lis([0, 1, 0, 3, 2, 3])            ->  4
        0, 1, 2, 3.

    length_of_lis([7, 7, 7, 7])                  ->  1
        Equal values are not "strictly" increasing, so just one 7.

    length_of_lis([])                            ->  0
        No items at all.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2) for the DP solution: for each i, look back at every
         j < i (a loop inside a loop). O(n log n) for the stretch goal.
- Space: O(n) for the dp list, one entry per item.

========================================================================
EDGE CASES TO TEST
========================================================================
- [] -> 0
- Single item: [5] -> 1
- All equal: [7, 7, 7, 7] -> 1 (strictly increasing!)
- Already sorted ascending: [1, 2, 3, 4] -> 4 (the length of the list)
- Sorted descending: [4, 3, 2, 1] -> 1
- Negative numbers: [-5, -3, -4, -1] -> 3 (-5, -3, -1 or -5, -4, -1)
- The best subsequence uses neither the first nor the last item:
  [9, 1, 2, 3, 0] -> 3 (1, 2, 3)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Handle the empty list first.
2. dp = [1] * len(nums).
3. Double loop: for i in range(n): for j in range(i): if nums[j] < nums[i]
   then dp[i] = max(dp[i], dp[j] + 1).
4. Return max(dp).
5. Stretch (O(n log n)): keep a list `tails`, where tails[k] is the
   smallest possible last value of an increasing subsequence of length
   k + 1. For each x, `bisect.bisect_left(tails, x)` tells you which
   entry to replace (or to append, if it's past the end). len(tails) is
   the answer.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `[1] * n` to initialise a DP list
- Nested loops over `range(i)`
- `max()` on a list
- The `bisect` module: bisect_left finds where a value belongs in a
  sorted list using binary search (repeatedly halving the search range)

========================================================================
STRETCH GOALS
========================================================================
- Implement the O(n log n) version with `bisect` and test it against the
  O(n^2) version on random lists.
- Return one actual longest subsequence, not just its length.
- Count the number of longest increasing subsequences (LeetCode #673).
"""


def length_of_lis(nums: list[int]) -> int:
    """Return the length of the longest strictly increasing subsequence.

    Args:
        nums: The sequence to examine. Not modified.

    Returns:
        The length of the longest subsequence whose values strictly
        increase. 0 for an empty list.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
