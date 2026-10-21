r"""
Challenge: Title Case
Level:     02 - Strings
Topics:    split(), join(), capitalize(), enumerate(), sets / frozensets
Source:    Classic string exercise (inspired by Codewars "Title Case")

========================================================================
YOUR TASK
========================================================================
Write `title_case(sentence, minor_words=...)`. It returns `sentence` in
"title case", the way book and film titles are written: most words start
with a capital letter, but small "minor" words such as "of" or "the"
stay lower-case, unless they are the very first word.

    title_case("the lord of the rings")  ->  'The Lord of the Rings'

========================================================================
WHAT "MINOR WORDS" AND "CAPITALISED" MEAN
========================================================================
`minor_words` is the collection of words that stay lower-case. When the
caller leaves it out, it defaults to:

    frozenset({"a", "an", "the", "of", "and", "or", "in", "on"})

A SET is like a list with no duplicates and super-fast `in` checks. A
FROZENSET is an immutable set: it can never be changed. It's used as
the default here because default arguments should never be mutable
(changeable in place).

A word is "capitalised" when its first character is upper-case and ALL
the other characters are lower-case:

    "hELLO"  capitalised is  "Hello"

========================================================================
THE RULES
========================================================================
Your function must:
1. Split the sentence into words on whitespace (spaces, tabs,
   newlines). Any amount of whitespace counts as ONE separator, and
   whitespace at the start and end is dropped.
2. Join the converted words with exactly ONE space.
3. Always capitalise the FIRST word, even if it is a minor word.
4. Make every other word that is a minor word entirely lower-case.
   Compare in lower case, so a minor word written as "The" or "THE" in
   the sentence still matches "the".
5. Capitalise every remaining word.
6. NOT split words on punctuation or hyphens. "well-known" is one word
   and becomes "Well-known". "(the" is not equal to "the", so it is not
   a minor word. Capitalising it leaves "(the", because its first
   character is "(".
7. Return "" when `sentence` is empty or only whitespace.
8. Not use `str.title()` for the whole thing. It capitalises every word
   and mishandles apostrophes: "it's".title() gives "It'S".

You can assume:
- `sentence` is a str.
- `minor_words` is any set or frozenset of strings, and its entries are
  already lower-case.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    title_case("the lord of the rings")
        ->  'The Lord of the Rings'
        The first "the" is capitalised because it comes first. "of" and
        the second "the" are minor words, so they stay lower-case.

    title_case("a TALE   of two  cities")
        ->  'A Tale of Two Cities'
        "TALE" becomes "Tale", and the extra spaces shrink to one.

    title_case("war and peace", minor_words=frozenset())
        ->  'War And Peace'
        With an empty set there are no minor words, so "and" is
        capitalised too.

    title_case("   ")
        ->  ''
        There are no words at all.

========================================================================
EDGE CASES TO TEST
========================================================================
- First word is a minor word: title_case("of mice and men")
  -> 'Of Mice and Men'
- Minor words in the middle go lower-case, even if typed in CAPS:
  title_case("of mice AND men") -> 'Of Mice and Men'
- Mixed-case words are normalised: title_case("hELLO") -> 'Hello'
- Several spaces and tabs collapse to one space:
  title_case("the  old\tman") -> 'The Old Man'
- Leading and trailing whitespace is removed:
  title_case("  the end  ") -> 'The End'
- title_case("") -> '' and title_case("   ") -> ''
- A single word: title_case("hello") -> 'Hello'
- A custom set: title_case("the cat in the hat", frozenset({"cat"}))
  -> 'The cat In The Hat'
- An empty set: title_case("war and peace", minor_words=frozenset())
  -> 'War And Peace'
- A word with an apostrophe: title_case("it's") -> "It's"

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `sentence.split()` (no argument) handles rule 1's whitespace for you.
2. `word.capitalize()` capitalises a word exactly as rule 5 needs:
   "hELLO".capitalize() is "Hello".
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
- Keyword arguments (passing an argument by its name):
  title_case(s, minor_words=...)

========================================================================
STRETCH GOALS
========================================================================
- Also always capitalise the LAST word (a common style rule).
- Preserve the original spacing instead of collapsing it (hint: look at
  `re.split(r"(\s+)", ...)`, which splits on whitespace but keeps the
  whitespace pieces in the result).
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
