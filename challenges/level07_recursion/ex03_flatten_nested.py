"""
Challenge: Flatten a Nested List (and measure its depth)
Level:     07 - Recursion
Topics:    recursion over nested data, isinstance(), list building
Source:    Classic recursion exercise (related to LeetCode #341 "Flatten
           Nested List Iterator")

========================================================================
PROBLEM
========================================================================
A NESTED LIST is a list whose items may themselves be lists, which may
contain more lists, and so on, to any depth:

    [1, [2, 3], [[4], 5], [], [[[6]]]]

Part 1 - flatten(nested):
    Return a NEW flat list containing every non-list item, in the order
    you would meet them reading the original from left to right.
        [1, [2, 3], [[4], 5], [], [[[6]]]]  ->  [1, 2, 3, 4, 5, 6]
    Only `list` objects are "opened up". Anything else - ints, strings,
    tuples, None, dicts - counts as a single item and is kept as-is.
    (So a tuple (1, 2) stays as the one item (1, 2); the string "abc"
    stays as "abc", it is NOT split into characters.)
    The input must NOT be modified.

Part 2 - depth(nested):
    Return the maximum nesting depth. The rules are:
        - A value that is not a list has depth 0.        depth(5) == 0
        - A list's depth is 1 + the largest depth of its items,
          where an empty list counts as depth 1.         depth([]) == 1
    Examples:
        depth([1, 2, 3])         == 1
        depth([1, [2, 3]])       == 2
        depth([[[]]])            == 3
        depth([1, [2, [3, [4]]]]) == 4

Both functions must be recursive: when you meet an inner list, call the
function on that inner list.

========================================================================
EXAMPLES
========================================================================
    >>> flatten([1, [2, [3, [4]]], 5])
    [1, 2, 3, 4, 5]

    >>> flatten([[], [[]], [[], []]])
    []

    >>> flatten(["ab", ("c", "d"), [None]])
    ['ab', ('c', 'd'), None]

    >>> depth([1, [2, [3]]])
    3

    >>> depth("hello")
    0

========================================================================
CONSTRAINTS
========================================================================
- flatten: `nested` must be a list; otherwise raise `TypeError`.
- depth: accepts ANY value (non-lists return 0, see rules above).
- Nesting depth is at most ~500, so recursion is safe.
- Total number of items is at most 10_000.
- Do not mutate the input. flatten returns a brand-new list, even when
  the input is already flat (so `flatten(x) is not x`).
- Must be recursive.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(total number of items and lists) - each is visited once.
- Space: O(D) call stack where D is the nesting depth, plus the
  output list.

========================================================================
EDGE CASES TO TEST
========================================================================
- flatten([]) -> []           and depth([]) -> 1
- Already-flat list: flatten([1, 2, 3]) == [1, 2, 3], but a new object
- Only empty lists inside: flatten([[], [[]]]) -> []
- Strings and tuples are NOT flattened
- The original input is unchanged afterwards (compare with a copy made
  via `copy.deepcopy` before calling)
- depth of a non-list: depth(42) == 0, depth(None) == 0
- depth of a lopsided list: depth([1, [[[2]]], 3]) == 4
- flatten("not a list") -> TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Test "is this a list?" with `isinstance(item, list)`.
2. flatten: start with `result = []`. Loop over the items. For a
   non-list item, `append` it; for a list item, call flatten on it and
   `extend` result with what comes back.
3. `append(x)` adds x as ONE item; `extend(xs)` adds each item of xs.
   Mixing them up is the most common bug here.
4. depth: base case is "not a list" -> 0. For a list, compute the depth
   of every item and take the max. `max(values, default=0)` handles the
   empty list neatly, then add 1.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Recursing over tree-like / nested data
- `isinstance()` checks
- `list.append` vs `list.extend`
- `max(..., default=...)` and generator expressions
- `copy.deepcopy` for checking that input was not mutated

========================================================================
STRETCH GOALS
========================================================================
- Write `flatten_gen(nested)` as a recursive GENERATOR using
  `yield` and `yield from`, and test `list(flatten_gen(x)) == flatten(x)`.
- Add a `max_depth` parameter: flatten only that many levels, e.g.
  flatten([1, [2, [3]]], max_depth=1) -> [1, 2, [3]].
- Also open up tuples (but still not strings).
"""

from typing import Any


def flatten(nested: list[Any]) -> list[Any]:
    """Return a new flat list of all non-list items in `nested`.

    Must be implemented recursively. Order is preserved (left to right).
    Only `list` instances are flattened; every other value is one item.

    Args:
        nested: A list that may contain other lists to any depth.

    Returns:
        A new list with every non-list value, in reading order.

    Raises:
        TypeError: If `nested` is not a list.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def depth(nested: Any) -> int:
    """Return the maximum nesting depth of `nested`.

    Must be implemented recursively. Non-list values have depth 0;
    a list has depth 1 + the max depth of its items ([] has depth 1).

    Args:
        nested: Any value, usually a (possibly nested) list.

    Returns:
        The nesting depth as a non-negative int.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
