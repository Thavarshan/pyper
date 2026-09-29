"""Level 12 - Algorithms.

Goal: learn the problem-solving PATTERNS that turn slow brute-force
solutions (often O(n^2) or exponential) into fast ones. Recognising which
pattern fits a problem is the real skill.

Two pointers
    Keep two indexes into a sequence and move them according to a rule,
    instead of checking every pair with nested loops. Often the pointers
    start at opposite ends of a SORTED list and walk towards each other:
    each step rules out a whole group of pairs at once, giving O(n)
    instead of O(n^2).

        [1, 2, 4, 7, 11]
         ^            ^
        left        right      sum too big? move right in. too small? left out.

Sliding window
    A special two-pointer technique for contiguous chunks (substrings,
    subarrays). A "window" [left, right] slides along: grow it by moving
    `right`, shrink it by moving `left` whenever it breaks a rule. Each
    element enters and leaves the window at most once -> O(n).

        "a b c a b c b b"
         [-----]           window "abc" has no repeats
           [-----]         saw another 'a' -> slide left past the old one

Greedy algorithms
    Make the locally best choice at each step and never look back (e.g.
    "keep track of the cheapest price so far"). Greedy is simple and fast
    but only correct for certain problems - part of the skill is
    convincing yourself WHY it works (or finding the counter-example).

Dynamic programming (DP)
    DP applies when a problem can be split into smaller sub-problems whose
    answers are REUSED many times ("overlapping subproblems") and the best
    answer is built from best answers to smaller pieces ("optimal
    substructure"). Instead of recomputing, you store each sub-answer once.

    Two styles:
      - Memoisation (top-down): write the natural recursive solution and
        cache results so each sub-problem is computed only once. In Python,
        `@functools.cache` does the caching for you.
      - Tabulation (bottom-up): fill in a table (list or 2D list) starting
        from the smallest sub-problems, so every value you need is already
        computed when you need it. No recursion, no recursion limit.

    The recipe: (1) define what dp[i] (or dp[i][j]) MEANS in words, (2) write
    the recurrence relating it to smaller entries, (3) identify base cases,
    (4) decide the fill order, (5) optionally shrink the table if you only
    need the last row or last few values.
"""
