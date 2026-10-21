r"""
Challenge: Parse Int List
Level:     06 - Errors and Parsing
Topics:    split/strip, int(), converting and re-raising exceptions
Source:    Classic input-parsing exercise

========================================================================
YOUR TASK
========================================================================
Users type lists of numbers in all sorts of messy ways. Write
`parse_int_list(text)`. It turns a string of comma-separated integers
into a list of ints, and raises a helpful ValueError if any item is
not an integer.

    parse_int_list(" 1 ,2,   3 ")  ->  [1, 2, 3]

========================================================================
THE RULES
========================================================================
Your function must:
1. Split the items on commas ",".
2. Ignore whitespace (spaces, tabs) around each item:
   " 1 ,2,   3 " gives [1, 2, 3].
3. Return [] for an empty string, or for a string of only whitespace.
4. Accept a leading "+" or "-" sign on each item: "-5, +7" gives
   [-5, 7].
5. Raise `ValueError` for any item that is not a valid integer. That
   includes floats like "2.5", words, and EMPTY items caused by a
   stray comma ("1,,2", "1,2," or ",1").
6. Use exactly this format for the error message:

       invalid integer 'abc' at position 1

   It shows the bad item's repr after stripping whitespace (which puts
   it in quotes), and its 0-based position (the first item is
   position 0). For "1, abc, 3" the message is the one above. For
   "1,,2" it is:

       invalid integer '' at position 1

You can assume:
- `text` is a str.

Note: Python's `int()` also accepts underscores, as in "1_000". You
may accept those too. Either way is fine, so don't test it.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    parse_int_list("1, 2, 3")      ->  [1, 2, 3]
        The spaces around the items are ignored.

    parse_int_list("  42  ")       ->  [42]
        A single item with no commas is fine.

    parse_int_list("")             ->  []
        Nothing to parse.

    parse_int_list("10, 2.5, 3")
        ->  raises ValueError: invalid integer '2.5' at position 1
        "2.5" is not an integer, and it is item 1 (counting from 0).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string "" and whitespace-only "   " -> []
- A single number, with and without surrounding spaces: "7" and " 7 "
  -> [7]
- Negative and explicitly positive numbers: "-1,+2" -> [-1, 2]
- Tabs as whitespace: "1,\t2" -> [1, 2]
- A word in the middle: "1, abc, 3" -> ValueError with the message
  "invalid integer 'abc' at position 1"
- A float: "3.14" -> ValueError
- Trailing comma: "1,2," -> ValueError at position 2
- Leading comma: ",1" -> ValueError at position 0

Tip for testing messages: the `match=` in `pytest.raises(ValueError,
match=...)` is a regex (a text pattern where some characters, like
".", have special meanings). Escape those characters with
`re.escape(...)`, for example for the dot in "'2.5'".

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Handle the "empty or whitespace-only" case first:
   `if not text.strip():`.
2. `text.split(",")` gives the raw pieces ("tokens"). `enumerate`
   gives each token's position.
3. `int(" 7 ")` already ignores surrounding whitespace, but strip each
   token anyway, so the error message shows the clean token.
4. Wrap `int(token)` in try/except ValueError, and raise a NEW
   ValueError with your own message. Write `raise ... from err` to
   keep the original error attached (this is called exception
   chaining).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `str.split(sep)` vs `str.split()` (no argument): they differ on
  empty strings! Try `"".split(",")` in the REPL.
- `str.strip()`
- Converting strings with `int()` and the ValueError it raises
- Catching an exception and raising a more helpful one
- Exception chaining with `raise NewError(...) from err`
- `pytest.raises(ValueError, match=r"...")` and `re.escape`

========================================================================
STRETCH GOALS
========================================================================
- Accept ranges: "1-3, 7" -> [1, 2, 3, 7] (careful with negative
  numbers!).
- Add a `sep` parameter so "1;2;3" can be parsed with sep=";".
- Collect ALL the bad tokens and report them together in one error.
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
