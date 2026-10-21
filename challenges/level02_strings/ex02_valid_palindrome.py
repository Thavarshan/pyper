"""
Challenge: Valid Palindrome
Level:     02 - Strings
Topics:    str.isalnum(), str.lower(), two pointers, while loops
Source:    LeetCode #125 "Valid Palindrome"

========================================================================
YOUR TASK
========================================================================
Write `is_palindrome(s)`. It returns True if `s` reads the same forwards
and backwards once you ignore upper/lower case and skip everything that
is not a letter or a digit. Otherwise it returns False.

    is_palindrome("A man, a plan, a canal: Panama")  ->  True

========================================================================
WHAT "PALINDROME" MEANS
========================================================================
A PALINDROME reads the same forwards and backwards, like "racecar" or
"noon". Letters and digits together are called ALPHANUMERIC characters.

To check a sentence, first "clean" it: keep only the alphanumeric
characters and make them lower-case. Then compare the cleaned text with
itself backwards:

    original:   "A man, a plan, a canal: Panama"
    cleaned:    "amanaplanacanalpanama"
    backwards:  "amanaplanacanalpanama"    the same, so True

========================================================================
THE RULES
========================================================================
Your function must:
1. Treat upper and lower case as the same: "A" matches "a".
2. Skip every character that is not a letter or a digit. Spaces,
   punctuation and symbols are ignored entirely.
3. Treat digits like letters: "12321" -> True, and "0P" -> False
   (0 and p differ).
4. Return True for a string with NO alphanumeric characters, including
   "". The cleaned string is empty, and an empty string reads the same
   both ways.
5. Return a real bool: True or False.

You can assume:
- `s` is a str with 0 to 200_000 characters. That is long, so go
  through the string a few times at most, not once for every character
  (no loop inside a loop).

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    is_palindrome("A man, a plan, a canal: Panama")  ->  True
        Cleaned, it is "amanaplanacanalpanama", the same backwards.

    is_palindrome("race a car")                      ->  False
        Cleaned, it is "raceacar". Backwards it is "racaecar".

    is_palindrome(" ")                               ->  True
        Nothing is left after cleaning, and empty counts as a
        palindrome.

    is_palindrome("0P")                              ->  False
        Cleaned, it is "0p". The 0 and the p differ.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string: is_palindrome("") -> True
- Only punctuation and spaces: is_palindrome(".,! ") -> True
- A single character: is_palindrome("x") -> True
- Mixed case: is_palindrome("Aa") -> True
- Digits and letters: is_palindrome("0P") -> False
- Even length: is_palindrome("abba") -> True, and odd length:
  is_palindrome("abcba") -> True
- The famous Panama sentence -> True
- A near-palindrome that differs in the middle:
  is_palindrome("abcxba") -> False

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
- Generator expressions inside "".join(...), such as
  "".join(ch for ch in s if ch.isalnum())
- The two-pointer technique with `while` loops

========================================================================
STRETCH GOALS
========================================================================
- Implement BOTH approaches (clean-and-reverse, and two pointers) and
  run the same tests against both with @pytest.mark.parametrize (a
  pytest feature that runs one test once for each input you list).
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
