"""
Challenge: Count Vowels
Level:     02 - Strings
Topics:    iterating over characters, the `in` operator, dicts, counting
Source:    Classic beginner exercise

========================================================================
YOUR TASK
========================================================================
Write two functions:

    count_vowels(s)  returns the TOTAL number of vowels in `s`.
    vowel_counts(s)  returns a dict saying how many times EACH vowel
                     appears in `s`.

    count_vowels("Hello World")  ->  3

========================================================================
THE RULES
========================================================================
Your functions must:
1. Count only the five vowels a, e, i, o, u. "y" is NOT a vowel here.
2. Count upper-case vowels too: "A" counts as an "a".
3. Count only the plain ASCII letters (the basic English alphabet).
   Accented letters, like an "e" with an accent, are NOT counted.
4. `count_vowels` returns the total as an int.
5. `vowel_counts` returns a dict with EXACTLY five keys: "a", "e", "i",
   "o", "u" (always lower-case). Each key maps to how many times that
   vowel appears, upper and lower case added together.
6. `vowel_counts` keeps the key for a vowel that does not appear, with
   the value 0.

So the values of vowel_counts(s) always add up to count_vowels(s).

Note: the order of the keys does not affect `==` for dicts, so tests
don't care about it. Inserting them in the order a, e, i, o, u is still
nice.

You can assume:
- `s` is a str. It may be empty.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    count_vowels("Hello World")  ->  3
        e, o and o.

    count_vowels("rhythm")       ->  0
        "y" does not count as a vowel.

    vowel_counts("Banana")
        ->  {'a': 3, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        Three a's. The other vowels still have a key, with 0.

    vowel_counts("AEIOU aeiou")
        ->  {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}
        Upper and lower case are added together.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string: count_vowels("") -> 0 and
  vowel_counts("") -> {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
- No vowels: count_vowels("rhythm"), count_vowels("xyz") and
  count_vowels("123") -> 0
- Only vowels: count_vowels("aeiou") -> 5
- Mixed case counts upper-case vowels: count_vowels("ApPlE") -> 2
- "y" is not a vowel: count_vowels("y") -> 0
- Digits, spaces and punctuation are ignored: count_vowels("a1 e!") -> 2
- The totals agree: sum(vowel_counts(s).values()) == count_vowels(s)
  for any s

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `ch in "aeiou"` is True if `ch` is one of those letters.
2. Lower-case the whole string first with s.lower(), so you only need to
   check lower-case vowels.
3. For the dict, start with {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
   (or `dict.fromkeys("aeiou", 0)`) and add 1 as you find each vowel.
4. `sum(1 for ch in s if ...)` counts matches in one line: it adds a 1
   for every character that passes the check.

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
- Re-implement vowel_counts using `collections.Counter` (a dict that
  counts things for you).
- Write `most_common_vowel(s) -> str | None` (it returns a str or None)
  giving the vowel that appears most. Ties go to the one earliest in
  "aeiou". Return None if there are no vowels.
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
