"""
Challenge: Search Insert Position
Level:     09 - Searching and Sorting
Topics:    binary search variant, lower bound, loop invariants
Source:    LeetCode #35 "Search Insert Position"

========================================================================
YOUR TASK
========================================================================
Write `search_insert(nums, target)`. `nums` is a sorted list. If
`target` is in it, return its index. If not, return the index where it
WOULD go if you inserted it and kept the list sorted.

    search_insert([1, 3, 5, 6], 2)  ->  1

========================================================================
WHAT THE ANSWER MEANS
========================================================================
Another way to say it: return the index of the first item that is
GREATER THAN OR EQUAL TO `target`. If every item is smaller, return
len(nums). This position is often called the "lower bound".

    nums:     [1, 3, 5, 6]
    index:     0  1  2  3   4
    target 5 -> 2   (5 is there, at index 2)
    target 2 -> 1   (2 would go between 1 and 3)
    target 7 -> 4   (bigger than everything: goes at the end)

So after `nums.insert(result, target)`, the list would still be
sorted.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the index of the first item >= `target`, or len(nums) if
   every item is smaller. The result is always between 0 and
   len(nums), both included.
2. Use binary search, which is O(log n) (it halves the range each
   step), not a linear scan that checks every item.
3. Not change (mutate) `nums`.
4. Not use the `bisect` module, `list.index` or `in` in the solution.
   You can use `bisect.bisect_left` in your TESTS as a reference: it
   computes exactly this answer.

You can assume:
- `nums` is sorted ascending and all its values are different.
- 0 <= len(nums) <= 10**4.
- -10**4 <= nums[i], target <= 10**4.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    search_insert([1, 3, 5, 6], 5)  ->  2
        5 is in the list, at index 2.

    search_insert([1, 3, 5, 6], 2)  ->  1
        2 is missing. It belongs between 1 and 3, at index 1.

    search_insert([1, 3, 5, 6], 7)  ->  4
        7 is bigger than everything, so it goes at the end:
        len(nums) is 4.

    search_insert([1, 3, 5, 6], 0)  ->  0
        0 is smaller than everything, so it goes at the front.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(log n): each step halves the range, so 10_000 items need
  only about 14 steps.
- Space: O(1): only a few variables.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: search_insert([], 5) -> 0
- Target smaller than everything -> 0
- Target larger than everything -> len(nums)
- Target equal to the first item: search_insert([1, 3, 5], 1) -> 0
- Target equal to the last item: search_insert([1, 3, 5], 5) -> 2
- Target between two items: search_insert([1, 3, 5], 4) -> 2
- Single-item list [5]: target 3 -> 0, target 5 -> 0, target 8 -> 1
- Negative numbers: search_insert([-5, -2, 0], -3) -> 1
- Random sorted lists vs bisect.bisect_left (fixed random seed)
- Property: inserting `target` at the returned index keeps the list
  sorted

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with the binary search from ex02. What are `low` and `high`
   when the loop ends without finding the target?
2. With `low = 0, high = len(nums) - 1` and `while low <= high`, if
   the target is missing, `low` ends up exactly at the insert
   position.
3. Alternative "half-open" style: `low = 0, high = len(nums)`,
   `while low < high`: if nums[mid] < target then low = mid + 1, else
   high = mid. Return low. Notice that high starts at len(nums), not
   len(nums) - 1.
4. Trace the loop on paper for [1, 3] with targets 0, 2 and 4. The
   answers should be 0, 1 and 2.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Binary search variations (lower bound / upper bound)
- Inclusive vs half-open ranges: [low, high] includes high,
  [low, high) stops just before it
- Loop invariants (facts that stay true on every pass of a loop)
- The `bisect` module as a reference implementation

========================================================================
STRETCH GOALS
========================================================================
- Allow duplicates and return the FIRST valid index (still the lower
  bound).
- Write `upper_bound(nums, target)`: the first index with a value
  > target (the same as bisect.bisect_right).
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
