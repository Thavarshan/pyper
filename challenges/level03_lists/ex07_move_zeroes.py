"""
Challenge: Move Zeroes
Level:     03 - Lists
Topics:    in-place mutation, returning None, two pointers, swapping
Source:    LeetCode #283 "Move Zeroes"

========================================================================
PROBLEM
========================================================================
Write `move_zeroes(nums)` that moves every 0 in the list to the END,
while keeping all the non-zero numbers in their original relative order.

    [0, 1, 0, 3, 12]  becomes  [1, 3, 12, 0, 0]

IMPORTANT - this function works IN PLACE:
    - It must change the list it was given (it "mutates" it).
    - It must NOT create and return a new list. It returns None.
    - It is fine to use a few extra variables, but not a second list.

"In place" matters because the caller keeps using THEIR list object:

    data = [0, 1, 0, 3, 12]
    move_zeroes(data)        # returns None
    print(data)              # [1, 3, 12, 0, 0]

A test therefore calls the function and then checks the ORIGINAL list.

========================================================================
EXAMPLES
========================================================================
    >>> nums = [0, 1, 0, 3, 12]
    >>> move_zeroes(nums)
    >>> nums
    [1, 3, 12, 0, 0]

    >>> nums = [0]
    >>> move_zeroes(nums)
    >>> nums
    [0]

    >>> nums = [4, 2, 0, -1]
    >>> move_zeroes(nums)
    >>> nums
    [4, 2, -1, 0]

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of ints, 0 <= len(nums) <= 10_000.
- Modify `nums` in place; return None.
- Do not build a second list (so no `nums[:] = [...]` shortcuts in your
  final solution - try them as a first step if you like).
- The relative order of the non-zero values must not change.
- The length of the list must not change.

========================================================================
EDGE CASES TO TEST
========================================================================
- The LeetCode example [0, 1, 0, 3, 12]
- No zeroes -> list unchanged
- All zeroes -> list unchanged
- Zeroes already at the end -> unchanged
- Empty list -> still empty, no error
- Negative numbers are kept in order
- The function returns None (`assert move_zeroes(x) is None`)
- It is the SAME list object afterwards (save id(nums) or use `is`)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Think of a "write" position, starting at 0: the place where the next
   non-zero number should go.
2. Loop over the list with a "read" index. Every time you read a
   non-zero value, put it at the write position and move write forward.
3. After the loop, every index from `write` to the end should be 0.
4. A cleverer single pass: instead of copying, SWAP nums[read] and
   nums[write] - Python can swap in one line: a[i], a[j] = a[j], a[i].
5. Avoid calling nums.remove(0) / nums.append(0) inside a loop over
   nums - modifying a list while iterating over it skips elements.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Mutating a list vs creating a new one
- Functions that return None (a Python convention for in-place
  operations, like list.sort() and list.reverse())
- Assigning to indexes: nums[i] = value
- Tuple-swap: a, b = b, a
- The read/write two-pointer technique
- The danger of changing a list while looping over it

========================================================================
STRETCH GOALS
========================================================================
- Minimise the number of writes to the list.
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
