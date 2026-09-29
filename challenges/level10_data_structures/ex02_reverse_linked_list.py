"""
Challenge: Reverse Linked List
Level:     10 - Data Structures
Topics:    linked lists, pointer manipulation, iteration vs recursion
Source:    LeetCode #206 "Reverse Linked List"

========================================================================
PROBLEM
========================================================================
You are given the `head` of a singly linked list (or `None` for an empty
list). Reverse the list so that every `.next` pointer points the other
way, and return the NEW head (which was the old last node).

A singly linked list is a chain of `ListNode` objects. Each node has a
`.val` (an int) and a `.next` (the next node, or None at the end):

    before:   head
               |
               v
              [1] -> [2] -> [3] -> [4] -> None

    after:                          new head
                                      |
                                      v
              None <- [1] <- [2] <- [3] <- [4]

Reverse the list IN PLACE: re-use the existing nodes by changing their
`.next` pointers. Do not create new ListNode objects and do not copy the
values into a Python list and back.

You will write TWO versions:
    - `reverse_list`           : iterative (a while loop)
    - `reverse_list_recursive` : recursive (the function calls itself)

Both must return the same result.

The `ListNode` class lives in `challenges.common.structures`, along with
`list_to_linked` and `linked_to_list` to make testing easy.

========================================================================
EXAMPLES
========================================================================
    >>> from challenges.common.structures import list_to_linked, linked_to_list
    >>> linked_to_list(reverse_list(list_to_linked([1, 2, 3, 4])))
    [4, 3, 2, 1]

    >>> linked_to_list(reverse_list(list_to_linked([7])))
    [7]

    >>> reverse_list(None) is None
    True

========================================================================
CONSTRAINTS
========================================================================
- The list has between 0 and 5_000 nodes.
- Node values are ints (may be negative or repeated).
- An empty list (head is None) -> return None.
- The recursive version may hit Python's recursion limit (~1000) on very
  long lists; tests for it should use lists shorter than ~500 nodes.

========================================================================
COMPLEXITY TARGET
========================================================================
- reverse_list:           Time O(n), Space O(1) (just a few variables).
- reverse_list_recursive: Time O(n), Space O(n) (one stack frame per node).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty list (None) -> None
- Single node -> the same node, whose .next is still None
- Two nodes -> [2, 1]
- Duplicate values [1, 1, 2] -> [2, 1, 1]
- The OLD head's .next must be None afterwards (otherwise you made a cycle
  and linked_to_list will loop forever!)
- The returned head is the same object as the old tail (use `is`)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Draw it! Three boxes and arrows on paper. Decide what each variable
   points at before and after one step.
2. Iterative: keep two pointers, `prev` (starts as None) and `curr`
   (starts at head). Each step flips `curr.next` to point at `prev`.
3. Before you flip `curr.next`, save it (`nxt = curr.next`), or you lose
   the rest of the list forever.
4. One step: nxt = curr.next; curr.next = prev; prev = curr; curr = nxt.
   When curr becomes None, `prev` is the new head.
5. Recursive: base case - empty or single node, return it. Otherwise
   reverse everything after head (`new_head = recurse(head.next)`), then
   make head.next point back at head, set head.next = None, return
   new_head.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Objects and references: variables hold references, not copies
- `is` vs `==` (same object vs equal value)
- `Optional[ListNode]` / `ListNode | None` type hints
- Tuple assignment: `a, b = b, a` evaluates the right side first
- Recursion: base case + recursive case; `sys.getrecursionlimit()`

========================================================================
STRETCH GOALS
========================================================================
- Do the iterative version's loop body in one tuple-assignment line.
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
