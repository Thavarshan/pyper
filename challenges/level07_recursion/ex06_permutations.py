"""
Challenge: All Permutations
Level:     07 - Recursion
Topics:    recursion, backtracking, factorial growth, list slicing
Source:    LeetCode #46 "Permutations"

========================================================================
YOUR TASK
========================================================================
Write `permutations(nums)`. It RETURNS a list of every possible ordering
of the items in `nums`, each ordering being a list. Write it recursively
(the function, or a helper inside it, calls itself). The order of the
orderings in the outer list does not matter.

    permutations([1, 2])  ->  [[1, 2], [2, 1]]   (in any order)

========================================================================
WHAT A "PERMUTATION" IS
========================================================================
A PERMUTATION is one possible ordering (arrangement) of a collection's
items, using every item exactly once. For [1, 2, 3] there are six:

    [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]

A list of n distinct items has n! ("n factorial") permutations, which
is n * (n-1) * ... * 2 * 1. There are n choices for the first place,
n-1 left for the second, and so on. For 3 items: 3 * 2 * 1 = 6. This
grows VERY quickly: 10! = 3,628,800.

One way to picture it, for [1, 2, 3]: pick who goes first, then
arrange the rest.

    first 1, then arrange [2, 3]  ->  [1, 2, 3], [1, 3, 2]
    first 2, then arrange [1, 3]  ->  [2, 1, 3], [2, 3, 1]
    first 3, then arrange [1, 2]  ->  [3, 1, 2], [3, 2, 1]

"Arrange the rest" is the same problem on a smaller list, so it is a
recursive call.

ORDER: the order of the permutations in the outer list does not
matter. The order INSIDE each permutation is the whole point, so never
sort inside. To test, sort only the outer list, on both sides:

    assert sorted(permutations([1, 2])) == sorted([[1, 2], [2, 1]])

========================================================================
THE RULES
========================================================================
Your function must:
1. Return every permutation of `nums`, each exactly once.
2. Return a `list` of `list`s. Each inner list is a separate object.
3. Return [[]] for an empty input. There is exactly one way to arrange
   zero items (the empty arrangement), which matches 0! == 1.
4. Not modify (mutate) `nums`. If you swap items in place while
   working, put them back before returning.
5. Be recursive. Do NOT use `itertools.permutations` (or any other
   itertools function) in your solution. You MAY use it in your tests.

You can assume:
- 0 <= len(nums) <= 8
- Every number is between -10 and 10, and all the numbers are DISTINCT
  (no duplicates).

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    sorted(permutations([1, 2, 3]))
        ->  [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2],
             [3, 2, 1]]
        3! = 6 orderings. Sorted here only so the order is fixed.

    permutations([7])  ->  [[7]]
        One item can only be arranged one way.

    permutations([])   ->  [[]]
        One arrangement: the empty one.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n * n!). There are n! permutations and each one is n items
  long to build. Going from 8 items to 9 makes about 10 times the work.
- Space: O(n) for the call stack. One waiting call per position at the
  deepest point. The output itself is O(n * n!).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: permutations([]) -> [[]]
- One item: permutations([7]) -> [[7]]
- Two items: sorted(permutations([1, 2])) -> [[1, 2], [2, 1]]
- len(result) == math.factorial(len(nums)) for sizes 0..6
- No duplicate permutations: turn each into a tuple and put them in a
  set. The set's size equals len(result).
- Every permutation holds exactly the same items as nums:
  sorted(p) == sorted(nums) for every p
- The input list is unchanged afterwards
- Negative numbers work: sorted(permutations([-1, 2]))
  -> [[-1, 2], [2, -1]]

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Pick each item in turn to go FIRST. For each choice, the rest of the
   permutation is any permutation of the remaining items.
2. The "remaining items" when you pick index i are
   `nums[:i] + nums[i+1:]`.
3. Base case: an empty list has one permutation, so return [[]].
4. Combine: for each `rest` in permutations(remaining), produce
   `[chosen] + rest`.
5. Backtracking alternative (choose, explore, un-choose): keep a
   `current` list and a `used` set. Append an unused number, mark it
   used, recurse, then pop it and un-mark it. Save a COPY of `current`
   when it is full length.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Backtracking and recursion trees
- List slicing and concatenation
- Factorial growth and `math.factorial`
- Turning lists into tuples so they can go in a set (lists can't,
  because they can change)
- Using the standard library (itertools) as a test oracle (a trusted
  source of right answers)

========================================================================
STRETCH GOALS
========================================================================
- In a test, compare your result with
  `[list(p) for p in itertools.permutations(nums)]` (both sorted).
- LeetCode #47 "Permutations II": allow duplicate values but return
  each distinct permutation only once.
- Write it as a generator (a function that uses `yield`) that hands out
  permutations one at a time.
- Make your result come out in lexicographic (dictionary, sorted) order
  naturally when the input is sorted.
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
