"""
Challenge: Best Time to Buy and Sell Stock
Level:     12 - Algorithms
Topics:    greedy, single pass, tracking a running minimum
Source:    LeetCode #121 "Best Time to Buy and Sell Stock"

========================================================================
PROBLEM
========================================================================
You get a list `prices` where prices[i] is a stock's price on day i. You
may make at most ONE trade: buy on one day and sell on a LATER day.
Return the maximum profit you can make. If no trade makes money, return 0
(you just don't trade).

You must buy BEFORE you sell - you can't sell on day 1 and buy on day 5.

    day:     0  1  2  3  4  5
    price:   7  1  5  3  6  4
                ^        ^
               buy      sell     profit = 6 - 1 = 5

Brute force checks every (buy, sell) pair: O(n^2). The GREEDY insight: if
you are selling on day i, the best day to have bought is simply the
cheapest day BEFORE i. So scan left to right once, remembering the lowest
price seen so far and the best profit seen so far.

    price:        7   1   5   3   6   4
    min so far:   7   1   1   1   1   1
    profit today: 0   0   4   2   5   3
    best:         0   0   4   4   5   5    -> 5

========================================================================
EXAMPLES
========================================================================
    >>> max_profit([7, 1, 5, 3, 6, 4])
    5

    >>> max_profit([7, 6, 4, 3, 1])
    0

    >>> max_profit([2, 4, 1])
    2

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(prices) <= 100_000.
- 0 <= prices[i] <= 10_000 (ints).
- Fewer than 2 prices -> 0 (no trade possible).
- Do not mutate `prices`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n) - one pass.
- Space: O(1) - two variables.

========================================================================
EDGE CASES TO TEST
========================================================================
- [] and [5] -> 0
- Strictly decreasing prices -> 0
- Strictly increasing -> last - first
- The minimum comes AFTER the maximum ([2, 4, 1]) -> must not return 4-1!
- All prices equal -> 0
- The best trade isn't using the global minimum: [3, 8, 1, 2] -> 5

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Write the O(n^2) version first (two nested loops) - it's great for
   checking the fast version in a test.
2. Keep `min_price` (cheapest so far) and `best` (best profit so far).
3. For each price: update best with `price - min_price`, then update
   min_price.
4. Initialise best = 0 so "no profitable trade" naturally returns 0.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `max()` / `min()` with two arguments inside a loop
- `float("inf")` as an initial "infinitely expensive" minimum
- `itertools.accumulate(prices, min)` gives running minimums
- Comparing a fast solution against a brute-force one in tests

========================================================================
STRETCH GOALS
========================================================================
- Also return the (buy_day, sell_day) indexes.
- Unlimited trades allowed (LeetCode #122).
- Write a property-based test comparing against brute force on random
  lists (using `random`).
"""


def max_profit(prices: list[int]) -> int:
    """Return the best profit from one buy followed by one later sell.

    Args:
        prices: Price of the stock on each day. Not modified.

    Returns:
        The maximum profit achievable, or 0 if no profitable trade exists
        (including when there are fewer than 2 prices).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
