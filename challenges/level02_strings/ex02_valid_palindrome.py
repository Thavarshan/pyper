"""
Challenge: Valid Palindrome
Level:     02 - Strings
Topics:    str.isalnum(), str.lower(), two pointers, while loops
Source:    LeetCode #125 "Valid Palindrome"

========================================================================
PROBLEM
========================================================================
A PALINDROME reads the same forwards and backwards, like "racecar" or
"noon".

Write `is_palindrome(s)` that returns True if `s` is a palindrome once
you:
    - ignore upper/lower case ("A" and "a" count as the same), and
    - ignore every character that is not a letter or a digit (spaces,
      punctuation, symbols are skipped entirely).

Such letters-and-digits characters are called ALPHANUMERIC.

So "A man, a plan, a canal: Panama" is a palindrome, because after
cleaning it becomes "amanaplanacanalpanama".

========================================================================
EXAMPLES
========================================================================
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True

    >>> is_palindrome("race a car")
    False

    >>> is_palindrome(" ")
    True

    >>> is_palindrome("0P")
    False

========================================================================
CONSTRAINTS
========================================================================
- `s` is a str, 0 <= len(s) <= 200_000.
- A string with NO alphanumeric characters (including "") counts as a
  palindrome -> True (the cleaned string is empty, and empty reads the
  same both ways).
- Digits count: "12321" -> True, "0P" -> False (0 and p differ).
- Return a real bool.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string ""                      -> True
- Only punctuation/spaces, e.g. ".,! " -> True
- Single character                     -> True
- Mixed case "Aa"                      -> True
- Digits and letters, "0P"             -> False
- Even-length and odd-length palindromes
- The famous Panama sentence           -> True
- A near-palindrome that differs in the middle -> False

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `ch.isalnum()` is True for letters and digits.
2. Simple approach: build a cleaned, lower-cased string, then compare it
   with its reverse (cleaned[::-1]).
3. That builds extra strings. The TWO POINTER approach avoids it: put
   `left` at index 0 and `right` at the last index, and move them toward
   each other, skipping non-alphanumeric characters.
4. With two pointers, loop `while left < right:` and compare
   s[left].lower() with s[right].lower().

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `str.isalnum()`, `str.isalpha()`, `str.isdigit()`
- `str.lower()` (and `str.casefold()` for international text)
- Generator expressions inside "".join(...)
- The two-pointer technique with `while` loops

========================================================================
STRETCH GOALS
========================================================================
- Implement BOTH approaches (clean-and-reverse, and two pointers) and
  run the same tests against both with @pytest.mark.parametrize.
- LeetCode #680 "Valid Palindrome II": return True if the string can be
  a palindrome after deleting AT MOST one character.
"""


def is_palindrome(s: str) -> bool:
    """Return True if `s` is a palindrome, ignoring case and non-alphanumerics.

    Args:
        s: The text to check.

    Returns:
        True if the lower-cased alphanumeric characters of `s` read the
        same forwards and backwards, otherwise False.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
