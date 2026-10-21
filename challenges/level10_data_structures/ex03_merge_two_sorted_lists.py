"""
Challenge: Merge Two Sorted Lists
Level:     10 - Data Structures
Topics:    linked lists, the dummy/sentinel node trick, two pointers
Source:    LeetCode #21 "Merge Two Sorted Lists"

========================================================================
YOUR TASK
========================================================================
Write `merge_two_lists(list1, list2)`. It gets the heads of two sorted
linked lists and RETURNS the head of ONE sorted linked list made from
all their nodes.

    list1:   [1] -> [3] -> [5] -> None
    list2:   [2] -> [3] -> [6] -> [8] -> None

    result:  [1] -> [2] -> [3] -> [3] -> [5] -> [6] -> [8] -> None

========================================================================
BACKGROUND
========================================================================
A linked list is a chain of `ListNode` objects. Each node has a `.val`
and a `.next` (the next node, or None at the end). The `ListNode`
class and two test helpers live in `challenges.common.structures`:

    list_to_linked([1, 2, 3])  builds 1 -> 2 -> 3 and returns its head
    linked_to_list(head)       turns a linked list back into [1, 2, 3]

"Sorted" here means non-decreasing: smallest first, and duplicates
are allowed.

THE DUMMY NODE TRICK: the fiddly part is choosing the first node of
the result. A common trick is to create one throw-away "dummy" node
(also called a sentinel, a special stand-in node). You build the
answer hanging off `dummy.next` and return `dummy.next` at the end.
That way "the result is still empty" is never a special case. This
one extra node is allowed: it is not part of the answer.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the head of one linked list, sorted in non-decreasing order,
   holding every node from both inputs.
2. Return None when both lists are empty.
3. Build the result by re-linking (splicing) the existing nodes. Do
   not create new ListNode objects for the values, and do not dump the
   values into a Python list and sort it. (The one dummy node above is
   fine.)

When two values are equal, it does not matter which list's node comes
first. The resulting VALUES are the same either way.

You can assume:
- Both inputs are sorted in non-decreasing order.
- Each list has between 0 and 50 nodes (you can test bigger ones).
- -100 <= node value <= 100.
- The input lists may be changed (mutated), since their nodes are
  re-used.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return. The helpers come
from `challenges.common.structures`.

    a = list_to_linked([1, 2, 4])
    b = list_to_linked([1, 3, 4])
    linked_to_list(merge_two_lists(a, b))  ->  [1, 1, 2, 3, 4, 4]
        Take the smaller front node each time.

    merge_two_lists(None, None)  ->  None
        Both lists are empty, so the result is empty.

    linked_to_list(merge_two_lists(None, list_to_linked([0])))  ->  [0]
        One list is empty, so the result is the other list.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n + m): each node of both lists is visited once.
- Space: O(1) extra (iterative): only a few pointer variables. The
  output doesn't count, because it re-uses the existing nodes.

========================================================================
EDGE CASES TO TEST
========================================================================
- Both empty: merge_two_lists(None, None) -> None
- One empty: merge_two_lists(list_to_linked([1, 2]), None) gives
  [1, 2], the other list unchanged
- All of list1 smaller than all of list2: [1, 2] and [5, 6] ->
  [1, 2, 5, 6] (list1 then list2)
- Lists of very different lengths: [5] and [1, 2, 3, 7, 9] ->
  [1, 2, 3, 5, 7, 9]
- Duplicate values across and within lists: [1, 1, 3] and [1, 3] ->
  [1, 1, 1, 3, 3]
- Negative values: [-3, 0] and [-5, 2] -> [-5, -3, 0, 2]

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Compare the two current heads. The smaller one must come next in
   the result.
2. Keep a `tail` pointer to the last node of the result, so you can
   attach the next node with `tail.next = ...`.
3. Start with `dummy = ListNode()` and `tail = dummy`.
4. Loop while BOTH lists still have nodes: attach the smaller head,
   move that list on to its next node, and move tail on.
5. When one list runs out, the other is already sorted. Attach the
   whole remainder in one step: `tail.next = list1 or list2`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The sentinel / dummy node pattern
- `x or y` gives back x if x is truthy (treated as True by `if`),
  otherwise y. Here that means "a node, or None".
- `while a and b:` loops
- Recursion as an alternative: merge(a, b) = smaller head +
  merge(rest)

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
