r"""
Challenge: Parse Config
Level:     06 - Errors and Parsing
Topics:    line-by-line parsing, custom exceptions, str.partition
Source:    Simplified INI / .env file parser

========================================================================
YOUR TASK
========================================================================
Write `parse_config(text)`. It reads the text of a simple config file,
made of "key = value" lines, and returns a dict that maps each key to
its value (both strings). A bad line raises a `ConfigError` that says
which line was wrong.

    parse_config("host = localhost\nport=5432")
        ->  {'host': 'localhost', 'port': '5432'}

========================================================================
BACKGROUND: THE FILE FORMAT AND ConfigError
========================================================================
Configuration files often look like this:

    # database settings      <- line 1: a comment, skipped
    host = localhost         <- line 2: key "host", value "localhost"
    port=5432                <- line 3: spaces around "=" are optional
                             <- line 4: blank, skipped
    name = my app            <- line 5: a value can contain spaces

That text gives {'host': 'localhost', 'port': '5432', 'name': 'my app'}.

`ConfigError` is a custom exception (an exception class written for
this program). It is already defined for you, just below this
docstring. Read it: it shows how a custom exception can carry extra
data. Its constructor (its `__init__`) takes a line number and a short
reason, and builds the full message from them:

    err = ConfigError(3, "missing '='")
    str(err)            # -> "line 3: missing '='"
    err.line_number     # -> 3
    err.reason          # -> "missing '='"

So you raise it with `raise ConfigError(line_number, "missing '='")`,
and callers can read `err.line_number` to find the bad line.

========================================================================
THE RULES
========================================================================
Your function must:
1. Split the text into lines with `str.splitlines()`. Number the lines
   from 1, counting EVERY line, including blank and comment lines.
2. Skip blank lines (empty, or only whitespace).
3. Skip comment lines: lines whose first non-whitespace character is
   "#". A "#" later in a line is NOT a comment. It is part of the
   value.
4. Split every other line at its FIRST "=". The part before it is the
   key, and the part after it is the value. Strip whitespace from
   both. So "url = a=b" gives the key "url" and the value "a=b".
5. Allow an empty value: "debug =" gives {"debug": ""}.
6. Treat keys as case-sensitive, and always keep values as strings (no
   converting to int or bool).
7. Return a new dict[str, str], with the keys in file order.
8. Raise `ConfigError` (not ValueError) for a bad line, created as
   `ConfigError(line_number, reason)`. The three errors, with their
   reasons and the full messages they produce:

       a line with no "="           reason: "missing '='"
                                    -> "line 3: missing '='"
       a key that is empty after    reason: "empty key"
       stripping, as in "= value"   -> "line 3: empty key"
       a key seen before            reason: "duplicate key 'host'"
                                    -> "line 7: duplicate key 'host'"

   For a duplicate, report the line of the SECOND occurrence.
9. Stop at the FIRST error, so the error reports the earliest bad
   line.
10. Not use the `configparser` module.

You can assume:
- `text` is a str.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    parse_config("host = localhost\nport=5432")
        ->  {'host': 'localhost', 'port': '5432'}
        Two lines, two keys. The spaces around "=" are stripped.

    parse_config("# comment\n\n  name =  my app  ")
        ->  {'name': 'my app'}
        Line 1 is a comment and line 2 is blank, so both are skipped.
        The space inside "my app" stays.

    parse_config("")
        ->  {}
        No lines, no keys.

    parse_config("a = 1\njunk line")
        ->  raises ConfigError: line 2: missing '='
        Line 2 has no "=". The error's line_number is 2.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty text, and text with only comments and blank lines -> {}
- Whitespace around keys, values and "=": "  a  =  1  " -> {'a': '1'}
- A value containing "=": "url = a=b" -> {'url': 'a=b'}
- A value containing "#": "color = #fff" -> {'color': '#fff'}
- An empty value: "debug =" -> {'debug': ''}
- An indented comment "   # note" is skipped
- Missing "=": "a = 1\njunk line" -> ConfigError, and
  `excinfo.value.line_number` is 2
- Empty key: "= 5" -> ConfigError with the message "line 1: empty key"
- Duplicate key: "host=a\nhost=b" -> ConfigError on line 2 (the
  SECOND occurrence)
- Line numbers count blank and comment lines too: "# c\n\nx" ->
  ConfigError on line 3
- ConfigError is a subclass of Exception, so `except Exception` would
  catch it: issubclass(ConfigError, Exception) is True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `for line_number, line in enumerate(text.splitlines(), start=1):`
2. `stripped = line.strip()`. Then skip the line if `not stripped` or
   `stripped.startswith("#")`.
3. `key, sep, value = stripped.partition("=")` splits at the first
   "=". If `sep` is "", there was no "=" at all. Strip `key` and
   `value` afterwards.
4. Check `if key in result:` BEFORE storing, to detect duplicates.
5. `raise ConfigError(line_number, "empty key")`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Custom exception classes, `super().__init__(message)`
- Exceptions carrying extra attributes (err.line_number)
- `str.splitlines()`, `str.partition()`, `str.startswith()`
- `enumerate(..., start=1)`
- `pytest.raises(...) as excinfo` and inspecting `excinfo.value` (the
  exception that was raised)

========================================================================
STRETCH GOALS
========================================================================
- Support [sections] (header lines like "[database]" that group the
  keys below them): return dict[str, dict[str, str]], with a "default"
  section for keys before the first header.
- Allow quoted values: name = "  spaced  " keeps the inner spaces.
- Add `parse_typed_config`, which converts "true"/"false" to bool and
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
