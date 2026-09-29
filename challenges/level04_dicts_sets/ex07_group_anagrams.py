"""
Challenge: Group Anagrams
Level:     04 - Dictionaries and Sets
Topics:    choosing a dict key, tuples as keys, grouping, sorted()
Source:    LeetCode #49 "Group Anagrams"

========================================================================
PROBLEM
========================================================================
Two words are "anagrams" of each other if you can rearrange the
letters of one to get the other, using every letter exactly once.
"listen" and "silent" are anagrams; "abc" and "abcc" are not.

Given a list of words, put the words that are anagrams of each other
into the same group, and return the list of groups.

Ordering rules (so your tests have one exact right answer):
- Groups appear in the order in which their FIRST word appears in the
  input.
- Inside each group, words keep their original input order.
- Duplicate words are kept: ["a", "a"] -> [["a", "a"]].

Comparison is case-SENSITIVE and exact: "Tea" and "eat" are NOT
anagrams ('T' != 't'). Empty string "" is a valid word (it is an anagram
only of another "").

========================================================================
EXAMPLES
========================================================================
    >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    >>> group_anagrams([""])
    [['']]

    >>> group_anagrams(["a"])
    [['a']]

    >>> group_anagrams([])
    []

========================================================================
CONSTRAINTS
========================================================================
- `words` is a list of str, length 0 to 10_000; each word 0 to 100 chars.
- Return a `list[list[str]]` following the ordering rules above.
- Do not modify `words`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time O(n * k log k), space O(n * k) for n words of length up to k:
  each word is sorted once to build its key, then grouped in O(1).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty input list             -> []
- A single empty string [""]   -> [[""]]
- No anagrams at all           -> each word in its own group
- All words anagrams           -> one group
- Duplicate words ["ab", "ba", "ab"] -> [["ab", "ba", "ab"]]
- Case sensitivity ["Ab", "bA", "ab"] -> [["Ab", "bA"], ["ab"]]
- Group order follows first appearance

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Anagrams become IDENTICAL when you sort their letters:
   sorted("tea") == sorted("eat") == ['a', 'e', 't'].
2. A list can't be a dict key, but a tuple or a string can:
   `"".join(sorted(word))` or `tuple(sorted(word))`.
3. Build a dict: key -> list of words. `setdefault` or
   `defaultdict(list)` help here.
4. Because dicts remember insertion order, `list(groups.values())`
   already gives you groups in first-appearance order.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Designing a "canonical key" so equivalent items collide in a dict
- `sorted()` on a string returns a list of characters
- `str.join()`
- Tuples as dict keys
- `dict.values()` and converting it with `list()`

========================================================================
STRETCH GOALS
========================================================================
- Use a letter-count key instead of sorting: a tuple of 26 counts for
  lowercase-only input. What is its time complexity?
- `are_anagrams(a, b) -> bool` using `collections.Counter`.
- Make grouping case-insensitive and ignore spaces ("Dormitory" /
  "dirty room").
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Group words that are anagrams of each other.

    Args:
        words: The words to group. Not modified.

    Returns:
        A list of groups (lists of words). Groups are ordered by the first
        appearance of any of their words; words inside a group keep their
        input order.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
