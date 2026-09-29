"""
Challenge: Search Insert Position
Level:     09 - Searching and Sorting
Topics:    binary search variant, lower bound, loop invariants
Source:    LeetCode #35 "Search Insert Position"

========================================================================
PROBLEM
========================================================================
You're given a list of DISTINCT integers sorted in ascending order and
a `target` value.

    - If `target` is in the list, return its index.
    - If it is not, return the index where it WOULD go if you inserted
      it so the list stayed sorted.

In other words: return the index of the first element that is
GREATER THAN OR EQUAL TO `target`, or len(nums) if every element is
smaller. (This position is often called the "lower bound".)

After `nums.insert(result, target)` the list would still be sorted.

You must use binary search - O(log n) - not a linear scan.

========================================================================
EXAMPLES
========================================================================
    >>> search_insert([1, 3, 5, 6], 5)
    2

    >>> search_insert([1, 3, 5, 6], 2)
    1

    >>> search_insert([1, 3, 5, 6], 7)
    4

    >>> search_insert([1, 3, 5, 6], 0)
    0

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(nums) <= 10**4, sorted ascending, all values distinct.
- -10**4 <= nums[i], target <= 10**4
- The result is always in the range 0..len(nums) (inclusive).
- Do not use the `bisect` module, `list.index` or `in` in the
  solution. You can use `bisect.bisect_left` in TESTS as a reference -
  it computes exactly this answer.
- Do not modify `nums`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(log n)
- Space: O(1)

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> 0
- Target smaller than everything -> 0
- Target larger than everything -> len(nums)
- Target equal to the first / last element
- Target between two elements
- Single-element list: less, equal, greater
- Negative numbers
- Random sorted lists vs bisect.bisect_left (fixed seed)
- Property: inserting at the returned index keeps the list sorted

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with the binary search from ex02. What are `low` and `high`
   when the loop ends without finding the target?
2. With `low = 0, high = len(nums) - 1` and `while low <= high`, if the
   target is missing, `low` ends up exactly at the insert position.
3. Alternative "half-open" style: `low = 0, high = len(nums)`,
   `while low < high`: if nums[mid] < target then low = mid + 1 else
   high = mid. Return low. Notice high starts at len(nums), not
   len(nums) - 1.
4. Trace the loop on paper for [1, 3] with targets 0, 2 and 4.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Binary search variations (lower bound / upper bound)
- Inclusive vs half-open ranges ([low, high] vs [low, high))
- Loop invariants
- The `bisect` module as a reference implementation

========================================================================
STRETCH GOALS
========================================================================
- Allow duplicates and return the FIRST valid index (still lower bound).
- Write `upper_bound(nums, target)`: first index with value > target
  (same as bisect.bisect_right).
- LeetCode #34 "Find First and Last Position of Element in Sorted
  Array" using lower and upper bound.
"""


def search_insert(nums: list[int], target: int) -> int:
    """Return the index of `target`, or where it would be inserted.

    Args:
        nums: Distinct ints sorted in ascending order. Not modified.
        target: The value to find or place.

    Returns:
        The index of the first element >= target, or len(nums) if all
        elements are smaller.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
