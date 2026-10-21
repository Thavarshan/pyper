"""Level 09 - Searching and Sorting.

Goal: write the classic searching and sorting algorithms yourself, and
learn to reason about how fast they are.

Concepts covered:
- Big-O notation (how the running time grows as the input grows):
  O(1), O(log n), O(n), O(n log n), O(n^2)
- Time vs space complexity (running time vs extra memory), and the
  best / average / worst case
- Linear search and binary search, written both iteratively (with a
  loop) and recursively (a function that calls itself)
- Loop invariants (facts that stay true on every pass of a loop) and
  off-by-one errors with low/high indices
- Simple sorts: bubble sort, insertion sort
- Divide-and-conquer sorts (split the problem, solve the halves, join
  the answers): merge sort, quick sort
- Stable vs unstable sorting (whether equal items keep their original
  order), and sorting in place (changing the list itself) vs returning
  a new list
- Using binary search on "almost sorted" data (rotated arrays)
- Testing algorithms against a trusted reference like sorted()
"""
