"""
Challenge: Binary Search
Level:     09 - Searching and Sorting
Topics:    binary search, low/high pointers, while loops, recursion
Source:    LeetCode #704 "Binary Search"

========================================================================
PROBLEM
========================================================================
BINARY SEARCH finds a value in a SORTED list by repeatedly halving the
part of the list that could still contain it - like looking up a word
in a paper dictionary: open in the middle, decide whether your word is
before or after, and throw away the other half.

    Search 7 in [1, 3, 5, 7, 9, 11]
    low=0, high=5 -> mid=2 -> 5 < 7  -> search right half: low=3
    low=3, high=5 -> mid=4 -> 9 > 7  -> search left half:  high=3
    low=3, high=3 -> mid=3 -> 7 == 7 -> found at index 3

Write two versions that behave identically:

    binary_search(nums, target)
        ITERATIVE (uses a while loop). Return the index of `target`
        in `nums`, or -1 if it isn't there.

    binary_search_recursive(nums, target, low=0, high=None)
        RECURSIVE. `low` and `high` are the inclusive bounds of the
        slice still being searched; callers normally omit them
        (high=None means "len(nums) - 1"). Same return value.

`nums` is sorted in ascending (increasing) order and has NO duplicates,
so the answer is unique.

========================================================================
EXAMPLES
========================================================================
    >>> binary_search([-1, 0, 3, 5, 9, 12], 9)
    4

    >>> binary_search([-1, 0, 3, 5, 9, 12], 2)
    -1

    >>> binary_search([], 1)
    -1

    >>> binary_search_recursive([1, 3, 5, 7], 1)
    0

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(nums) <= 10**5, sorted ascending, all values distinct.
- Do not use `list.index`, the `x in items` membership test, or the `bisect` module in your
  solution (you may use them in tests as a reference).
- Do NOT slice the list in the recursive version (nums[mid:] copies
  the data, which costs O(n)); pass `low`/`high` indices instead.
- Do not modify `nums`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(log n) - each step halves the search range.
- Space: iterative O(1); recursive O(log n) for the call stack.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> -1
- One element: found and not found
- Target is the first element / the last element
- Target smaller than everything / larger than everything -> -1
- Target that would fall between two elements -> -1
- Even and odd lengths
- A big list, e.g. list(range(0, 2_000_000, 2)), for several targets
- Both functions agree on every test (use @pytest.mark.parametrize
  with the function itself as a parameter!)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Keep two indices: `low = 0` and `high = len(nums) - 1`. Loop while
   `low <= high` (note the `<=` - with `<` you'd miss one-element
   ranges).
2. `mid = (low + high) // 2`.
3. If nums[mid] < target the answer must be to the right:
   `low = mid + 1`. If bigger: `high = mid - 1`. The +1 / -1 matter -
   without them the loop can run forever.
4. Recursive version: base case is `low > high` -> return -1.
   Otherwise compare with nums[mid] and recurse on one half.
5. Replace `high=None` at the start: `if high is None: high = len(nums) - 1`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- while loops with two pointers
- Integer division `//`
- Off-by-one errors and loop invariants ("if target exists, it is
  always between low and high")
- Default parameters with None as a sentinel
- Parametrizing tests over several implementations

========================================================================
STRETCH GOALS
========================================================================
- Compare your results with `bisect.bisect_left` in tests.
- Support duplicates: return the FIRST index of target (LeetCode #34).
- Count how many loop iterations happen for n = 1_000_000 and check it
  is at most 20.
"""


def binary_search(nums: list[int], target: int) -> int:
    """Iteratively find `target` in sorted `nums`.

    Args:
        nums: A list of distinct ints sorted in ascending order.
        target: The value to find.

    Returns:
        The index of `target`, or -1 if it is not present.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def binary_search_recursive(
    nums: list[int], target: int, low: int = 0, high: int | None = None
) -> int:
    """Recursively find `target` in sorted `nums[low..high]` (inclusive).

    Args:
        nums: A list of distinct ints sorted in ascending order.
        target: The value to find.
        low: First index of the range to search (default 0).
        high: Last index of the range to search (default: last index).

    Returns:
        The index of `target`, or -1 if it is not present.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
