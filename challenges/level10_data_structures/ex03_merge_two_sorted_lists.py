"""
Challenge: Merge Two Sorted Lists
Level:     10 - Data Structures
Topics:    linked lists, the dummy/sentinel node trick, two pointers
Source:    LeetCode #21 "Merge Two Sorted Lists"

========================================================================
PROBLEM
========================================================================
You get the heads of two singly linked lists, `list1` and `list2`. Each
list is already sorted in non-decreasing order (smallest first,
duplicates allowed). Combine them into ONE sorted linked list and return
its head.

Build the result by re-linking (splicing) the existing nodes - do not
create new ListNode objects for the values, and do not dump the values
into a Python list and sort it.

    list1:   [1] -> [3] -> [5] -> None
    list2:   [2] -> [3] -> [6] -> [8] -> None

    result:  [1] -> [2] -> [3] -> [3] -> [5] -> [6] -> [8] -> None

When two values are equal, it does not matter which list's node comes
first (the resulting VALUES are the same either way).

The DUMMY NODE trick: the fiddly part is choosing the first node of the
result. A common trick is to create one throw-away "dummy" node, build
the answer hanging off `dummy.next`, and return `dummy.next` at the end.
That way "the result is still empty" is never a special case. (This
extra node is allowed - it is not part of the answer.)

========================================================================
EXAMPLES
========================================================================
    >>> from challenges.common.structures import list_to_linked, linked_to_list
    >>> a = list_to_linked([1, 2, 4])
    >>> b = list_to_linked([1, 3, 4])
    >>> linked_to_list(merge_two_lists(a, b))
    [1, 1, 2, 3, 4, 4]

    >>> merge_two_lists(None, None) is None
    True

    >>> linked_to_list(merge_two_lists(None, list_to_linked([0])))
    [0]

========================================================================
CONSTRAINTS
========================================================================
- Each list has between 0 and 50 nodes (you can test bigger).
- -100 <= node value <= 100.
- Both inputs are sorted in non-decreasing order.
- Both empty -> return None.
- The input lists may be modified (their nodes are re-used).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n + m) - each node is visited once.
- Space: O(1) extra (iterative), ignoring the output which re-uses nodes.

========================================================================
EDGE CASES TO TEST
========================================================================
- Both empty -> None
- One empty -> the other list unchanged
- All of list1 smaller than all of list2 -> list1 then list2
- Lists of very different lengths
- Duplicate values across and within lists
- Negative values

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Compare the two current heads. The smaller one must come next in
   the result.
2. Keep a `tail` pointer to the last node of the result so you can
   attach the next node with `tail.next = ...`.
3. Start with `dummy = ListNode()` and `tail = dummy`.
4. Loop while BOTH lists still have nodes: attach the smaller head,
   advance that list, advance tail.
5. When one list runs out, the other is already sorted - attach the whole
   remainder in one step: `tail.next = list1 or list2`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The sentinel / dummy node pattern
- `x or y` returns the first truthy value (a node, or None)
- `while a and b:` loops
- Recursion as an alternative: merge(a, b) = smaller head + merge(rest)

========================================================================
STRETCH GOALS
========================================================================
- Write a recursive version.
- Merge k sorted lists (LeetCode #23) using `heapq`.
"""

from __future__ import annotations

from challenges.common.structures import ListNode


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """Merge two sorted linked lists into one sorted linked list.

    Args:
        list1: Head of the first sorted list, or None if empty.
        list2: Head of the second sorted list, or None if empty.

    Returns:
        The head of the merged sorted list made from the original nodes,
        or None if both inputs are empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
