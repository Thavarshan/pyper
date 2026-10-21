"""
Challenge: Reverse Linked List
Level:     10 - Data Structures
Topics:    linked lists, pointer manipulation, iteration vs recursion
Source:    LeetCode #206 "Reverse Linked List"

========================================================================
YOUR TASK
========================================================================
Write two functions that reverse a linked list and RETURN its new
head (the node that used to be last):

    reverse_list(head)            uses a while loop (ITERATIVE)
    reverse_list_recursive(head)  calls itself (RECURSIVE)

    1 -> 2 -> 3 -> 4   becomes   4 -> 3 -> 2 -> 1

========================================================================
WHAT A LINKED LIST IS
========================================================================
A singly linked list is a chain of `ListNode` objects. Each node has a
`.val` (an int) and a `.next` (the next node, or None at the end).
`head` is the first node, or None for an empty list.

Reversing it means making every `.next` arrow point the other way:

    before:   head
               |
               v
              [1] -> [2] -> [3] -> [4] -> None

    after:                          new head
                                      |
                                      v
              None <- [1] <- [2] <- [3] <- [4]

The `ListNode` class lives in `challenges.common.structures`, along
with two helpers that make testing easy:

    list_to_linked([1, 2, 3])  builds 1 -> 2 -> 3 and returns its head
    linked_to_list(head)       turns a linked list back into [1, 2, 3]

========================================================================
THE RULES
========================================================================
Your functions must:
1. Return the new head of the reversed list (the old last node).
2. Return None when the list is empty (head is None).
3. Reverse the list IN PLACE: re-use the existing nodes by changing
   their `.next` pointers. Do not create new ListNode objects, and do
   not copy the values into a Python list and back.
4. Give the same result in both versions.

You can assume:
- The list has between 0 and 5_000 nodes.
- Node values are ints. They may be negative or repeated.
- Each recursive call uses up one level of Python's recursion limit
  (about 1000 levels by default). So the recursive version may crash
  on very long lists. Test it with lists shorter than about 500
  nodes.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return. The helpers come
from `challenges.common.structures`.

    linked_to_list(reverse_list(list_to_linked([1, 2, 3, 4])))
        ->  [4, 3, 2, 1]
        Build 1 -> 2 -> 3 -> 4, reverse it, read it back.

    linked_to_list(reverse_list(list_to_linked([7])))
        ->  [7]
        A single node reversed is itself.

    reverse_list(None)  ->  None
        An empty list stays empty.

========================================================================
COMPLEXITY TARGET
========================================================================
- reverse_list:           Time O(n): one walk along the list.
                          Space O(1): just a few variables.
- reverse_list_recursive: Time O(n): one call per node.
                          Space O(n): each call waits on the call
                          stack until the deeper ones finish, so there
                          is one stack frame per node.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list: reverse_list(None) -> None
- Single node -> the same node, and its .next is still None
- Two nodes: [1, 2] -> [2, 1]
- Duplicate values: [1, 1, 2] -> [2, 1, 1]
- The OLD head's .next must be None afterwards. Otherwise you made a
  cycle (a loop of nodes), and linked_to_list will loop forever!
- The returned head is the same object as the old tail (the old last
  node). Check it with `is`.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Draw it! Three boxes and arrows on paper. Decide what each variable
   points at before and after one step.
2. Iterative: keep two pointers, `prev` (starts as None) and `curr`
   (starts at head). Each step flips `curr.next` to point at `prev`.
3. Before you flip `curr.next`, save it (`nxt = curr.next`), or you
   lose the rest of the list forever.
4. One step is these four lines, in this order:
       nxt = curr.next
       curr.next = prev
       prev = curr
       curr = nxt
   When curr becomes None, `prev` is the new head.
5. Recursive: the base case is an empty list or a single node, so
   return it. Otherwise reverse everything after head
   (`new_head = recurse(head.next)`). Then make the node after head
   point back at head (`head.next.next = head`), set
   `head.next = None`, and return new_head.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Objects and references: variables hold references, not copies
- `is` vs `==` (same object vs equal value)
- `Optional[ListNode]` / `ListNode | None` type hints
- Tuple assignment: `a, b = b, a` evaluates the right side first
- Recursion: base case + recursive case, and `sys.getrecursionlimit()`

========================================================================
STRETCH GOALS
========================================================================
- Write the iterative version's loop body as one tuple-assignment
  line.
- Reverse only positions left..right (LeetCode #92).
- Reverse the list in groups of k (LeetCode #25).
"""

from __future__ import annotations

from challenges.common.structures import ListNode


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list in place using a loop.

    Args:
        head: The first node of the list, or None for an empty list.

    Returns:
        The new head of the reversed list (the old last node), or None if
        the list was empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list in place using recursion.

    Args:
        head: The first node of the list, or None for an empty list.

    Returns:
        The new head of the reversed list (the old last node), or None if
        the list was empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
