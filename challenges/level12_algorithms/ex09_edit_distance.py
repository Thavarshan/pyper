"""
Challenge: Edit Distance
Level:     12 - Algorithms
Topics:    2D dynamic programming, string comparison
Source:    LeetCode #72 "Edit Distance" (also called Levenshtein distance)

========================================================================
PROBLEM
========================================================================
Given two strings `word1` and `word2`, return the MINIMUM number of
single-character operations needed to turn word1 into word2. The
allowed operations are:

    - INSERT a character          "ros"   -> "rose"
    - DELETE a character          "horse" -> "hose"
    - REPLACE one character       "hose"  -> "rose"

    word1 = "horse", word2 = "ros"   -> 3
        horse -> rorse   (replace 'h' with 'r')
        rorse -> rose    (delete 'r')
        rose  -> ros     (delete 'e')

This is how spell checkers measure "how close" two words are.

2D DYNAMIC PROGRAMMING:
Let dp[i][j] = the edit distance between the first i characters of word1
and the first j characters of word2 (i.e. word1[:i] and word2[:j]).

Base cases (the first row and column):
    - dp[i][0] = i   (turn i characters into "" by deleting all of them)
    - dp[0][j] = j   (turn "" into j characters by inserting all of them)

For i, j >= 1, look at the LAST characters word1[i-1] and word2[j-1]:
    - If they are equal, they cost nothing:  dp[i][j] = dp[i-1][j-1]
    - Otherwise take 1 + the cheapest of:
          dp[i-1][j-1]   replace word1[i-1] with word2[j-1]  (diagonal)
          dp[i-1][j]     delete  word1[i-1]                   (from above)
          dp[i][j-1]     insert  word2[j-1]                   (from the left)

Fill the table row by row, left to right; the answer is in the
bottom-right corner, dp[len(word1)][len(word2)].

    word1 = "horse" (rows), word2 = "ros" (columns)

              ""   r    o    s
         ""    0    1    2    3
         h     1    1    2    3
         o     2    2    1    2
         r     3    2    2    2
         s     4    3    3    2
         e     5    4    4    3   <- answer: 3

    e.g. cell (o, o): the letters match, so copy the diagonal (h, r) = 1.
         cell (h, o): no match -> 1 + min(diag 1, above 2, left 1) = 2.

========================================================================
EXAMPLES
========================================================================
    >>> min_distance("horse", "ros")
    3

    >>> min_distance("intention", "execution")
    5

    >>> min_distance("", "abc")
    3

    >>> min_distance("same", "same")
    0

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(word1), len(word2) <= 500.
- Strings may contain any characters; comparison is case-sensitive
  ("a" and "A" differ).
- Both empty -> 0.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(m * n) - one step per table cell.
- Space: O(m * n) for the full table; O(min(m, n)) for the stretch goal.

========================================================================
EDGE CASES TO TEST
========================================================================
- Both empty -> 0
- One empty -> the length of the other
- Identical strings -> 0
- Single replacement: "cat" vs "cut" -> 1
- Case sensitivity: "a" vs "A" -> 1
- Symmetry: min_distance(a, b) == min_distance(b, a)
- Completely different strings of equal length -> that length

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Draw the table for a tiny example ("ab" -> "b") on paper first.
2. Create the table with a list comprehension:
   `dp = [[0] * (n + 1) for _ in range(m + 1)]`
   (NOT `[[0] * (n + 1)] * (m + 1)` - that repeats the SAME row object!)
3. Fill row 0 and column 0 with the base cases.
4. Double loop i from 1..m, j from 1..n; remember the strings are
   0-indexed, so the "last characters" are word1[i - 1] and word2[j - 1].
5. Stretch: each row only depends on the previous row - keep two rows.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- 2D lists and the `[[0] * n] * m` aliasing trap
- Off-by-one thinking: table indexes vs string indexes
- `min()` with three arguments
- `functools.cache` for a top-down version: solve(i, j) recursively

========================================================================
STRETCH GOALS
========================================================================
- Reduce space to two rows (or one row plus a variable).
- Return the list of operations, not just the count (backtrack through
  the table from the bottom-right corner).
- Longest Common Subsequence (LeetCode #1143) - a closely related table.
"""


def min_distance(word1: str, word2: str) -> int:
    """Return the minimum number of edits to turn word1 into word2.

    Args:
        word1: The starting string.
        word2: The target string.

    Returns:
        The smallest number of single-character inserts, deletes and
        replacements that transform word1 into word2.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
