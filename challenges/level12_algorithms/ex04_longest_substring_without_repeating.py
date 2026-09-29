"""
Challenge: Longest Substring Without Repeating Characters
Level:     12 - Algorithms
Topics:    sliding window, dicts / sets, string indexing
Source:    LeetCode #3 "Longest Substring Without Repeating Characters"

========================================================================
PROBLEM
========================================================================
Given a string `s`, return the LENGTH of the longest SUBSTRING that
contains no repeated characters.

A substring is a CONTIGUOUS run of characters: in "pwwkew", "wke" is a
substring but "pwke" is not (that skips a character - it would be a
"subsequence").

    s = "abcabcbb"
    substrings with all-different characters include "abc", "bca", "cab"
    longest length = 3

SLIDING WINDOW: keep a window s[left:right+1] that never contains a
repeat. Move `right` forward one character at a time. If the new
character is already in the window, move `left` forward until it isn't.
Record the largest window size you ever see.

    s = "a b c a b c b b"
         0 1 2 3 4 5 6 7

    right=0..2   window "abc"            best = 3
    right=3 'a'  'a' is at 0 in window -> left = 1, window "bca"
    right=4 'b'  'b' is at 1 in window -> left = 2, window "cab"
    ...

A dict `last_seen = {char: index}` lets you jump `left` directly past the
previous occurrence instead of stepping one at a time. Careful: only jump
FORWARD - a character last seen before `left` is outside the window and
doesn't matter.

========================================================================
EXAMPLES
========================================================================
    >>> length_of_longest_substring("abcabcbb")
    3

    >>> length_of_longest_substring("bbbbb")
    1

    >>> length_of_longest_substring("pwwkew")
    3

    >>> length_of_longest_substring("")
    0

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(s) <= 50_000.
- `s` may contain letters, digits, symbols and spaces. Characters are
  case-sensitive ("a" and "A" are different). Spaces count as characters.
- Empty string -> 0.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n) - each character enters and leaves the window at most once.
- Space: O(k) where k is the number of distinct characters.

========================================================================
EDGE CASES TO TEST
========================================================================
- "" -> 0
- Single character "a" -> 1
- All the same "bbbbb" -> 1
- All different "abcdef" -> 6
- The answer is at the end: "aab" -> 2
- The stale-index trap: "abba" -> 2 (left must never move backwards)
- Spaces and mixed case: "a A a" -> 3 ("a A" or "A a"; " A " repeats the space)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Brute force: check every substring with a set - O(n^3) but fine for
   short test strings and a useful reference.
2. Sliding window with a set: when s[right] is in the set, remove
   s[left] and move left forward, repeating until it's gone.
3. Dict version: `last_seen[ch]` = most recent index of ch.
4. For each right: if ch in last_seen and last_seen[ch] >= left, set
   left = last_seen[ch] + 1. Then update last_seen[ch] = right and
   best = max(best, right - left + 1).
5. `enumerate(s)` gives you (index, char) pairs.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `enumerate()`
- Sets: add / remove / `in`
- Dicts for "last position seen" lookups
- Slicing strings `s[a:b]` (b is exclusive) and window length right - left + 1

========================================================================
STRETCH GOALS
========================================================================
- Return the substring itself (the first longest one if tied).
- Longest substring with at most k distinct characters (LeetCode #340).
- Minimum window substring (LeetCode #76) - a harder sliding window.
"""


def length_of_longest_substring(s: str) -> int:
    """Return the length of the longest substring with no repeated chars.

    Args:
        s: The string to search (case-sensitive; spaces count).

    Returns:
        The length of the longest run of consecutive, all-different
        characters. 0 for the empty string.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
