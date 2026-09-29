"""
Challenge: Linked List Cycle
Level:     10 - Data Structures
Topics:    linked lists, Floyd's tortoise and hare, fast/slow pointers
Source:    LeetCode #141 "Linked List Cycle"

========================================================================
PROBLEM
========================================================================
Given the `head` of a singly linked list, return True if the list
contains a CYCLE, otherwise False.

A cycle means that following `.next` pointers never reaches None -
instead some node's `.next` points back to an earlier node, so you would
loop forever:

    [3] -> [2] -> [0] -> [-4]
            ^              |
            |______________|        (-4).next is the node [2]  -> True

    [1] -> [2] -> None                                          -> False

Important: two nodes with the same VALUE are not a cycle. A cycle is
about the same node OBJECT being reached twice (compare with `is`).

FLOYD'S TORTOISE AND HARE: move two pointers through the list. The
"tortoise" (slow) moves 1 step at a time, the "hare" (fast) moves 2
steps. If there is no cycle, the hare falls off the end (reaches None).
If there IS a cycle, both end up running around the loop, and because
the hare gains one step per move, it must eventually land on the exact
same node as the tortoise. Like two runners on a circular track - the
faster one always laps the slower one.

Your main solution should use Floyd's algorithm (O(1) extra space).

========================================================================
EXAMPLES
========================================================================
    >>> from challenges.common.structures import list_to_linked
    >>> has_cycle(list_to_linked([1, 2, 3]))
    False

    >>> head = list_to_linked([3, 2, 0, -4])
    >>> head.next.next.next.next = head.next     # -4 -> 2
    >>> has_cycle(head)
    True

    >>> has_cycle(None)
    False

========================================================================
CONSTRAINTS
========================================================================
- The list has between 0 and 10_000 nodes.
- Node values are ints (duplicates allowed - they do not imply a cycle).
- Empty list (None) -> False.
- Do not modify the list (no changing .val or .next).
- Never call `linked_to_list` on a list that might have a cycle: it would
  loop forever.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n)
- Space: O(1) with Floyd's algorithm (O(n) if you use a set of seen nodes).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list -> False
- Single node, no cycle -> False
- Single node pointing to itself (node.next = node) -> True
- Two nodes pointing to each other -> True
- Cycle back to the head (tail.next = head) -> True
- Long list with no cycle but repeated values -> False

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Simplest idea first: remember every node you have visited in a `set`.
   If you see one again -> cycle. (ListNode is a dataclass, which makes it
   unhashable by default, so store `id(node)` in the set instead.)
2. Now do it without the set: two pointers, `slow` and `fast`, both start
   at head.
3. Each step: slow = slow.next, fast = fast.next.next.
4. Before moving fast two steps, make sure `fast` and `fast.next` are not
   None - if either is None there is no cycle.
5. If at any point `slow is fast` -> return True.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Identity (`is`) vs equality (`==`) - essential here!
- `id(obj)` gives a unique integer for a live object
- Why `@dataclass` objects are unhashable by default (eq=True sets
  __hash__ to None)
- `while fast and fast.next:` - short-circuit evaluation prevents errors

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
