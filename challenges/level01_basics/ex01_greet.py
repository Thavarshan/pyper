r"""
Challenge: Greet
Level:     01 - Basics
Topics:    functions, strings, f-strings, str.strip(), conditionals
Source:    Classic "Hello, World!" warm-up

========================================================================
PROBLEM
========================================================================
Write a function `greet(name)` that returns a friendly greeting string.

    - Remove any whitespace (spaces, tabs, newlines) from the START and
      END of `name` before using it. Whitespace in the middle is kept,
      so "  Ada Lovelace  " becomes "Ada Lovelace".
    - If, after stripping, the name is empty (the caller passed "" or
      only whitespace such as "   "), greet the whole world instead.
    - Otherwise return exactly "Hello, <name>!" - a capital H, a comma,
      one space, the name, and an exclamation mark.

The function RETURNS the string. It must not print anything.

"Whitespace" means characters you cannot see but that take up space:
the space " ", the tab "\t" and the newline "\n" are the common ones.

========================================================================
EXAMPLES
========================================================================
    >>> greet("Ada")
    'Hello, Ada!'

    >>> greet("   Grace  ")
    'Hello, Grace!'

    >>> greet("")
    'Hello, World!'

    >>> greet(" \t\n ")
    'Hello, World!'

========================================================================
CONSTRAINTS
========================================================================
- `name` is a str. You do not need to handle other types.
- Do not change the capitalisation of the name: greet("bob") returns
  "Hello, bob!".
- Whitespace inside the name is preserved exactly: "Mary  Jane" keeps
  its two spaces.

========================================================================
EDGE CASES TO TEST
========================================================================
- A normal name                      -> "Hello, Ada!"
- Leading and trailing spaces        -> stripped
- Tabs / newlines around the name    -> stripped
- Empty string ""                    -> "Hello, World!"
- Whitespace-only string "    "      -> "Hello, World!"
- A name with an inner space         -> inner space kept
- Lower-case name                    -> capitalisation unchanged

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `"  hi  ".strip()` returns "hi". Strings are immutable, so strip()
   gives you a NEW string - store it in a variable.
2. An empty string is "falsy": `if not text:` is True when text == "".
3. An f-string lets you drop variables straight into text:
   f"Hello, {name}!".
4. Try to write it so there is only ONE return statement building the
   greeting (hint: decide what the name is first, then build the text).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Defining a function with `def` and returning a value with `return`
- The difference between `return` and `print()`
- String methods: `.strip()`, `.lstrip()`, `.rstrip()`
- f-strings: f"..." with {expressions} inside
- Truthiness: empty strings are False in an `if`
- Type hints: `name: str` and `-> str`

========================================================================
STRETCH GOALS
========================================================================
- Add an optional parameter `greeting: str = "Hello"` so
  greet("Ada", greeting="Hi") returns "Hi, Ada!".
- Write `greet_all(names: list[str]) -> list[str]` that greets everyone
  using a list comprehension.
"""


def greet(name: str) -> str:
    """Return a greeting for `name`.

    Args:
        name: The person's name. Surrounding whitespace is ignored.

    Returns:
        "Hello, <name>!" with the stripped name, or "Hello, World!" if the
        stripped name is empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
