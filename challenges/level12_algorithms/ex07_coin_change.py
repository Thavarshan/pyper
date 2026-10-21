"""
Challenge: Coin Change
Level:     12 - Algorithms
Topics:    dynamic programming (1D table), why greedy fails
Source:    LeetCode #322 "Coin Change"

========================================================================
YOUR TASK
========================================================================
Write `coin_change(coins, amount)`. You have as many coins as you like
of each value in `coins`. RETURN the FEWEST coins that add up to
exactly `amount`, or -1 if it can't be done.

    coin_change([1, 2, 5], 11)  ->  3      (5 + 5 + 1)

========================================================================
WHY GREEDY FAILS, AND HOW DYNAMIC PROGRAMMING WORKS
========================================================================
A GREEDY approach makes the best-looking choice right now and never
goes back: "always take the biggest coin that fits". That works for
real currencies, but not in general:

    coins = [1, 3, 4], amount = 6
    greedy:  4 + 1 + 1   = 3 coins
    best:    3 + 3       = 2 coins

DYNAMIC PROGRAMMING (DP) builds the answer from answers to smaller
versions of the same problem, and stores them so nothing is worked out
twice. Here, let dp[a] = the fewest coins that make amount a.
    - Base case (the answer you just know): dp[0] = 0.
    - For a > 0: the LAST coin used was some coin c <= a, and the rest
      makes a - c in the best possible way. So
          dp[a] = 1 + min(dp[a - c] for each coin c <= a)
      ignoring amounts that are impossible.
    - Fill dp from 0 up to amount ("tabulation"), so the smaller
      answers are always ready when you need them.

    coins = [1, 2, 5]
    a:      0  1  2  3  4  5  6  7  8  9  10  11
    dp[a]:  0  1  1  2  2  1  2  2  3  3  2   3

    dp[11] = 1 + min(dp[11 - 1], dp[11 - 2], dp[11 - 5])
           = 1 + min(dp[10], dp[9], dp[6])
           = 1 + min(2, 3, 2)
           = 3

Use a value like `float("inf")` (infinity) to mean "impossible so far",
and turn it into -1 at the end. amount + 1 also works: it is more than
the most coins you could ever need (amount coins of value 1).

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the minimum number of coins that add up to exactly `amount`.
2. Return -1 if the amount cannot be made.
3. Return 0 when amount is 0 (no coins needed).
4. Raise ValueError if amount is negative, if `coins` is empty, or if
   any coin is 0 or less. Check this BEFORE the "amount is 0" shortcut,
   so coin_change([], 0) raises ValueError instead of returning 0.
5. Give the same answer whatever order the coins come in, and even if
   a coin value is listed twice.
6. Not change (mutate) `coins`.

You can assume:
- `coins` is a list of ints. When valid, it holds 1 to 12 coins, each
  at least 1.
- `amount` is an int. When valid, it is from 0 to 10_000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    coin_change([1, 2, 5], 11)  ->  3
        5 + 5 + 1. See the table above.

    coin_change([2], 3)         ->  -1
        Coins of 2 only make even amounts.

    coin_change([1], 0)         ->  0
        Amount 0 needs no coins.

    coin_change([1, 3, 4], 6)   ->  2
        3 + 3. Greedy would say 3 (4 + 1 + 1).

    coin_change([1, 2], -1)     ->  raises ValueError

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(amount * len(coins)). For each amount from 1 up to `amount`,
         try each coin once.
- Space: O(amount). One list slot per amount from 0 to `amount`.

========================================================================
EDGE CASES TO TEST
========================================================================
- amount = 0: coin_change([1], 0) -> 0
- Impossible amount: coin_change([2], 3) -> -1
- The greedy trap: coin_change([1, 3, 4], 6) -> 2
- A single coin that divides the amount exactly: coin_change([5], 20)
  -> 4
- Unsorted coins and duplicate coins give the same answer:
  coin_change([5, 1, 2], 11) -> 3, coin_change([1, 2, 2, 5], 11) -> 3
- A large amount (10_000) runs quickly
- Invalid inputs raise ValueError: coin_change([1, 2], -1),
  coin_change([], 5), coin_change([], 0), coin_change([0, 1], 3),
  coin_change([-1, 2], 3)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Try the recursive definition first, with @functools.cache:
   best(a) = 0 if a == 0, else 1 + min(best(a - c)) over usable coins.
2. For tabulation: `dp = [INF] * (amount + 1)` and `dp[0] = 0`.
3. Outer loop over a from 1 to amount. Inner loop over coins. If c <= a
   and dp[a - c] + 1 < dp[a], update dp[a].
4. Return dp[amount] if it's not INF, else -1.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `float("inf")` as a sentinel (a special stand-in value) for
  "impossible"
- 1D DP tables with lists
- `min()` with a generator expression and the `default=` argument
- `functools.cache` for the top-down version

========================================================================
STRETCH GOALS
========================================================================
- Also return WHICH coins to use (keep a `choice` list and backtrack:
  walk back from `amount`, subtracting the coin you chose each time).
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
