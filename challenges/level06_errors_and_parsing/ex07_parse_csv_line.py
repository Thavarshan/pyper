"""
Challenge: Parse a CSV Line
Level:     06 - Errors and Parsing
Topics:    state machines, character-by-character parsing, quoting rules
Source:    Simplified RFC 4180 (the CSV format standard)

========================================================================
PROBLEM
========================================================================
CSV ("comma-separated values") looks easy - just split on commas? But
what if a field itself contains a comma, like an address? CSV solves it
with QUOTING. Write `parse_csv_line(line)` that splits ONE line of CSV
into a list of field strings, following these rules:

1. Fields are separated by commas.
       a,b,c              -> ['a', 'b', 'c']
2. Whitespace is part of the field (it is NOT stripped).
       a, b               -> ['a', ' b']
3. Empty fields are allowed, and n commas always mean n + 1 fields.
       a,,c               -> ['a', '', 'c']
       (an empty line)    -> ['']            (one empty field)
       ,                  -> ['', '']
4. A field that STARTS with a double quote (") is a "quoted field". It
   continues until the matching closing quote. Inside it, commas are
   ordinary characters, and the surrounding quotes are NOT part of the
   value.
       "hello, world",x   -> ['hello, world', 'x']
5. Inside a quoted field, two double quotes in a row ("") stand for ONE
   literal double-quote character. This is called "escaping".
       "say ""hi"" now"   -> ['say "hi" now']
6. After a closing quote, the next character must be a comma or the end
   of the line. Anything else is an error.
       "abc"def           -> ValueError
7. A quote character that appears in the MIDDLE of an unquoted field is
   just an ordinary character.
       ab"c,d             -> ['ab"c', 'd']
8. A quoted field with no closing quote is an error:
       "abc,def           -> ValueError("unterminated quoted field")

Do NOT use the `csv` module (comparing with it is a stretch goal).
The line will not contain newline characters.

========================================================================
EXAMPLES
========================================================================
    >>> parse_csv_line("name,age,city")
    ['name', 'age', 'city']

    >>> parse_csv_line('"Smith, John",42,"New York"')
    ['Smith, John', '42', 'New York']

    >>> parse_csv_line('a,"say ""cheese"" now",c')
    ['a', 'say "cheese" now', 'c']

    >>> parse_csv_line('""')             # a quoted empty field
    ['']

    >>> parse_csv_line('"oops,1')
    Traceback (most recent call last):
    ...
    ValueError: unterminated quoted field

Tip: in your tests, use single-quoted Python strings for CSV text that
contains double quotes, as above, so you don't need backslashes.

========================================================================
CONSTRAINTS
========================================================================
- `line` is a str without "\\n". Return a list[str] with at least one
  element.
- Raise `ValueError` for an unterminated quoted field and for any
  character other than a comma directly after a closing quote.
- No `csv` module, no regular expressions (practise the loop!).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time O(n), space O(n): a single pass over the characters, building
  each field once.

========================================================================
EDGE CASES TO TEST
========================================================================
- Plain fields; spaces preserved
- Empty line "" -> ['']; "," -> ['', '']; "a," -> ['a', '']
- Quoted field containing commas
- Escaped quotes "" inside a quoted field
- Quoted empty field '""' -> [''] and '"",""' -> ['', '']
- Quote in the middle of an unquoted field is literal
- Unterminated quote '"abc' -> ValueError
- Junk after closing quote '"a"b,c' -> ValueError
- A quoted field that is last on the line, and one that is first

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Think of a "state machine": at every character you are in one of a
   few STATES, and the state decides what the character means. Useful
   states: START_OF_FIELD, IN_UNQUOTED, IN_QUOTED, AFTER_CLOSING_QUOTE.
2. Keep `fields = []` and `current = []` (a list of characters for the
   field being built); `"".join(current)` when a field ends.
3. In IN_QUOTED, when you see '"', peek at the NEXT character: if it is
   also '"', it's an escaped quote (append one '"' and skip ahead two);
   otherwise the quoted field has ended. A `while i < len(line)` loop
   with an index makes peeking easy.
4. When the loop ends: if you are still IN_QUOTED, raise the error;
   otherwise append the last field (this is why "" gives ['']).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Index-based `while` loops (when a `for` loop isn't flexible enough)
- Modelling parsing as a state machine (strings or an `enum.Enum` for
  the states)
- Building strings efficiently with a list + "".join()
- Why "just use split" breaks down on real-world data

========================================================================
STRETCH GOALS
========================================================================
- Compare your results with `next(csv.reader([line]))` on all your test
  inputs (a parametrized test is perfect). Where do they differ? (Hint:
  try '"abc"def' - the csv module is more lenient.)
- Add a `delimiter` parameter so you can parse tab-separated values.
- Write the inverse, `format_csv_line(fields)`, quoting only fields that
  need it (contain a comma, a quote, or leading/trailing spaces) and
  check that parse_csv_line(format_csv_line(f)) == f.
"""


def parse_csv_line(line: str) -> list[str]:
    """Split one CSV line into its fields, honouring double-quote rules.

    Args:
        line: A single line of CSV text (no newline characters).

    Returns:
        The list of field values (quotes removed, "" unescaped to ").
        Always at least one element.

    Raises:
        ValueError: If a quoted field is never closed, or a closing quote
            is followed by something other than a comma or end of line.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
