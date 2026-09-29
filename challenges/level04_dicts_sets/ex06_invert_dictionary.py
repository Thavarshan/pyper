"""
Challenge: Invert a Dictionary
Level:     04 - Dictionaries and Sets
Topics:    iterating over dict items, hashable keys, grouping
Source:    Classic dict exercise

========================================================================
PROBLEM
========================================================================
"Inverting" a dict means swapping its keys and values, so that what
used to be a value becomes a key and points back to the old key.

    {"a": 1, "b": 2}   inverted is   {1: "a", 2: "b"}

Part 1 - `invert(d)`

Return a NEW dict with keys and values swapped. If two keys share the
same value, a simple swap is impossible (a dict key can only map to ONE
value), so raise `ValueError` in that case. The resulting dict's keys
must appear in the same order as the corresponding entries in `d`.

Part 2 - `invert_grouped(d)`

Handle duplicates gracefully instead: return a dict mapping each value
to a LIST of all the keys that had that value.
- The result's keys appear in the order each value was FIRST seen in `d`.
- Each list holds the original keys in the order they appear in `d`.
- Every value is wrapped in a list, even if only one key had it.

Both functions must leave the input dict unchanged.

A reminder about "hashable": only immutable things (str, int, float,
tuple, bool, None...) can be dict keys. Since values become keys here,
the input's values must be hashable. If a value is a list (unhashable),
Python itself will raise `TypeError` when you try to use it as a key -
you do not need to check for that yourself.

========================================================================
EXAMPLES
========================================================================
    >>> invert({"a": 1, "b": 2, "c": 3})
    {1: 'a', 2: 'b', 3: 'c'}

    >>> invert({"x": 1, "y": 1})
    Traceback (most recent call last):
    ...
    ValueError: duplicate value 1 for keys 'x' and 'y'

    >>> invert_grouped({"apple": "fruit", "carrot": "veg", "banana": "fruit"})
    {'fruit': ['apple', 'banana'], 'veg': ['carrot']}

    >>> invert_grouped({})
    {}

========================================================================
CONSTRAINTS
========================================================================
- `d` is a dict whose values are hashable.
- Return NEW dicts; never modify `d`.
- `invert` raises `ValueError` on any duplicate value (the message
  wording is up to you, but naming the value is helpful).
- `invert_grouped` never raises for duplicates.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty dict                           -> {} for both functions
- One entry {"k": "v"}                 -> {"v": "k"} / {"v": ["k"]}
- Duplicate values                     -> invert raises ValueError
- Order of keys in results (compare `list(result)` to an expected list,
  because `==` on dicts ignores order!)
- Mixed value types {"a": 1, "b": "1"} -> 1 and "1" are DIFFERENT keys
- Unhashable value {"a": [1]}          -> TypeError (raised by Python)
- The input dict is unchanged afterwards

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `for key, value in d.items():` walks the dict in insertion order.
2. For `invert`, before storing `result[value] = key`, check
   `if value in result:` and raise.
3. For `invert_grouped`, `result.setdefault(value, []).append(key)`
   creates the list the first time and appends every time.
4. `collections.defaultdict(list)` is another way - but convert it back
   to a plain `dict` before returning.
5. A dict comprehension `{v: k for k, v in d.items()}` inverts in one
   line, but silently drops duplicates. Why?

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- dict.items() and tuple unpacking in for loops
- Hashability and why lists can't be keys
- dict.setdefault() and collections.defaultdict
- Dict comprehensions
- Dicts preserve insertion order (and `==` ignores it)

========================================================================
STRETCH GOALS
========================================================================
- `invert_grouped` that returns `dict[value, set[keys]]` instead.
- Prove `invert(invert(d)) == d` for any dict with unique values.
- Add `on_duplicate="error" | "first" | "last"` to `invert`.
"""

from collections.abc import Hashable


def invert(d: dict[Hashable, Hashable]) -> dict[Hashable, Hashable]:
    """Return a new dict with keys and values swapped.

    Args:
        d: The dict to invert. Values must be hashable and unique.
            Not modified.

    Returns:
        A new dict mapping each original value to its original key,
        in the same order as `d`.

    Raises:
        ValueError: If two keys in `d` share the same value.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def invert_grouped(d: dict[Hashable, Hashable]) -> dict[Hashable, list[Hashable]]:
    """Return a new dict mapping each value to the list of keys that had it.

    Args:
        d: The dict to invert. Values must be hashable. Not modified.

    Returns:
        A new dict whose keys are the distinct values of `d` (in order of
        first appearance) and whose values are lists of the original keys
        (in their original order).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
