r"""
Challenge: All Subsets (the Power Set)
Level:     07 - Recursion
Topics:    recursion, backtracking, include/exclude choices, list copying
Source:    LeetCode #78 "Subsets"

========================================================================
YOUR TASK
========================================================================
Write `subsets(nums)`. It RETURNS a list of every subset of the list
`nums`, each subset being a list. Write it recursively (the function,
or a helper inside it, calls itself). The order of the result does not
matter.

    subsets([1, 2])  ->  [[], [1], [2], [1, 2]]   (in any order)

========================================================================
WHAT A "SUBSET" IS
========================================================================
A SUBSET of a collection is any selection of its items. You may pick
none of them, some of them, or all of them. The collection of ALL
subsets is called the POWER SET.

For [1, 2, 3] the subsets are:

    [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]

A list of n items has exactly 2**n subsets. For each item you make a
separate yes/no choice: "include it" or "leave it out". 3 items means
2 * 2 * 2 = 8 combinations of choices, so 8 subsets. That yes/no
choice is the heart of the recursive solution:

                              []
                 leave 1 /          \ take 1
                       []            [1]
           leave 2 /    \ take 2    /    \
                 []      [2]      [1]     [1,2]
                /  \     /  \     /  \     /  \
              []  [3]  [2] [2,3] [1] [1,3] [1,2] [1,2,3]

    At the bottom row, each left branch leaves 3 out and each right
    branch takes it. The 8 leaves are the 8 subsets.

ORDER DOES NOT MATTER: neither the order of the subsets in the outer
list, nor the order of the numbers inside each subset. For the input
[1, 2], the result may contain [2, 1] or [1, 2] for that subset, and
the subsets may come in any order.

HOW TO TEST WHEN ORDER DOES NOT MATTER: "normalise" both sides before
comparing. Sort inside each subset, then sort the outer list:

    def normalise(result):
        return sorted(sorted(s) for s in result)

    assert normalise(subsets([1, 2])) == normalise([[], [1], [2], [1, 2]])

========================================================================
THE RULES
========================================================================
Your function must:
1. Return every subset of `nums`, each exactly once.
2. Return a `list` of `list`s (not tuples, not sets).
3. Make each inner list its own separate object, so appending to one
   subset does not change another.
4. Not modify (mutate) `nums`.
5. Be recursive. Do not use `itertools` (`combinations` and friends) in
   your solution. You may use it in your tests.

You can assume:
- 0 <= len(nums) <= 10
- Every number is between -10 and 10, and all the numbers are DISTINCT
  (no duplicates).

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return. Because order does
not matter, the first and last results are shown normalised.

    sorted(sorted(s) for s in subsets([1, 2, 3]))
        ->  [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        2**3 = 8 subsets.

    subsets([])  ->  [[]]
        One subset: the empty one. Note this is a list holding an
        empty list, not an empty list.

    sorted(sorted(s) for s in subsets([0]))  ->  [[], [0]]
        Leave 0 out, or take it.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n * 2**n). There are 2**n subsets and each takes up to n
  steps to build or copy. Every extra item DOUBLES the work.
- Space: O(n) for the call stack. One waiting call per item at the
  deepest point. The output itself is O(n * 2**n).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty input: subsets([]) -> [[]] (one subset, the empty one)
- One item: normalise(subsets([5])) -> [[], [5]]
- len(subsets(nums)) == 2**len(nums) for several sizes
- No duplicate subsets: turn each subset into a tuple of its sorted
  items and put them in a set. The set's size equals len(result).
- [] and the full list (in some order) are always in the result
- Negative numbers and zero: normalise(subsets([-1, 0]))
  -> [[], [-1], [-1, 0], [0]]
- The input list is unchanged afterwards

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Think "include or exclude": the subsets of nums are the subsets of
   the rest (nums without nums[0]) PLUS each of those with nums[0]
   added.
2. Base case: subsets([]) == [[]], a list holding one empty list. Not
   [], which would mean "no subsets at all".
3. Backtracking version: write a helper `build(index, current)`. At
   each index it either skips nums[index], or appends it to current,
   recurses, then pops it off again ("undo the choice"). This
   choose, explore, un-choose pattern is called BACKTRACKING.
4. When you save `current` into the result, save a COPY (`current[:]`
   or `list(current)`). Otherwise every saved subset is the same list
   object, and they all end up identical (all empty, after the last
   pop).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Backtracking: choose, explore, un-choose
- References vs copies of lists (aliasing bugs: two names for the same
  list)
- Nested functions (a helper defined inside a function)
- Sorting lists of lists (`sorted` compares lists item by item)
- Comparing results order-independently in tests

========================================================================
STRETCH GOALS
========================================================================
- In a test, compare with an itertools-based answer built from
  `itertools.combinations(nums, k)` for k in 0..n.
- LeetCode #90 "Subsets II": allow duplicate values but still return
  each distinct subset only once.
- Write a non-recursive version using binary counting: each number
  from 0 to 2**n - 1, written in binary, says which items to take.
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
