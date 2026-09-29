"""
Challenge: Find Minimum in a Rotated Sorted Array
Level:     09 - Searching and Sorting
Topics:    binary search on a condition, reasoning about sorted halves
Source:    LeetCode #153 "Find Minimum in Rotated Sorted Array"

========================================================================
PROBLEM
========================================================================
Start with a list of DISTINCT numbers sorted in ascending order, e.g.
[0, 1, 2, 4, 5, 6, 7]. ROTATING it means taking some number of items
off the front and moving them to the back (keeping their order):

    rotate by 0: [0, 1, 2, 4, 5, 6, 7]   (unchanged)
    rotate by 3: [4, 5, 6, 7, 0, 1, 2]
    rotate by 6: [7, 0, 1, 2, 4, 5, 6]

A rotated list is made of two ascending "runs", and the smallest value
sits right where the second run starts (at the "drop").

Write `find_min(nums)` that returns the SMALLEST value in such a list.
You must do it in O(log n) time - so not with min() or a loop over
every item. Binary search works even though the list isn't fully
sorted, because at every step you can tell which half the minimum is
in.

The key observation: compare the middle item with the LAST item.
    - If nums[mid] > nums[high], the drop (and the minimum) is somewhere
      to the RIGHT of mid.
    - Otherwise the stretch from mid to high is sorted, so the minimum
      is at mid or to its LEFT.

========================================================================
EXAMPLES
========================================================================
    >>> find_min([3, 4, 5, 1, 2])
    1

    >>> find_min([4, 5, 6, 7, 0, 1, 2])
    0

    >>> find_min([11, 13, 15, 17])
    11

    >>> find_min([42])
    42

========================================================================
CONSTRAINTS
========================================================================
- 1 <= len(nums) <= 5000 for valid input; values distinct; the list is
  an ascending list rotated by 0..len(nums)-1 positions.
- Empty list -> raise ValueError (there is no minimum).
- Do not use min(), sorted() or a full linear scan in the solution.
  Use min() in TESTS as the reference answer.
- Do not modify `nums`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(log n)
- Space: O(1)

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> ValueError
- One element
- Two elements, rotated and not: [1, 2] and [2, 1]
- Not rotated at all (already sorted)
- Rotated by one position (min at index 1) and by n-1 positions
  (min at the last index)
- Negative numbers
- EVERY rotation of a sample list: for k in range(n), test
  find_min(base[k:] + base[:k]) == min(base)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Use `low = 0`, `high = len(nums) - 1` and loop `while low < high`
   (strictly less - you stop when one candidate is left).
2. `mid = (low + high) // 2`.
3. If nums[mid] > nums[high]: `low = mid + 1` (mid can't be the min).
   Else: `high = mid` (mid MIGHT be the min, so keep it - don't use
   mid - 1).
4. When the loop ends, low == high and nums[low] is the minimum.
5. Why compare with nums[high] instead of nums[low]? Try both on an
   unrotated list and see which one breaks.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Binary search on a condition instead of an exact value
- Choosing `high = mid` vs `high = mid - 1` (which candidates can be
  safely discarded?)
- Generating many test cases with slicing (rotations)
- Raising ValueError for input that has no answer

========================================================================
STRETCH GOALS
========================================================================
- Also return the ROTATION COUNT (the index of the minimum).
- LeetCode #33 "Search in Rotated Sorted Array": find a target in
  O(log n).
- LeetCode #154: allow duplicates. What happens to the worst case?
"""


def find_min(nums: list[int]) -> int:
    """Return the smallest value in a rotated ascending list.

    Args:
        nums: Distinct ints forming an ascending list rotated by some
            number of positions. Not modified.

    Returns:
        The minimum value.

    Raises:
        ValueError: If `nums` is empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
