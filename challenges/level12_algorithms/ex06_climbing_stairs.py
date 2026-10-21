r"""
Challenge: Climbing Stairs
Level:     12 - Algorithms
Topics:    dynamic programming, memoisation, tabulation, functools.cache
Source:    LeetCode #70 "Climbing Stairs"

========================================================================
YOUR TASK
========================================================================
Write `climb_stairs(n)`. You climb a staircase of `n` steps, taking
either 1 step or 2 steps at a time. RETURN how many DIFFERENT ways
there are to reach exactly step n. The order of moves matters: 1+2 and
2+1 are different ways.

    climb_stairs(3)  ->  3      (1+1+1, 1+2, 2+1)

========================================================================
DYNAMIC PROGRAMMING, STEP BY STEP
========================================================================
    n = 3:  1+1+1,  1+2,  2+1                 -> 3 ways
    n = 4:  1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 -> 5 ways

This is your FIRST DYNAMIC PROGRAMMING (DP) problem, so take your time
here. DP means building the answer from answers to smaller versions of
the same problem, and storing those answers so you never work one out
twice. The same thinking solves many harder problems.

------------------------------------------------------------------------
Step 1 - find the recursive structure
------------------------------------------------------------------------
Think about the LAST move onto step n. It was either:
    - a 1-step from step n-1, or
    - a 2-step from step n-2.
Those two groups don't overlap, and together they cover every way. So

    ways(n) = ways(n - 1) + ways(n - 2)

The base cases (the smallest answers, which you just know) are
ways(0) = 1 (one way to "climb" zero steps: do nothing) and
ways(1) = 1. (Yes, these are the Fibonacci numbers!)

    ways(4) = ways(3) + ways(2) = 3 + 2 = 5

------------------------------------------------------------------------
Step 2 - notice the problem with plain recursion
------------------------------------------------------------------------
Turning that formula straight into a recursive function (one that
calls itself) works, but it recomputes the same values over and over:

                         ways(5)
                    /              \
               ways(4)            ways(3)
              /      \            /     \
         ways(3)   ways(2)   ways(2)  ways(1)
         /    \      ...       ...
     ways(2) ways(1)

ways(3) is computed twice, ways(2) three times, and so on. Each extra
step makes the call tree about 1.6 times bigger. That is exponential
growth, usually written O(2^n), and n = 40 already takes ages. These
repeated calls are called OVERLAPPING SUBPROBLEMS: the signature of a
problem where dynamic programming helps.

------------------------------------------------------------------------
Step 3 - memoisation (top-down DP)
------------------------------------------------------------------------
"Memoise" means remember answers you've already computed. Keep a dict
{k: ways(k)}. Before computing ways(k), check the dict. Now each value
is computed only once: O(n) time and O(n) space. Python can do this for
you: put the `@functools.cache` decorator above a recursive function.
The downside: the recursion goes n calls deep, and Python stops at
about 1_000 nested calls (the "recursion limit"). So n = 1_000 already
crashes with RecursionError.

------------------------------------------------------------------------
Step 4 - tabulation (bottom-up DP)
------------------------------------------------------------------------
Flip it around: fill a list from the smallest case upwards, so that
when you compute dp[i], dp[i-1] and dp[i-2] are already known.

    i:      0  1  2  3  4  5  6
    dp[i]:  1  1  2  3  5  8  13

    dp[2] = dp[1] + dp[0] = 1 + 1 = 2
    dp[3] = dp[2] + dp[1] = 2 + 1 = 3, and so on.

No recursion at all. O(n) time, O(n) space.

------------------------------------------------------------------------
Step 5 - shrink the space
------------------------------------------------------------------------
dp[i] only ever needs the previous TWO values. So keep just two
variables and slide them along: O(n) time, O(1) space (a fixed number
of variables, however big n is).

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the number of ordered sequences of 1-steps and 2-steps that
   add up to exactly n.
2. Return 1 for n = 0 (the empty climb).
3. Raise ValueError if n is negative.
4. Handle n = 1_000 quickly: no exponential recursion and no
   recursion-limit crash. (So your main solution should be the loop of
   step 4 or 5, not the recursive versions.) Python ints never
   overflow, so the huge answer is fine.

You can assume:
- `n` is an int. Valid values go from 0 to 1_000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    climb_stairs(1)  ->  1
        Just one 1-step.

    climb_stairs(2)  ->  2
        1+1 or 2.

    climb_stairs(3)  ->  3
        1+1+1, 1+2 or 2+1.

    climb_stairs(5)  ->  8
        ways(4) + ways(3) = 5 + 3.

    climb_stairs(-1) ->  raises ValueError

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). One step of work for each stair.
- Space: O(1) for the final version (two variables). The memo and table
         versions use O(n), one stored answer per stair.

========================================================================
EDGE CASES TO TEST
========================================================================
- n = 0 -> 1
- n = 1 -> 1
- n = 2 -> 2
- n = 10 -> 89
- n = 1_000 finishes fast and returns a big int (209 digits long)
- climb_stairs(n) == climb_stairs(n - 1) + climb_stairs(n - 2) for
  several n (for example n = 2 to 20)
- n = -1 -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Write out the answers for n = 0 to 6 by hand. Spot the pattern.
2. Write the naive recursive version first and test it on small n.
3. Add `@functools.cache` to a recursive helper and watch n = 35 become
   instant.
4. Tabulation: `dp = [0] * (n + 1)`, set the base cases, then
   `for i in range(2, n + 1): dp[i] = dp[i - 1] + dp[i - 2]`.
   (Careful: for n = 0 the list has only one slot, so dp[1] doesn't
   exist.)
5. O(1) space: start with `a, b = 1, 1` (ways(0) and ways(1)). Repeat
   `a, b = b, a + b` n times, then return a.

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
  against each other with @pytest.mark.parametrize (which runs one test
  function on many inputs).
- Allow a list of allowed step sizes, e.g. steps=(1, 3, 5).
- Min Cost Climbing Stairs (LeetCode #746).
- O(log n) using matrix exponentiation (a trick that jumps ahead many
  steps at once by multiplying small 2x2 grids of numbers).
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
