"""
Challenge: Top K Frequent Elements
Level:     10 - Data Structures
Topics:    collections.Counter, sorting with keys, heaps, bucket sort
Source:    LeetCode #347 "Top K Frequent Elements"

========================================================================
PROBLEM
========================================================================
Given a list of integers `nums` and an integer `k`, return the `k`
values that appear MOST OFTEN in the list.

To make the answer deterministic (so tests are simple), the returned
list must be ordered like this:

    1. By frequency, highest first.
    2. If two values have the SAME frequency, the smaller value first.

Each value appears at most once in the result.

    nums = [4, 1, 1, 2, 2, 3, 3, 3]
    counts:  3 -> 3 times,  1 -> 2 times,  2 -> 2 times,  4 -> 1 time
    ordered: [3, 1, 2, 4]     (1 and 2 tie at 2, so 1 comes first)

    k = 2  ->  [3, 1]
    k = 3  ->  [3, 1, 2]

========================================================================
EXAMPLES
========================================================================
    >>> top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    [1, 2]

    >>> top_k_frequent([4, 1, 1, 2, 2, 3, 3, 3], 3)
    [3, 1, 2]

    >>> top_k_frequent([5, -1, 5, -1, 7], 2)
    [-1, 5]

    >>> top_k_frequent([9], 1)
    [9]

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of ints (may be negative), length 0..100_000.
- `k` must satisfy 1 <= k <= number of DISTINCT values in nums.
  Otherwise raise `ValueError` (this includes nums = []).
- Return a new list; do not mutate `nums`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n log n) with sorting is fine; O(n log k) with a heap or O(n)
         with bucket sort for the stretch goals.
- Space: O(n) for the counts.

========================================================================
EDGE CASES TO TEST
========================================================================
- k equals the number of distinct values -> every distinct value, ordered
- All values have the same frequency -> smallest k values ascending
- Ties at the boundary: [1, 2, 3, 3], k = 2 -> [3, 1]
- Negative numbers in ties: -1 comes before 5
- Single element list
- k = 0, k too large, or empty nums -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Step one is counting. `collections.Counter(nums)` does it for you and
   behaves like a dict {value: count}.
2. `len(counter)` is the number of distinct values - use it to check k.
3. `sorted()` accepts `key=`. A key can return a TUPLE; tuples compare
   element by element.
4. You want count descending but value ascending. Negating the count
   makes "bigger count" sort first: key=lambda v: (-counts[v], v).
5. Sort the distinct values with that key and slice the first k.
   (Beware: Counter.most_common() does NOT break ties by value!)

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
- Bucket sort: make a list of buckets indexed by frequency (0..n) and walk
  from the highest bucket down - O(n) overall.
- Solve "Top K Frequent Words" (LeetCode #692) - same idea with strings.
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
