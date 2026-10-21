r"""
Challenge: Kth Largest Element in an Array
Level:     10 - Data Structures
Topics:    heaps, the heapq module, priority queues
Source:    LeetCode #215 "Kth Largest Element in an Array"

========================================================================
YOUR TASK
========================================================================
Write `find_kth_largest(nums, k)`. It returns the k-th LARGEST value
in the list `nums`. Use a heap (explained below).

    find_kth_largest([3, 2, 1, 5, 6, 4], 2)  ->  5

========================================================================
WHAT "K-TH LARGEST" MEANS
========================================================================
Sort the list from biggest to smallest. The k-th largest is the value
at position k, counting from 1. Duplicates COUNT as separate items: it
is the k-th largest item, not the k-th largest different value.

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    sorted big -> small: [6, 5, 5, 4, 3, 3, 2, 2, 1]
                          1  2  3  4  ...
    k = 4  ->  4

Sorting works (O(n log n)), but the goal here is to learn HEAPS.

========================================================================
WHAT A HEAP IS
========================================================================
A (min-)heap is a special arrangement of items in a list where the
smallest item is always at index 0. You can add an item, or remove the
smallest, in O(log n) time. You can peek at the smallest in O(1) time.

Think of it as a binary tree where every parent is <= its children:

            1              stored as list: [1, 3, 2, 7, 4]
           / \
          3   2            parent of index i is at (i - 1) // 2
         / \               children of i are 2*i + 1 and 2*i + 2
        7   4

Python's `heapq` module gives you:

    heapq.heappush(h, x)   add x
    heapq.heappop(h)       remove and return the smallest
    heapq.heapify(lst)     turn a list into a heap, in O(n)
    h[0]                   peek at the smallest

THE KEY IDEA: keep a min-heap of the k largest values seen so far. Its
smallest member, h[0], is then exactly the k-th largest!

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the k-th largest value of `nums`, counting duplicates as
   separate items.
2. Raise `ValueError` unless 1 <= k <= len(nums). This includes any k
   when `nums` is empty.
3. Not change (mutate) the caller's `nums` list.

You can assume:
- `nums` is a list of ints. Values may be negative and repeated.
- len(nums) is between 0 and 100_000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    find_kth_largest([3, 2, 1, 5, 6, 4], 2)           ->  5
        Biggest first: 6, 5, ... The 2nd is 5.

    find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)  ->  4
        Biggest first: 6, 5, 5, 4. Both 5s count, so the 4th is 4.

    find_kth_largest([7], 1)                          ->  7
        One item, and it is the largest.

    find_kth_largest([], 1)  ->  raises ValueError
        There is no 1st largest in an empty list.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n log k) with a heap of size k: n pushes and pops, each
  costing about log k because the heap never holds more than k items.
- Space: O(k): the heap holds at most k items (plus one while adding).

========================================================================
EDGE CASES TO TEST
========================================================================
- k = 1 -> the maximum: find_kth_largest([3, 1, 2], 1) -> 3
- k = len(nums) -> the minimum: find_kth_largest([3, 1, 2], 3) -> 1
- Duplicates: find_kth_largest([5, 5, 5], 2) -> 5
- Negative numbers: find_kth_largest([-1, -5, -3], 2) -> -3
- k = 0, k > len(nums), or nums = [] -> raises ValueError
- The input list is unchanged after the call

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. First make it work with `sorted(nums, reverse=True)[k - 1]`. Write
   your tests, THEN replace it with the heap version. Your tests keep
   you safe.
2. Check that k is valid before doing anything else.
3. Create an empty list `heap`. For each number, `heappush` it.
4. Whenever the heap grows beyond k items, `heappop`. That throws away
   the smallest, which can't be among the k largest.
5. At the end, `heap[0]` is the answer. (`heapq.heappushpop` does a
   push and a pop in one faster call.)

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `import heapq`: heappush, heappop, heapify, heappushpop, nlargest
- Python only has a MIN-heap. For a max-heap, push negated values (-x)
- `sorted()` returns a new list, while `list.sort()` mutates in place
- Raising `ValueError` for invalid arguments

========================================================================
STRETCH GOALS
========================================================================
- Solve it in one line with `heapq.nlargest` (then look at its
  source!).
- Implement Quickselect: average O(n) time. It is quick sort's
  partition step, but you only recurse into the side that holds the
  answer.
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
