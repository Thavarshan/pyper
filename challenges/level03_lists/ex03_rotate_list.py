"""
Challenge: Rotate a List
Level:     03 - Lists
Topics:    slicing, modulo, negative numbers, returning new lists
Source:    Based on the idea of LeetCode #189 "Rotate Array"

========================================================================
YOUR TASK
========================================================================
Write `rotate_right(nums, k)`. It takes the last `k` items of the list,
moves them to the front, and RETURNS the result as a brand-new list.

    rotate_right([1, 2, 3, 4, 5], 2)  ->  [4, 5, 1, 2, 3]

========================================================================
WHAT "ROTATE" MEANS
========================================================================
Picture the list as people standing in a circle. Rotating RIGHT by one
step means everybody moves one place to the right, and the person at
the end wraps around to the front:

    start:              [1, 2, 3, 4, 5]
    rotate right by 1:  [5, 1, 2, 3, 4]    (5 wrapped to the front)
    rotate right by 2:  [4, 5, 1, 2, 3]    (then 4 wrapped too)

Two things follow from the circle picture:

    - Rotating 5 items by 5 steps brings everyone back to where they
      started. So for a list of 5, rotating by 7 is the same as
      rotating by 2 (7 = 5 + 2).
    - Rotating by a NEGATIVE number goes the other way (to the LEFT):
      rotating by -1 moves the FIRST item to the end.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a NEW list. Do not change (mutate) `nums` itself; after the
   call, the caller's list must look exactly as it did before.
2. Rotate right by `k` steps when `k` is positive.
3. Rotate LEFT by `abs(k)` steps when `k` is negative.
4. Handle any size of `k`, including one bigger than the list
   (wrap around, as described above).
5. When `k` is 0, return an unchanged copy (still a new list).
6. When `nums` is empty, return [] whatever `k` is.

You can assume:
- `nums` is a list. Its items can be of any type.
- `k` is an int (positive, negative or zero, any size).

Note: LeetCode #189 changes the list "in place" (it edits the original
list instead of making a new one). This version returns a new list; an
in-place version is a stretch goal.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    rotate_right([1, 2, 3, 4, 5], 2)   ->  [4, 5, 1, 2, 3]
        The last 2 items (4, 5) move to the front.

    rotate_right([1, 2, 3], 4)         ->  [3, 1, 2]
        4 steps on a list of 3 is a full lap plus 1 step, so it's the
        same as rotating by 1.

    rotate_right([1, 2, 3, 4, 5], -1)  ->  [2, 3, 4, 5, 1]
        Negative, so rotate LEFT by 1: the first item moves to the end.

    rotate_right([], 3)                ->  []
        Nothing to rotate.

========================================================================
EDGE CASES TO TEST
========================================================================
- k = 0              -> same order, but a NEW list
                        (check `result is not nums`)
- k = len(nums)      -> same order (one full lap)
- k bigger than the list, e.g. 7 on 5 items -> same as k = 2
- Negative k, e.g. -1 on [1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1]
- Very negative k, e.g. -7 on 5 items -> same as k = -2
- Empty list with any k -> [] (and no crash: see hint 3)
- A one-item list    -> the same single item
- The original list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Try it on paper first: rotating right by 2 means "the LAST 2 items,
   followed by everything else".
2. Slicing gets you both pieces: nums[-2:] is the last 2 items and
   nums[:-2] is everything before them. Join them with `+`.
3. Shrink k first with `k % len(nums)` ("the remainder after dividing
   by the length"). This handles big k AND negative k, because in
   Python `%` by a positive number always gives 0 up to len-1:
   -1 % 5 == 4 (and rotating left by 1 IS rotating right by 4).
   But `% 0` crashes with ZeroDivisionError, so deal with the empty
   list before you get here.
4. Wondering about k % n == 0? -0 is just 0, so nums[-0:] is the WHOLE
   list and nums[:-0] is EMPTY. Joined, they give the whole list back,
   which is the right answer. Add a test to prove it to yourself.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Slicing with negative indexes: nums[-2:], nums[:-2]
- How `%` (modulo, the remainder) works with negative numbers
- Avoiding division/modulo by zero
- Joining lists with `+` (which builds a new list)
- Copying a list: nums[:] or list(nums)

========================================================================
STRETCH GOALS
========================================================================
- Solve it without slicing: work out each item's new position with
  result[(i + k) % n] = nums[i].
- Write `rotate_right_in_place(nums, k) -> None`, which changes the
  list itself instead of returning a new one (the LeetCode #189
  version). Look up the "reverse three times" trick.
- Look at `collections.deque.rotate()` in the standard library.
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
