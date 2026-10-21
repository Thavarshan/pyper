r"""
Challenge: Run-Length Encoding
Level:     02 - Strings
Topics:    tracking state in loops, str.isdigit(), int(), parsing, ValueError
Source:    Classic compression exercise (see also Exercism "Run-Length Encoding")

========================================================================
YOUR TASK
========================================================================
Write two functions:

    encode(text)     compresses `text` with run-length encoding.
    decode(encoded)  turns the encoded form back into the original text.

    encode("aaabcc")  ->  'a3b1c2'

========================================================================
WHAT "RUN-LENGTH ENCODING" MEANS
========================================================================
RUN-LENGTH ENCODING (RLE) is a simple way to compress text. A "run" is
a group of the same character repeated back-to-back. Each run is
written as the character followed by how many times it repeats:

    "aaabcc"  ->  runs: aaa, b, cc  ->  a3, b1, c2  ->  "a3b1c2"

Because the counts are digits, this format can't tell "the character
5" from "a count of 5". That is why `encode` refuses text that contains
digits.

========================================================================
THE RULES
========================================================================
Your functions must:
1. `encode` writes each run as the character, then its count in
   ordinary decimal digits.
2. `encode` ALWAYS writes the count, even when it is 1: "b" -> "b1".
3. `encode` writes counts with as many digits as they need: 12 a's
   -> "a12".
4. `encode` keeps the runs in the same order as in the text.
5. `encode` is case-sensitive, and treats spaces like any other
   character: "aA" -> "a1A1", and "  " (two spaces) -> " 2".
6. `encode` raises ValueError if `text` contains a digit (a character
   for which str.isdigit() is True). Any other character (letters,
   spaces, punctuation) is fine.
7. `decode` is the exact inverse (the opposite) of `encode`, so
   decode(encode(t)) == t for every digit-free t.
8. `decode` raises ValueError for MALFORMED (badly formed) input,
   meaning any of:
     - a character that is not followed by a count ("a", "a3b")
     - a count with no character before it ("3a")
     - a count of zero, or a count with a leading zero ("a0", "a03")
9. Both return "" for "": encode("") == "" and decode("") == "".

You can assume:
- Inputs are str. They may be empty.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    encode("aaabcc")           ->  'a3b1c2'
        Three a's, one b, two c's. The count 1 is written too.

    encode("WWWWWWWWWWWWBWW")  ->  'W12B1W2'
        Twelve W's, one B, then two more W's as a separate run.

    decode("a3b1c2")           ->  'aaabcc'
        "a" three times, "b" once, "c" twice.

    decode("x2 3y1")           ->  'xx   y'
        The space is an ordinary character: " 3" means three spaces.

    encode("a1")               ->  raises ValueError
        The text contains a digit.

    decode("a03")              ->  raises ValueError
        A count may not start with 0.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string both ways: encode("") -> '' and decode("") -> ''
- A single character: encode("a") -> 'a1' and decode("a1") -> 'a'
- No repeats: encode("abc") -> 'a1b1c1' and decode("a1b1c1") -> 'abc'
- Multi-digit counts (10+ repeats): encode("x" * 10) -> 'x10'
- The same character in two separate runs: encode("aabaa") -> 'a2b1a2'
- Case sensitivity and spaces: encode("aA") -> 'a1A1' and
  encode("  ") -> ' 2'
- A digit in the text: encode("a1") -> raises ValueError
- Malformed input: decode("a"), decode("a3b"), decode("3a"),
  decode("a0") and decode("a03") -> each raises ValueError
- Round trip: decode(encode(t)) == t for several strings, such as
  "aaabcc" and "hello  world"

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. For encode, remember the CURRENT character and its count. When the
   next character differs, write out the run and start a new one.
   Don't forget to write out the LAST run after the loop ends!
2. For decode, walk through with an index `i`. At i you expect a
   non-digit character. Then collect all the digit characters that
   follow it to form the count.
3. `"12".isdigit()` is True, and `int("12")` gives 12.
4. "a" * 3 == "aaa": string repetition makes decoding each run easy.
5. `itertools.groupby` groups consecutive equal items. Try it once
   you have a loop-based solution.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Keeping "state" (the current character and its count) while looping
- Index-based `while` loops for parsing (reading structured text piece
  by piece)
- `str.isdigit()`, `int()`, `str()`
- String repetition with `*`
- Designing and raising errors for malformed input
- `itertools.groupby`

========================================================================
STRETCH GOALS
========================================================================
- Rewrite encode using `itertools.groupby` in one line.
- Rewrite decode using the `re` (regular expressions) module:
  re.findall(r"(\D)(\d+)", s) finds every "one non-digit, then one or
  more digits" pair. You still need to detect malformed input!
- Variant format: leave out the count when it is 1 ("aaab" -> "a3b").
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
