"""
Challenge: Binary Search
Level:     09 - Searching and Sorting
Topics:    binary search, low/high pointers, while loops, recursion
Source:    LeetCode #704 "Binary Search"

========================================================================
YOUR TASK
========================================================================
Write two versions of binary search. Each one finds `target` in a
SORTED list and gives back its index, or -1 if it isn't there:

    binary_search(nums, target)            uses a while loop
                                           (ITERATIVE)
    binary_search_recursive(nums, target)  calls itself
                                           (RECURSIVE)

    binary_search([-1, 0, 3, 5, 9, 12], 9)  ->  4

========================================================================
WHAT "BINARY SEARCH" MEANS
========================================================================
Binary search finds a value in a SORTED list by halving the part of
the list that could still hold it. Think of looking up a word in a
paper dictionary: open it in the middle, decide whether your word
comes before or after, and throw away the other half.

You keep two indices, `low` and `high`. They mark the first and last
positions that could still hold the target (both ends included). Each
step looks at the middle position, `mid`:

    Search 7 in [1, 3, 5, 7, 9, 11]
    low=0, high=5 -> mid=2 -> 5 < 7  -> search right half: low=3
    low=3, high=5 -> mid=4 -> 9 > 7  -> search left half:  high=3
    low=3, high=3 -> mid=3 -> 7 == 7 -> found at index 3

Each step halves the range, so 1 million items need only about 20
steps.

The recursive version takes two extra parameters, `low` and `high`:
the first and last index still being searched (both included).
Callers normally leave them out. `high=None` means "len(nums) - 1".

========================================================================
THE RULES
========================================================================
Your functions must:
1. Return the index of `target` in `nums`, or -1 if it isn't there.
2. Behave identically: both versions give the same answer for the
   same input.
3. binary_search uses a loop (iterative). binary_search_recursive
   calls itself (recursive).
4. In the recursive version, pass `low`/`high` indices to the next
   call. Do NOT slice the list: nums[mid:] copies the data, which
   costs O(n) (time that grows with the length of the list).
5. Not change (mutate) `nums`.
6. Not use `list.index`, the `x in items` membership test, or the
   `bisect` module. (You may use them in your TESTS as a reference.)

You can assume:
- `nums` is sorted in ascending (increasing) order.
- All values in `nums` are different (no duplicates), so the answer
  is unique.
- 0 <= len(nums) <= 10**5.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    binary_search([-1, 0, 3, 5, 9, 12], 9)  ->  4
        9 is at index 4.

    binary_search([-1, 0, 3, 5, 9, 12], 2)  ->  -1
        2 would sit between 0 and 3, but it isn't in the list.

    binary_search([], 1)                    ->  -1
        Nothing to search.

    binary_search_recursive([1, 3, 5, 7], 1)  ->  0
        1 is the first item. `low` and `high` were left out.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(log n): each step halves the search range, so doubling the
  list adds just one more step.
- Space: iterative O(1): only a few variables.
         Recursive O(log n): each call waits on the "call stack" until
         the next one returns, and there are about log n calls.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: binary_search([], 1) -> -1
- One element, found: binary_search([5], 5) -> 0
- One element, not found: binary_search([5], 3) -> -1
- Target is the first element: binary_search([1, 3, 5, 7], 1) -> 0
- Target is the last element: binary_search([1, 3, 5, 7], 7) -> 3
- Target smaller than everything: binary_search([1, 3, 5], 0) -> -1
- Target larger than everything: binary_search([1, 3, 5], 9) -> -1
- Target that would fall between two elements:
  binary_search([1, 3, 5], 4) -> -1
- Even and odd lengths
- A big list, e.g. list(range(0, 2_000_000, 2)), for several targets:
  an even target t gives t // 2, an odd one gives -1
- Both functions agree on every test (use @pytest.mark.parametrize
  with the function itself as a parameter!)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Keep two indices: `low = 0` and `high = len(nums) - 1`. Loop while
   `low <= high`. Note the `<=`: with `<` you would skip a range of
   one item, so binary_search([5], 5) would wrongly return -1.
2. `mid = (low + high) // 2`.
3. If nums[mid] < target, the answer must be to the right:
   `low = mid + 1`. If it's bigger: `high = mid - 1`. The +1 and -1
   matter. Without them the loop can run forever.
4. Recursive version: the base case is `low > high`, which means
   return -1. Otherwise compare with nums[mid] and recurse on one
   half.
5. Replace `high=None` at the start:
   `if high is None: high = len(nums) - 1`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- while loops with two pointers
- Integer division `//`
- Off-by-one errors and loop invariants (facts that stay true on every
  pass, like "if the target exists, it is always between low and
  high")
- Default parameters with None as a sentinel (a special stand-in
  value)
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
