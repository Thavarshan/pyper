"""
Challenge: Reverse a String / Reverse Words
Level:     02 - Strings
Topics:    slicing, loops over characters, split(), join()
Source:    Classic warm-up (see also LeetCode #344 and #151)

========================================================================
PROBLEM
========================================================================
Write two functions.

1. `reverse_string(s)` returns the characters of `s` in reverse order.
   "hello" -> "olleh". Every character is reversed, including spaces
   and punctuation.

2. `reverse_words(sentence)` reverses the ORDER OF THE WORDS, but not
   the letters inside each word. "the sky is blue" -> "blue is sky the".

   A "word" is any run of non-whitespace characters. The result:
     - has no leading or trailing whitespace, and
     - has exactly ONE space between words, even if the input had
       several spaces, tabs or newlines between them.
   Punctuation stays attached to its word: "Hello, world!" ->
   "world! Hello,".

========================================================================
EXAMPLES
========================================================================
    >>> reverse_string("hello")
    'olleh'

    >>> reverse_string("ab c")
    'c ba'

    >>> reverse_words("the sky is blue")
    'blue is sky the'

    >>> reverse_words("  hello   world  ")
    'world hello'

========================================================================
CONSTRAINTS
========================================================================
- Inputs are str. They may be empty.
- reverse_string("") returns "".
- reverse_words of an empty or whitespace-only string returns "".
- Return new strings (strings are immutable, so you couldn't change the
  input anyway).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string for both functions
- A single character / a single word
- A palindrome like "racecar" reverses to itself
- reverse_string keeps spaces and punctuation in reversed positions
- reverse_words with extra spaces at the start, end and in the middle
- reverse_words with tabs/newlines between words
- Reversing twice gives back the original (reverse_string only)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Slicing: s[start:stop:step]. A step of -1 walks backwards, so s[::-1]
   is the whole string reversed.
2. `sentence.split()` with NO arguments splits on any whitespace and
   throws away empty pieces - it handles the "extra spaces" rule for you.
3. `" ".join(list_of_words)` glues a list back into one string.
4. Lists can be reversed too: words[::-1] or reversed(words).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Slicing with a negative step
- `str.split()` vs `str.split(" ")` (try both on "a  b" and compare!)
- `str.join()`
- `reversed()` and why it returns an iterator, not a list
- Strings are immutable

========================================================================
STRETCH GOALS
========================================================================
- Write reverse_string WITHOUT slicing or reversed(): loop over the
  characters and build the result yourself (prepend, or loop over
  indexes from the end).
- Write reverse_each_word("hello world") -> "olleh dlrow".
- Research why building a string with `result = ch + result` in a loop
  is slow for long strings, and how a list + "".join() fixes it.
"""


def reverse_string(s: str) -> str:
    """Return `s` with its characters in reverse order.

    Args:
        s: Any string (may be empty).

    Returns:
        A new string containing the characters of `s` reversed.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def reverse_words(sentence: str) -> str:
    """Return the words of `sentence` in reverse order.

    Args:
        sentence: Text containing words separated by whitespace.

    Returns:
        The words in reverse order joined by single spaces, with no
        leading or trailing whitespace. "" if there are no words.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
