"""
Challenge: Longest Increasing Subsequence
Level:     12 - Algorithms
Topics:    dynamic programming O(n^2), binary search with bisect (stretch)
Source:    LeetCode #300 "Longest Increasing Subsequence"

========================================================================
PROBLEM
========================================================================
Given a list of ints `nums`, return the LENGTH of the longest STRICTLY
increasing subsequence.

A SUBSEQUENCE keeps the original order but may SKIP elements (unlike a
substring/subarray, which must be contiguous). "Strictly increasing"
means each element is greater than the one before - equal values do not
count.

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
                  2  5     7  101          -> length 4
                  2     3  7       18      -> also length 4

DYNAMIC PROGRAMMING (O(n^2)):
    Let dp[i] = length of the longest increasing subsequence that ENDS
    exactly at index i (so nums[i] is its last element).
    - Every element alone is a subsequence of length 1, so start dp[i] = 1.
    - To end at i, the previous element must be some j < i with
      nums[j] < nums[i]; then dp[i] = max(dp[i], dp[j] + 1).
    - The answer is max(dp) - the best subsequence can end anywhere.

    i:        0   1   2   3   4   5   6    7
    nums[i]:  10  9   2   5   3   7   101  18
    dp[i]:    1   1   1   2   2   3   4    4      -> max = 4

========================================================================
EXAMPLES
========================================================================
    >>> length_of_lis([10, 9, 2, 5, 3, 7, 101, 18])
    4

    >>> length_of_lis([0, 1, 0, 3, 2, 3])
    4

    >>> length_of_lis([7, 7, 7, 7])
    1

    >>> length_of_lis([])
    0

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(nums) <= 2_500.
- -10_000 <= nums[i] <= 10_000.
- Empty list -> 0.
- Do not mutate `nums`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2) for the DP solution; O(n log n) for the stretch goal.
- Space: O(n).

========================================================================
EDGE CASES TO TEST
========================================================================
- [] -> 0
- Single element -> 1
- All equal -> 1 (strictly increasing!)
- Already sorted ascending -> n
- Sorted descending -> 1
- Negative numbers
- The best subsequence doesn't include the first or last element

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Handle the empty list first.
2. dp = [1] * len(nums).
3. Double loop: for i in range(n): for j in range(i): if nums[j] < nums[i]
   then dp[i] = max(dp[i], dp[j] + 1).
4. Return max(dp).
5. Stretch (O(n log n)): keep a list `tails` where tails[k] is the smallest
   possible last value of an increasing subsequence of length k + 1. For
   each x, `bisect.bisect_left(tails, x)` tells you which entry to replace
   (or to append if it's past the end). len(tails) is the answer.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `[1] * n` to initialise a DP list
- Nested loops over `range(i)`
- `max()` on a list
- The `bisect` module: bisect_left keeps a list sorted with binary search

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
