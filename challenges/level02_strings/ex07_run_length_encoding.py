r"""
Challenge: Run-Length Encoding
Level:     02 - Strings
Topics:    tracking state in loops, str.isdigit(), int(), parsing, ValueError
Source:    Classic compression exercise (see also Exercism "Run-Length Encoding")

========================================================================
PROBLEM
========================================================================
RUN-LENGTH ENCODING (RLE) is a simple way to compress text. A "run" is a
group of the same character repeated back-to-back. Each run is written
as the character followed by how many times it repeats.

Write two functions:

1. `encode(text)` - compress. Format (be precise!):
     - Each run becomes: the character, then its count in decimal.
     - The count is ALWAYS written, even when it is 1: "b" -> "b1".
     - Counts can have several digits: 12 a's -> "a12".
     - Runs appear in the same order as in the text.

       "aaabcc"       -> "a3b1c2"
       "aaaaaaaaaaaa" -> "a12"
       ""             -> ""

2. `decode(encoded)` - the exact inverse, so decode(encode(t)) == t.

     "a3b1c2" -> "aaabcc"

   `decode` must raise ValueError for MALFORMED input, meaning any of:
     - a character that is not followed by a count ("a3b")
     - a count with no character before it ("3a")
     - a count of zero, or with a leading zero ("a0", "a03")

DIGITS IN THE TEXT: since counts are digits, this format can't tell
"character 5" from "count 5". So `encode` only accepts text that
contains NO digit characters; if `text` contains a digit, raise
ValueError. Any other character (letters, spaces, punctuation) is fine.

========================================================================
EXAMPLES
========================================================================
    >>> encode("aaabcc")
    'a3b1c2'

    >>> encode("WWWWWWWWWWWWBWW")
    'W12B1W2'

    >>> decode("a3b1c2")
    'aaabcc'

    >>> decode("x2 3y1")
    'xx   y'

========================================================================
CONSTRAINTS
========================================================================
- Inputs are str (may be empty; encode("") == "" and decode("") == "").
- Encoding is case-sensitive: "aA" -> "a1A1".
- Spaces are ordinary characters: "  " -> " 2".
- encode raises ValueError if `text` contains a digit (str.isdigit()).
- decode raises ValueError for the malformed cases listed above.
- Round trip: decode(encode(t)) == t for every digit-free t.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string both ways
- Single character "a" <-> "a1"
- No repeats "abc" <-> "a1b1c1"
- Multi-digit counts (10+ repeats)
- The same character in two separate runs: "aabaa" -> "a2b1a2"
- Case sensitivity and spaces
- encode with a digit in the text -> ValueError
- decode malformed: "a", "a3b", "3a", "a0", "a03" -> ValueError
- Round trip on several strings

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. For encode, remember the CURRENT character and its count. When the
   next character differs, write out the run and start a new one.
   Don't forget to write out the LAST run after the loop ends!
2. For decode, walk through with an index `i`. At i you expect a
   non-digit character; then collect all following digit characters to
   form the count.
3. `"12".isdigit()` is True; `int("12")` gives 12.
4. "a" * 3 == "aaa" - string repetition makes decoding each run easy.
5. `itertools.groupby` groups consecutive equal items - try it once
   you have a loop-based solution.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Keeping "state" (current char, count) while looping
- Index-based `while` loops for parsing
- `str.isdigit()`, `int()`, `str()`
- String repetition with `*`
- Designing and raising errors for malformed input
- `itertools.groupby`

========================================================================
STRETCH GOALS
========================================================================
- Rewrite encode using `itertools.groupby` in one line.
- Rewrite decode using the `re` module: re.findall(r"(\D)(\d+)", s)
  (and still detect malformed input!).
- Variant format: omit the count when it is 1 ("aaab" -> "a3b").
"""


def encode(text: str) -> str:
    """Run-length encode `text`.

    Args:
        text: The text to compress. Must not contain digit characters.

    Returns:
        The encoded string: each run as <character><count>, with the count
        always present.

    Raises:
        ValueError: If `text` contains a digit.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def decode(encoded: str) -> str:
    """Decode a run-length encoded string produced by `encode`.

    Args:
        encoded: A string of <character><count> pairs.

    Returns:
        The original, expanded text.

    Raises:
        ValueError: If `encoded` is malformed (missing count, count
            without a character, zero count or a count with a leading 0).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
