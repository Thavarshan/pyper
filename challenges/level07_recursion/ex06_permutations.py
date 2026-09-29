"""
Challenge: All Permutations
Level:     07 - Recursion
Topics:    recursion, backtracking, factorial growth, list slicing
Source:    LeetCode #46 "Permutations"

========================================================================
PROBLEM
========================================================================
A PERMUTATION is one possible ordering (arrangement) of a collection's
items, using every item exactly once. For [1, 2, 3] there are six:

    [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]

Write `permutations(nums)` that returns every permutation of `nums`.
All numbers in `nums` are DISTINCT.

A list of n distinct items has n! ("n factorial") permutations:
n * (n-1) * ... * 2 * 1. There are n choices for the first position,
n-1 for the second, and so on. That grows VERY quickly: 10! = 3,628,800.

The ORDER OF THE PERMUTATIONS in the outer list does not matter (but
of course the order INSIDE each permutation is the whole point, so do
not sort inside!). To test, sort the outer list on both sides:

    assert sorted(permutations([1, 2])) == sorted([[1, 2], [2, 1]])

========================================================================
EXAMPLES
========================================================================
    >>> sorted(permutations([1, 2, 3]))
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

    >>> permutations([7])
    [[7]]

    >>> permutations([])
    [[]]

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(nums) <= 8
- -10 <= nums[i] <= 10, all values distinct.
- Return a `list` of `list`s. Each inner list is a separate object.
- Do not modify `nums` (or if you swap in place while working, restore
  it before returning).
- Must be recursive. Do NOT use `itertools.permutations` (or any other
  itertools function) in your solution. You MAY use it in your tests.
- Empty input returns [[]]: there is exactly one way to arrange zero
  items (the empty arrangement), matching 0! == 1.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n * n!) - there are n! permutations, each n long.
- Space: O(n) call stack depth (plus the O(n * n!) output).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> [[]]
- One item -> [[x]]
- Two items -> both orders
- len(result) == math.factorial(len(nums)) for sizes 0..6
- No duplicate permutations (convert to tuples and put in a set)
- Every permutation contains exactly the same items as nums
  (sorted(p) == sorted(nums))
- Input unchanged afterwards
- Negative numbers work

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Pick each item in turn to go FIRST. For each choice, the rest of the
   permutation is any permutation of the remaining items.
2. The "remaining items" when picking index i are
   `nums[:i] + nums[i+1:]`.
3. Base case: an empty list has one permutation: [[]].
4. Combine: for each `rest` in permutations(remaining), produce
   `[chosen] + rest`.
5. Backtracking alternative: keep a `current` list and a `used` set,
   append an unused number, recurse, then pop and un-mark it. Save a
   copy of `current` when it is full length.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Backtracking and recursion trees
- List slicing and concatenation
- Factorial growth and `math.factorial`
- Converting lists to tuples so they can go in a set
- Using the standard library (itertools) as a test oracle

========================================================================
STRETCH GOALS
========================================================================
- In a test, compare your result with
  `[list(p) for p in itertools.permutations(nums)]` (sorted).
- LeetCode #47 "Permutations II": allow duplicate values but return
  each distinct permutation only once.
- Write it as a generator that yields permutations one at a time.
- Make your result come out in lexicographic (sorted) order naturally
  when the input is sorted.
"""


def permutations(nums: list[int]) -> list[list[int]]:
    """Return every permutation (ordering) of the distinct ints in `nums`.

    Must be implemented recursively without itertools. The order of the
    permutations in the returned list is unspecified.

    Args:
        nums: A list of distinct integers. Not modified.

    Returns:
        A list of len(nums)! lists, each a distinct permutation.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
