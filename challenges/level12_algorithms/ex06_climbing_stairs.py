"""
Challenge: Climbing Stairs
Level:     12 - Algorithms
Topics:    dynamic programming, memoisation, tabulation, functools.cache
Source:    LeetCode #70 "Climbing Stairs"

========================================================================
PROBLEM
========================================================================
You are at the bottom of a staircase with `n` steps. Each move you climb
either 1 step or 2 steps. In how many DIFFERENT ways can you reach the
top (exactly step n)? The ORDER of moves matters: 1+2 and 2+1 are
different ways.

    n = 3:  1+1+1,  1+2,  2+1                -> 3 ways
    n = 4:  1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 -> 5 ways

This is your FIRST DYNAMIC PROGRAMMING problem, so take your time with
the explanation below - the same thinking solves many harder problems.

------------------------------------------------------------------------
Step 1 - find the recursive structure
------------------------------------------------------------------------
Think about the LAST move onto step n. It was either:
    - a 1-step from step n-1, or
    - a 2-step from step n-2.
Those two groups don't overlap and together cover every way, so

    ways(n) = ways(n - 1) + ways(n - 2)

with base cases ways(0) = 1 (one way to "climb" zero steps: do nothing)
and ways(1) = 1. (Yes - these are the Fibonacci numbers!)

------------------------------------------------------------------------
Step 2 - notice the problem with plain recursion
------------------------------------------------------------------------
Translating that formula directly into a recursive function works, but
it recomputes the same values over and over:

                         ways(5)
                    /              \\
               ways(4)            ways(3)
              /      \\            /     \\
         ways(3)   ways(2)   ways(2)  ways(1)
         /    \\      ...       ...
     ways(2) ways(1)

ways(3) is computed twice, ways(2) three times... The call tree roughly
doubles with every extra step: O(2^n). n = 40 already takes ages. These
repeated calls are called OVERLAPPING SUBPROBLEMS - the signature of a
problem where dynamic programming helps.

------------------------------------------------------------------------
Step 3 - memoisation (top-down DP)
------------------------------------------------------------------------
"Memoise" = remember answers you've already computed. Keep a dict
{k: ways(k)}; before computing ways(k), check the dict. Now each value is
computed once: O(n) time, O(n) space. Python does this for you with the
`@functools.cache` decorator placed above a recursive function.
Downside: recursion depth n - very large n hits the recursion limit.

------------------------------------------------------------------------
Step 4 - tabulation (bottom-up DP)
------------------------------------------------------------------------
Flip it around: fill a list from the smallest case upwards so that when
you compute dp[i], dp[i-1] and dp[i-2] are already known.

    i:      0  1  2  3  4  5  6
    dp[i]:  1  1  2  3  5  8  13

No recursion at all. O(n) time, O(n) space.

------------------------------------------------------------------------
Step 5 - shrink the space
------------------------------------------------------------------------
dp[i] only ever needs the previous TWO values, so keep just two
variables and slide them along: O(n) time, O(1) space.

========================================================================
EXAMPLES
========================================================================
    >>> climb_stairs(1)
    1

    >>> climb_stairs(2)
    2

    >>> climb_stairs(3)
    3

    >>> climb_stairs(5)
    8

========================================================================
CONSTRAINTS
========================================================================
- `n` is an int, 0 <= n <= 1_000 for valid input.
- climb_stairs(0) == 1 (the empty climb).
- Negative n raises `ValueError`.
- Your main solution must handle n = 1_000 quickly (no exponential
  recursion, no recursion-limit crash). Python ints never overflow, so
  the huge answer is fine.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n)
- Space: O(1) for the final version (O(n) for memo / table versions).

========================================================================
EDGE CASES TO TEST
========================================================================
- n = 0 -> 1
- n = 1 -> 1
- n = 2 -> 2
- n = 10 -> 89
- n = 1_000 finishes fast (and returns a big int)
- The result for n equals result(n-1) + result(n-2) for several n
- n = -1 -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Write out the answers for n = 0..6 by hand. Spot the pattern.
2. Write the naive recursive version first and test it on small n.
3. Add `@functools.cache` to a recursive helper and watch n = 35 become
   instant.
4. Tabulation: `dp = [0] * (n + 1)`, set the base cases, then
   `for i in range(2, n + 1): dp[i] = dp[i - 1] + dp[i - 2]`.
5. O(1) space: `a, b = 1, 1` then repeat `a, b = b, a + b` n - 1 times.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Recursion and why naive recursion can be exponential
- `functools.cache` / `functools.lru_cache(maxsize=None)` for memoisation
- Building a DP table with `[0] * (n + 1)`
- Simultaneous assignment `a, b = b, a + b`
- `time.perf_counter()` to measure how much faster each version is

========================================================================
STRETCH GOALS
========================================================================
- Implement all four versions (naive, memo, table, O(1)) and test them
  against each other with @pytest.mark.parametrize.
- Allow a list of allowed step sizes, e.g. steps=(1, 3, 5).
- Min Cost Climbing Stairs (LeetCode #746).
- O(log n) using matrix exponentiation.
"""


def climb_stairs(n: int) -> int:
    """Return the number of distinct ways to climb n steps using 1s and 2s.

    Args:
        n: Number of steps. Must be >= 0.

    Returns:
        The number of ordered sequences of 1- and 2-steps that sum to n
        (1 for n = 0).

    Raises:
        ValueError: If `n` is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
