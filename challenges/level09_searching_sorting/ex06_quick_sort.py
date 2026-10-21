"""
Challenge: Quick Sort
Level:     09 - Searching and Sorting
Topics:    divide and conquer, pivots, partitioning, worst-case analysis
Source:    Classic algorithm (Tony Hoare, 1959)

========================================================================
YOUR TASK
========================================================================
Write `quick_sort(items)`. It RETURNS a NEW list with the items in
ascending order, using the quick sort algorithm. The input list stays
as it was.

    quick_sort([3, 6, 1, 8, 3, 2])  ->  [1, 2, 3, 3, 6, 8]

========================================================================
HOW QUICK SORT WORKS
========================================================================
Quick sort is a divide-and-conquer sort: it splits the problem into
smaller ones, solves those, and joins the answers.

    1. Pick one item as the PIVOT.
    2. PARTITION (split) the items into three groups:
           less    - items smaller than the pivot
           equal   - items equal to the pivot
           greater - items larger than the pivot
    3. Quick-sort `less` and `greater` (recursively, meaning the
       function calls itself), then join:
           quick_sort(less) + equal + quick_sort(greater)
    Base case: a list with 0 or 1 items is already sorted.

    [3, 6, 1, 8, 3, 2]  pivot = 3
    less = [1, 2]   equal = [3, 3]   greater = [6, 8]
    -> [1, 2] + [3, 3] + [6, 8] = [1, 2, 3, 3, 6, 8]

This "three lists" version is the easiest to understand. The classic
in-place version (which rearranges the list itself) is a stretch goal.

PIVOT CHOICE AND THE WORST CASE
    Quick sort is fast when the pivot splits the list roughly in HALF
    each time: O(n log n). But if the pivot is always the smallest or
    largest item, one side is empty and the other has n-1 items. That
    gives n levels of recursion and O(n^2) time.

    That's exactly what happens if you always pick the FIRST item and
    the input is already sorted! On 10_000 sorted items it goes 10_000
    calls deep, past Python's recursion limit (about 1000), and
    crashes with RecursionError.

    Common fixes:
        - pick the MIDDLE item:  items[len(items) // 2]
        - pick a RANDOM item:    random.choice(items)
        - "median of three": the middle value of the first, middle
          and last items

    Grouping all items EQUAL to the pivot together also matters. It
    avoids O(n^2) on lists with many duplicates (like [7] * 10_000).

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a NEW list, sorted ascending. Return a new list object even
   for 0 or 1 items.
2. Never change (mutate) the input.
3. Pick the middle item or a random item as the pivot.
4. Not raise RecursionError on already-sorted input of 10_000 items,
   or on 10_000 equal items. So choose the pivot wisely and group the
   equal items.
5. Not use sorted(), list.sort() or heapq in the solution. Use
   sorted() in your TESTS as the reference.

It does NOT need to be stable (keep equal items in their original
order). Quick sort generally isn't.

You can assume:
- All items can be compared with each other.
- len(items) is between 0 and 10**5.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    quick_sort([3, 6, 1, 8, 3, 2])  ->  [1, 2, 3, 3, 6, 8]
        See the walk-through above. Both 3s end up together.

    quick_sort([])                  ->  []
        Nothing to sort, but still a new list.

    quick_sort(["b", "c", "a"])     ->  ['a', 'b', 'c']
        Strings sort alphabetically.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n log n) on average: about log n levels of splitting, with
         O(n) work per level. O(n^2) in the worst case, when unlucky
         pivots split off only one item at a time.
- Space: this version uses O(n) extra for the new lists. The recursion
         depth is O(log n) on average.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: quick_sort([]) -> []
- One item: quick_sort([4]) -> [4]
- Two items in either order: quick_sort([2, 1]) -> [1, 2] and
  quick_sort([1, 2]) -> [1, 2]
- Already sorted input of 10_000 items:
  quick_sort(list(range(10_000))) -> list(range(10_000)), with no
  RecursionError
- Reverse-sorted input of 10_000 items -> sorted, no RecursionError
- All equal items: quick_sort([5] * 10_000) -> [5] * 10_000
- Many duplicates, negatives, floats
- Strings
- The input is unchanged, and the result is a new object
- Random lists vs sorted(), with a fixed random seed

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Base case: `if len(items) <= 1: return list(items)`.
2. `pivot = items[len(items) // 2]`.
3. Build the three groups with list comprehensions:
   `less = [x for x in items if x < pivot]`, and the same idea with
   `==` and `>`.
4. Return `quick_sort(less) + equal + quick_sort(greater)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Divide and conquer with uneven splits
- Best / average / worst case analysis
- List comprehensions with conditions
- Why input order can make an algorithm slow
- `random.choice` and seeding for reproducible tests (random.seed(0)
  gives the same "random" numbers every run)

========================================================================
STRETCH GOALS
========================================================================
- Implement IN-PLACE quick sort (it rearranges the list itself) with
  the Lomuto or Hoare partition scheme:
  quick_sort_inplace(items, low=0, high=None) -> None.
- Implement "median of three" pivot selection.
- Quickselect: find the k-th smallest item in O(n) average time
  (LeetCode #215 "Kth Largest Element in an Array").
- Time first-element pivot vs middle pivot on sorted input of 900
  items (small enough to stay under the recursion limit).
"""

from typing import Any


def quick_sort(items: list[Any]) -> list[Any]:
    """Return a new list with `items` sorted ascending, via quick sort.

    Not required to be stable. The input list is not modified.

    Args:
        items: A list of mutually comparable values.

    Returns:
        A new, sorted list.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
