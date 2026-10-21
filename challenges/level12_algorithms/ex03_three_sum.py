"""
Challenge: 3Sum
Level:     12 - Algorithms
Topics:    sorting, two pointers, skipping duplicates
Source:    LeetCode #15 "3Sum"

========================================================================
YOUR TASK
========================================================================
Write `three_sum(nums)`. It finds every group of three numbers from
`nums` that adds up to 0, and RETURNS them as a sorted list of
triplets, with no triplet listed twice.

    three_sum([-1, 0, 1, 2, -1, -4])  ->  [[-1, -1, 2], [-1, 0, 1]]

========================================================================
THE IDEA: SORT, THEN USE TWO POINTERS
========================================================================
The three numbers must come from three DIFFERENT positions in the list.
So a value can appear twice in a triplet only if it appears at least
twice in `nums`. Above, [-1, -1, 2] is allowed because -1 is in the
list twice.

The brute-force way tries every group of three with three nested loops.
That is O(n^3): 10 times more numbers means 1000 times more work.

The trick: SORT first. Then, for each index i, treat s[i] as `a` and
look for two numbers to its right that add up to -a. Use TWO POINTERS
for that: L starts just after i, R starts at the end.
    - sum too small -> move L right (to a bigger number)
    - sum too big   -> move R left (to a smaller number)
    - sum is 0      -> found one! record it, move both pointers

Walk-through on the sorted list:

    s = [-4, -1, -1, 0, 1, 2]       (indexes 0 to 5)

    i=0 (a=-4): L and R never find a sum of 0      (best is -1)
    i=1 (a=-1): L=2 (-1), R=5 (2) -> -1 + -1 + 2 = 0   found!
                L=3 (0),  R=4 (1) -> -1 +  0 + 1 = 0   found!
    i=2 (a=-1): same `a` as i=1, skip it (it would find the same
                triplets again)
    i=3 (a=0):  L=4 (1),  R=5 (2) -> 0 + 1 + 2 = 3     too big, R left
    i=4 (a=1):  a > 0, and everything to its right is bigger, so no
                later triplet can add up to 0. Stop.

    result: [[-1, -1, 2], [-1, 0, 1]]

Because the list is sorted, equal values sit next to each other. That
makes duplicates easy to skip.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return every unique triplet [a, b, c] of values with a + b + c == 0,
   using three different positions in `nums`.
2. Sort each triplet ascending: [a, b, c] with a <= b <= c.
3. List each triplet only once: [-1, 0, 1] appears once even if it
   could be formed from different positions.
4. Sort the outer list ascending, the way `sorted()` sorts lists of
   lists (compare first items, then second items on a tie, and so on).
   For example, [-1, -1, 2] comes before [-1, 0, 1].
5. Return [] if there are no triplets, including when `nums` has fewer
   than 3 numbers.
6. Not change (mutate) `nums`. Sort a copy with `sorted(nums)`.

You can assume:
- `nums` is a list of 0 to 3_000 ints.
- Each number is from -100_000 to 100_000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    three_sum([-1, 0, 1, 2, -1, -4])  ->  [[-1, -1, 2], [-1, 0, 1]]
        See the walk-through above.

    three_sum([0, 1, 1])              ->  []
        The only group of three adds up to 2.

    three_sum([0, 0, 0, 0])           ->  [[0, 0, 0]]
        Many choices of three zeros, but they all give the same
        triplet, so it is listed once.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2). Sorting takes O(n log n) (a bit more than one pass).
         Then, for each of the n indexes, one two-pointer scan of
         O(n). n scans of n steps each is n^2.
- Space: O(n) for the sorted copy (the output is not counted).

========================================================================
EDGE CASES TO TEST
========================================================================
- [] -> [], and [1, 2] -> []
- No valid triplet: [0, 1, 1] -> []
- All zeros: [0, 0, 0, 0] -> [[0, 0, 0]] (once!)
- Many duplicates: [-2, 0, 0, 2, 2] -> [[-2, 0, 2]]
- Several triplets, to check the outer ordering:
  [-4, -1, -1, 0, 1, 2, 3] -> [[-4, 1, 3], [-1, -1, 2], [-1, 0, 1]]
- The input list is unchanged afterwards

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Easiest correct version: three nested loops. Add `tuple(sorted(...))`
   of each zero-sum triple to a set, then convert to lists and sort.
   Great as a reference in your tests.
2. Fast version: s = sorted(nums). Loop i over the indexes. Skip i if
   i > 0 and s[i] == s[i - 1] (same `a` as last time). Don't drop the
   `i > 0` check: at i = 0, s[i - 1] is s[-1], the LAST item, so
   [0, 0, 0, 0] would skip every i and wrongly return [].
3. left, right = i + 1, len(s) - 1. While left < right, compare
   s[i] + s[left] + s[right] with 0 and move a pointer.
4. On a match: record it and move BOTH pointers. Then keep moving left
   while left < right and s[left] == s[left - 1], to skip duplicate `b`
   values. (Without `left < right`, [0, 0, 0] runs left off the end of
   the list and crashes with IndexError.)
5. Early exit: if s[i] > 0, no later triplet can sum to 0.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `sorted()` (new list) vs `.sort()` (in place, changes the original)
- Sets of tuples for removing duplicates (lists are unhashable, so they
  can't go in a set. Tuples can.)
- Lexicographic ordering of lists (dictionary-style: first item first):
  [-1, -1, 2] < [-1, 0, 1]
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
