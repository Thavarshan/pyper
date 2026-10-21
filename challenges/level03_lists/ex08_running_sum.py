"""
Challenge: Running Sum
Level:     03 - Lists
Topics:    accumulators, building new lists, prefix sums
Source:    LeetCode #1480 "Running Sum of 1d Array"

========================================================================
YOUR TASK
========================================================================
Write `running_sum(nums)`. It returns a NEW list where each position
holds the total of all the numbers up to and including that position.

    running_sum([1, 2, 3, 4])  ->  [1, 3, 6, 10]

========================================================================
WHAT A "RUNNING SUM" IS
========================================================================
The RUNNING SUM (also called a cumulative sum or PREFIX SUM) keeps a
total as you walk along the list, and writes the total down at every
step:

    nums        = [1,   2,     3,       4]
    running sum = [1, 1+2, 1+2+3, 1+2+3+4]
                = [1,   3,     6,      10]

Prefix sums are a powerful tool you'll meet again later. Once you have
them, you can find the sum of any slice nums[i:j] with one subtraction.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a NEW list with the same length as `nums`.
2. Make element i of the result equal to
   nums[0] + nums[1] + ... + nums[i].
3. Not change (mutate) `nums`.
4. Work in a single pass (one loop). Don't recompute
   sum(nums[:i + 1]) for every position.

You can assume:
- `nums` is a list of ints and/or floats. It may be empty.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    running_sum([1, 2, 3, 4])     ->  [1, 3, 6, 10]
        1, then 1+2, then 1+2+3, then 1+2+3+4.

    running_sum([1, 1, 1, 1, 1])  ->  [1, 2, 3, 4, 5]
        Adding 1 each time just counts up.

    running_sum([3, -1, 0, 2])    ->  [3, 2, 2, 4]
        The -1 brings the total down. Adding 0 leaves it the same.

    running_sum([])               ->  []
        No numbers, so no totals.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: running_sum([]) -> []
- A single element: running_sum([5]) -> [5]
- Negative numbers and zeros: running_sum([3, -1, 0, 2]) -> [3, 2, 2, 4]
- The last element equals sum(nums): running_sum([1, 2, 3, 4])[-1]
  -> 10
- Floats: running_sum([0.1, 0.2]) -> [0.1, 0.3], compared with
  pytest.approx (float maths isn't exact: 0.1 + 0.2 gives
  0.30000000000000004)
- The input list is unchanged and the result is a different object
  (`result is not nums`)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Keep a variable `total = 0`. For each number, add it to total, then
   append total to the result list.
2. Why not `sum(nums[:i + 1])` in a loop? It re-adds everything from
   the start each time, so it gets much slower as the list grows.
3. Check out `itertools.accumulate` AFTER solving it with a loop.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The accumulator pattern (a variable that builds up a result as you
  loop), here producing a list
- Why repeated work in a loop is slow (a first taste of complexity)
- `itertools.accumulate`
- Prefix sums as a technique

========================================================================
STRETCH GOALS
========================================================================
- Write `range_sum(prefix, i, j)`, which uses a running-sum list to
  return sum(nums[i:j]) in constant time (the same small amount of
  work, however long the list is). Hint: it's easier if the prefix
  list starts with an extra 0.
- Write `running_sum_in_place(nums) -> None`, which overwrites nums
  instead of returning a new list (the way LeetCode's version is often
  solved).
- Write `running_max(nums)`: each position holds the largest value seen
  so far.
"""


def running_sum(nums: list[float]) -> list[float]:
    """Return the running (cumulative) sum of `nums` as a new list.

    Args:
        nums: A list of numbers. It is not modified.

    Returns:
        A list of the same length where element i is
        nums[0] + nums[1] + ... + nums[i].
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
