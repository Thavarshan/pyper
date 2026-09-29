"""
Challenge: First Unique Character
Level:     04 - Dictionaries and Sets
Topics:    counting with dicts, two-pass algorithms, enumerate
Source:    LeetCode #387 "First Unique Character in a String"

========================================================================
PROBLEM
========================================================================
Given a string `s`, find the FIRST character that appears exactly once
in the whole string and return its index (position, starting at 0).
If every character repeats, or the string is empty, return -1.

"Unique" here means "occurs exactly one time in the entire string", not
"different from its neighbours". In "abca", 'a' is NOT unique (it
appears twice) but 'b' is, so the answer is 1.

Characters are compared exactly as they are: this is case-SENSITIVE,
so 'a' and 'A' are different characters. Spaces and punctuation are
characters too.

========================================================================
EXAMPLES
========================================================================
    >>> first_unique_char("leetcode")
    0

    >>> first_unique_char("loveleetcode")
    2

    >>> first_unique_char("aabb")
    -1

    >>> first_unique_char("aA")
    0

========================================================================
CONSTRAINTS
========================================================================
- `s` is a str of length 0 to 100_000.
- Any characters are allowed (letters, digits, spaces, emoji...).
- Return an int: a valid index, or -1.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time O(n), space O(k) where k is the number of distinct characters:
  one pass to count, one pass to find the first count of 1.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string ""           -> -1
- Single character "z"      -> 0
- All repeated "aabbcc"     -> -1
- Unique character is last "aabbc" -> 4
- Case sensitivity "aA"     -> 0, "aAa" -> 1
- Spaces count as characters "a a" -> 1 (the space)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. You can't know whether a character is unique until you've seen the
   whole string - so do it in two passes.
2. Pass 1: build a dict of character -> count.
3. Pass 2: loop with `enumerate(s)` and return the first index whose
   character has count 1.
4. `collections.Counter(s)` does pass 1 in a single line.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Iterating over a string character by character
- Building a frequency dict (dict.get or Counter)
- `enumerate()`
- Returning a sentinel value (-1) to mean "not found"

========================================================================
STRETCH GOALS
========================================================================
- Solve it with a brute-force `s.count(ch)` inside the loop and explain
  why that is O(n^2).
- Write `first_unique_char_value(s) -> str | None` returning the
  character itself instead of its index.
"""


def first_unique_char(s: str) -> int:
    """Return the index of the first non-repeating character in s.

    Args:
        s: The string to search. Comparison is case-sensitive.

    Returns:
        The index of the first character that appears exactly once,
        or -1 if there is none.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
