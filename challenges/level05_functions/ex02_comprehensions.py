"""
Challenge: Comprehensions Workout
Level:     05 - Functions, Deeper
Topics:    list/dict/set comprehensions, nested comprehensions, zip
Source:    Classic Python idiom practice

========================================================================
PROBLEM
========================================================================
A "comprehension" is a compact way to build a list, dict or set from
another iterable, in a single expression:

    [x * 2 for x in nums]                 # list comprehension
    [x for x in nums if x > 0]            # ...with a filter
    {word: len(word) for word in words}   # dict comprehension
    {word[0] for word in words}           # set comprehension

Implement the five small functions below. The rule of this challenge:
each function body should be a SINGLE `return` statement containing a
comprehension (write a loop version first if that helps, then convert).

1. `squares_of_evens(nums)`   -> list of the squares of the EVEN numbers
                                 only, in original order.
2. `word_lengths(words)`      -> dict mapping each word to its length.
                                 If a word repeats, it appears once (a
                                 dict can't have duplicate keys).
3. `unique_first_letters(words)` -> set of the first character of each
                                 word, lowercased. Empty strings are
                                 skipped (they have no first letter).
4. `flatten_matrix(matrix)`   -> one flat list of all values, row by row
                                 (left to right, top to bottom).
5. `transpose(matrix)`        -> swap rows and columns: row i of the
                                 result is column i of the input.

A "matrix" here is a list of rows, each row a list of numbers:
    [[1, 2, 3],
     [4, 5, 6]]        has 2 rows and 3 columns.
Its transpose is
    [[1, 4],
     [2, 5],
     [3, 6]]           which has 3 rows and 2 columns.

========================================================================
EXAMPLES
========================================================================
    >>> squares_of_evens([1, 2, 3, 4, -6])
    [4, 16, 36]

    >>> word_lengths(["hi", "there", "hi"])
    {'hi': 2, 'there': 5}

    >>> unique_first_letters(["Apple", "avocado", "banana", ""]) == {"a", "b"}
    True

    >>> flatten_matrix([[1, 2], [3], []])
    [1, 2, 3]

    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]

========================================================================
CONSTRAINTS
========================================================================
- All inputs are lists and must NOT be modified.
- `flatten_matrix` accepts rows of different lengths (including empty
  rows); it only flattens ONE level (no deeper nesting).
- `transpose` requires a rectangular matrix (all rows the same length).
  If rows have different lengths, raise `ValueError`.
  `transpose([])` returns `[]`. A matrix of empty rows like `[[], []]`
  has zero columns, so its transpose is `[]`.
- `transpose` must return a list of LISTS (not tuples).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty inputs for every function -> [], {}, set(), [], []
- squares_of_evens: negatives and zero (0 is even: 0 -> 0)
- word_lengths: repeated words, empty string "" -> {"": 0}
- unique_first_letters: mixed case collapses ("A" and "a" -> {"a"})
- flatten_matrix: empty rows in the middle
- transpose: a single row [[1, 2, 3]] -> [[1], [2], [3]]
- transpose: a square matrix; transposing twice gives back the original
- transpose: ragged rows [[1, 2], [3]] -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Filter goes at the end: `[expr for x in xs if condition]`.
2. Nested comprehension reads like nested for loops, in the SAME order:
   `[v for row in matrix for v in row]`.
3. Transpose: `zip(*matrix)` groups the i-th item of every row together
   (the `*` "unpacks" the rows as separate arguments to zip). Convert
   each tuple with `list(...)`.
4. For the ragged check, compare every `len(row)` with `len(matrix[0])`
   before transposing (a plain `if` + `raise` before the return is fine).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- List, dict and set comprehensions
- Conditional filtering inside comprehensions
- Nested comprehensions and their reading order
- `zip()` and argument unpacking with `*`
- Readability: when a comprehension is too clever, use a loop

========================================================================
STRETCH GOALS
========================================================================
- `transpose` without zip: `[[row[i] for row in matrix] for i in ...]`.
- A generator expression version of `squares_of_evens` and
  `sum(...)` over it without building a list.
- `flatten_deep(nested)` that flattens ANY depth (needs recursion, not
  just a comprehension).
"""


def squares_of_evens(nums: list[int]) -> list[int]:
    """Return the squares of the even numbers in nums, in order.

    Args:
        nums: A list of ints. Not modified.

    Returns:
        A new list of n * n for each even n in `nums`.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def word_lengths(words: list[str]) -> dict[str, int]:
    """Map each word to its length.

    Args:
        words: A list of strings. Not modified.

    Returns:
        A dict {word: len(word)} with one entry per distinct word.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def unique_first_letters(words: list[str]) -> set[str]:
    """Return the set of lowercased first characters of non-empty words.

    Args:
        words: A list of strings. Not modified.

    Returns:
        A set of single lowercase characters.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    """Flatten a list of rows into a single list, row by row.

    Args:
        matrix: A list of lists (rows may differ in length). Not modified.

    Returns:
        A new flat list of all values in reading order.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Return the transpose of a rectangular matrix.

    Args:
        matrix: A list of equal-length rows. Not modified.

    Returns:
        A new list of lists where result[i][j] == matrix[j][i].

    Raises:
        ValueError: If the rows are not all the same length.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
