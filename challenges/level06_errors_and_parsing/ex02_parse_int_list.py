"""
Challenge: Parse Int List
Level:     06 - Errors and Parsing
Topics:    split/strip, int(), converting and re-raising exceptions
Source:    Classic input-parsing exercise

========================================================================
PROBLEM
========================================================================
Users type lists of numbers in all sorts of messy ways. Write
`parse_int_list(text)` that turns a comma-separated string of integers
into a list of ints.

Rules:
1. Items are separated by commas ",".
2. Whitespace (spaces, tabs) around each item is ignored:
   " 1 ,2,   3 " -> [1, 2, 3].
3. An empty string, or a string of only whitespace, gives [].
4. Each item may have a leading "+" or "-" sign: "-5, +7" -> [-5, 7].
5. Anything else is an error. Raise `ValueError` if an item is not a
   valid integer, INCLUDING an empty item caused by a stray comma
   ("1,,2", "1,2," or ",1").
6. The error message must name the bad token (in quotes, using its
   repr, after stripping whitespace) and its 0-based position in the
   list, in exactly this format:

       invalid integer 'abc' at position 1

   For "1, abc, 3" that is the message above. For "1,,2" it is:

       invalid integer '' at position 1

========================================================================
EXAMPLES
========================================================================
    >>> parse_int_list("1, 2, 3")
    [1, 2, 3]

    >>> parse_int_list("  42  ")
    [42]

    >>> parse_int_list("")
    []

    >>> parse_int_list("10, 2.5, 3")
    Traceback (most recent call last):
    ...
    ValueError: invalid integer '2.5' at position 1

========================================================================
CONSTRAINTS
========================================================================
- `text` is a str.
- Return a `list[int]`.
- Floats like "2.5", words, and empty items are invalid -> ValueError.
- Python's `int()` also accepts underscores ("1_000") - you may accept
  those too (it's fine either way; don't test it).
- Error messages follow the exact format above so tests can use
  `pytest.raises(ValueError, match=...)`.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string "" and whitespace-only "   " -> []
- Single number, with and without surrounding spaces
- Negative and explicitly positive numbers "-1,+2" -> [-1, 2]
- Tabs as whitespace "1,\\t2" -> [1, 2]
- A word in the middle -> message mentions the word and position 1
- A float "3.14" -> ValueError
- Trailing comma "1,2," -> ValueError at position 2
- Leading comma ",1" -> ValueError at position 0
- Hint for testing messages: `match` is a regex, so escape special
  characters with `re.escape(...)` (e.g. for "'2.5'", the dot).

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Check the "empty/whitespace-only" case first: `if not text.strip():`.
2. `text.split(",")` gives the raw tokens; `enumerate` gives positions.
3. `int(" 7 ")` already tolerates surrounding whitespace, but strip
   anyway so the error message shows the clean token.
4. Wrap `int(token)` in try/except ValueError, and raise a NEW
   ValueError with your own message. Use `raise ... from err` to keep
   the original error attached (exception chaining).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `str.split(sep)` vs `str.split()` (no argument) - they differ on
  empty strings! Try `"".split(",")` in the REPL.
- `str.strip()`
- Converting strings with `int()` and the ValueError it raises
- Catching an exception and raising a more helpful one
- Exception chaining with `raise NewError(...) from err`
- `pytest.raises(ValueError, match=r"...")` and `re.escape`

========================================================================
STRETCH GOALS
========================================================================
- Accept ranges: "1-3, 7" -> [1, 2, 3, 7] (careful with negative numbers!).
- Add a `sep` parameter so "1;2;3" can be parsed with sep=";".
- Collect ALL bad tokens and report them together in one error.
"""


def parse_int_list(text: str) -> list[int]:
    """Parse a comma-separated string of integers.

    Args:
        text: e.g. "1, 2, 3". Whitespace around items is ignored; an empty
            or whitespace-only string gives [].

    Returns:
        The list of parsed ints, in order.

    Raises:
        ValueError: If any item is not a valid integer, with the message
            "invalid integer '<token>' at position <index>".
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
