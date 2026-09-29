"""
Challenge: 3Sum
Level:     12 - Algorithms
Topics:    sorting, two pointers, skipping duplicates
Source:    LeetCode #15 "3Sum"

========================================================================
PROBLEM
========================================================================
Given a list of ints `nums`, find every UNIQUE triplet of values
[a, b, c] such that a + b + c == 0, where a, b and c come from three
DIFFERENT positions in the list (the same value may be used more than
once only if it appears more than once in the list).

Output format (so tests can compare exactly):
    - Each triplet is a `list[int]` sorted ascending: [a, b, c] with
      a <= b <= c.
    - No duplicate triplets: [-1, 0, 1] appears once even if it could be
      formed from different positions.
    - The outer list is sorted ascending (lexicographically - Python's
      normal list ordering, i.e. what `sorted()` gives).
    - No triplets -> [].

    nums = [-1, 0, 1, 2, -1, -4]
    sorted:  [-4, -1, -1, 0, 1, 2]
    triplets: [-1, -1, 2] and [-1, 0, 1]
    result:  [[-1, -1, 2], [-1, 0, 1]]

Brute force (three nested loops) is O(n^3). The trick: SORT first, then
for each index i treat nums[i] as `a` and solve "two sum = -a" on the
part to its right using TWO POINTERS (left just after i, right at the end):

    a = -1 (i=1)     [-4, -1, -1, 0, 1, 2]
                           i   L         R     -1 + -1 + 2 = 0  found!
    sum too small -> move L right; sum too big -> move R left.

Because the list is sorted, duplicates sit next to each other, so you can
skip over repeated values to avoid duplicate triplets.

========================================================================
EXAMPLES
========================================================================
    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]

    >>> three_sum([0, 1, 1])
    []

    >>> three_sum([0, 0, 0, 0])
    [[0, 0, 0]]

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(nums) <= 3_000.
- -100_000 <= nums[i] <= 100_000.
- Fewer than 3 numbers -> [].
- Do not mutate `nums` (sort a copy with `sorted(nums)`).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2) - O(n log n) sort + O(n) two-pointer scan per index.
- Space: O(n) for the sorted copy (output not counted).

========================================================================
EDGE CASES TO TEST
========================================================================
- [] and [1, 2] -> []
- No valid triplet -> []
- All zeros [0, 0, 0, 0] -> [[0, 0, 0]] (once!)
- Many duplicates, e.g. [-2, 0, 0, 2, 2] -> [[-2, 0, 2]]
- Several triplets - check the outer ordering
- The input list is unchanged afterwards

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Easiest correct version: three nested loops, add `tuple(sorted(...))`
   of each zero-sum triple to a set, then convert and sort. Great as a
   reference in your tests.
2. Fast version: s = sorted(nums). Loop i over indexes; skip i if
   s[i] == s[i - 1] (same `a` as last time).
3. left, right = i + 1, len(s) - 1. While left < right, compare
   s[i] + s[left] + s[right] with 0 and move a pointer.
4. On a match: record it, move BOTH pointers, then keep moving left while
   s[left] == s[left - 1] to skip duplicate `b` values.
5. Early exit: if s[i] > 0, no later triplet can sum to 0.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `sorted()` (new list) vs `.sort()` (in place)
- Sets of tuples for de-duplication (lists are unhashable, tuples are not)
- Lexicographic ordering of lists: [-1, -1, 2] < [-1, 0, 1]
- `itertools.combinations(nums, 3)` for the brute-force reference

========================================================================
STRETCH GOALS
========================================================================
- Generalise to `k_sum(nums, k, target)`.
- 3Sum Closest (LeetCode #16).
- Solve Two Sum II (LeetCode #167) as a warm-up for the inner loop.
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """Return all unique triplets of values that sum to zero.

    Args:
        nums: The numbers to search. Not modified.

    Returns:
        A sorted list of unique triplets, each an ascending list [a, b, c]
        with a + b + c == 0. Returns [] if there are none.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
