"""
Challenge: Second Largest
Level:     03 - Lists
Topics:    tracking two values in one loop, distinct values, sets
Source:    Classic interview warm-up

========================================================================
YOUR TASK
========================================================================
Write `second_largest(nums)`. It returns the second largest DISTINCT
value in the list.

    second_largest([3, 1, 4, 1, 5, 9, 2, 6])  ->  6

========================================================================
WHAT "DISTINCT" MEANS
========================================================================
Distinct means "different". Extra copies of the largest value do not
count as the second largest:

    [5, 5, 3]
    distinct values:  5, 3
    largest:          5
    second largest:   3     (NOT the other 5)

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the largest value that is strictly smaller than the maximum.
2. Raise ValueError when the list has fewer than 2 distinct values:
   when it is empty, has one element, or every element is the same,
   like [7, 7, 7]. There is no second largest then.
3. Not change (mutate) `nums`. So no nums.sort(), which reorders the
   caller's list.

You can assume:
- `nums` is a list of ints and/or floats.

Aim for ONE pass (one loop) without sorting (see hints 2 to 4). A
sorting solution is a fine first step.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    second_largest([3, 1, 4, 1, 5, 9, 2, 6])  ->  6
        The largest is 9. The next one down is 6.

    second_largest([5, 5, 3])                 ->  3
        Both 5s are the same value, so the answer is 3.

    second_largest([-1, -2, -3])              ->  -2
        -1 is the largest, and -2 is next.

    second_largest([10, 20])                  ->  10
        Two distinct values: 20 is the largest, 10 is second.

    second_largest([7, 7, 7])                 ->  raises ValueError
        Only one distinct value (7), so there is no second largest.

========================================================================
EDGE CASES TO TEST
========================================================================
- A normal unsorted list: [3, 1, 4, 1, 5, 9, 2, 6] -> 6
- The largest value appears several times: [5, 5, 3] -> 3
- The second largest appears several times: [9, 4, 4] -> 4
- All negative numbers: [-1, -2, -3] -> -2
- Exactly two distinct values: [10, 20] -> 10
- Largest at the start vs at the end: [9, 1, 5] -> 5 and [1, 5, 9] -> 5
- [], [7] and [7, 7, 7] -> raises ValueError
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Simple approach: turn the list into a set (removes duplicates),
   check its size, then sort it and take the second-to-last element.
2. One-pass approach: keep two trackers, `largest` and `second`, both
   starting as None (meaning "no value yet").
3. For each number x:
     - If `largest` is None or x is bigger than largest: the old
       largest becomes second, and x becomes largest.
     - Else, if x is smaller than largest and (`second` is None or x
       is bigger than second): x becomes second.
     - If x equals largest, ignore it (it is a duplicate).
4. After the loop, if `second` is still None, raise ValueError.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Using None as "no value yet" and checking with `is None`
- Updating two related variables correctly (order matters!)
- `set()` to find distinct values
- `sorted()` returns a new list, while `list.sort()` changes the
  original

========================================================================
STRETCH GOALS
========================================================================
- Generalise: `kth_largest_distinct(nums, k)` (ValueError if k is out
  of range).
- Look at `heapq.nlargest` in the standard library and how it could
  help.
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
