"""
Challenge: Valid Anagram
Level:     02 - Strings
Topics:    counting with dicts, collections.Counter, sorted()
Source:    LeetCode #242 "Valid Anagram"

========================================================================
PROBLEM
========================================================================
Two words are ANAGRAMS of each other if you can rearrange the letters of
one to get exactly the other, using every letter exactly once. "listen"
and "silent" are anagrams; "rat" and "car" are not.

Write `is_anagram(s, t)` that returns True if `t` is an anagram of `s`.

For this challenge the comparison is EXACT:
    - Case matters: "A" and "a" are different characters.
    - Every character counts, including spaces and punctuation.
So is_anagram("Listen", "silent") is False (capital L vs lower-case s
and l), and is_anagram("a b", "ab") is False (the space counts).

Put differently: the two strings are anagrams exactly when every
character appears the SAME NUMBER OF TIMES in both.

========================================================================
EXAMPLES
========================================================================
    >>> is_anagram("anagram", "nagaram")
    True

    >>> is_anagram("rat", "car")
    False

    >>> is_anagram("aab", "abb")
    False

    >>> is_anagram("", "")
    True

========================================================================
CONSTRAINTS
========================================================================
- `s` and `t` are str, each up to 50_000 characters.
- Comparison is case-sensitive and includes all characters.
- A string is an anagram of itself.
- Return a real bool.

========================================================================
EDGE CASES TO TEST
========================================================================
- Classic anagram pair -> True
- Different lengths -> False (quick exit!)
- Same letters, different counts ("aab" vs "abb") -> False
- Two empty strings -> True
- Identical strings -> True
- Case difference ("Aa" vs "aa") -> False
- Strings with spaces or digits

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. If the lengths differ, they cannot be anagrams.
2. Easy approach: sorted(s) == sorted(t). sorted() on a string returns a
   list of its characters in order.
3. Counting approach: build a dict {character: count} for each string
   and compare the two dicts with ==.
4. `collections.Counter(s)` builds that counting dict for you.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `sorted()` works on any iterable and returns a list
- Counting with a dict and `dict.get(key, 0)`
- `collections.Counter` and comparing Counters with ==
- Early returns for quick "obviously false" cases

========================================================================
STRETCH GOALS
========================================================================
- Implement it three ways: sorting, a manual dict, and Counter.
- Write `is_anagram_loose(s, t)` that ignores case and non-letters, so
  "Dormitory" and "dirty room!" are anagrams.
- LeetCode #49 "Group Anagrams": group a list of words into lists of
  anagrams.
"""


def is_anagram(s: str, t: str) -> bool:
    """Return True if `t` is an anagram of `s` (case-sensitive, exact).

    Args:
        s: The first string.
        t: The second string.

    Returns:
        True if both strings contain exactly the same characters with the
        same counts, otherwise False.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
