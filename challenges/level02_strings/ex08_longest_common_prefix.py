"""
Challenge: Longest Common Prefix
Level:     02 - Strings
Topics:    nested loops, indexing, zip(), min(), str.startswith()
Source:    LeetCode #14 "Longest Common Prefix"

========================================================================
PROBLEM
========================================================================
A PREFIX is the beginning part of a string: "fl", "flo" and "flow" are
all prefixes of "flower" (and so is "", the empty prefix).

Given a list of strings, write `longest_common_prefix(strs)` that
returns the longest string that is a prefix of EVERY string in the list.
If they share no common beginning, return "".

    ["flower", "flow", "flight"] -> "fl"
    ["dog", "racecar", "car"]    -> ""

Comparison is case-sensitive: "Apple" and "apple" share no prefix.

========================================================================
EXAMPLES
========================================================================
    >>> longest_common_prefix(["flower", "flow", "flight"])
    'fl'

    >>> longest_common_prefix(["dog", "racecar", "car"])
    ''

    >>> longest_common_prefix(["interview"])
    'interview'

    >>> longest_common_prefix(["ab", "a"])
    'a'

========================================================================
CONSTRAINTS
========================================================================
- `strs` is a list of str.
- If `strs` is EMPTY, return "" (there are no strings to share a prefix).
- Any string in the list may be empty; then the answer is "".
- The answer can never be longer than the shortest string.
- Do not modify the input list.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list [] -> ""
- A single string -> that string
- No common prefix -> ""
- One string is the prefix of the others (["ab", "abc", "abcd"]) -> "ab"
- All strings identical -> that string
- A list containing "" -> ""
- Case sensitivity (["Ab", "ab"]) -> ""
- The common prefix is the whole shortest string, which is NOT first

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. "Vertical scanning": check index 0 of every string, then index 1, and
   so on. Stop at the first index where a string is too short or the
   characters don't all match.
2. The prefix can't be longer than the shortest string: min(strs,
   key=len) finds it.
3. `zip(*strs)` groups the 1st characters together, then the 2nd, etc.,
   and stops at the shortest string. A group is "all equal" when
   len(set(group)) == 1.
4. "Horizontal scanning": start with prefix = strs[0] and shorten it
   (prefix = prefix[:-1]) until every string .startswith(prefix).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Nested loops and breaking out early (`break` / `return`)
- `zip()` and argument unpacking with `*`
- `min(..., key=len)`
- `str.startswith()`
- Slicing a prefix: s[:i]

========================================================================
STRETCH GOALS
========================================================================
- Solve it with both vertical and horizontal scanning.
- Look up `os.path.commonprefix` in the stdlib and compare it with yours.
- Write `longest_common_suffix(strs)`.
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
