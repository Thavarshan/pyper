r"""
Challenge: Word Frequency
Level:     04 - Dictionaries and Sets
Topics:    dicts as counters, string cleaning, sorting with a key function
Source:    Classic text-processing exercise

========================================================================
YOUR TASK
========================================================================
Write two functions:

- `word_frequency(text)` counts how many times each word appears in a
  piece of text. It returns a dict mapping word -> count.
- `most_common_words(text, n)` returns the `n` most frequent words as a
  list of (word, count) tuples, most frequent first.

    word_frequency("The cat and the hat.")
        ->  {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}

========================================================================
WHAT COUNTS AS A "WORD"
========================================================================
Follow these steps EXACTLY:

1. Split the text on whitespace (spaces, tabs, newlines), the same way
   `str.split()` with no arguments does.
2. From each piece, strip punctuation characters from the START and
   END only. "Punctuation" means the characters in
   `string.punctuation`:  !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
   Punctuation in the MIDDLE of a word is kept, so "don't" stays
   "don't" and "well-known" stays "well-known".
3. If a piece is empty after stripping (like a lone "--" or "!!!"), it
   is not a word. Skip it.
4. Ignore case: "The", "THE" and "the" are the same word. Store every
   word in lowercase.

For example, "Don't stop -- don't!" goes through the steps like this:

    split:    "Don't"   "stop"   "--"     "don't!"
    strip:    "Don't"   "stop"   ""       "don't"
    lower:    "don't"   "stop"   (skip)   "don't"

    result:   {"don't": 2, 'stop': 1}

========================================================================
THE RULES
========================================================================
Your functions must:
1. word_frequency: return a dict mapping each lowercase word to the
   number of times it appears, using the word steps above. Text with
   no words gives {}.
2. most_common_words: order the (word, count) tuples from most to least
   frequent.
3. most_common_words: when two words have the SAME count, put the one
   that comes first alphabetically first (the tie-break rule).
4. most_common_words: if there are fewer than `n` distinct words,
   return all of them.
5. most_common_words: return [] when `n` is 0.
6. most_common_words: raise ValueError when `n` is negative.
7. Not change anything outside the function (no global state: no
   variables kept outside the function between calls).

You can assume:
- `text` is a str. It may be empty or contain only whitespace.
- `n` is an int.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    word_frequency("The cat and the hat.")
        ->  {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
        "The" and "the" are the same word. The "." is stripped from
        the end of "hat.".

    word_frequency("Hello, hello... HELLO!")  ->  {'hello': 3}
        Case is ignored, and the punctuation at the ends is stripped.

    word_frequency("Don't stop -- don't!")
        ->  {"don't": 2, 'stop': 1}
        The apostrophe is in the MIDDLE, so it stays. "--" becomes
        empty and is skipped.

    most_common_words("b a c b a b", 2)       ->  [('b', 3), ('a', 2)]
        b appears 3 times and a twice. Only the top 2 are returned.

    most_common_words("pear apple fig", 2)
        ->  [('apple', 1), ('fig', 1)]
        All tied at 1, so alphabetical order decides.

    most_common_words("a b", -1)              ->  raises ValueError
        n can't be negative.

Note: dicts compare equal regardless of key order, so in your tests
`word_frequency(...) == {...}` works no matter which order you write
the keys in.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string: word_frequency("") -> {} and
  most_common_words("", 3) -> []
- Only punctuation: word_frequency("... !!! --") -> {}
- Mixed case: word_frequency("Go go GO") -> {'go': 3}
- Newlines and tabs: word_frequency("a\nb\ta") -> {'a': 2, 'b': 1}
- Apostrophes inside words: word_frequency("it's") -> {"it's": 1}
- n larger than the number of distinct words:
  most_common_words("a b", 5) -> [('a', 1), ('b', 1)]
- n = 0: most_common_words("a b", 0) -> []
- Ties broken alphabetically: most_common_words("pear apple fig", 3)
  -> [('apple', 1), ('fig', 1), ('pear', 1)]
- n = -1 -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `import string`, then `string.punctuation` gives you all the
   punctuation characters.
2. `"...hi!".strip(string.punctuation)` returns "hi". `strip` accepts
   a string of characters to remove from both ends.
3. Counting pattern: `counts[word] = counts.get(word, 0) + 1`.
   (Later, try `collections.Counter`.)
4. To sort by count (biggest first), then by word (A to Z), use a key
   that returns a tuple: `key=lambda pair: (-pair[1], pair[0])`.
   The minus sign makes bigger counts sort first.
5. Slicing `my_list[:n]` never fails, even if n > len(my_list).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `str.lower()`, `str.split()`, `str.strip(chars)`
- The `string` module
- dict.get(key, default) and dict.items()
- `sorted()` with a `key=` function, and tuple keys for sorting by
  more than one thing
- Tuples as lightweight records: ("word", 3)
- collections.Counter (stretch)

========================================================================
STRETCH GOALS
========================================================================
- Rewrite `word_frequency` using `collections.Counter`.
- Add a `stop_words` parameter: a set of words to ignore, such as
  "the".
- Compare your tie-breaking with `Counter.most_common()`. Does it
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
