"""
Challenge: Longest Substring Without Repeating Characters
Level:     12 - Algorithms
Topics:    sliding window, dicts / sets, string indexing
Source:    LeetCode #3 "Longest Substring Without Repeating Characters"

========================================================================
YOUR TASK
========================================================================
Write `length_of_longest_substring(s)`. It RETURNS the length of the
longest substring of `s` in which no character appears twice.

    length_of_longest_substring("abcabcbb")  ->  3      ("abc")

========================================================================
SUBSTRINGS AND THE SLIDING WINDOW
========================================================================
A SUBSTRING is a run of characters that sit next to each other. In
"pwwkew", "wke" is a substring, but "pwke" is not: it skips a
character. (Picking characters in order but allowing skips gives a
"subsequence", which is a different thing.)

    s = "abcabcbb"
    substrings with all-different characters include "abc", "bca", "cab"
    longest length = 3

SLIDING WINDOW: keep a "window" s[left:right+1] that never contains a
repeat. Move `right` forward one character at a time. If the new
character is already in the window, move `left` forward until it
isn't. Record the largest window size you ever see.

    s = "a b c a b c b b"
         0 1 2 3 4 5 6 7

    right=0..2   window "abc"                            best = 3
    right=3 'a'  'a' is at 0 in window -> left = 1, window "bca"
    right=4 'b'  'b' is at 1 in window -> left = 2, window "cab"
    right=5 'c'  'c' is at 2 in window -> left = 3, window "abc"
    right=6 'b'  'b' is at 4 in window -> left = 5, window "cb"
    right=7 'b'  'b' is at 6 in window -> left = 7, window "b"
    best stays 3

A dict `last_seen = {char: index}` lets you jump `left` straight past
the previous copy of a character instead of stepping one at a time.
Careful: only ever move `left` FORWARD. A character last seen before
`left` is outside the window and doesn't matter. In "abba", when the
last 'a' arrives, its old copy at index 0 is already outside the window
"b" (left = 2). Jumping left back to 1 would wrongly give 3 instead
of 2.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the length of the longest substring with no repeated
   character, as an int.
2. Treat characters as case-sensitive: "a" and "A" are different.
3. Count spaces as characters like any other.
4. Return 0 for the empty string "".

You can assume:
- `s` is a str of 0 to 50_000 characters: letters, digits, symbols and
  spaces.
- With up to 50_000 characters, checking every substring is too slow
  for big inputs: aim for one pass with a sliding window.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    length_of_longest_substring("abcabcbb")  ->  3
        "abc" (also "bca" and "cab"). See the walk-through above.

    length_of_longest_substring("bbbbb")     ->  1
        Every substring longer than 1 repeats "b".

    length_of_longest_substring("pwwkew")    ->  3
        "wke". ("pwke" is longer but is not a substring.)

    length_of_longest_substring("")          ->  0
        No characters at all.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). Each character enters the window once and leaves it at
         most once, so there is no loop inside a loop.
- Space: O(k), where k is the number of DIFFERENT characters in `s`
         (the size of your set or dict).

========================================================================
EDGE CASES TO TEST
========================================================================
- "" -> 0
- Single character: "a" -> 1
- All the same: "bbbbb" -> 1
- All different: "abcdef" -> 6
- The answer is at the end: "aab" -> 2
- The stale-index trap: "abba" -> 2 (left must never move backwards)
- Spaces and mixed case: "a A a" -> 3 ("a A" or "A a". " A " is not
  allowed because it repeats the space)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Brute force: check every substring with a set. It is O(n^3) but fine
   for short test strings, and a useful reference.
2. Sliding window with a set: when s[right] is in the set, remove
   s[left] and move left forward. Repeat until it's gone.
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
- Slicing strings `s[a:b]` (b is exclusive, so it's left out) and the
  window length right - left + 1

========================================================================
STRETCH GOALS
========================================================================
- Return the substring itself (the first longest one if tied).
- Longest substring with at most k distinct characters (LeetCode #340).
- Minimum window substring (LeetCode #76), a harder sliding window.
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
