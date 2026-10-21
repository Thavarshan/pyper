"""
Challenge: Linked List Cycle
Level:     10 - Data Structures
Topics:    linked lists, Floyd's tortoise and hare, fast/slow pointers
Source:    LeetCode #141 "Linked List Cycle"

========================================================================
YOUR TASK
========================================================================
Write `has_cycle(head)`. It gets the head of a linked list and returns
True if the list contains a CYCLE (a loop of nodes), otherwise False.

    has_cycle(list_to_linked([1, 2, 3]))  ->  False

========================================================================
WHAT A "CYCLE" IS
========================================================================
A linked list is a chain of `ListNode` objects. Each node has a `.val`
and a `.next` (the next node, or None at the end).

In a normal list, following `.next` always reaches None. In a list
with a cycle it never does. Instead, some node's `.next` points back
to an earlier node, so you would loop forever:

    [3] -> [2] -> [0] -> [-4]
            ^              |
            |______________|        (-4).next is the node [2]  -> True

    [1] -> [2] -> None                                          -> False

Important: two nodes with the same VALUE are not a cycle. A cycle
means the same node OBJECT is reached twice (compare with `is`).

========================================================================
FLOYD'S TORTOISE AND HARE
========================================================================
Move two pointers through the list. The "tortoise" (slow) moves 1 step
at a time. The "hare" (fast) moves 2 steps.

    - No cycle: the hare falls off the end (reaches None).
    - A cycle: both end up running around the loop. The hare gains
      one step on each move, so it must eventually land on exactly the
      same node as the tortoise.

It's like two runners on a circular track: the faster one always laps
the slower one.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return True if following `.next` ever revisits a node, otherwise
   False.
2. Return False for an empty list (head is None).
3. Not change the list (do not change any `.val` or `.next`).
4. Use Floyd's algorithm in your main solution, so it uses only O(1)
   extra space (a few variables, nothing that grows with the list).

You can assume:
- The list has between 0 and 10_000 nodes.
- Node values are ints. Duplicates are allowed, and they do not mean
  there is a cycle.

Warning for your tests: never call `linked_to_list` on a list that
might have a cycle. It would loop forever.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return. The helper comes
from `challenges.common.structures`.

    has_cycle(list_to_linked([1, 2, 3]))  ->  False
        1 -> 2 -> 3 -> None: the end is reached.

    has_cycle(None)  ->  False
        An empty list has no cycle.

Building a cycle by hand, then checking it:

    head = list_to_linked([3, 2, 0, -4])
    head.next.next.next.next = head.next   # -4 now points back at 2
    has_cycle(head)                        # -> True

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n): the pointers take a number of steps proportional to
  the length of the list.
- Space: O(1) with Floyd's algorithm: just two pointers. (It is O(n)
  if you use a set of seen nodes, because the set grows with the
  list.)

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: has_cycle(None) -> False
- Single node, no cycle: has_cycle(list_to_linked([1])) -> False
- Single node pointing to itself (node.next = node) -> True
- Two nodes pointing to each other -> True
- Cycle back to the head (tail.next = head) -> True
- Long list with no cycle but repeated values -> False

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Simplest idea first: remember every node you have visited in a
   `set`. If you see one again, there is a cycle. ListNode is hashable
   (it can go in a set): it is a dataclass made with `eq=False`, so
   nodes compare and hash by identity, not by value. You can store the
   nodes themselves, or `id(node)`.
2. Now do it without the set: two pointers, `slow` and `fast`, both
   start at head.
3. Each step: slow = slow.next, fast = fast.next.next.
4. Before moving fast two steps, make sure `fast` and `fast.next` are
   not None. If either is None, there is no cycle.
5. If at any point `slow is fast`, return True.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Identity (`is`) vs equality (`==`): essential here!
- `id(obj)` gives a unique integer for a live object
- Why `@dataclass` objects are unhashable by default (the default
  eq=True sets __hash__ to None), and why ListNode uses eq=False to
  keep them hashable
- `while fast and fast.next:` short-circuit evaluation (the right side
  is only checked when the left side is truthy) prevents errors

========================================================================
STRETCH GOALS
========================================================================
- Return the node where the cycle begins (LeetCode #142). Floyd's
  algorithm has a neat second phase for this.
- Return the length of the cycle.
"""

from __future__ import annotations

from challenges.common.structures import ListNode


def has_cycle(head: ListNode | None) -> bool:
    """Return True if the linked list starting at `head` contains a cycle.

    Args:
        head: The first node of the list, or None for an empty list.

    Returns:
        True if following .next pointers ever revisits a node, otherwise
        False. The list is not modified.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
