"""
Challenge: All Subsets (the Power Set)
Level:     07 - Recursion
Topics:    recursion, backtracking, include/exclude choices, list copying
Source:    LeetCode #78 "Subsets"

========================================================================
PROBLEM
========================================================================
A SUBSET of a collection is any selection of its items - you may pick
none of them, some of them, or all of them. The collection of ALL
subsets is called the POWER SET.

For [1, 2, 3] the subsets are:
    [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]

Write `subsets(nums)` that returns every subset of the list `nums`.
The numbers in `nums` are all DISTINCT (no duplicates), so the result
must contain each subset exactly once.

A list of n items has exactly 2**n subsets, because for each item you
make an independent yes/no choice: "include it" or "leave it out".
That choice is the heart of the recursive solution.

ORDER DOES NOT MATTER - neither the order of the subsets in the outer
list, nor the order of the numbers inside each subset. [[2, 1], []] and
[[], [1, 2]] are both acceptable for the same input.

HOW TO TEST WHEN ORDER DOES NOT MATTER: normalise both sides before
comparing - sort inside each subset, then sort the outer list:

    def normalise(result):
        return sorted(sorted(s) for s in result)

    assert normalise(subsets([1, 2])) == normalise([[], [1], [2], [1, 2]])

========================================================================
EXAMPLES
========================================================================
    >>> sorted(sorted(s) for s in subsets([1, 2, 3]))
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

    >>> subsets([])
    [[]]

    >>> sorted(sorted(s) for s in subsets([0]))
    [[], [0]]

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(nums) <= 10
- -10 <= nums[i] <= 10, all values distinct.
- Return a `list` of `list`s (not tuples, not sets).
- Each inner list must be its own separate object (appending to one
  subset must not change another).
- Do not modify `nums`.
- Must be recursive. Do not use `itertools` (combinations etc.) in your
  solution - you may use it in tests.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n * 2**n) - there are 2**n subsets, each up to n long.
- Space: O(n) call stack depth (plus the O(n * 2**n) output).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty input -> [[]] (one subset: the empty one)
- One item -> two subsets: [] and [x]
- len(result) == 2**len(nums) for several sizes
- No duplicate subsets (convert each to a tuple of sorted items and put
  them in a set - the set size should equal len(result))
- The empty list and the full list are always present
- Negative numbers and zero are handled
- Input list is unchanged afterwards

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Think "include or exclude": subsets(nums) = subsets of the rest
   (without nums[0]) PLUS each of those with nums[0] added.
2. Base case: subsets([]) == [[]] - a list containing one empty list.
   (Not [] - that would mean "no subsets at all"!)
3. Backtracking version: write a helper `build(index, current)` that at
   each index either skips nums[index] or appends it, recurses, then
   pops it off again ("undo the choice").
4. When saving `current` into the result, save a COPY
   (`current[:]` or `list(current)`). Otherwise every saved subset is the
   same list object and they all end up identical.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Backtracking: choose, explore, un-choose
- References vs copies of lists (aliasing bugs)
- Nested functions (a helper defined inside a function)
- Sorting lists of lists (`sorted` compares lists element by element)
- Comparing results order-independently in tests

========================================================================
STRETCH GOALS
========================================================================
- In a test, compare with an itertools-based answer built from
  `itertools.combinations(nums, k)` for k in 0..n.
- LeetCode #90 "Subsets II": allow duplicate values but still return
  each distinct subset only once.
- Write a non-recursive version using binary counting (0..2**n - 1).
"""


def subsets(nums: list[int]) -> list[list[int]]:
    """Return every subset of `nums` (the power set).

    Must be implemented recursively. The order of subsets and the order
    of elements inside each subset are unspecified.

    Args:
        nums: A list of distinct integers. Not modified.

    Returns:
        A list of 2**len(nums) lists, each a distinct subset.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
