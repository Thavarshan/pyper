"""
Challenge: Edit Distance
Level:     12 - Algorithms
Topics:    2D dynamic programming, string comparison
Source:    LeetCode #72 "Edit Distance" (also called Levenshtein distance)

========================================================================
YOUR TASK
========================================================================
Write `min_distance(word1, word2)`. It RETURNS the smallest number of
single-character edits that turn word1 into word2. An edit is an
insert, a delete or a replace of one character.

    min_distance("horse", "ros")  ->  3

========================================================================
THE THREE EDITS, AND A 2D DYNAMIC PROGRAMMING TABLE
========================================================================
The allowed edits:

    - INSERT a character          "ros"   -> "rose"
    - DELETE a character          "horse" -> "hose"
    - REPLACE one character       "hose"  -> "rose"

    word1 = "horse", word2 = "ros"   -> 3
        horse -> rorse   (replace 'h' with 'r')
        rorse -> rose    (delete 'r')
        rose  -> ros     (delete 'e')

This is how spell checkers measure how close two words are.

DYNAMIC PROGRAMMING (DP) builds the answer from answers to smaller
versions of the same problem, stored in a table. Here the table is 2D
(rows and columns):

Let dp[i][j] = the edit distance between the first i characters of
word1 and the first j characters of word2 (word1[:i] and word2[:j]).

Base cases (the first row and the first column):
    - dp[i][0] = i   (turn i characters into "" by deleting all of them)
    - dp[0][j] = j   (turn "" into j characters by inserting all of them)

For i, j >= 1, look at the LAST characters, word1[i-1] and word2[j-1]:
    - If they are equal, they cost nothing:  dp[i][j] = dp[i-1][j-1]
    - Otherwise take 1 + the cheapest of:
          dp[i-1][j-1]   replace word1[i-1] with word2[j-1]  (diagonal)
          dp[i-1][j]     delete  word1[i-1]                   (from above)
          dp[i][j-1]     insert  word2[j-1]                   (from the left)

Fill the table row by row, left to right. The answer is in the
bottom-right corner, dp[len(word1)][len(word2)].

    word1 = "horse" (rows), word2 = "ros" (columns)

              ""   r    o    s
         ""    0    1    2    3
         h     1    1    2    3
         o     2    2    1    2
         r     3    2    2    2
         s     4    3    3    2
         e     5    4    4    3   <- answer: 3

    Cell (row o, column o): the letters match, so copy the diagonal
    cell (row h, column r), which is 1.
    Cell (row h, column o): no match, so 1 + min(diagonal 1, above 2,
    left 1) = 2.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the smallest number of single-character inserts, deletes and
   replacements that turn word1 into word2.
2. Compare characters case-sensitively: "a" and "A" are different.
3. Return 0 when both strings are empty.

You can assume:
- `word1` and `word2` are strings of 0 to 500 characters each.
- They may contain any characters.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    min_distance("horse", "ros")            ->  3
        See the steps and the table above.

    min_distance("intention", "execution")  ->  5
        For example: delete 't', then replace 'i' -> 'e',
        'n' -> 'x', 'n' -> 'c', and insert 'u'.

    min_distance("", "abc")                 ->  3
        Insert all 3 characters.

    min_distance("same", "same")            ->  0
        Already equal, so no edits.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(m * n), where m and n are the two lengths. One step per
         table cell.
- Space: O(m * n) for the full table. O(min(m, n)) for the stretch
         goal, which keeps only two rows.

========================================================================
EDGE CASES TO TEST
========================================================================
- Both empty: min_distance("", "") -> 0
- One empty -> the length of the other: ("abc", "") -> 3
- Identical strings: ("same", "same") -> 0
- Single replacement: ("cat", "cut") -> 1
- Case sensitivity: ("a", "A") -> 1
- Symmetry: min_distance(a, b) == min_distance(b, a), for example
  ("horse", "ros") and ("ros", "horse") both give 3
- Completely different strings of equal length -> that length:
  ("abc", "xyz") -> 3

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Draw the table for a tiny example ("ab" -> "b", answer 1) on paper
   first.
2. Create the table with a list comprehension:
   `dp = [[0] * (n + 1) for _ in range(m + 1)]`
   NOT `[[0] * (n + 1)] * (m + 1)`: that repeats the SAME row object,
   so changing one row changes them all.
3. Fill row 0 and column 0 with the base cases.
4. Double loop: i from 1 to m, j from 1 to n. Remember the strings are
   0-indexed (they start at index 0), so the "last characters" are
   word1[i - 1] and word2[j - 1].
5. Stretch: each row only depends on the previous row, so keep just two
   rows.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- 2D lists and the `[[0] * n] * m` aliasing trap (aliasing: two names
  for the same object)
- Off-by-one thinking: table indexes vs string indexes
- `min()` with three arguments
- `functools.cache` for a top-down version: solve(i, j) recursively

========================================================================
STRETCH GOALS
========================================================================
- Reduce space to two rows (or one row plus a variable).
- Return the list of operations, not just the count (backtrack through
  the table from the bottom-right corner: at each cell, see which
  neighbour the value came from).
- Longest Common Subsequence (LeetCode #1143), a closely related table.
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
