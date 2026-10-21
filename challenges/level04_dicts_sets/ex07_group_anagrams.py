"""
Challenge: Group Anagrams
Level:     04 - Dictionaries and Sets
Topics:    choosing a dict key, tuples as keys, grouping, sorted()
Source:    LeetCode #49 "Group Anagrams"

========================================================================
YOUR TASK
========================================================================
Write `group_anagrams(words)`. Put words that are anagrams of each
other into the same group, and return the list of groups (a list of
lists of words).

    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        ->  [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

========================================================================
WHAT AN "ANAGRAM" IS
========================================================================
Two words are anagrams of each other if you can rearrange the letters
of one to get the other, using every letter exactly once.

    "listen" and "silent"   ->  anagrams (same letters, new order)
    "abc" and "abcc"        ->  NOT anagrams ("abcc" has an extra c)

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a `list[list[str]]`: a list of groups, each group a list of
   words.
2. Order the groups by when their FIRST word appears in the input.
3. Keep the words inside each group in their original input order.
4. Keep duplicate words: ["a", "a"] -> [["a", "a"]].
5. Compare words exactly and case-SENSITIVELY: "Tea" and "eat" are
   NOT anagrams ('T' is not 't').
6. Treat the empty string "" as a valid word. It is an anagram only of
   another "".
7. Not change (mutate) `words`.

You can assume:
- `words` is a list of str with 0 to 10_000 words.
- Each word is 0 to 100 characters long.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        ->  [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        "eat" comes first, so its group is first. "tan" starts the
        second group and "bat" the third.

    group_anagrams([""])   ->  [['']]
        One empty word makes one group.

    group_anagrams(["a"])  ->  [['a']]
        One word makes one group.

    group_anagrams([])     ->  []
        No words, so no groups.

========================================================================
COMPLEXITY TARGET
========================================================================
- O(n * k log k) time, for n words of length up to k. Each word is
  sorted once to build its key (about k log k steps), then added to
  its group with one dict lookup, which is O(1) (the same tiny time
  however big the dict is).
- O(n * k) space: the dict stores every word, plus a key of up to k
  characters for each group.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty input list: [] -> []
- A single empty string: [""] -> [['']]
- No anagrams at all: ["abc", "def"] -> [['abc'], ['def']]
- All words anagrams: ["abc", "cab", "bca"] -> [['abc', 'cab', 'bca']]
- Duplicate words: ["ab", "ba", "ab"] -> [['ab', 'ba', 'ab']]
- Case sensitivity: ["Ab", "bA", "ab"] -> [['Ab', 'bA'], ['ab']]
- Group order follows first appearance: ["b", "a", "b"]
  -> [['b', 'b'], ['a']]

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
   already gives you the groups in first-appearance order.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Designing a "canonical key" (one standard form that all equivalent
  items share) so equivalent items land on the same dict key
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
