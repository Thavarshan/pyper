r"""
Challenge: Title Case
Level:     02 - Strings
Topics:    split(), join(), capitalize(), enumerate(), sets / frozensets
Source:    Classic string exercise (inspired by Codewars "Title Case")

========================================================================
PROBLEM
========================================================================
Book and film titles are written in "title case": most words start with
a capital letter, but small "minor" words such as "of" or "the" stay
lower-case - unless they are the very first word.

Write `title_case(sentence, minor_words=...)` that converts `sentence`
to title case using these exact rules:

    1. Split the sentence into words on whitespace. Any amount of
       whitespace (several spaces, tabs, newlines) counts as ONE
       separator, and leading/trailing whitespace is dropped. The
       result joins the words with exactly ONE space.
    2. The FIRST word is always capitalised, even if it is a minor word.
    3. Every other word that is a minor word (compared
       case-insensitively) becomes entirely lower-case.
    4. Every other word becomes "capitalised": its first character
       upper-case and ALL the remaining characters lower-case.
       ("hELLO" -> "Hello".)

`minor_words` defaults to:
    frozenset({"a", "an", "the", "of", "and", "or", "in", "on"})

A FROZENSET is an immutable (unchangeable) set. A set is like a list
with no duplicates and super-fast `in` checks. It's used as the default
here because default arguments should never be mutable.

========================================================================
EXAMPLES
========================================================================
    >>> title_case("the lord of the rings")
    'The Lord of the Rings'

    >>> title_case("a TALE   of two  cities")
    'A Tale of Two Cities'

    >>> title_case("war and peace", minor_words=frozenset())
    'War And Peace'

    >>> title_case("   ")
    ''

========================================================================
CONSTRAINTS
========================================================================
- `sentence` is a str; it may be empty or whitespace-only -> return "".
- `minor_words` is any set/frozenset of strings. Compare in lower case,
  so a minor word written as "The" in the sentence still matches "the".
  You may assume the entries of `minor_words` are already lower-case.
- Words are NOT split on punctuation or hyphens: "well-known" is one
  word and becomes "Well-known"; "(the" is not equal to "the", so it is
  capitalised as "(the" (its first character is "(").
- Do not use `str.title()` for the whole thing (it capitalises every
  word and mishandles apostrophes: "it's".title() == "It'S").

========================================================================
EDGE CASES TO TEST
========================================================================
- First word is a minor word -> still capitalised
- Minor words in the middle -> lower-case, even if typed in CAPS
- Mixed-case words are normalised ("hELLO" -> "Hello")
- Multiple spaces / tabs between words collapse to one space
- Leading and trailing whitespace removed
- Empty string and whitespace-only string -> ""
- A single word
- A custom minor_words set (and an empty one)
- A word with an apostrophe: "it's" -> "It's"

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `sentence.split()` (no argument) handles rule 1's whitespace for you.
2. `word.capitalize()` does rule 4 exactly: "hELLO".capitalize() is
   "Hello".
3. `enumerate(words)` gives you (index, word) pairs, so you can tell
   when index == 0.
4. Collect the converted words in a list, then " ".join(...) them.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `str.split()`, `str.join()`, `str.capitalize()`, `str.lower()`
- `enumerate()` for index + value
- `set` vs `frozenset`, and fast `in` membership tests
- Why default arguments must not be mutable
- Keyword arguments: title_case(s, minor_words=...)

========================================================================
STRETCH GOALS
========================================================================
- Also always capitalise the LAST word (a common style rule).
- Preserve the original spacing instead of collapsing it (hint: look at
  `re.split(r"(\s+)", ...)`).
- Rewrite the loop as a single list comprehension.
"""

DEFAULT_MINOR_WORDS: frozenset[str] = frozenset(
    {"a", "an", "the", "of", "and", "or", "in", "on"}
)


def title_case(sentence: str, minor_words: frozenset[str] = DEFAULT_MINOR_WORDS) -> str:
    """Convert `sentence` to title case.

    Args:
        sentence: The text to convert.
        minor_words: Lower-case words that stay lower-case unless they are
            the first word.

    Returns:
        The title-cased words joined by single spaces, or "" if the
        sentence contains no words.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
