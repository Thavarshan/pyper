"""
Challenge: Running Sum
Level:     03 - Lists
Topics:    accumulators, building new lists, prefix sums
Source:    LeetCode #1480 "Running Sum of 1d Array"

========================================================================
PROBLEM
========================================================================
The RUNNING SUM (also called a cumulative sum or PREFIX SUM) of a list
is a new list where each position holds the total of all the elements
up to and including that position in the original list:

    nums        = [1, 2, 3, 4]
    running sum = [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10]

Write `running_sum(nums)` that returns the running sum as a NEW list.
The input list must not be changed.

Prefix sums are a powerful tool you'll meet again later: once you have
them, you can find the sum of any slice nums[i:j] with one subtraction.

========================================================================
EXAMPLES
========================================================================
    >>> running_sum([1, 2, 3, 4])
    [1, 3, 6, 10]

    >>> running_sum([1, 1, 1, 1, 1])
    [1, 2, 3, 4, 5]

    >>> running_sum([3, -1, 0, 2])
    [3, 2, 2, 4]

    >>> running_sum([])
    []

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of ints and/or floats (may be empty).
- Return a new list with the same length as `nums`.
- Do not modify `nums`.
- Do it in a single pass (one loop) - don't recompute sum(nums[:i+1])
  for every position.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> []
- A single element -> [that element]
- Negative numbers and zeros
- The last element equals sum(nums)
- Floats (compare with pytest.approx)
- The input list is unchanged and the result is a different object

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Keep a variable `total = 0`. For each number, add it to total, then
   append total to the result list.
2. Why not `sum(nums[:i + 1])` in a loop? It re-adds everything from the
   start each time, so it gets much slower as the list grows.
3. Check out `itertools.accumulate` AFTER solving it with a loop.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The accumulator pattern producing a list
- Why repeated work in a loop is slow (a first taste of complexity)
- `itertools.accumulate`
- Prefix sums as a technique

========================================================================
STRETCH GOALS
========================================================================
- Write `range_sum(prefix, i, j)` that uses a running-sum list to return
  sum(nums[i:j]) in constant time. (Hint: it's easier if the prefix list
  starts with an extra 0.)
- Write `running_sum_in_place(nums) -> None` that overwrites nums (the
  way LeetCode's version is often solved).
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
