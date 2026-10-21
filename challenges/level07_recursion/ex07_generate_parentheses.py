"""
Challenge: Generate Parentheses
Level:     07 - Recursion
Topics:    backtracking with constraints (pruning), string building
Source:    LeetCode #22 "Generate Parentheses"

========================================================================
YOUR TASK
========================================================================
Write `generate_parentheses(n)`. It RETURNS a sorted list of every
well-formed string made of exactly `n` pairs of parentheses. Build the
strings recursively, one character at a time.

    generate_parentheses(2)  ->  ['(())', '()()']

========================================================================
WHAT "WELL-FORMED" MEANS
========================================================================
A string of parentheses is WELL-FORMED (or "balanced") when every "("
has a matching ")" after it, and no bracket is closed before it was
opened:

    well-formed:      "()",  "(())",  "()()",  "(()())"
    NOT well-formed:  ")(",  "(()",   "())(",  "((("

The number of results follows a famous sequence, the Catalan numbers:

    n:             0  1  2  3   4   5
    how many:      1  1  2  5  14  42

The smart way is to build each string one character at a time, and
PRUNE (skip) any branch that could never become well-formed. For
example, once you have "())" there is no point going on: a ")" closed
something that was never opened. The slow way would be to generate
all 2**(2n) strings of "(" and ")" (for n = 10, about a million) and
throw the bad ones away. Don't do that.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return ALL well-formed strings with exactly `n` pairs, so each
   string has length 2 * n.
2. Contain no duplicates.
3. Return the list SORTED in normal Python string order (what
   `sorted()` gives). "(" comes before ")" in that order, so the
   string that starts "(((" comes first.
4. Return [''] when `n` is 0. There is one way to use zero pairs: the
   empty string.
5. Raise `ValueError` if `n` is negative.
6. Raise `TypeError` if `n` is not an int.
7. Be recursive and use backtracking (build, recurse, undo). Don't
   generate all 2**(2n) strings and filter them.

You can assume:
- 0 <= n <= 10 for valid input.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    generate_parentheses(1)  ->  ['()']
        The only way to use one pair.

    generate_parentheses(2)  ->  ['(())', '()()']
        Nested, or side by side. Sorted, "(())" comes first because
        its second character "(" sorts before ")".

    generate_parentheses(3)
        ->  ['((()))', '(()())', '(())()', '()(())', '()()()']
        5 strings, as the Catalan numbers predict.

    generate_parentheses(0)  ->  ['']
        One string: the empty one.

    generate_parentheses(-1)  ->  raises ValueError

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  roughly proportional to (number of results) * n. Pruning
  means you never explore a dead-end branch, so all the work goes into
  building strings that end up in the answer.
- Space: O(n) for the call stack. The string grows by one character
  per call, so at most 2 * n calls are waiting at once. The output
  list is extra.

========================================================================
EDGE CASES TO TEST
========================================================================
- n = 0 -> ['']
- n = 1 -> ['()']
- n = 3 -> exactly the five strings in EXAMPLES, in that order
- The count matches the Catalan numbers: n = 4 -> 14 strings,
  n = 5 -> 42 strings
- Every string has length 2 * n
- Every string is well-formed. Write a small `is_balanced` helper in
  your test file that keeps a running counter: +1 for "(", -1 for ")",
  never below 0, and 0 at the end.
- No duplicates: len(set(result)) == len(result)
- The result is sorted: result == sorted(result)
- n = -1 -> raises ValueError
- n = "3" -> raises TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Track two counts while building: how many "(" you have used
   (`opened`) and how many ")" (`closed`).
2. You may add "(" only while opened < n.
3. You may add ")" only while closed < opened. Otherwise you would be
   closing a bracket that was never opened.
4. Base case: when the string's length is 2 * n, it is complete. Add
   it to the results.
5. Strings are immutable (they can't be changed in place). So passing
   `current + "("` into the recursive call leaves `current` itself
   untouched, and the choice is "undone" for free when the call
   returns.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Backtracking with pruning (only explore branches that can still
  succeed)
- Passing state (counters, partial strings) through recursive calls
- String immutability and concatenation
- Sorting strings and character order (`ord("(") < ord(")")`, 40 < 41)

========================================================================
STRETCH GOALS
========================================================================
- Write `is_valid(s)` for strings using "()[]{}" (LeetCode #20).
- Compute just the COUNT of results for n up to 100 without generating
  them. Use the Catalan formula, or dynamic programming (building the
  answer for n from saved answers for smaller n).
- Turn your function into a generator (a function that uses `yield`)
  that hands out the strings in sorted order without a final sort.
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
