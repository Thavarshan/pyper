r"""
Challenge: Parse a CSV Line
Level:     06 - Errors and Parsing
Topics:    state machines, character-by-character parsing, quoting rules
Source:    Simplified RFC 4180 (the CSV format standard)

========================================================================
YOUR TASK
========================================================================
Write `parse_csv_line(line)`. It splits ONE line of CSV
("comma-separated values") text into a list of field strings,
following the CSV quoting rules.

    parse_csv_line('"Smith, John",42,"New York"')
        ->  ['Smith, John', '42', 'New York']

========================================================================
BACKGROUND: WHY CSV NEEDS QUOTES
========================================================================
CSV looks easy: just split on commas? But what if a field itself
contains a comma, like an address or "Smith, John"? Splitting on every
comma cuts it in two:

    '"Smith, John",42'.split(",")  ->  ['"Smith', ' John"', '42']

CSV solves this with QUOTING. Wrap a field in double quotes, and any
commas inside the quotes are ordinary characters:

    "Smith, John",42      two fields:  Smith, John   and   42

If a quoted field needs a double-quote character inside it, write two
double quotes in a row. This is called "escaping":

    "say ""hi"" now"      one field:   say "hi" now

(In this section and in THE RULES, CSV text is shown raw, the way it
would appear in a file, with no Python quotes around it.)

========================================================================
THE RULES
========================================================================
Your function must:
1. Separate fields with commas:
       a,b,c              -> ['a', 'b', 'c']
2. Keep whitespace as part of the field (do NOT strip it):
       a, b               -> ['a', ' b']
3. Allow empty fields. n commas always mean n + 1 fields:
       a,,c               -> ['a', '', 'c']
       (an empty line)    -> ['']            (one empty field)
       ,                  -> ['', '']
4. Treat a field that STARTS with a double quote (") as a "quoted
   field". It continues until the matching closing quote. Inside it,
   commas are ordinary characters, and the surrounding quotes are NOT
   part of the value:
       "hello, world",x   -> ['hello, world', 'x']
5. Inside a quoted field, read two double quotes in a row ("") as ONE
   literal double-quote character:
       "say ""hi"" now"   -> ['say "hi" now']
6. After a closing quote, require a comma or the end of the line.
   Raise ValueError for anything else:
       "abc"def           -> ValueError
7. Treat a quote in the MIDDLE of an unquoted field as an ordinary
   character:
       ab"c,d             -> ['ab"c', 'd']
8. Raise ValueError("unterminated quoted field") for a quoted field
   with no closing quote:
       "abc,def           -> ValueError: unterminated quoted field
9. Always return a list[str] with at least one element.
10. Not use the `csv` module (comparing with it is a stretch goal) or
    regular expressions. Practise the loop!

You can assume:
- `line` is a str with no newline characters ("\n").

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return. The calls use
single-quoted Python strings, so the double quotes inside them are
part of the CSV text.

    parse_csv_line("name,age,city")   ->  ['name', 'age', 'city']
        Plain fields, split on the commas.

    parse_csv_line('"Smith, John",42,"New York"')
        ->  ['Smith, John', '42', 'New York']
        The comma inside the quotes doesn't split. The quotes
        themselves are removed.

    parse_csv_line('a,"say ""cheese"" now",c')
        ->  ['a', 'say "cheese" now', 'c']
        Each "" inside the quoted field becomes one ".

    parse_csv_line('""')              ->  ['']
        A quoted field with nothing inside: one empty field.

    parse_csv_line('"oops,1')
        ->  raises ValueError: unterminated quoted field
        The quote is never closed, so the comma counts as part of the
        field, and the line ends in the middle of it.

Tip: in your tests, use single-quoted Python strings for CSV text that
contains double quotes, as above, so you don't need backslashes.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time O(n), where n is the length of the line: a single pass over the
  characters, with no loop inside a loop.
- Space O(n): each field is built once, so the extra memory grows only
  in step with the length of the line.

========================================================================
EDGE CASES TO TEST
========================================================================
- Plain fields: "a,b" -> ['a', 'b']. Spaces are kept:
  "a, b" -> ['a', ' b']
- Empty line "" -> ['']. Also "," -> ['', ''] and "a," -> ['a', '']
- A quoted field containing commas: '"a,b",c' -> ['a,b', 'c']
- Escaped quotes inside a quoted field: '"x""y"' -> ['x"y']
- Quoted empty fields: '""' -> [''] and '"",""' -> ['', '']
- A quote in the middle of an unquoted field is literal:
  'ab"c,d' -> ['ab"c', 'd']
- Unterminated quote: '"abc' -> ValueError
- Junk after a closing quote: '"a"b,c' -> ValueError
- A quoted field that is last on the line: 'x,"q"' -> ['x', 'q'], and
  one that is first: '"q",x' -> ['q', 'x']

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Think of a "state machine": at every character you are in one of a
   few STATES, and the state decides what the character means. Useful
   states: START_OF_FIELD, IN_UNQUOTED, IN_QUOTED,
   AFTER_CLOSING_QUOTE. For example, a comma in IN_QUOTED is just a
   character, but a comma in IN_UNQUOTED ends the field.
2. Keep `fields = []` and `current = []` (a list of the characters of
   the field being built). Use `"".join(current)` when a field ends.
3. In IN_QUOTED, when you see '"', peek at the NEXT character. If it
   is also '"', it's an escaped quote: append one '"' and skip ahead
   two characters. Otherwise the quoted field has ended. A
   `while i < len(line)` loop with an index `i` makes peeking easy.
4. When the loop ends: if you are still IN_QUOTED, raise the error.
   Otherwise append the last field (this is why "" gives ['']).

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
- Compare your results with `next(csv.reader([line]))` on all your
  test inputs (a parametrized test is perfect). Where do they differ?
  (Hint: try '"abc"def'. The csv module is more lenient: it returns
  ['abcdef'] instead of raising an error.)
- Add a `delimiter` parameter (the separator character) so you can
  parse tab-separated values.
- Write the inverse, `format_csv_line(fields)`, quoting only the
  fields that need it (they contain a comma, a quote, or leading or
  trailing spaces), and check that
  parse_csv_line(format_csv_line(f)) == f.
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
