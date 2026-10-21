"""
Challenge: Invert a Dictionary
Level:     04 - Dictionaries and Sets
Topics:    iterating over dict items, hashable keys, grouping
Source:    Classic dict exercise

========================================================================
YOUR TASK
========================================================================
Write two functions that swap a dict's keys and values:

- `invert(d)` returns a NEW dict with keys and values swapped. It
  raises ValueError if two keys share the same value.
- `invert_grouped(d)` returns a NEW dict mapping each value to a LIST
  of all the keys that had that value.

    invert({"a": 1, "b": 2})  ->  {1: 'a', 2: 'b'}

========================================================================
WHAT "INVERTING" MEANS
========================================================================
Inverting a dict swaps its keys and values. What used to be a value
becomes a key, and it points back to the old key:

    {"a": 1, "b": 2}    inverted is    {1: "a", 2: "b"}

Trouble starts when two keys share a value:

    {"x": 1, "y": 1}    would need     {1: "x", 1: "y"}

A dict key can only map to ONE value, so a simple swap is impossible.
`invert` raises an error in that case. `invert_grouped` collects all
the keys into a list instead: {1: ["x", "y"]}.

Only HASHABLE things can be dict keys. These are the immutable
(unchangeable) types: str, int, float, tuple, bool, None and so on.
Since values become keys here, the input's values must be hashable. If
a value is a list (unhashable), Python itself raises TypeError when you
try to use it as a key. You do not need to check for that yourself.

========================================================================
THE RULES
========================================================================
Your functions must:
1. Both: return a NEW dict, and never change (mutate) `d`.
2. invert: map each original value to its original key.
3. invert: raise ValueError if any value appears more than once. The
   message wording is up to you, but naming the value is helpful.
4. invert: put the result's keys in the same order as the
   corresponding entries in `d`.
5. invert_grouped: map each value to a list of ALL the keys that had
   it, in the order those keys appear in `d`.
6. invert_grouped: wrap every value's keys in a list, even if only one
   key had that value.
7. invert_grouped: order the result's keys by when each value was
   FIRST seen in `d`.
8. invert_grouped: never raise for duplicate values.

You can assume:
- `d` is a dict whose values are hashable.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    invert({"a": 1, "b": 2, "c": 3})  ->  {1: 'a', 2: 'b', 3: 'c'}
        Each value becomes a key that points back to its old key.

    invert({"x": 1, "y": 1})          ->  raises ValueError
        Both keys have the value 1. The message is up to you, for
        example: duplicate value 1 for keys 'x' and 'y'

    invert_grouped({"apple": "fruit", "carrot": "veg", "banana": "fruit"})
        ->  {'fruit': ['apple', 'banana'], 'veg': ['carrot']}
        "fruit" is seen first, so it is the first key. Its list keeps
        'apple' before 'banana', as in the input. "veg" only had one
        key, but it still gets a list.

    invert_grouped({})                ->  {}
        Nothing to invert.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty dict -> {} for both functions
- One entry: invert({"k": "v"}) -> {'v': 'k'} and
  invert_grouped({"k": "v"}) -> {'v': ['k']}
- Duplicate values: invert({"x": 1, "y": 1}) -> raises ValueError
- Order of keys in results: compare `list(result)` to an expected
  list, because `==` on dicts ignores order!
  For example, list(invert({"b": 2, "a": 1})) -> [2, 1]
- Mixed value types: invert({"a": 1, "b": "1"}) -> {1: 'a', '1': 'b'}
  (1 and "1" are DIFFERENT keys)
- Unhashable value: invert({"a": [1]}) -> raises TypeError (raised by
  Python itself)
- The input dict is unchanged afterwards

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `for key, value in d.items():` walks the dict in insertion order
   (the order the keys were added).
2. For `invert`, before storing `result[value] = key`, check
   `if value in result:` and raise.
3. For `invert_grouped`, `result.setdefault(value, []).append(key)`
   creates the list the first time and appends every time.
4. `collections.defaultdict(list)` is another way, but convert it back
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
- Dicts keep insertion order (and `==` ignores it)

========================================================================
STRETCH GOALS
========================================================================
- An `invert_grouped` that returns `dict[value, set[keys]]` instead
  (a set of keys for each value, not a list).
- Prove `invert(invert(d)) == d` for any dict with unique values.
- Add an `on_duplicate="error" | "first" | "last"` parameter to
  `invert`. It chooses what happens on a duplicate value: raise an
  error, keep the first key, or keep the last key.
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
