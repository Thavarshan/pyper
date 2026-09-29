"""
Challenge: Generate Parentheses
Level:     07 - Recursion
Topics:    backtracking with constraints (pruning), string building
Source:    LeetCode #22 "Generate Parentheses"

========================================================================
PROBLEM
========================================================================
A string of parentheses is WELL-FORMED (or "balanced") when every "("
has a matching ")" that comes after it, and brackets never close before
they are opened. For example:

    well-formed:     "()",  "(())",  "()()",  "(()())"
    NOT well-formed: ")(",  "(()",   "())(",  "((("

Write `generate_parentheses(n)` that returns ALL well-formed strings
made of exactly `n` pairs of parentheses (so each string has length
2 * n), with no duplicates.

To make results deterministic, return the list SORTED in normal Python
string order (`sorted()`). In ASCII "(" comes before ")", so "((...))"
comes first.

The number of results grows like the Catalan numbers:
n = 0, 1, 2, 3, 4, 5  ->  1, 1, 2, 5, 14, 42 strings.

The smart recursive approach builds the string one character at a time
and PRUNES (skips) any branch that could never become well-formed,
instead of generating all 2**(2n) strings and filtering.

========================================================================
EXAMPLES
========================================================================
    >>> generate_parentheses(1)
    ['()']

    >>> generate_parentheses(2)
    ['(())', '()()']

    >>> generate_parentheses(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']

    >>> generate_parentheses(0)
    ['']

========================================================================
CONSTRAINTS
========================================================================
- `n` is an int, 0 <= n <= 10.
- n = 0 returns [''] (one way to use zero pairs: the empty string).
- If `n` is negative, raise `ValueError`. If `n` is not an int, raise
  `TypeError`.
- Return a sorted `list[str]` with no duplicates.
- Must be recursive (backtracking). Don't brute-force all 2**(2n)
  strings and filter them.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  roughly proportional to (number of results) * n, since
  pruning means you never explore a dead-end branch.
- Space: O(n) call stack depth (plus the output list).

========================================================================
EDGE CASES TO TEST
========================================================================
- n = 0 -> ['']
- n = 1 -> ['()']
- n = 3 -> exactly the five strings in EXAMPLES, in that order
- Count matches Catalan numbers: n=4 -> 14, n=5 -> 42
- Every string has length 2 * n
- Every string is well-formed (write a small `is_balanced` helper in
  your test file that keeps a running counter)
- No duplicates: len(set(result)) == len(result)
- The result is sorted: result == sorted(result)
- n = -1 -> ValueError; n = "3" -> TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Track two counts while building: how many "(" you have used
   (`opened`) and how many ")" (`closed`).
2. You may add "(" only while opened < n.
3. You may add ")" only while closed < opened (otherwise you would be
   closing a bracket that was never opened).
4. Base case: when the string's length is 2 * n, it is complete - add it
   to the results.
5. Strings are immutable, so passing `current + "("` into the recursive
   call automatically "undoes" the choice when the call returns.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Backtracking with pruning (only explore valid branches)
- Passing state (counters, partial strings) through recursive calls
- String immutability and concatenation
- Sorting strings and character ordering (`ord("(") < ord(")")`)

========================================================================
STRETCH GOALS
========================================================================
- Write `is_valid(s)` for strings with "()[]{}" (LeetCode #20).
- Compute just the COUNT of results for n up to 100 without generating
  them (Catalan formula or dynamic programming).
- Turn your function into a generator that yields strings in sorted
  order without needing a final sort.
"""


def generate_parentheses(n: int) -> list[str]:
    """Return all well-formed strings of `n` pairs of parentheses.

    Must be implemented recursively (backtracking).

    Args:
        n: The number of "()" pairs. Must be >= 0.

    Returns:
        A sorted list of distinct well-formed strings, each of length
        2 * n. generate_parentheses(0) == [''].

    Raises:
        TypeError: If `n` is not an int.
        ValueError: If `n` is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
