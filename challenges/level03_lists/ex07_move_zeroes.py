"""
Challenge: Move Zeroes
Level:     03 - Lists
Topics:    in-place mutation, returning None, two pointers, swapping
Source:    LeetCode #283 "Move Zeroes"

========================================================================
YOUR TASK
========================================================================
Write `move_zeroes(nums)`. It moves every 0 in the list to the END and
keeps the non-zero numbers in their original order. It changes the
list it was given and returns None.

    [0, 1, 0, 3, 12]  becomes  [1, 3, 12, 0, 0]

========================================================================
WHAT "IN PLACE" MEANS
========================================================================
Most list functions so far returned a NEW list. This one works IN
PLACE: it changes (mutates) the caller's own list and returns None.
Python's list.sort() and list.reverse() work the same way.

This matters because the caller keeps using THEIR list object:

    data = [0, 1, 0, 3, 12]
    move_zeroes(data)        # returns None
    print(data)              # [1, 3, 12, 0, 0]

So a test calls the function and then checks the ORIGINAL list.

========================================================================
THE RULES
========================================================================
Your function must:
1. Change `nums` itself and return None. Do not create and return a
   new list.
2. Move every 0 to the end of the list.
3. Keep the non-zero values in their original relative order (the same
   order among themselves).
4. Keep the length of the list the same.
5. Not build a second list. A few extra variables are fine. This rules
   out `nums[:] = [...]` shortcuts in your final solution, but you may
   try one as a first step.

You can assume:
- `nums` is a list of ints with 0 to 10_000 elements.

========================================================================
EXAMPLES
========================================================================
Each example is a short script. The `# ->` comments show the value you
should get.

    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)        # -> None
    nums                     # -> [1, 3, 12, 0, 0]
        1, 3 and 12 keep their order. Both zeroes go to the end.

    nums = [0]
    move_zeroes(nums)
    nums                     # -> [0]
        A single 0 is already at the end.

    nums = [4, 2, 0, -1]
    move_zeroes(nums)
    nums                     # -> [4, 2, -1, 0]
        -1 is not zero, so it stays in order with 4 and 2.

========================================================================
EDGE CASES TO TEST
========================================================================
- The LeetCode example: [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
- No zeroes: [1, 2, 3] -> stays [1, 2, 3]
- All zeroes: [0, 0, 0] -> stays [0, 0, 0]
- Zeroes already at the end: [1, 0, 0] -> stays [1, 0, 0]
- Empty list: [] -> stays [], and no error
- Negative numbers keep their order: [-1, 0, -2] -> [-1, -2, 0]
- The function returns None: `assert move_zeroes(x) is None`
- It is the SAME list object afterwards (save id(nums) before the
  call, or keep a second name for it and check with `is`)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Think of a "write" position, starting at 0: the place where the
   next non-zero number should go.
2. Loop over the list with a "read" index. Every time you read a
   non-zero value, put it at the write position and move write
   forward.
3. After the loop, every index from `write` to the end should be 0.
4. A cleverer single pass: instead of copying, SWAP nums[read] and
   nums[write]. Python can swap in one line: a[i], a[j] = a[j], a[i].
5. Avoid calling nums.remove(0) inside a `for` loop over nums.
   Changing a list while you loop over it makes the loop skip
   elements: on [0, 0], that loop removes only one zero and leaves
   [0]. (Adding nums.append(0) after each remove happens to give the
   right answer, but only by luck, and every remove() searches the
   list from the start, so it is slow.)

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Mutating a list vs creating a new one
- Functions that return None (a Python convention for in-place
  operations, like list.sort() and list.reverse())
- Assigning to indexes: nums[i] = value
- Tuple swap: a, b = b, a
- The read/write two-pointer technique
- The danger of changing a list while looping over it

========================================================================
STRETCH GOALS
========================================================================
- Make as few writes to the list as possible.
- Generalise: `move_value_to_end(nums, value)`.
- LeetCode #27 "Remove Element" and #26 "Remove Duplicates from Sorted
  Array" use the same read/write pointer idea.
"""


def move_zeroes(nums: list[int]) -> None:
    """Move all zeroes in `nums` to the end, in place.

    Args:
        nums: The list to rearrange. It is modified in place; non-zero
            values keep their relative order.

    Returns:
        None. The caller's list is changed instead.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
