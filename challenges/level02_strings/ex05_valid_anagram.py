"""
Challenge: Valid Anagram
Level:     02 - Strings
Topics:    counting with dicts, collections.Counter, sorted()
Source:    LeetCode #242 "Valid Anagram"

========================================================================
YOUR TASK
========================================================================
Write `is_anagram(s, t)`. It returns True if `t` is an anagram of `s`
(the same characters, rearranged), and False otherwise.

    is_anagram("listen", "silent")  ->  True

========================================================================
WHAT "ANAGRAM" MEANS
========================================================================
Two strings are ANAGRAMS if you can rearrange the characters of one to
get exactly the other, using every character exactly once. Put another
way, every character appears the SAME NUMBER OF TIMES in both:

    "listen"  has  e, i, l, n, s, t  (one of each)
    "silent"  has  e, i, l, n, s, t  (one of each)   ->  anagrams

    "rat"     has  a, r, t
    "car"     has  a, c, r                           ->  not anagrams

========================================================================
THE RULES
========================================================================
Your function must:
1. Return True when every character appears the same number of times
   in `s` and in `t`, and False otherwise.
2. Treat case as different: "A" and "a" are different characters. So
   is_anagram("Listen", "silent") is False, because the capital "L"
   does not match the lower-case "l".
3. Count every character, including spaces and punctuation. So
   is_anagram("a b", "ab") is False, because only the first one has a
   space.
4. Return True when a string is compared with itself.
5. Return a real bool: True or False.

You can assume:
- `s` and `t` are str, each up to 50_000 characters long. That is
  long, so avoid a loop inside a loop (such as calling s.count(ch)
  once for every character).

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    is_anagram("anagram", "nagaram")  ->  True
        Both have three a's and one each of g, m, n and r.

    is_anagram("rat", "car")          ->  False
        "rat" has a t, but "car" has a c instead.

    is_anagram("aab", "abb")          ->  False
        Same letters, different counts: two a's against one.

    is_anagram("", "")                ->  True
        Two empty strings contain exactly the same (no) characters.

========================================================================
EDGE CASES TO TEST
========================================================================
- A classic pair: is_anagram("listen", "silent") -> True
- Different lengths: is_anagram("ab", "abc") -> False
  (a quick exit: different lengths can never be anagrams)
- Same letters, different counts: is_anagram("aab", "abb") -> False
- Two empty strings: is_anagram("", "") -> True
- Identical strings: is_anagram("abc", "abc") -> True
- A case difference: is_anagram("Aa", "aa") -> False
- Spaces and digits count like letters: is_anagram("a 1", "1 a")
  -> True, but is_anagram("a b", "ab") -> False

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. If the lengths differ, they cannot be anagrams.
2. Easy approach: sorted(s) == sorted(t). sorted() on a string returns a
   list of its characters in order: sorted("cab") is ['a', 'b', 'c'].
3. Counting approach: build a dict {character: count} for each string
   and compare the two dicts with ==.
4. `collections.Counter(s)` builds that counting dict for you.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `sorted()` works on any iterable (anything you can loop over) and
  returns a list
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
