"""
Challenge: Roman to Integer
Level:     04 - Dictionaries and Sets
Topics:    dicts as lookup tables, looking ahead in a loop, validation
Source:    LeetCode #13 "Roman to Integer"

========================================================================
YOUR TASK
========================================================================
Write `roman_to_int(s)`. It converts a Roman numeral string to an int.

    roman_to_int("MCMXCIV")  ->  1994

========================================================================
HOW ROMAN NUMERALS WORK
========================================================================
Roman numerals are written with seven letters:

    I = 1    V = 5    X = 10    L = 50    C = 100    D = 500    M = 1000

Normally the letters go from largest to smallest, left to right, and
you just add them up:

    "VIII"  =  5 + 1 + 1 + 1  =  8
    "LX"    =  50 + 10        =  60

The twist is "subtractive notation". When a SMALLER letter comes
directly before a LARGER one, the smaller one is subtracted instead of
added. There are six such pairs:

    IV = 4    IX = 9    XL = 40    XC = 90    CD = 400    CM = 900

So "MCMXCIV" breaks down like this:

    M       CM     XC     IV
    1000  + 900  + 90   + 4     =  1994

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the numeral's value as an int, using the add/subtract rule
   above.
2. Raise ValueError if `s` is empty.
3. Raise ValueError if `s` contains any character other than the
   uppercase letters I V X L C D M. This is case-sensitive, and covers
   "abc", lowercase "iv", spaces, digits and so on.
4. NOT reject "badly formed" numerals made of valid letters (like
   "IIII" or "IC"). Just apply the add/subtract rule, so "IIII" gives 4
   and "IC" gives 99. Rejecting them is a stretch goal.

You can assume:
- `s` is a str.
- For valid numerals the result is between 1 and 3999.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    roman_to_int("III")      ->  3
        1 + 1 + 1.

    roman_to_int("LVIII")    ->  58
        50 + 5 + 1 + 1 + 1. No letter is smaller than the one after
        it, so just add.

    roman_to_int("MCMXCIV")  ->  1994
        1000 + 900 (CM) + 90 (XC) + 4 (IV).

    roman_to_int("XIZ")      ->  raises ValueError
        'Z' is not a Roman numeral letter. Example message:
        invalid Roman numeral character 'Z'

========================================================================
COMPLEXITY TARGET
========================================================================
- O(n) time: one pass over the string, with no loop inside a loop.
- O(1) space: a fixed 7-entry lookup table and a few variables, the
  same however long the string is.

========================================================================
EDGE CASES TO TEST
========================================================================
- Single letters: "I" -> 1, "M" -> 1000
- Every subtractive pair: "IV" -> 4, "IX" -> 9, "XL" -> 40,
  "XC" -> 90, "CD" -> 400, "CM" -> 900
- Largest standard value: "MMMCMXCIX" -> 3999
- Empty string: "" -> raises ValueError
- Lowercase: "xiv" -> raises ValueError
- Invalid letter: "MXQ" -> raises ValueError
- Whitespace: " X " -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Store the seven values in a dict: `VALUES = {"I": 1, "V": 5, ...}`.
2. Validate first: loop over the characters and raise if one is
   `not in VALUES`.
3. For each position i, compare VALUES[s[i]] with the NEXT letter's
   value (if there is a next letter). If the next is bigger, subtract.
   Otherwise, add.
4. Alternative trick: walk the string from RIGHT to LEFT, remembering
   the value of the letter you just looked at. Subtract when the
   current value is smaller than that one, otherwise add.

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
  or "IL". (Hint: `int_to_roman(roman_to_int(s)) == s` is a neat
  check.)
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
