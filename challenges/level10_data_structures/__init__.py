"""Level 10 - Data Structures.

Goal: learn the classic data structures that show up again and again in
real programs and in coding interviews, and learn to pick the right one
for the job.

Stacks
    A stack is "last in, first out" (LIFO), like a pile of plates: you
    only ever add to, look at, or remove from the TOP. In Python a plain
    `list` is a perfect stack: `.append(x)` pushes, `.pop()` pops and
    `lst[-1]` peeks. All three are O(1). Stacks are the natural tool for
    anything that "nests" (brackets, undo history, function calls).

Linked lists
    A singly linked list is a chain of nodes where each node holds a value
    and a reference (`.next`) to the following node. The last node points
    to `None`:

        head
         |
         v
        [1] -> [2] -> [3] -> None

    Unlike a Python list there is no indexing: to reach the 3rd node you
    must walk from the head. What linked lists ARE good at is re-wiring:
    inserting or removing a node you already hold is O(1) - you just move
    a couple of `.next` pointers. Most linked list problems are about
    moving pointers carefully without losing the rest of the chain. Draw
    boxes and arrows on paper - it really helps. The `ListNode` class and
    helper builders live in `challenges.common.structures`.

Heaps (priority queues)
    A heap is a tree-shaped structure, stored inside a plain list, that
    always keeps the SMALLEST item at index 0 (a "min-heap"). Adding an
    item or removing the smallest costs O(log n); peeking at the smallest
    is O(1). Python's `heapq` module turns any list into a min-heap. Heaps
    are the go-to tool for "top k", "k-th largest" and "always process
    the cheapest thing next" problems.

Hash maps, counters and ordered dicts
    You met `dict` and `set` in level 04. Here you combine them with other
    structures: `collections.Counter` for counting, and
    `collections.OrderedDict`, which remembers insertion order AND can
    move a key to the end in O(1) - exactly what an LRU cache needs.

Designing classes with complexity guarantees
    Two challenges (MinStack, LRUCache) ask you to build a class whose
    every method runs in O(1) time. The trick is always the same: store
    a little EXTRA information so you never need to search.
"""
