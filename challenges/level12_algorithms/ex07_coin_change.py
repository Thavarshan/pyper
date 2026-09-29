"""
Challenge: Coin Change
Level:     12 - Algorithms
Topics:    dynamic programming (1D table), why greedy fails
Source:    LeetCode #322 "Coin Change"

========================================================================
PROBLEM
========================================================================
You have unlimited coins of each denomination in `coins`. Return the
FEWEST number of coins that add up to exactly `amount`. If it can't be
done, return -1. For amount 0 the answer is 0 (no coins needed).

    coins = [1, 2, 5], amount = 11   ->  3   (5 + 5 + 1)
    coins = [2],       amount = 3    -> -1   (odd amounts are impossible)

WHY NOT GREEDY? "Always take the biggest coin that fits" works for real
currencies, but not in general:

    coins = [1, 3, 4], amount = 6
    greedy:  4 + 1 + 1   = 3 coins
    best:    3 + 3       = 2 coins

DYNAMIC PROGRAMMING: let dp[a] = fewest coins that make amount a.
    - Base case: dp[0] = 0.
    - For a > 0: the LAST coin used was some coin c <= a, and the rest
      makes a - c optimally, so
          dp[a] = 1 + min(dp[a - c] for each coin c <= a)
      ignoring amounts that are impossible.
    - Fill dp from 0 up to amount (tabulation), so smaller answers are
      always ready.

    coins = [1, 2, 5]
    a:      0  1  2  3  4  5  6  7  8  9  10  11
    dp[a]:  0  1  1  2  2  1  2  2  3  3  2   3

Use a value like `float("inf")` (or amount + 1, which is more than the
maximum possible count) to mean "impossible so far", and convert it to
-1 at the end.

========================================================================
EXAMPLES
========================================================================
    >>> coin_change([1, 2, 5], 11)
    3

    >>> coin_change([2], 3)
    -1

    >>> coin_change([1], 0)
    0

    >>> coin_change([1, 3, 4], 6)
    2

========================================================================
CONSTRAINTS
========================================================================
- 1 <= len(coins) <= 12; each coin is a positive int (>= 1).
- Coins may be given in any order and may contain duplicates.
- 0 <= amount <= 10_000.
- amount 0 -> 0.
- A negative amount, an empty coins list, or a coin <= 0 raises
  `ValueError`. Validate BEFORE the "amount is 0" shortcut, so
  coin_change([], 0) raises ValueError rather than returning 0.
- Do not mutate `coins`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(amount * len(coins))
- Space: O(amount)

========================================================================
EDGE CASES TO TEST
========================================================================
- amount = 0 -> 0
- Impossible amount -> -1
- The greedy trap: [1, 3, 4], 6 -> 2
- A single coin that divides the amount exactly: [5], 20 -> 4
- Unsorted coins and duplicate coins give the same answer
- A large amount (10_000) runs quickly
- Invalid inputs -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Try the recursive definition first with @functools.cache:
   best(a) = 0 if a == 0, else 1 + min(best(a - c)) over usable coins.
2. For tabulation: `dp = [INF] * (amount + 1)` and `dp[0] = 0`.
3. Outer loop over a from 1 to amount; inner loop over coins; if c <= a
   and dp[a - c] + 1 < dp[a], update dp[a].
4. Return dp[amount] if it's not INF, else -1.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `float("inf")` as a sentinel for "impossible"
- 1D DP tables with lists
- `min()` with a generator expression and the `default=` argument
- `functools.cache` for the top-down version

========================================================================
STRETCH GOALS
========================================================================
- Also return WHICH coins to use (keep a `choice` list and backtrack).
- Coin Change II (LeetCode #518): count the number of combinations.
- Write a greedy version and a test that proves it can be wrong.
"""


def coin_change(coins: list[int], amount: int) -> int:
    """Return the fewest coins that sum to `amount`, or -1 if impossible.

    Args:
        coins: Available denominations (unlimited supply of each), all > 0.
            Not modified.
        amount: The target total, >= 0.

    Returns:
        The minimum number of coins needed, 0 if amount is 0, or -1 if the
        amount cannot be made.

    Raises:
        ValueError: If amount < 0, coins is empty, or any coin is <= 0.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
