r"""
Challenge: Parse Duration
Level:     06 - Errors and Parsing
Topics:    character-by-character parsing, validation, divmod, round-trips
Source:    Inspired by duration formats in tools like Go, systemd and CI configs

========================================================================
YOUR TASK
========================================================================
Write two functions that convert between duration strings and
seconds:

- `parse_duration(text)` turns a string like "1h30m15s" into a total
  number of seconds (an int).
- `format_duration(seconds)` does the reverse: it turns a number of
  seconds into the standard duration string.

    parse_duration("1h30m15s")  ->  5415
    format_duration(5415)       ->  '1h30m15s'

========================================================================
BACKGROUND: THE DURATION FORMAT
========================================================================
A duration string is made of one or more parts. Each part is a whole
number followed straight away by a unit letter:

    h = hours (3600 s)    m = minutes (60 s)    s = seconds (1 s)

    "1h30m15s"  =  1h + 30m + 15s  =  3600 + 1800 + 15  =  5415 seconds

- Any SUBSET of the units may appear ("2h", "45m", "1h5s", "90s"). But
  they must appear in the order h, then m, then s, and each unit at
  most once.
- The numbers are NOT limited to their clock range: "90m" (5400 s) and
  "100s" are fine. Leading zeros are fine too ("05m").

So several strings can mean the same duration: "90m" and "1h30m" are
both 5400 seconds. format_duration always writes the one "canonical"
(standard) form. In it, minutes and seconds stay in 0-59, and zero
parts are left out:

    5415 s  =  1 h + 1815 s  =  1 h + 30 m + 15 s   ->  "1h30m15s"
    5400 s  =  1 h + 1800 s  =  1 h + 30 m + 0 s    ->  "1h30m"

========================================================================
THE RULES
========================================================================
For `parse_duration`, your function must:
1. Return the total number of seconds as an int (>= 0).
2. Read each part as one or more digits 0-9, followed by a lowercase
   unit letter: "h", "m" or "s".
3. Accept any subset of the units, in h, m, s order, each at most
   once.
4. Accept numbers beyond the clock range, leading zeros, and zeros:
   "0s" and "0h0m0s" are valid and return 0.
5. Raise `ValueError` for anything else (the message wording is up to
   you). That includes:
   - an empty string ""
   - a unit with no number before it ("h", "1hm")
   - a number with no unit after it ("15", "1h30")
   - an unknown unit ("5d"), including an uppercase one ("5M")
   - units out of order ("30m1h") or repeated ("1h2h")
   - spaces, signs or decimals anywhere ("1h 30m", "-5s", "1.5h")
6. Not use `eval`. Regular expressions are allowed as a stretch goal,
   but try a plain loop first.

For `format_duration`, your function must:
7. Split the seconds into hours, minutes (0-59) and seconds (0-59).
8. Write only the NON-ZERO parts, in h, m, s order.
9. Return "0s" for 0 seconds.
10. Raise `TypeError` if `seconds` is not an int. A bool counts as
    "not an int" here, even though Python treats True as 1.
11. Raise `ValueError` if `seconds` is negative.

Together, the two functions must make a round trip (each undoes the
other): for every n >= 0, parse_duration(format_duration(n)) == n.

You can assume:
- `text` is a str.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    parse_duration("1h30m15s")   ->  5415
        3600 + 30 * 60 + 15.

    parse_duration("45m")        ->  2700
        45 * 60. Units can be left out.

    parse_duration("1h5s")       ->  3605
        Leaving out m in the middle is fine too.

    parse_duration("30m1h")      ->  raises ValueError
        h must come before m. (The message wording is up to you.)

    format_duration(5415)        ->  '1h30m15s'
        The reverse of the first example.

    format_duration(3600)        ->  '1h'
        Zero minutes and zero seconds are left out.

    format_duration(0)           ->  '0s'
        The one special case: zero is written "0s", not "".

========================================================================
EDGE CASES TO TEST
========================================================================
- Each unit alone: "2h" -> 7200, "3m" -> 180, "4s" -> 4
- All three units, and every pair: "1h2m" -> 3720, "1h2s" -> 3602,
  "2m3s" -> 123
- Values beyond the clock range: "90m" -> 5400, "3600s" -> 3600
- Zero: "0s" -> 0, and format_duration(0) -> "0s"
- Invalid strings, each -> ValueError: "", "15", "h", "1h30", "5d",
  "30m1h", "1h1h", " 1h", "1.5h", "-1s", "1H" (use
  @pytest.mark.parametrize to run one test over all of them!)
- format_duration leaves out zero parts: 3605 -> "1h5s", 60 -> "1m"
- format_duration(-1) -> ValueError, format_duration(1.5) -> TypeError
- Round trip for many values:
  all(parse_duration(format_duration(n)) == n
      for n in range(0, 10_000, 7))  is True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Walk the string one character at a time, collecting digits into a
   `number` string. When you hit a letter, that letter is the unit for
   the digits you collected.
2. A dict `UNITS = {"h": 3600, "m": 60, "s": 1}` gives each unit's
   size. Dicts remember their order, so it also gives each unit's rank
   (position): `list(UNITS).index(unit)` is 0 for "h", 1 for "m" and
   2 for "s".
3. Remember the rank of the last unit used. A new unit's rank must be
   strictly greater. That one check catches both "out of order" and
   "repeated".
4. After the loop, if `number` is not empty, the string ended with
   digits and no unit: that's an error.
5. For format_duration: `hours, rest = divmod(seconds, 3600)`, then
   `minutes, secs = divmod(rest, 60)`. (`divmod(a, b)` gives the
   whole-number quotient and the remainder at once:
   divmod(5415, 3600) is (1, 1815).)

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Character-by-character parsing (a tiny "state machine": code that
  remembers what it is in the middle of, such as "collecting digits",
  and treats each character based on that)
- str.isdigit(), but beware: it's True for some non-ASCII digits like
  "²". Comparing `"0" <= ch <= "9"` is stricter.
- `divmod()`
- Round-trip testing (checking that a function and its inverse undo
  each other)
- `@pytest.mark.parametrize` for many invalid inputs

========================================================================
STRETCH GOALS
========================================================================
- Re-implement parse_duration with one regular expression:
  `re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?", text)`. Then
  handle the case where it matches the empty string.
- Add "d" (days) and "ms" (milliseconds) units.
- Return a `datetime.timedelta` instead of an int.
"""


def parse_duration(text: str) -> int:
    """Convert a duration like "1h30m15s" to total seconds.

    Args:
        text: One or more <digits><unit> parts with units h, m, s used
            at most once each and in that order.

    Returns:
        The total number of seconds.

    Raises:
        ValueError: If `text` does not follow the format.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def format_duration(seconds: int) -> str:
    """Convert a number of seconds to the canonical duration string.

    Args:
        seconds: A non-negative int.

    Returns:
        A string like "1h30m15s" containing only non-zero parts, or "0s".

    Raises:
        TypeError: If `seconds` is not an int (or is a bool).
        ValueError: If `seconds` is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
