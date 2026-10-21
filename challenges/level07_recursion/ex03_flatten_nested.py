"""
Challenge: Flatten a Nested List (and measure its depth)
Level:     07 - Recursion
Topics:    recursion over nested data, isinstance(), list building
Source:    Classic recursion exercise (related to LeetCode #341 "Flatten
           Nested List Iterator")

========================================================================
YOUR TASK
========================================================================
Write two recursive functions (functions that call themselves) for
lists that contain other lists:

- `flatten(nested)` returns a NEW flat list of every non-list item.
- `depth(nested)` returns how deeply the lists are nested.

    flatten([1, [2, [3, [4]]], 5])  ->  [1, 2, 3, 4, 5]
    depth([1, [2, [3]]])            ->  3

========================================================================
WHAT A "NESTED LIST" IS
========================================================================
A NESTED LIST is a list whose items may themselves be lists, which may
hold more lists, and so on, to any depth:

    [1, [2, 3], [[4], 5], [], [[[6]]]]

FLATTENING it means pulling every non-list item out into one plain
list, in the order you meet them reading left to right:

    [1, [2, 3], [[4], 5], [], [[[6]]]]  ->  [1, 2, 3, 4, 5, 6]

DEPTH counts how many lists you are inside at the deepest point:

    - A value that is not a list has depth 0.     depth(5)   == 0
    - A list's depth is 1 + the largest depth of its items.
      An empty list has depth 1.                  depth([])  == 1

    depth([1, 2, 3])           ->  1    (one list, no lists inside)
    depth([1, [2, 3]])         ->  2    (a list inside a list)
    depth([[[]]])              ->  3
    depth([1, [2, [3, [4]]]])  ->  4

Recursion fits naturally here: when you meet an inner list, call the
same function on that inner list.

========================================================================
THE RULES
========================================================================
`flatten(nested)` must:
1. Return a NEW flat list holding every non-list item, in left-to-right
   reading order.
2. Open up only `list` objects. Everything else (ints, strings, tuples,
   None, dicts) counts as ONE item and is kept as it is. So the tuple
   (1, 2) stays as the one item (1, 2), and the string "abc" stays as
   "abc". It is NOT split into characters.
3. Return a brand-new list even when the input is already flat, so
   `flatten(x) is not x`.
4. Raise `TypeError` if `nested` is not a list.

`depth(nested)` must:
5. Accept ANY value. A non-list returns 0.
6. Return 1 + the largest depth of the items for a list, and 1 for an
   empty list.

Both functions must:
7. Not mutate (change) the input in any way.
8. Be recursive. A loop over the items of one list is fine, as long as
   inner lists are handled by a recursive call.

You can assume:
- The nesting depth is at most about 500, so recursion is safe (Python
  allows about 1000 calls waiting at once). See hint 4 for one trap.
- There are at most 10_000 items in total.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    flatten([1, [2, [3, [4]]], 5])       ->  [1, 2, 3, 4, 5]
        Every inner list is opened, however deep.

    flatten([[], [[]], [[], []]])        ->  []
        Only empty lists, so there are no items to keep.

    flatten(["ab", ("c", "d"), [None]])  ->  ['ab', ('c', 'd'), None]
        The string and the tuple are single items. Only the list
        [None] is opened.

    depth([1, [2, [3]]])                 ->  3
        [3] sits inside [2, [3]], which sits inside the outer list.

    depth("hello")                       ->  0
        Not a list.

    flatten("not a list")                ->  raises TypeError

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(total number of items and lists). Each item and each list
  is visited once, so twice as much data means about twice the work.
- Space: O(D) for the call stack, where D is the nesting depth (one
  waiting call per level), plus the output list.

========================================================================
EDGE CASES TO TEST
========================================================================
- flatten([]) -> []   and   depth([]) -> 1
- An already-flat list: flatten([1, 2, 3]) == [1, 2, 3], and the
  result is a new object (`result is not original`)
- Only empty lists inside: flatten([[], [[]]]) -> []
- Strings and tuples are NOT flattened:
  flatten(["ab", ("c", "d")]) -> ['ab', ('c', 'd')]
- The input is unchanged afterwards. Make a copy with `copy.deepcopy`
  before the call and check `nested == the_copy` after it.
- depth of a non-list: depth(42) -> 0, depth(None) -> 0
- depth of a lopsided list: depth([1, [[[2]]], 3]) -> 4
- flatten("not a list") -> raises TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Test "is this a list?" with `isinstance(item, list)`.
2. flatten: start with `result = []` and loop over the items. For a
   non-list item, `append` it. For a list item, call flatten on it and
   `extend` result with what comes back.
3. `append(x)` adds x as ONE item. `extend(xs)` adds each item of xs
   separately. Mixing them up is the most common bug here.
4. depth: the base case is "not a list" -> 0. For a list, work out the
   depth of every item, take the largest, and add 1.
   `max([depth(i) for i in nested], default=0)` handles the empty list
   neatly (`default` is what max returns for an empty list). Use a list
   comprehension `[...]` here, not a generator expression `(...)`: in
   Python a generator adds an extra hidden call per level, so it hits
   RecursionError at about 490 levels instead of about 990.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Recursing over tree-like (nested) data
- `isinstance()` checks
- `list.append` vs `list.extend`
- `max(..., default=...)`, list comprehensions and generator
  expressions
- `copy.deepcopy` for checking that the input was not mutated

========================================================================
STRETCH GOALS
========================================================================
- Write `flatten_gen(nested)` as a recursive GENERATOR (a function that
  hands out values one at a time with `yield` instead of building a
  list). Use `yield` and `yield from`, and test
  `list(flatten_gen(x)) == flatten(x)`.
- Add a `max_depth` parameter that flattens only that many levels:
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
