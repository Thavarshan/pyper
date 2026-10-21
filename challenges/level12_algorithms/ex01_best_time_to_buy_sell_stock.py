"""
Challenge: Best Time to Buy and Sell Stock
Level:     12 - Algorithms
Topics:    greedy, single pass, tracking a running minimum
Source:    LeetCode #121 "Best Time to Buy and Sell Stock"

========================================================================
YOUR TASK
========================================================================
Write `max_profit(prices)`. prices[i] is a stock's price on day i. You
may buy once and sell once, on a LATER day. RETURN the biggest profit
you can make, or 0 if no trade makes money.

    max_profit([7, 1, 5, 3, 6, 4])  ->  5      (buy at 1, sell at 6)

========================================================================
THE IDEA: REMEMBER THE CHEAPEST DAY SO FAR
========================================================================
    day:     0  1  2  3  4  5
    price:   7  1  5  3  6  4
                ^        ^
               buy      sell     profit = 6 - 1 = 5

You must buy BEFORE you sell: you can't sell on day 1 and buy on day 5.

The brute-force way checks every (buy, sell) pair. That is O(n^2): a
loop inside a loop, so 10 times more prices means 100 times more work.

The GREEDY insight (greedy means making the best choice right now and
never going back): if you sell on day i, the best day to have bought is
simply the cheapest day BEFORE i. So scan left to right once,
remembering the lowest price seen so far and the best profit seen so
far:

    price:        7   1   5   3   6   4
    min so far:   7   1   1   1   1   1
    profit today: 0   0   4   2   5   3     (price - min so far)
    best:         0   0   4   4   5   5     -> 5

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the largest value of prices[sell] - prices[buy] where the
   sell day comes after the buy day.
2. Return 0 if no trade makes a profit (you simply don't trade).
3. Return 0 when there are fewer than 2 prices (no trade is possible).
4. Not change (mutate) `prices`.

You can assume:
- `prices` is a list of 0 to 100_000 ints.
- Each price is from 0 to 10_000.
- With up to 100_000 prices, the O(n^2) brute force is too slow for
  big inputs: aim for one pass.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    max_profit([7, 1, 5, 3, 6, 4])  ->  5
        Buy on day 1 (price 1), sell on day 4 (price 6).

    max_profit([7, 6, 4, 3, 1])     ->  0
        Prices only fall, so every trade loses money. Don't trade.

    max_profit([2, 4, 1])           ->  2
        Buy at 2, sell at 4. The 1 comes last, so you can't buy there
        and sell at 4 afterwards.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). One pass over the list, no loop inside a loop.
- Space: O(1). Just two variables, however long the list is.

========================================================================
EDGE CASES TO TEST
========================================================================
- [] -> 0, and [5] -> 0
- Strictly decreasing prices: [7, 6, 4, 3, 1] -> 0
- Strictly increasing prices: [1, 2, 3, 4] -> 3 (last - first)
- The minimum comes AFTER the maximum: [2, 4, 1] -> 2
  (must not return 4 - 1 = 3!)
- All prices equal: [3, 3, 3] -> 0
- The best trade doesn't use the overall minimum: [3, 8, 1, 2] -> 5
  (buy at 3, sell at 8, rather than buy at 1, sell at 2)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Write the O(n^2) version first (two nested loops). It's great for
   checking the fast version in a test.
2. Keep `min_price` (cheapest so far) and `best` (best profit so far).
3. For each price: update best with `price - min_price`, then update
   min_price.
4. Start with best = 0, so "no profitable trade" naturally returns 0.

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
- Write a property-based test (a test that checks a rule on many
  random inputs instead of a few hand-picked ones): compare against
  brute force on random lists made with `random`.
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
