"""
Challenge: Kth Largest Element in an Array
Level:     10 - Data Structures
Topics:    heaps, the heapq module, priority queues
Source:    LeetCode #215 "Kth Largest Element in an Array"

========================================================================
PROBLEM
========================================================================
Given a list of integers `nums` and an integer `k`, return the k-th
LARGEST value in the list.

"k-th largest" means: if you sorted the list from biggest to smallest,
it is the value at position k (counting from 1). Duplicates COUNT as
separate elements - it is the k-th largest element, not the k-th largest
distinct value:

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    sorted big -> small: [6, 5, 5, 4, 3, 3, 2, 2, 1]
                          1  2  3  4  ...
    k = 4  ->  4

Sorting works (O(n log n)), but the goal here is to learn HEAPS.

What is a HEAP? A (min-)heap is a special arrangement of items in a list
where the smallest item is always at index 0. You can add an item or
remove the smallest in O(log n) time, and peek at the smallest in O(1).
Conceptually it is a binary tree where every parent is <= its children:

            1              stored as list: [1, 3, 2, 7, 4]
           / \\
          3   2            parent of index i is at (i - 1) // 2
         / \\               children of i are 2*i + 1 and 2*i + 2
        7   4

Python's `heapq` module gives you `heapq.heappush(h, x)`,
`heapq.heappop(h)` (removes and returns the smallest), `heapq.heapify(lst)`
(turns a list into a heap in O(n)) and `h[0]` to peek.

The KEY IDEA: keep a min-heap of the k largest values seen so far. Its
smallest member (h[0]) is then exactly the k-th largest!

Do not modify the caller's `nums` list.

========================================================================
EXAMPLES
========================================================================
    >>> find_kth_largest([3, 2, 1, 5, 6, 4], 2)
    5

    >>> find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4

    >>> find_kth_largest([7], 1)
    7

========================================================================
CONSTRAINTS
========================================================================
- `nums` is a list of ints, length 0..100_000; values may be negative
  and repeated.
- `k` must satisfy 1 <= k <= len(nums). Otherwise (including any k when
  nums is empty) raise `ValueError`.
- Do not mutate `nums`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n log k) with a size-k heap.
- Space: O(k).

========================================================================
EDGE CASES TO TEST
========================================================================
- k = 1 -> the maximum
- k = len(nums) -> the minimum
- Duplicates: [5, 5, 5], k = 2 -> 5
- Negative numbers
- k = 0, k > len(nums), or nums = [] -> ValueError
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. First make it work with `sorted(nums, reverse=True)[k - 1]`, write your
   tests, THEN replace it with the heap version - your tests keep you safe.
2. Validate k before doing anything else.
3. Create an empty list `heap`. For each number, `heappush` it.
4. Whenever the heap grows beyond k items, `heappop` - that throws away
   the smallest, which can't be among the k largest.
5. At the end `heap[0]` is the answer. (Or `heapq.heappushpop` does push
   and pop in one faster call.)

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `import heapq`: heappush, heappop, heapify, heappushpop, nlargest
- Python only has a MIN-heap; for a max-heap push negated values (-x)
- `sorted()` returns a new list; `list.sort()` mutates in place
- Raising `ValueError` for invalid arguments

========================================================================
STRETCH GOALS
========================================================================
- Solve it in one line with `heapq.nlargest` (then look at its source!).
- Implement Quickselect: average O(n) time.
- Build a `KthLargest` class that accepts a stream of numbers via
  `add(val)` and returns the current k-th largest (LeetCode #703).
"""


def find_kth_largest(nums: list[int], k: int) -> int:
    """Return the k-th largest element of `nums` (duplicates count).

    Args:
        nums: The numbers to search. Not modified.
        k: Which largest to return, 1-based (k=1 is the maximum).

    Returns:
        The k-th largest value.

    Raises:
        ValueError: If k < 1 or k > len(nums).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
