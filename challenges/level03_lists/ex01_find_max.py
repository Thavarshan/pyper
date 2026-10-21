"""
Challenge: Find the Maximum (and Minimum)
Level:     03 - Lists
Topics:    looping over lists, tracking the "best so far", tuples
Source:    Classic beginner exercise

========================================================================
YOUR TASK
========================================================================
Write two functions, WITHOUT using the built-ins max(), min() or
sorted():

- `find_max(nums)` returns the largest number in the list.
- `find_min_and_max(nums)` returns the smallest and the largest number
  together, as a tuple `(smallest, largest)`.

    find_min_and_max([3, 7, 2, 9, 4])  ->  (2, 9)

A TUPLE is like a list that can't be changed, written with round
brackets: (2, 9). Functions often return a tuple to hand back several
values at once.

========================================================================
THE RULES
========================================================================
Your functions must:
1. Not use max(), min(), sorted() or list.sort().
2. Return the element itself, unchanged: find_max([1, 2.5]) returns
   2.5.
3. For find_min_and_max, return `(smallest, largest)` in that order.
4. For find_min_and_max, find both values in a SINGLE pass over the
   list (one loop).
5. Raise ValueError if the list is empty, because an empty list has no
   largest or smallest element. This applies to BOTH functions.
6. Not change (mutate) `nums`.

You can assume:
- `nums` is a list of ints and/or floats.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    find_max([3, 7, 2, 9, 4])          ->  9
        9 is the biggest number in the list.

    find_max([-5, -2, -9])             ->  -2
        All negative: -2 is the closest to zero, so it is the biggest.

    find_min_and_max([3, 7, 2, 9, 4])  ->  (2, 9)
        Smallest first, then largest.

    find_min_and_max([42])             ->  (42, 42)
        With one item, that item is both the smallest and the largest.

    find_max([])                       ->  raises ValueError
        An empty list has no largest element.

========================================================================
EDGE CASES TO TEST
========================================================================
- A single element: find_max([7]) -> 7 and
  find_min_and_max([7]) -> (7, 7)
- All negative numbers: find_max([-5, -2, -9]) -> -2
  (a classic bug is starting the "best" at 0, which wrongly gives 0)
- The maximum is the first element: find_max([9, 1, 2]) -> 9
- The maximum is the last element: find_max([1, 2, 9]) -> 9
- Duplicates of the maximum: find_max([5, 5, 1]) -> 5
- Mixed ints and floats: find_max([1, 2.5, 2]) -> 2.5
- Empty list -> raises ValueError, for BOTH functions
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Don't start your "largest so far" at 0. What if every number is
   negative? Start it at the FIRST element, nums[0].
2. Check for an empty list BEFORE touching nums[0]. Otherwise you get
   an IndexError instead of the ValueError we want.
3. Loop over the remaining elements (nums[1:], or all of them) and
   update the tracker whenever you see something bigger.
4. For find_min_and_max, keep TWO trackers in the same loop and
   `return smallest, largest` (the comma makes a tuple).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The "best so far" pattern
- Why starting with nums[0] beats starting with 0
- Returning multiple values as a tuple, and unpacking them:
  lo, hi = find_min_and_max(nums)
- IndexError vs ValueError, and choosing which to raise

========================================================================
STRETCH GOALS
========================================================================
- Write `find_max_index(nums) -> int`, which returns the index
  (position) of the first occurrence of the maximum.
- Make find_max accept any iterable (anything you can loop over with
  `for`, such as a generator), not just lists. (Hint: iter() and
  next().)
- Add a `key` parameter like the built-in max(..., key=len). The key
  is a function that says what to compare: max(words, key=len) finds
  the longest word.
"""


def find_max(nums: list[float]) -> float:
    """Return the largest number in `nums` without using max().

    Args:
        nums: A non-empty list of numbers.

    Returns:
        The largest element.

    Raises:
        ValueError: If `nums` is empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def find_min_and_max(nums: list[float]) -> tuple[float, float]:
    """Return (smallest, largest) of `nums` using a single loop.

    Args:
        nums: A non-empty list of numbers.

    Returns:
        A tuple (minimum, maximum).

    Raises:
        ValueError: If `nums` is empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
