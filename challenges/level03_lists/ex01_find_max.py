"""
Challenge: Find the Maximum (and Minimum)
Level:     03 - Lists
Topics:    looping over lists, tracking the "best so far", tuples
Source:    Classic beginner exercise

========================================================================
PROBLEM
========================================================================
Write two functions WITHOUT using the built-ins max(), min() or sorted():

1. `find_max(nums)` returns the largest number in the list.
2. `find_min_and_max(nums)` returns a TUPLE `(smallest, largest)` - in
   that order - computed in a SINGLE pass over the list (one loop).

A TUPLE is like a list that can't be changed, written with parentheses:
(1, 9). Functions often return tuples to hand back several values.

Both functions raise ValueError if the list is empty, because an empty
list has no largest or smallest element.

========================================================================
EXAMPLES
========================================================================
    >>> find_max([3, 7, 2, 9, 4])
    9

    >>> find_max([-5, -2, -9])
    -2

    >>> find_min_and_max([3, 7, 2, 9, 4])
    (2, 9)

    >>> find_min_and_max([42])
    (42, 42)

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of ints and/or floats.
- Do NOT use max(), min(), sorted() or list.sort().
- Empty list -> raise ValueError.
- Do not modify the input list.
- Return the element itself (so find_max([1, 2.5]) returns 2.5).

========================================================================
EDGE CASES TO TEST
========================================================================
- A single element -> that element (and (x, x) for find_min_and_max)
- All negative numbers (a classic bug is starting the "best" at 0!)
- The maximum is the first element / the last element
- Duplicates of the maximum ([5, 5, 1])
- Mixed ints and floats
- Empty list -> ValueError for both functions
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Don't start your "largest so far" at 0 - what if every number is
   negative? Start it at the FIRST element, nums[0].
2. Check for an empty list BEFORE touching nums[0] (otherwise you get an
   IndexError instead of the ValueError we want).
3. Loop over the remaining elements (nums[1:] or all of them) and update
   the tracker whenever you see something bigger.
4. For find_min_and_max, keep TWO trackers in the same loop and
   `return smallest, largest` (the comma makes a tuple).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The "best so far" pattern
- Why initialising with nums[0] beats initialising with 0
- Returning multiple values as a tuple, and unpacking:
  lo, hi = find_min_and_max(nums)
- IndexError vs ValueError, and choosing which to raise

========================================================================
STRETCH GOALS
========================================================================
- Write `find_max_index(nums) -> int` returning the index of the first
  occurrence of the maximum.
- Make find_max accept any iterable (e.g. a generator), not just lists.
  (Hint: iter() and next().)
- Add a `key` parameter like the built-in max(..., key=len).
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
