"""
Challenge: Count Vowels
Level:     02 - Strings
Topics:    iterating over characters, the `in` operator, dicts, counting
Source:    Classic beginner exercise

========================================================================
PROBLEM
========================================================================
The VOWELS for this challenge are the five letters a, e, i, o, u.
(We do NOT count "y".) Upper-case vowels count too: "A" is a vowel.

Write two functions:

1. `count_vowels(s)` returns the TOTAL number of vowels in `s` as an int.

2. `vowel_counts(s)` returns a dict with EXACTLY five keys - "a", "e",
   "i", "o", "u" (always lower-case) - mapping each vowel to how many
   times it appears in `s` (upper and lower case combined). Vowels that
   do not appear still have a key with the value 0.

========================================================================
EXAMPLES
========================================================================
    >>> count_vowels("Hello World")
    3

    >>> count_vowels("rhythm")
    0

    >>> vowel_counts("Banana")
    {'a': 3, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    >>> vowel_counts("AEIOU aeiou")
    {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}

========================================================================
CONSTRAINTS
========================================================================
- `s` is a str (may be empty).
- Only the plain ASCII letters a, e, i, o, u (either case) are vowels.
  Accented letters like "e" with an accent are NOT counted.
- vowel_counts always returns all five keys, and the values always add
  up to count_vowels(s).
- (Dict key order does not affect `==` in tests, but inserting them in
  the order a, e, i, o, u is nice.)

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string -> 0 and all-zero dict
- No vowels ("rhythm", "xyz", "123") -> 0
- Only vowels ("aeiou")
- Mixed case ("ApPlE") counts upper-case vowels
- "y" is not a vowel
- Digits, spaces and punctuation are ignored
- sum(vowel_counts(s).values()) == count_vowels(s)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `ch in "aeiou"` is True if `ch` is one of those letters.
2. Lower-case the whole string first with s.lower() so you only need to
   check lower-case vowels.
3. For the dict, start with {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
   (or `dict.fromkeys("aeiou", 0)`) and add 1 as you find each vowel.
4. `sum(1 for ch in s if ...)` counts matches in one line.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Looping over a string character by character
- Membership testing with `in`
- Creating and updating dicts: d[key] += 1
- `dict.fromkeys()`
- `collections.Counter` (great for a stretch solution)

========================================================================
STRETCH GOALS
========================================================================
- Re-implement vowel_counts using `collections.Counter`.
- Write `most_common_vowel(s) -> str | None` returning the vowel that
  appears most (ties go to the one earliest in "aeiou"; None if there
  are no vowels).
- Add a parameter `vowels: str = "aeiou"` so callers can include "y".
"""


def count_vowels(s: str) -> int:
    """Count the vowels (a, e, i, o, u, any case) in `s`.

    Args:
        s: The text to scan.

    Returns:
        The total number of vowels.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def vowel_counts(s: str) -> dict[str, int]:
    """Count each vowel in `s`, case-insensitively.

    Args:
        s: The text to scan.

    Returns:
        A dict with exactly the keys "a", "e", "i", "o", "u", each mapped
        to the number of times that vowel appears (0 if absent).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
