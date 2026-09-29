"""
Challenge: Parse Config
Level:     06 - Errors and Parsing
Topics:    line-by-line parsing, custom exceptions, str.partition
Source:    Simplified INI / .env file parser

========================================================================
PROBLEM
========================================================================
Configuration files often look like this:

    # database settings
    host = localhost
    port=5432

    name = my app

Write `parse_config(text)` that turns such text into a dict of
str -> str.

Rules (lines are numbered starting at 1, counting EVERY line, including
blank and comment lines):
1. Split the text into lines (`str.splitlines()`).
2. Ignore blank lines (empty or only whitespace).
3. Ignore comment lines: lines whose first non-whitespace character is
   "#". (A "#" later in a line is NOT a comment; it's part of the value.)
4. Every other line must contain an "=". Split it at the FIRST "=":
   the part before is the key, the part after is the value. Strip
   whitespace from both. So "url = a=b" gives key "url", value "a=b".
5. The value may be empty ("debug =" -> {"debug": ""}).
6. The key must NOT be empty after stripping.
7. Keys are case-sensitive, and values are always kept as strings (no
   conversion to int/bool).

Errors - raise `ConfigError` (a custom exception, already defined for
you below) when:
- A non-blank, non-comment line has no "=":
      message: "line 3: missing '='"
- The key is empty (e.g. "= value"):
      message: "line 3: empty key"
- A key appears a second time:
      message: "line 7: duplicate key 'host'"

The ConfigError must also carry the line number as an attribute
`line_number` (an int), so callers can do `err.line_number`. Look at
the ConfigError class below: its constructor already takes care of
this - read it to see how custom exceptions can carry extra data.

========================================================================
EXAMPLES
========================================================================
    >>> parse_config("host = localhost\\nport=5432")
    {'host': 'localhost', 'port': '5432'}

    >>> parse_config("# comment\\n\\n  name =  my app  ")
    {'name': 'my app'}

    >>> parse_config("")
    {}

    >>> parse_config("a = 1\\njunk line")
    Traceback (most recent call last):
    ...
    ConfigError: line 2: missing '='

========================================================================
CONSTRAINTS
========================================================================
- `text` is a str; the result is a new dict[str, str] whose keys are in
  file order.
- Raise ConfigError (not ValueError) for malformed lines and duplicate
  keys, created as `ConfigError(line_number, reason)` where reason is
  e.g. "missing '='" (the class builds the full message).
- Stop at the FIRST error found (report the earliest bad line).
- Do not use the `configparser` module.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty text and text with only comments/blank lines -> {}
- Whitespace around keys, values and "="
- Value containing "=" ("url = a=b") and "#" ("color = #fff")
- Empty value ("debug =") -> ""
- Indented comment "   # note" is ignored
- Missing "=" -> ConfigError, check `excinfo.value.line_number`
- Empty key "= 5" -> ConfigError
- Duplicate key -> ConfigError reporting the SECOND occurrence's line
- Line numbers count blank/comment lines too
- ConfigError is a subclass of Exception (so `except Exception` would
  catch it) - `issubclass(ConfigError, Exception)`

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `for line_number, line in enumerate(text.splitlines(), start=1):`
2. `stripped = line.strip()`; then skip if `not stripped` or
   `stripped.startswith("#")`.
3. `key, sep, value = stripped.partition("=")` - if `sep` is "" there
   was no "=" at all.
4. Check `if key in result:` BEFORE storing to detect duplicates.
5. `raise ConfigError(line_number, "empty key")`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Custom exception classes, `super().__init__(message)`
- Exceptions carrying extra attributes (err.line_number)
- `str.splitlines()`, `str.partition()`, `str.startswith()`
- `enumerate(..., start=1)`
- `pytest.raises(...) as excinfo` and inspecting `excinfo.value`

========================================================================
STRETCH GOALS
========================================================================
- Support [sections]: return dict[str, dict[str, str]] with a
  "default" section for keys before the first header.
- Allow quoted values: name = "  spaced  " keeps inner spaces.
- Add `parse_typed_config` that converts "true"/"false" to bool and
  digit-only values to int.
"""


class ConfigError(Exception):
    """Raised when config text is malformed.

    Attributes:
        line_number: The 1-based line number where the problem was found.
        reason: A short description, e.g. "missing '='".

    This class is PROVIDED for you - you don't need to change it. Create
    one with ConfigError(3, "missing '='"); str(err) is then
    "line 3: missing '='".
    """

    def __init__(self, line_number: int, reason: str) -> None:
        self.line_number = line_number
        self.reason = reason
        super().__init__(f"line {line_number}: {reason}")


def parse_config(text: str) -> dict[str, str]:
    """Parse "key = value" lines into a dict.

    Args:
        text: The config file contents.

    Returns:
        A new dict mapping keys to (stripped) string values, in file order.

    Raises:
        ConfigError: For a line with no "=", an empty key, or a duplicate
            key. The error's `line_number` is the 1-based offending line.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
