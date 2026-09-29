"""
Challenge: Parse Duration
Level:     06 - Errors and Parsing
Topics:    character-by-character parsing, validation, divmod, round-trips
Source:    Inspired by duration formats in tools like Go, systemd and CI configs

========================================================================
PROBLEM
========================================================================
Part 1 - `parse_duration(text)`

Convert a compact duration string like "1h30m15s" into a total number
of SECONDS (an int).

Format rules:
- The string is made of one or more parts; each part is a whole number
  (one or more digits 0-9) immediately followed by a unit letter:
      h = hours (3600 s)    m = minutes (60 s)    s = seconds (1 s)
- Any SUBSET of units may appear ("2h", "45m", "1h5s", "90s"), but they
  must appear in the order h, then m, then s, and each unit at most once.
- Numbers are NOT limited to their "clock" range: "90m" (= 5400) and
  "100s" are fine. Leading zeros are fine ("05m").
- Lowercase unit letters only. No spaces, signs, decimals or other
  characters anywhere.

Raise `ValueError` for anything else, including:
- an empty string ""
- a unit with no number before it ("h", "1hm")
- a number with no unit ("15", "1h30")
- an unknown unit ("5d", "5M")
- units out of order ("30m1h") or repeated ("1h2h")
- spaces, signs or decimals ("1h 30m", "-5s", "1.5h")

Part 2 - `format_duration(seconds)`

The inverse: turn a non-negative int number of seconds into the
CANONICAL (standard) string:
- Break it into hours, minutes (0-59) and seconds (0-59).
- Include only the NON-ZERO parts, in h, m, s order.
- 0 seconds is written "0s".
- Raise `ValueError` if `seconds` is negative, and `TypeError` if it is
  not an int (bools are rejected too).

For every n >= 0: parse_duration(format_duration(n)) == n.

========================================================================
EXAMPLES
========================================================================
    >>> parse_duration("1h30m15s")
    5415

    >>> parse_duration("45m")
    2700

    >>> parse_duration("1h5s")
    3605

    >>> parse_duration("30m1h")
    Traceback (most recent call last):
    ...
    ValueError: units out of order or repeated: 'h'   (example wording only)

    >>> format_duration(5415)
    '1h30m15s'

    >>> format_duration(3600)
    '1h'

    >>> format_duration(0)
    '0s'

========================================================================
CONSTRAINTS
========================================================================
- parse_duration: `text` is a str; returns an int >= 0.
  "0s" and "0h0m0s" are valid and return 0.
- parse_duration raises ValueError for every invalid case listed
  above; the message wording is up to you.
- format_duration: returns the canonical string; ValueError for
  negatives, TypeError for non-int / bool.
- Do not use `eval`. Regular expressions are allowed as a stretch goal,
  but try a plain loop first.

========================================================================
EDGE CASES TO TEST
========================================================================
- Each unit alone: "2h", "3m", "4s"
- All three units, and every pair (h+m, h+s, m+s)
- Values beyond clock range: "90m" -> 5400, "3600s" -> 3600
- Zero: "0s" -> 0, format_duration(0) -> "0s"
- Invalid: "", "15", "h", "1h30", "5d", "30m1h", "1h1h", " 1h", "1.5h",
  "-1s", "1H" (use @pytest.mark.parametrize!)
- format_duration drops zero parts: 3605 -> "1h5s", 60 -> "1m"
- format_duration(-1) -> ValueError, format_duration(1.5) -> TypeError
- Round-trip for many values: all(parse_duration(format_duration(n)) == n
  for n in range(0, 10_000, 7))

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Walk the string one character at a time, collecting digits into a
   `number` string. When you hit a letter, that letter is the unit for
   the digits you collected.
2. A dict `UNITS = {"h": 3600, "m": 60, "s": 1}` gives each unit's size
   and, since dicts are ordered, its rank: `list(UNITS).index(unit)`.
3. Track the rank of the last unit used; a new unit's rank must be
   strictly greater, which handles both "out of order" and "repeated".
4. After the loop, if `number` is not empty, the string ended with
   digits and no unit -> error.
5. For format_duration: `hours, rest = divmod(seconds, 3600)` and then
   `minutes, secs = divmod(rest, 60)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Character-by-character parsing (a tiny "state machine")
- str.isdigit() - but beware, it's True for some non-ASCII digits like
  "²"; comparing `"0" <= ch <= "9"` is stricter
- `divmod()`
- Round-trip (inverse function) testing
- `@pytest.mark.parametrize` for many invalid inputs

========================================================================
STRETCH GOALS
========================================================================
- Re-implement parse_duration with one regular expression:
  `re.fullmatch(r"(?:(\\d+)h)?(?:(\\d+)m)?(?:(\\d+)s)?", text)` - and
  handle the "matched the empty string" case.
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
