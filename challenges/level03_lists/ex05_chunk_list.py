"""
Challenge: Chunk a List
Level:     03 - Lists
Topics:    range() with a step, slicing, lists of lists
Source:    Classic utility function (like itertools.batched in Python 3.12)

========================================================================
YOUR TASK
========================================================================
Write `chunk(items, size)`. It splits a list into consecutive pieces
("chunks") of length `size` and returns them as a list of lists.

    chunk([1, 2, 3, 4, 5, 6, 7], 3)  ->  [[1, 2, 3], [4, 5, 6], [7]]

This is useful in real code, for example to send records to a server
in batches of 100.

========================================================================
THE RULES
========================================================================
Your function must:
1. Make every chunk exactly `size` items long, EXCEPT possibly the last
   one. The last chunk holds whatever is left over, and it is never
   empty.
2. Keep the items in their original order.
3. Return [] when `items` is empty.
4. Raise ValueError when `size` is less than 1 (0 or negative), even
   if `items` is empty.
5. Return a NEW list of NEW lists. Do not change (mutate) `items`.
   Changing a chunk afterwards must not change `items` either.

You can assume:
- `items` is a list of any values.
- `size` is an int.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    chunk([1, 2, 3, 4, 5, 6, 7], 3)  ->  [[1, 2, 3], [4, 5, 6], [7]]
        Two full chunks of 3, then the 1 leftover item.

    chunk(["a", "b", "c", "d"], 2)   ->  [['a', 'b'], ['c', 'd']]
        4 items split evenly into 2 chunks of 2.

    chunk([1, 2], 5)                 ->  [[1, 2]]
        Fewer items than `size`: everything goes in one short chunk.

    chunk([], 3)                     ->  []
        No items, so no chunks (not [[]]).

    chunk([1, 2, 3], 0)              ->  raises ValueError
        A chunk size of 0 makes no sense.

========================================================================
EDGE CASES TO TEST
========================================================================
- Length divides evenly by size: chunk([1, 2, 3, 4], 2)
  -> [[1, 2], [3, 4]] (no short last chunk)
- Length does not divide evenly: chunk([1, 2, 3, 4, 5], 2)
  -> [[1, 2], [3, 4], [5]] (short last chunk)
- size larger than the list: chunk([1, 2], 5) -> [[1, 2]]
- size == 1: chunk([1, 2, 3], 1) -> [[1], [2], [3]]
- Empty list: chunk([], 3) -> []
- size 0 and negative size: chunk([1], 0), chunk([1], -2) and
  chunk([], 0) -> raises ValueError
- The input list is unchanged after the call, even if you then change
  a chunk (result[0][0] = 99)
- Flattening the chunks (joining them back into one list) gives the
  original list

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Validate `size` first, before any looping.
2. range(0, len(items), size) gives the START index of every chunk:
   for 7 items and size 3 -> 0, 3, 6.
3. items[start:start + size] is one chunk. Slicing past the end of a
   list is safe: it just stops at the end.
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
- Write a generator version, `iter_chunks(items, size)`, that `yield`s
  one chunk at a time instead of building the whole list.
- Add a `fill` parameter. If given, pad the last chunk to full size
  with it: chunk([1, 2, 3], 2, fill=0) -> [[1, 2], [3, 0]].
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
