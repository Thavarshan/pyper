"""
Challenge: First Unique Character
Level:     04 - Dictionaries and Sets
Topics:    counting with dicts, two-pass algorithms, enumerate
Source:    LeetCode #387 "First Unique Character in a String"

========================================================================
YOUR TASK
========================================================================
Write `first_unique_char(s)`. Find the FIRST character that appears
exactly once in the whole string, and return its index (position,
counting from 0). If there is no such character, return -1.

    first_unique_char("loveleetcode")  ->  2

========================================================================
WHAT "UNIQUE" MEANS
========================================================================
"Unique" here means "occurs exactly one time in the ENTIRE string". It
does not mean "different from its neighbours". In "abca":

    'a'  appears 2 times  ->  not unique
    'b'  appears 1 time   ->  unique, and it comes first
    'c'  appears 1 time   ->  unique, but later

So the answer is 1, the index of 'b'.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the index of the first character that occurs exactly once.
2. Return -1 if every character repeats, or the string is empty. Here
   -1 is a sentinel (a special stand-in value) that means "not found".
3. Compare characters exactly as they are. This is case-SENSITIVE, so
   'a' and 'A' are different characters. Spaces and punctuation are
   characters too.
4. Return an int: a valid index, or -1.

You can assume:
- `s` is a str of length 0 to 100_000.
- Any characters can appear: letters, digits, spaces, emoji and so on.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    first_unique_char("leetcode")      ->  0
        'l' appears only once, and it is the first character.

    first_unique_char("loveleetcode")  ->  2
        'l' and 'o' both appear twice. 'v', at index 2, appears once.

    first_unique_char("aabb")          ->  -1
        Every character repeats.

    first_unique_char("aA")            ->  0
        'a' and 'A' are different, so both are unique. 'a' comes
        first.

========================================================================
COMPLEXITY TARGET
========================================================================
- O(n) time: one pass to count, one pass to find the first count of 1.
  Two passes one after the other, with no loop inside a loop.
- O(k) space, where k is the number of distinct (different)
  characters: the dict holds one count per different character.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string: "" -> -1
- Single character: "z" -> 0
- All repeated: "aabbcc" -> -1
- Unique character is last: "aabbc" -> 4
- Case sensitivity: "aA" -> 0, and "aAa" -> 1
- Spaces count as characters: "a a" -> 1 (the space)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. You can't know whether a character is unique until you've seen the
   whole string. So do it in two passes.
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
- Solve it with a brute-force `s.count(ch)` inside the loop, and
  explain why that is O(n^2). (Each s.count scans the whole string, and
  you do it once per character.)
- Write `first_unique_char_value(s) -> str | None`, which returns the
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
