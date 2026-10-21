r"""
Challenge: Reverse a String / Reverse Words
Level:     02 - Strings
Topics:    slicing, loops over characters, split(), join()
Source:    Classic warm-up (see also LeetCode #344 and #151)

========================================================================
YOUR TASK
========================================================================
Write two functions:

    reverse_string(s)        returns the characters of `s` backwards.
    reverse_words(sentence)  returns the WORDS of `sentence` in reverse
                             order, each word still spelled forwards.

    reverse_string("hello")           ->  'olleh'
    reverse_words("the sky is blue")  ->  'blue is sky the'

========================================================================
WHAT A "WORD" IS
========================================================================
For `reverse_words`, a word is any run (unbroken group) of characters
that are not whitespace. Whitespace means the invisible spacing
characters: spaces, tabs and newlines. Punctuation is part of the word
it touches:

    "Hello, world!"   has two words:   Hello,   and   world!

========================================================================
THE RULES
========================================================================
Your functions must:
1. `reverse_string` reverses EVERY character, including spaces and
   punctuation: "ab c" becomes "c ba".
2. `reverse_words` reverses the ORDER of the words, not the letters
   inside them.
3. `reverse_words` returns no whitespace at the start or the end.
4. `reverse_words` puts exactly ONE space between words, even if the
   input had several spaces, tabs or newlines between them.
5. `reverse_words` keeps punctuation attached to its word:
   "Hello, world!" becomes "world! Hello,".
6. `reverse_string("")` returns "", and `reverse_words` returns "" for
   an empty or whitespace-only string.
7. Both return new strings. (Strings are immutable, meaning they can
   never be changed, so you couldn't change the input anyway.)

You can assume:
- Inputs are str. They may be empty.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    reverse_string("hello")             ->  'olleh'
        Every character, from last to first.

    reverse_string("ab c")              ->  'c ba'
        The space is a character too, so it moves as well.

    reverse_words("the sky is blue")    ->  'blue is sky the'
        The words swap order. Each word is still spelled forwards.

    reverse_words("  hello   world  ")  ->  'world hello'
        The spaces at both ends are dropped, and the gap between the
        words shrinks to one space.

========================================================================
EDGE CASES TO TEST
========================================================================
- reverse_string("") -> '' and reverse_words("") -> ''
- Whitespace only: reverse_words("   ") -> ''
- A single character or word: reverse_string("a") -> 'a' and
  reverse_words("word") -> 'word'
- A palindrome reverses to itself: reverse_string("racecar")
  -> 'racecar'
- Spaces and punctuation move too: reverse_string("Hi, you!")
  -> '!uoy ,iH'
- Extra spaces at the start, end and middle:
  reverse_words("  hello   world  ") -> 'world hello'
- Tabs and newlines between words:
  reverse_words("one\ttwo\nthree") -> 'three two one'
- Reversing twice gives back the original (reverse_string only):
  reverse_string(reverse_string("abc d!")) -> 'abc d!'

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Slicing: s[start:stop:step]. A step of -1 walks backwards, so s[::-1]
   is the whole string reversed.
2. `sentence.split()` with NO arguments splits on any whitespace and
   throws away empty pieces. It handles the "extra spaces" rule for you.
3. `" ".join(list_of_words)` glues a list back into one string, with a
   space between the pieces.
4. Lists can be reversed too: words[::-1] or reversed(words).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Slicing with a negative step
- `str.split()` vs `str.split(" ")` (try both on "a  b" and compare!)
- `str.join()`
- `reversed()` and why it returns an iterator (something you loop over
  one item at a time), not a list
- Strings are immutable

========================================================================
STRETCH GOALS
========================================================================
- Write reverse_string WITHOUT slicing or reversed(): loop over the
  characters and build the result yourself (add each character to the
  front, or loop over the indexes from the end).
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
