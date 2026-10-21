"""
Challenge: Find Minimum in a Rotated Sorted Array
Level:     09 - Searching and Sorting
Topics:    binary search on a condition, reasoning about sorted halves
Source:    LeetCode #153 "Find Minimum in Rotated Sorted Array"

========================================================================
YOUR TASK
========================================================================
Write `find_min(nums)`. `nums` is a sorted list that has been
"rotated" (explained below). Return the SMALLEST value in it, using
binary search.

    find_min([3, 4, 5, 1, 2])  ->  1

========================================================================
WHAT A "ROTATED" SORTED LIST IS
========================================================================
Start with a list of different numbers sorted in ascending order, like
[0, 1, 2, 4, 5, 6, 7]. ROTATING it means taking some items off the
front and moving them to the back, keeping their order:

    rotate by 0: [0, 1, 2, 4, 5, 6, 7]   (unchanged)
    rotate by 3: [4, 5, 6, 7, 0, 1, 2]   (0, 1, 2 moved to the back)
    rotate by 6: [7, 0, 1, 2, 4, 5, 6]

A rotated list is made of two ascending "runs". The smallest value
sits right where the second run starts, at the "drop":

    [4, 5, 6, 7, 0, 1, 2]
                ^ the drop: 7 then 0. The minimum is 0.

========================================================================
WHY BINARY SEARCH STILL WORKS
========================================================================
The list isn't fully sorted, but at every step you can still tell
which half holds the minimum. Compare the middle item with the LAST
item of the range you are searching (nums[high]):

    - If nums[mid] > nums[high], the drop (and so the minimum) is
      somewhere to the RIGHT of mid.
    - Otherwise the stretch from mid to high is sorted, so the minimum
      is at mid or to its LEFT.

Each step throws away about half of the range.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the smallest value in `nums`.
2. Run in O(log n) time (halving the range each step). So do not use
   min(), sorted() or a loop over every item. Use min() in your TESTS
   as the reference answer.
3. Raise ValueError when `nums` is empty (there is no minimum).
4. Not change (mutate) `nums`.

You can assume:
- Apart from the empty case, 1 <= len(nums) <= 5000.
- All values are different.
- `nums` is an ascending list rotated by 0 to len(nums) - 1 positions.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    find_min([3, 4, 5, 1, 2])        ->  1
        The drop is between 5 and 1.

    find_min([4, 5, 6, 7, 0, 1, 2])  ->  0
        The drop is between 7 and 0.

    find_min([11, 13, 15, 17])       ->  11
        Not rotated at all, so the first item is the smallest.

    find_min([42])                   ->  42
        Only one item.

    find_min([])                     ->  raises ValueError
        An empty list has no minimum.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(log n): each step halves the range, so 5000 items need only
  about 13 steps.
- Space: O(1): only a few variables.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: find_min([]) -> raises ValueError
- One element: find_min([42]) -> 42
- Two elements, not rotated: find_min([1, 2]) -> 1
- Two elements, rotated: find_min([2, 1]) -> 1
- Not rotated at all: find_min([11, 13, 15, 17]) -> 11
- Rotated by n-1 positions, min at index 1:
  find_min([7, 0, 1, 2, 4, 5, 6]) -> 0
- Rotated by one position, min at the last index:
  find_min([1, 2, 4, 5, 6, 7, 0]) -> 0
- Negative numbers: find_min([3, -5, -2, 0]) -> -5
- EVERY rotation of a sample list: for k in range(n), test
  find_min(base[k:] + base[:k]) == min(base)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Use `low = 0`, `high = len(nums) - 1` and loop `while low < high`.
   It's strictly less, because you stop when one candidate is left.
2. `mid = (low + high) // 2`.
3. If nums[mid] > nums[high]: `low = mid + 1` (mid can't be the min).
   Else: `high = mid`. mid MIGHT be the min, so keep it. Don't use
   mid - 1.
4. When the loop ends, low == high, and nums[low] is the minimum.
5. Why compare with nums[high] instead of nums[low]? Try both on an
   unrotated list and see which one breaks.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Binary search on a condition instead of an exact value
- Choosing `high = mid` vs `high = mid - 1` (which candidates can be
  safely thrown away?)
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
