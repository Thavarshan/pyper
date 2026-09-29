"""
Challenge: Chunk a List
Level:     03 - Lists
Topics:    range() with a step, slicing, lists of lists
Source:    Classic utility function (like itertools.batched in Python 3.12)

========================================================================
PROBLEM
========================================================================
Write `chunk(items, size)` that splits a list into consecutive pieces
("chunks") of length `size`, and returns them as a list of lists.

    chunk([1, 2, 3, 4, 5, 6, 7], 3) -> [[1, 2, 3], [4, 5, 6], [7]]

Rules:
    - Every chunk has exactly `size` items, EXCEPT possibly the last
      one, which holds whatever is left over (it is never empty).
    - Items keep their original order.
    - An empty input list gives an empty result: [].
    - `size` must be at least 1; otherwise raise ValueError.

This is useful in real code, e.g. sending records to a server in
batches of 100.

========================================================================
EXAMPLES
========================================================================
    >>> chunk([1, 2, 3, 4, 5, 6, 7], 3)
    [[1, 2, 3], [4, 5, 6], [7]]

    >>> chunk(["a", "b", "c", "d"], 2)
    [['a', 'b'], ['c', 'd']]

    >>> chunk([1, 2], 5)
    [[1, 2]]

    >>> chunk([], 3)
    []

========================================================================
CONSTRAINTS
========================================================================
- `items` is a list of any values; `size` is an int.
- size < 1 (0 or negative) -> raise ValueError, even if items is empty.
- Return a NEW list of NEW lists; do not modify `items`. Changing a
  chunk afterwards must not change `items`.

========================================================================
EDGE CASES TO TEST
========================================================================
- Length divides evenly by size (no short last chunk)
- Length does not divide evenly (short last chunk)
- size larger than the list -> one chunk with everything
- size == 1 -> every item in its own list
- Empty list -> []
- size 0 and negative size -> ValueError
- The input list is unchanged
- Flattening the chunks gives back the original list

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. range(0, len(items), size) gives the START index of every chunk:
   for 7 items and size 3 -> 0, 3, 6.
2. items[start:start + size] is one chunk. Slicing past the end of a
   list is safe - it just stops at the end.
3. Validate `size` first, before any looping.
4. The whole thing can become a single list comprehension.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- range(start, stop, step)
- Slicing never raises IndexError, even out of bounds
- Lists of lists (nested lists)
- Slices create new lists (copies)
- List comprehensions

========================================================================
STRETCH GOALS
========================================================================
- Write a generator version `iter_chunks(items, size)` that `yield`s one
  chunk at a time.
- Add a `fill` parameter: if given, pad the last chunk to full size with
  it: chunk([1, 2, 3], 2, fill=0) -> [[1, 2], [3, 0]].
- Read about `itertools.batched` (Python 3.12+).
"""

from typing import TypeVar

T = TypeVar("T")


def chunk(items: list[T], size: int) -> list[list[T]]:
    """Split `items` into consecutive chunks of length `size`.

    Args:
        items: The list to split. It is not modified.
        size: The length of each chunk; must be at least 1.

    Returns:
        A list of chunks (lists). All chunks have `size` items except
        possibly the last, which is shorter but never empty.

    Raises:
        ValueError: If `size` is less than 1.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
