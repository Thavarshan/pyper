"""
Challenge: Rotate a List
Level:     03 - Lists
Topics:    slicing, modulo, negative numbers, returning new lists
Source:    Based on the idea of LeetCode #189 "Rotate Array"

========================================================================
PROBLEM
========================================================================
ROTATING a list to the right by one step moves the last element to the
front, and shifts every other element one place to the right:

    [1, 2, 3, 4, 5]  -- rotate right by 1 -->  [5, 1, 2, 3, 4]
    [1, 2, 3, 4, 5]  -- rotate right by 2 -->  [4, 5, 1, 2, 3]

Write `rotate_right(nums, k)` that returns a NEW list which is `nums`
rotated right by `k` steps. The original list must not be changed.

    - `k` may be larger than the length of the list. Rotating a list of
      length 5 by 5 steps gives back the same order, so rotating by 7 is
      the same as rotating by 2.
    - A NEGATIVE `k` rotates to the LEFT: rotate_right([1, 2, 3, 4, 5], -1)
      gives [2, 3, 4, 5, 1].
    - k = 0 returns an unchanged copy.

(Unlike LeetCode #189, which rotates in place, this version returns a
new list. An in-place version is a stretch goal.)

========================================================================
EXAMPLES
========================================================================
    >>> rotate_right([1, 2, 3, 4, 5], 2)
    [4, 5, 1, 2, 3]

    >>> rotate_right([1, 2, 3], 4)
    [3, 1, 2]

    >>> rotate_right([1, 2, 3, 4, 5], -1)
    [2, 3, 4, 5, 1]

    >>> rotate_right([], 3)
    []

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of any values; `k` is an int (any size, any sign).
- An empty list returns [] for any k (careful: you can't do k % 0!).
- Return a new list (even when k is 0); do not modify `nums`.

========================================================================
EDGE CASES TO TEST
========================================================================
- k = 0 -> same order, but a new list object
- k = len(nums) -> same order
- k > len(nums), e.g. k = len + 2
- Negative k (rotate left), and very negative k (e.g. -7 on 5 items)
- Empty list with any k (no ZeroDivisionError!)
- Single-element list
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Try it by hand: rotating right by 2 means the LAST 2 elements move to
   the front, and the rest follow.
2. With slicing: nums[-2:] is the last 2 elements, nums[:-2] is the rest.
3. Reduce k first with k % len(nums). In Python, % with a positive
   divisor always gives a result from 0 to len-1, even for negative k:
   -1 % 5 == 4 (and rotating left by 1 equals rotating right by 4!).
4. Watch out for k % n == 0: nums[-0:] is the WHOLE list, not an empty
   one, because -0 == 0.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Slicing with negative indexes
- `%` with negative numbers in Python
- Guarding against division/modulo by zero
- Concatenating lists with `+` (which creates a new list)
- Copying a list: nums[:] or list(nums)

========================================================================
STRETCH GOALS
========================================================================
- Solve it without slicing, by computing each element's new index:
  result[(i + k) % n] = nums[i].
- Write `rotate_right_in_place(nums, k) -> None` that modifies the list
  itself (the LeetCode #189 version). Research the "reverse three
  times" trick.
- Look at `collections.deque.rotate()` in the stdlib.
"""

from typing import TypeVar

T = TypeVar("T")


def rotate_right(nums: list[T], k: int) -> list[T]:
    """Return a new list equal to `nums` rotated right by `k` steps.

    Args:
        nums: The list to rotate. It is not modified.
        k: Number of steps to the right. Negative values rotate left;
            values larger than len(nums) wrap around.

    Returns:
        A new, rotated list ([] if `nums` is empty).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
