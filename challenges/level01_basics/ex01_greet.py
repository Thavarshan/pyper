r"""
Challenge: Greet
Level:     01 - Basics
Topics:    functions, strings, f-strings, str.strip(), conditionals
Source:    Classic "Hello, World!" warm-up

========================================================================
YOUR TASK
========================================================================
Write `greet(name)`. It RETURNS a friendly greeting for `name`. Trim
any spaces off both ends of the name first.

    greet("Ada")  ->  'Hello, Ada!'

========================================================================
WHAT "WHITESPACE" MEANS
========================================================================
Whitespace means characters you cannot see but that take up space.
The common ones are the space " ", the tab "\t" and the newline "\n".

"Stripping" a string removes whitespace from its START and END only.
Whitespace in the middle stays where it is:

    "  Ada Lovelace  "   stripped becomes   "Ada Lovelace"

========================================================================
THE RULES
========================================================================
Your function must:
1. Strip whitespace from the start and end of `name` before using it.
   Keep whitespace in the middle exactly as it is: "Mary  Jane" keeps
   its two spaces.
2. Greet the whole world, "Hello, World!", when the stripped name is
   empty. That happens when the caller passes "" or only whitespace,
   such as "   ".
3. Otherwise return exactly "Hello, <name>!": a capital H, a comma, one
   space, the stripped name and an exclamation mark.
4. Keep the name's capitalisation: greet("bob") returns "Hello, bob!".
5. RETURN the string. Do not print anything.

You can assume:
- `name` is a str. You do not need to handle other types.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    greet("Ada")         ->  'Hello, Ada!'
        A plain name goes straight into the greeting.

    greet("   Grace  ")  ->  'Hello, Grace!'
        The spaces around the name are stripped first.

    greet("")            ->  'Hello, World!'
        Nothing is left after stripping, so greet the world.

    greet(" \t\n ")      ->  'Hello, World!'
        Spaces, a tab and a newline are all whitespace, so again
        nothing is left after stripping.

========================================================================
EDGE CASES TO TEST
========================================================================
- greet("Ada")         -> 'Hello, Ada!'
- greet("  Ada  ")     -> 'Hello, Ada!'          (spaces stripped)
- greet("\tAda\n")     -> 'Hello, Ada!'          (tab, newline stripped)
- greet("")            -> 'Hello, World!'
- greet("    ")        -> 'Hello, World!'        (whitespace only)
- greet("Mary  Jane")  -> 'Hello, Mary  Jane!'   (inner spaces kept)
- greet("bob")         -> 'Hello, bob!'          (capitalisation kept)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `"  hi  ".strip()` returns "hi". Strings are immutable (they can
   never be changed), so strip() gives you a NEW string. Store it in a
   variable.
2. An empty string is "falsy" (treated as False by `if`), so
   `if not text:` is True when text == "".
3. An f-string lets you drop variables straight into text:
   f"Hello, {name}!".
4. Try to write it with only ONE return statement that builds the
   greeting. Decide what the name is first, then build the text.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Defining a function with `def` and returning a value with `return`
- The difference between `return` and `print()`
- String methods: `.strip()`, `.lstrip()`, `.rstrip()`
- f-strings: f"..." with {expressions} inside
- Truthiness: empty strings count as False in an `if`
- Type hints: `name: str` and `-> str`

========================================================================
STRETCH GOALS
========================================================================
- Add an optional parameter `greeting: str = "Hello"` (optional because
  it has a default value), so greet("Ada", greeting="Hi") returns
  "Hi, Ada!".
- Write `greet_all(names: list[str]) -> list[str]` that greets everyone
  using a list comprehension (a one-line way to build a list:
  [greet(n) for n in names]).
"""


def greet(name: str, greeting: str = "Hello") -> str:
    """Return a greeting for `name`.

    Args:
        name: The person's name. Surrounding whitespace is ignored.

    Returns:
        "Hello, <name>!" with the stripped name, or "Hello, World!" if the
        stripped name is empty.
    """
    name = name.strip() or "World"
    return f"{greeting}, {name}!"


def greet_all(names: list[str]) -> list[str]:
    return [greet(name) for name in names]
