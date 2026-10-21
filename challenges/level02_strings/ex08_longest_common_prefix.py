"""
Challenge: Longest Common Prefix
Level:     02 - Strings
Topics:    nested loops, indexing, zip(), min(), str.startswith()
Source:    LeetCode #14 "Longest Common Prefix"

========================================================================
YOUR TASK
========================================================================
Write `longest_common_prefix(strs)`. It takes a list of strings and
returns the longest beginning that ALL of them share. If they share no
beginning, it returns "".

    longest_common_prefix(["flower", "flow", "flight"])  ->  'fl'

========================================================================
WHAT "PREFIX" MEANS
========================================================================
A PREFIX is the beginning part of a string. "fl", "flo" and "flow" are
all prefixes of "flower", and so is "" (the empty prefix). A COMMON
prefix is one that every string in the list starts with:

    flower
    flow
    flight
    ^^          "fl" is shared, but the third letters (o, o, i) differ

So the answer can never be longer than the shortest string in the list.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the longest string that is a prefix of EVERY string in
   `strs`.
2. Return "" if the strings share no common beginning.
3. Compare case-sensitively: "Apple" and "apple" share no prefix.
4. Return "" if `strs` is EMPTY (there are no strings to share a
   prefix).
5. Return "" if any string in the list is empty.
6. Not change (mutate) the input list.

You can assume:
- `strs` is a list of str.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    longest_common_prefix(["flower", "flow", "flight"])  ->  'fl'
        All three start with "fl", but the third letters differ.

    longest_common_prefix(["dog", "racecar", "car"])     ->  ''
        Even the first letters differ.

    longest_common_prefix(["interview"])                 ->  'interview'
        With only one string, the whole string is shared.

    longest_common_prefix(["ab", "a"])                   ->  'a'
        The prefix can't be longer than the shortest string, "a".

========================================================================
EDGE CASES TO TEST
========================================================================
- An empty list: longest_common_prefix([]) -> ''
- A single string: ["interview"] -> 'interview'
- No common prefix: ["dog", "racecar", "car"] -> ''
- One string is the prefix of the others: ["ab", "abc", "abcd"] -> 'ab'
- All strings identical: ["same", "same"] -> 'same'
- A list containing "": ["abc", "", "abd"] -> ''
- Case sensitivity: ["Ab", "ab"] -> ''
- The answer is the whole shortest string, which is NOT first:
  ["abcd", "abc", "ab"] -> 'ab'
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. "Vertical scanning": check index 0 of every string, then index 1, and
   so on. Stop at the first index where a string is too short or the
   characters don't all match.
2. The prefix can't be longer than the shortest string: min(strs,
   key=len) finds it.
3. `zip(*strs)` groups the 1st characters together, then the 2nd, and
   so on, and stops at the end of the shortest string. A group is "all
   equal" when len(set(group)) == 1.
4. "Horizontal scanning": start with prefix = strs[0] and shorten it
   (prefix = prefix[:-1]) until every string .startswith(prefix).
   Handle the empty list first, because strs[0] crashes on [].

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Nested loops and breaking out early (`break` / `return`)
- `zip()` and argument unpacking with `*` (zip(*strs) passes each
  string as a separate argument)
- `min(..., key=len)`
- `str.startswith()`
- Slicing a prefix: s[:i]

========================================================================
STRETCH GOALS
========================================================================
- Solve it with both vertical and horizontal scanning.
- Look up `os.path.commonprefix` in the standard library and compare it
  with yours.
- Write `longest_common_suffix(strs)` (a suffix is the ending part of a
  string).
"""


def longest_common_prefix(strs: list[str]) -> str:
    """Return the longest prefix shared by every string in `strs`.

    Args:
        strs: A list of strings (may be empty).

    Returns:
        The longest common prefix, or "" if there is none or `strs` is
        empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
