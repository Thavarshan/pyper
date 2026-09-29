r"""
Challenge: Word Frequency
Level:     04 - Dictionaries and Sets
Topics:    dicts as counters, string cleaning, sorting with a key function
Source:    Classic text-processing exercise

========================================================================
PROBLEM
========================================================================
Part 1 - `word_frequency(text)`

Count how many times each word appears in a piece of text and return
the counts as a dict mapping word -> count.

What counts as a "word" (follow these rules EXACTLY):
    1. Matching is case-insensitive: "The", "THE" and "the" are the same
       word. Store every word in lowercase.
    2. Split the text on whitespace (spaces, tabs, newlines), the same
       way `str.split()` with no arguments does.
    3. From each piece, strip punctuation characters from the START and
       END only. "Punctuation" means the characters in
       `string.punctuation`:  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
       Punctuation in the MIDDLE of a word is kept, so "don't" stays
       "don't" and "well-known" stays "well-known".
    4. If a piece becomes empty after stripping (e.g. a lone "--" or
       "!!!"), it is not a word and is ignored.

Part 2 - `most_common_words(text, n)`

Return the `n` most frequent words as a list of (word, count) tuples,
ordered from most to least frequent. When two words have the SAME
count, the one that comes first alphabetically goes first (tie-break
rule). If there are fewer than `n` distinct words, return all of them.

========================================================================
EXAMPLES
========================================================================
    >>> word_frequency("The cat and the hat.")
    {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}

    >>> word_frequency("Hello, hello... HELLO!")
    {'hello': 3}

    >>> word_frequency("Don't stop -- don't!")
    {"don't": 2, 'stop': 1}

    >>> most_common_words("b a c b a b", 2)
    [('b', 3), ('a', 2)]

    >>> most_common_words("pear apple fig", 2)   # all tied at 1
    [('apple', 1), ('fig', 1)]

Note: dicts compare equal regardless of key order, so in your tests
`word_frequency(...) == {...}` works no matter which order you write
the keys in.

========================================================================
CONSTRAINTS
========================================================================
- `text` is a str (it may be empty or contain only whitespace).
- `n` is an int. If `n` is negative, raise `ValueError`.
  `n == 0` returns an empty list.
- Do not modify anything outside your function (no global state).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string ""                  -> {} and most_common_words("", 3) -> []
- Only punctuation "... !!! --"    -> {}
- Mixed case "Go go GO"            -> {'go': 3}
- Newlines/tabs "a\nb\ta"         -> {'a': 2, 'b': 1}
- Apostrophes inside words "it's"  -> kept as "it's"
- n larger than the number of distinct words -> all words returned
- Ties broken alphabetically
- n = -1                           -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `import string` then `string.punctuation` gives you all punctuation.
2. `"...hi!".strip(string.punctuation)` returns "hi" - `strip` accepts
   a string of characters to remove from both ends.
3. Counting pattern: `counts[word] = counts.get(word, 0) + 1`.
   (Later, try `collections.Counter`.)
4. To sort by count descending then word ascending, use a key that
   returns a tuple: `key=lambda pair: (-pair[1], pair[0])`.
5. Slicing `my_list[:n]` never fails even if n > len(my_list).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `str.lower()`, `str.split()`, `str.strip(chars)`
- The `string` module
- dict.get(key, default) and dict.items()
- `sorted()` with a `key=` function and tuple keys for multi-level sort
- Tuples as lightweight records: ("word", 3)
- collections.Counter (stretch)

========================================================================
STRETCH GOALS
========================================================================
- Rewrite `word_frequency` using `collections.Counter`.
- Add a `stop_words` parameter (a set of words to ignore, e.g. "the").
- Compare your tie-breaking with `Counter.most_common()` - does it
  follow the same rule? (Hint: it doesn't sort ties alphabetically.)
"""


def word_frequency(text: str) -> dict[str, int]:
    """Count how often each (lowercased, punctuation-stripped) word occurs.

    Args:
        text: Any text. May be empty.

    Returns:
        A dict mapping each lowercase word to the number of times it
        appears. Empty dict if there are no words.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def most_common_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return the n most frequent words, most frequent first.

    Ties (equal counts) are ordered alphabetically by word.

    Args:
        text: Any text. May be empty.
        n: How many (word, count) pairs to return. Must be >= 0.

    Returns:
        A list of at most `n` (word, count) tuples.

    Raises:
        ValueError: If `n` is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
