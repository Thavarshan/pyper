"""
Challenge: Roman to Integer
Level:     04 - Dictionaries and Sets
Topics:    dicts as lookup tables, looking ahead in a loop, validation
Source:    LeetCode #13 "Roman to Integer"

========================================================================
PROBLEM
========================================================================
Roman numerals are written with seven letters:

    I = 1    V = 5    X = 10    L = 50    C = 100    D = 500    M = 1000

Normally the letters are written from largest to smallest, left to
right, and you just add them up:  "VIII" = 5 + 1 + 1 + 1 = 8,
"LX" = 50 + 10 = 60.

The twist is "subtractive notation": when a SMALLER letter comes
directly before a LARGER one, the smaller one is subtracted instead of
added. There are six such pairs:

    IV = 4    IX = 9    XL = 40    XC = 90    CD = 400    CM = 900

So "MCMXCIV" = M(1000) + CM(900) + XC(90) + IV(4) = 1994.

Write `roman_to_int(s)` that converts a Roman numeral string to an int.

Validation for this challenge:
- `s` must be non-empty and contain ONLY the uppercase letters
  I V X L C D M. Otherwise raise `ValueError` (that covers "", "abc",
  lowercase "iv", spaces, digits...).
- You do NOT need to reject "badly formed" numerals made of valid
  letters (like "IIII" or "IC"); just apply the add/subtract rule. That
  is a stretch goal.

========================================================================
EXAMPLES
========================================================================
    >>> roman_to_int("III")
    3

    >>> roman_to_int("LVIII")
    58

    >>> roman_to_int("MCMXCIV")
    1994

    >>> roman_to_int("XIZ")
    Traceback (most recent call last):
    ...
    ValueError: invalid Roman numeral character 'Z'

========================================================================
CONSTRAINTS
========================================================================
- `s` is a str. For valid numerals the result is 1..3999.
- Raise `ValueError` for an empty string or any character outside
  "IVXLCDM" (case-sensitive: lowercase is invalid).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time O(n), space O(1): one pass over the string with a fixed 7-entry
  lookup table.

========================================================================
EDGE CASES TO TEST
========================================================================
- Single letters: "I" -> 1, "M" -> 1000
- Every subtractive pair: "IV", "IX", "XL", "XC", "CD", "CM"
- Largest standard value "MMMCMXCIX" -> 3999
- Empty string ""  -> ValueError
- Lowercase "xiv"  -> ValueError
- Invalid letter "MXQ" -> ValueError
- Whitespace " X " -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Store the seven values in a dict: `VALUES = {"I": 1, "V": 5, ...}`.
2. Validate first: loop over the characters and raise if one is
   `not in VALUES`.
3. For each position i, compare VALUES[s[i]] with the NEXT letter's
   value (if there is a next letter). If the next is bigger, subtract;
   otherwise add.
4. Alternative trick: walk the string from RIGHT to LEFT, remembering
   the previous value; subtract when the current value is smaller than
   the previous one.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Dicts as constant lookup tables (UPPER_CASE names for constants)
- Indexing with `range(len(s))` vs `enumerate` vs `zip(s, s[1:])`
- Guarding against going past the end of a string
- `reversed()`
- Validating input and raising `ValueError` with a helpful message

========================================================================
STRETCH GOALS
========================================================================
- Write the inverse, `int_to_roman(n)` (LeetCode #12).
- Strict validation: reject malformed numerals like "IIII", "VV", "IC"
  or "IL". (Hint: `int_to_roman(roman_to_int(s)) == s` is a neat check.)
"""


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral string to an integer.

    Args:
        s: A non-empty string of the uppercase letters I, V, X, L, C, D, M.

    Returns:
        The integer value of the numeral.

    Raises:
        ValueError: If `s` is empty or contains any other character.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
