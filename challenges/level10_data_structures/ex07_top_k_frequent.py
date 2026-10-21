"""
Challenge: Top K Frequent Elements
Level:     10 - Data Structures
Topics:    collections.Counter, sorting with keys, heaps, bucket sort
Source:    LeetCode #347 "Top K Frequent Elements"

========================================================================
YOUR TASK
========================================================================
Write `top_k_frequent(nums, k)`. It returns a list of the `k` values
that appear MOST OFTEN in `nums`, most frequent first.

    top_k_frequent([1, 1, 1, 2, 2, 3], 2)  ->  [1, 2]

========================================================================
HOW THE RESULT IS ORDERED
========================================================================
To make the answer predictable (so tests are simple), order the result
like this:

    1. By frequency (how many times a value appears), highest first.
    2. If two values have the SAME frequency, the smaller value first.

    nums = [4, 1, 1, 2, 2, 3, 3, 3]
    counts:  3 -> 3 times,  1 -> 2 times,  2 -> 2 times,  4 -> 1 time
    ordered: [3, 1, 2, 4]     (1 and 2 tie at 2, so 1 comes first)

    k = 2  ->  [3, 1]
    k = 3  ->  [3, 1, 2]

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a NEW list of `k` values, ordered by frequency (highest
   first), with ties broken by the smaller value first.
2. Include each value at most once.
3. Raise `ValueError` unless 1 <= k <= the number of DISTINCT
   (different) values in `nums`. This includes nums = [].
4. Not change (mutate) `nums`.

You can assume:
- `nums` is a list of ints. Values may be negative.
- len(nums) is between 0 and 100_000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    top_k_frequent([1, 1, 1, 2, 2, 3], 2)        ->  [1, 2]
        1 appears 3 times, 2 appears twice, 3 once. Take the top 2.

    top_k_frequent([4, 1, 1, 2, 2, 3, 3, 3], 3)  ->  [3, 1, 2]
        3 appears 3 times. 1 and 2 tie at 2 times, so 1 comes first.

    top_k_frequent([5, -1, 5, -1, 7], 2)         ->  [-1, 5]
        5 and -1 tie at 2 times. -1 is smaller, so it comes first.

    top_k_frequent([9], 1)                       ->  [9]
        Only one value.

    top_k_frequent([], 1)                        ->  raises ValueError
        There are no values at all.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n log n) with sorting is fine. The stretch goals reach
         O(n log k) with a heap, or O(n) with bucket sort (one pass,
         no loop inside a loop).
- Space: O(n) for the counts (at most one entry per value).

========================================================================
EDGE CASES TO TEST
========================================================================
- k equals the number of distinct values -> every distinct value, in
  order: top_k_frequent([4, 1, 1, 2, 2, 3, 3, 3], 4) -> [3, 1, 2, 4]
- All values have the same frequency -> the smallest k values,
  ascending: top_k_frequent([3, 1, 2], 2) -> [1, 2]
- Ties at the boundary: top_k_frequent([1, 2, 3, 3], 2) -> [3, 1]
- Negative numbers in ties: -1 comes before 5 (see the examples)
- Single-item list: top_k_frequent([9], 1) -> [9]
- k = 0, k too large, or empty nums -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Step one is counting. `collections.Counter(nums)` does it for you
   and behaves like a dict {value: count}.
2. `len(counter)` is the number of distinct values. Use it to check k.
3. `sorted()` accepts `key=`. A key can return a TUPLE, and tuples
   compare item by item.
4. You want count descending but value ascending. Negating the count
   makes "bigger count" sort first: key=lambda v: (-counts[v], v).
5. Sort the distinct values with that key and slice the first k.
   (Beware: Counter.most_common() does NOT break ties by value! It
   keeps tied values in the order they first appeared.)

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `collections.Counter` and its `.most_common()` method
- `sorted(iterable, key=...)` with lambda functions
- Tuple comparison for multi-level sorting
- Slicing: `lst[:k]`
- `heapq.nsmallest(k, iterable, key=...)` as an O(n log k) alternative

========================================================================
STRETCH GOALS
========================================================================
- Use `heapq.nsmallest` with the same key instead of a full sort.
- Bucket sort: make a list of "buckets" (one list per frequency, from
  0 to n) and walk from the highest bucket down. That's O(n) overall.
- Solve "Top K Frequent Words" (LeetCode #692): the same idea with
  strings.
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return the k most frequent values in `nums`.

    Args:
        nums: The numbers to analyse. Not modified.
        k: How many values to return.

    Returns:
        A list of k distinct values ordered by frequency (highest first),
        ties broken by smaller value first.

    Raises:
        ValueError: If k < 1 or k is greater than the number of distinct
            values in `nums`.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
