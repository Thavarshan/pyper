"""
Challenge: Comprehensions Workout
Level:     05 - Functions, Deeper
Topics:    list/dict/set comprehensions, nested comprehensions, zip
Source:    Classic Python idiom practice

========================================================================
YOUR TASK
========================================================================
Write five small functions. Each one builds a new list, dict or set
from its input using a comprehension:

- `squares_of_evens(nums)`: the squares of the even numbers.
- `word_lengths(words)`: a dict mapping each word to its length.
- `unique_first_letters(words)`: a set of the words' first letters.
- `flatten_matrix(matrix)`: all of a matrix's values in one flat list.
- `transpose(matrix)`: the matrix with rows and columns swapped.

    squares_of_evens([1, 2, 3, 4, -6])  ->  [4, 16, 36]

========================================================================
BACKGROUND: COMPREHENSIONS AND MATRICES
========================================================================
A "comprehension" builds a list, dict or set from another iterable
(anything you can loop over) in a single expression. These two do the
same job:

    # Loop version
    result = []
    for x in nums:
        result.append(x * 2)

    # Comprehension version: the same thing in one line
    result = [x * 2 for x in nums]

The four shapes you need:

    [x * 2 for x in nums]                 # list comprehension
    [x for x in nums if x > 0]            # ...with a filter
    {word: len(word) for word in words}   # dict comprehension
    {word[0] for word in words}           # set comprehension

A "matrix" here is a list of rows, and each row is a list of numbers:

    [[1, 2, 3],
     [4, 5, 6]]        2 rows, 3 columns

To "transpose" it, turn each column into a row. Row 0 of the result is
column 0 of the input, row 1 is column 1, and so on:

    [[1, 4],
     [2, 5],
     [3, 6]]           3 rows, 2 columns

========================================================================
THE RULES
========================================================================
Your functions must:
1. Each have a body that is a single `return` statement containing a
   comprehension. (Write a loop version first if that helps, then
   convert it.) The one exception: `transpose` may also have an `if` +
   `raise` check before its return (see hint 4).
2. Not change (mutate) any input list.
3. `squares_of_evens`: return a list of the squares of the EVEN
   numbers only, in their original order.
4. `word_lengths`: return a dict mapping each word to its length. A
   repeated word appears only once, because a dict can't have
   duplicate keys.
5. `unique_first_letters`: return a set of the first character of each
   word, lowercased. Skip empty strings (they have no first letter).
6. `flatten_matrix`: return one flat list of all the values, row by
   row (left to right, top to bottom). Rows may have different
   lengths, including empty rows. Flatten only ONE level of nesting.
7. `transpose`: return a list of LISTS (not tuples), where row i of
   the result is column i of the input.
8. `transpose`: raise `ValueError` if the rows are not all the same
   length (the matrix must be "rectangular").
9. `transpose`: return [] for []. A matrix of empty rows, like
   [[], []], has zero columns, so its transpose is also [].

You can assume:
- `nums` is a list of ints and `words` is a list of strings.
- `matrix` is a list of lists of numbers.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    squares_of_evens([1, 2, 3, 4, -6])    ->  [4, 16, 36]
        2, 4 and -6 are even. Their squares are 4, 16 and 36.

    word_lengths(["hi", "there", "hi"])   ->  {'hi': 2, 'there': 5}
        "hi" appears twice but becomes only one key.

    unique_first_letters(["Apple", "avocado", "banana", ""])
        ->  {'a', 'b'}
        "A" is lowercased, so "Apple" and "avocado" share "a". The
        empty string is skipped. (A set may print in any order, so
        compare with == in your tests.)

    flatten_matrix([[1, 2], [3], []])     ->  [1, 2, 3]
        The rows are joined in order. The empty row adds nothing.

    transpose([[1, 2, 3], [4, 5, 6]])     ->  [[1, 4], [2, 5], [3, 6]]
        Column 0 (1 and 4) becomes row 0, and so on.

    transpose([[1, 2], [3]])              ->  raises ValueError
        The rows have different lengths.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty input for every function -> [], {}, set(), [], [] (in the
  order the functions are listed above)
- squares_of_evens with negatives and zero: [0, -2] -> [0, 4]
  (0 is even)
- word_lengths with repeated words, and with an empty string:
  [""] -> {"": 0}
- unique_first_letters with mixed case: ["A", "a"] -> {"a"}
- flatten_matrix with an empty row in the middle:
  [[1], [], [2]] -> [1, 2]
- transpose of a single row: [[1, 2, 3]] -> [[1], [2], [3]]
- transpose of a square matrix: transposing twice gives back the
  original
- transpose with ragged rows (rows of different lengths):
  [[1, 2], [3]] -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. The filter goes at the end: `[expr for x in xs if condition]`.
2. A nested comprehension reads like nested for loops, in the SAME
   order. `[v for row in matrix for v in row]` means:
       for row in matrix:
           for v in row:
               ...keep v...
3. For transpose, `zip(*matrix)` groups the i-th item of every row
   together. The `*` "unpacks" the rows: it passes each row to zip as
   a separate argument. So zip(*[[1, 2], [3, 4]]) is
   zip([1, 2], [3, 4]), which gives (1, 3) and then (2, 4). Turn each
   tuple into a list with `list(...)`.
4. For the ragged check, compare every `len(row)` with
   `len(matrix[0])` before transposing. A plain `if` + `raise` before
   the return is fine.

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
- Write a generator expression version of `squares_of_evens` (like a
  list comprehension but in round brackets: it makes values one at a
  time instead of building a list), and `sum(...)` over it.
- `flatten_deep(nested)`, which flattens ANY depth, such as
  [1, [2, [3]]] -> [1, 2, 3]. This needs recursion (a function that
  calls itself), not just a comprehension.
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
