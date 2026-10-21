"""Level 12 - Algorithms.

Goal: learn the problem-solving PATTERNS that turn slow brute-force
solutions into fast ones. Brute force means trying every possibility.
It is often O(n^2) (a loop inside a loop: 10 times more input means 100
times more work) or exponential (each extra item multiplies the work).
Recognising which pattern fits a problem is the real skill.

Two pointers
    Keep two indexes into a sequence and move them according to a rule,
    instead of checking every pair with nested loops. Often the pointers
    start at opposite ends of a SORTED list and walk towards each other.
    Each step rules out a whole group of pairs at once, giving O(n) (one
    pass) instead of O(n^2).

        [1, 2, 4, 7, 11]
         ^            ^
        left        right      sum too big? move right in. too small? left out.

Sliding window
    A special two-pointer technique for contiguous chunks (runs of
    neighbouring items, such as substrings and subarrays). A "window"
    [left, right] slides along: grow it by moving `right`, and shrink it
    by moving `left` whenever it breaks a rule. Each item enters and
    leaves the window at most once, so it is O(n).

        "a b c a b c b b"
         [-----]           window "abc" has no repeats
           [-----]         saw another 'a' -> slide left past the old one

Greedy algorithms
    Make the best-looking choice at each step and never look back (for
    example, "keep track of the cheapest price so far"). Greedy is simple
    and fast, but only correct for certain problems. Part of the skill is
    convincing yourself WHY it works (or finding the counter-example, an
    input where it gives the wrong answer).

Dynamic programming (DP)
    DP applies when a problem can be split into smaller sub-problems
    whose answers are REUSED many times ("overlapping subproblems"), and
    the best answer is built from the best answers to smaller pieces
    ("optimal substructure"). Instead of recomputing, you store each
    sub-answer once.

    Two styles:
      - Memoisation (top-down): write the natural recursive solution and
        cache (remember) results, so each sub-problem is computed only
        once. In Python, `@functools.cache` does the caching for you.
      - Tabulation (bottom-up): fill in a table (a list or a 2D list)
        starting from the smallest sub-problems, so every value you need
        is already computed when you need it. No recursion, so no
        recursion limit (Python's cap of about 1_000 nested calls).

    The recipe:
      1. Define what dp[i] (or dp[i][j]) MEANS, in words.
      2. Write the recurrence: the formula that builds it from smaller
         entries.
      3. Identify the base cases (the smallest answers, which you just
         know).
      4. Decide the fill order.
      5. Optionally shrink the table, if you only need the last row or
         the last few values.
"""
