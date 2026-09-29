"""
Challenge: Second Largest
Level:     03 - Lists
Topics:    tracking two values in one loop, distinct values, sets
Source:    Classic interview warm-up

========================================================================
PROBLEM
========================================================================
Write `second_largest(nums)` that returns the second largest DISTINCT
value in the list.

"Distinct" means duplicates of the largest value do not count as the
second largest. In [5, 5, 3], the largest is 5 and the second largest is
3 (NOT 5).

If the list has fewer than 2 distinct values - it is empty, has one
element, or every element is the same, like [7, 7, 7] - there is no
second largest, so raise ValueError.

========================================================================
EXAMPLES
========================================================================
    >>> second_largest([3, 1, 4, 1, 5, 9, 2, 6])
    6

    >>> second_largest([5, 5, 3])
    3

    >>> second_largest([-1, -2, -3])
    -2

    >>> second_largest([10, 20])
    10

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of ints and/or floats.
- Fewer than 2 distinct values -> raise ValueError.
- Do not modify the input list (so no nums.sort()!).
- Try to solve it in ONE pass without sorting (see hints); a sorting
  solution is a fine first step.

========================================================================
EDGE CASES TO TEST
========================================================================
- A normal unsorted list
- The largest value appears several times ([5, 5, 3] -> 3)
- The second largest appears several times ([9, 4, 4] -> 4)
- All negative numbers
- Exactly two distinct values
- Largest at the start vs at the end of the list
- [], [7], [7, 7, 7] -> ValueError
- The input list is unchanged

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Simple approach: turn the list into a set (removes duplicates), check
   its size, then sort it and take the second-to-last element.
2. One-pass approach: keep two trackers, `largest` and `second`, both
   starting as None.
3. For each number x:
     - if x is bigger than largest: the old largest becomes second, and
       x becomes largest;
     - else if x is smaller than largest but bigger than second: x
       becomes second;
     - if x equals largest, ignore it (it is a duplicate).
4. After the loop, if `second` is still None, raise ValueError.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Using None as "no value yet" and checking with `is None`
- Updating two related variables correctly (order matters!)
- `set()` to find distinct values
- `sorted()` returns a new list; `list.sort()` changes the original

========================================================================
STRETCH GOALS
========================================================================
- Generalise: `kth_largest_distinct(nums, k)` (ValueError if k is out of
  range).
- Look at `heapq.nlargest` in the stdlib and how it could help.
"""


def second_largest(nums: list[float]) -> float:
    """Return the second largest distinct value in `nums`.

    Args:
        nums: A list of numbers. It is not modified.

    Returns:
        The largest value that is strictly smaller than the maximum.

    Raises:
        ValueError: If `nums` contains fewer than 2 distinct values.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
