"""Ready-made data structures and builders for the linked list and tree challenges.

These are NOT challenges - they are fully implemented so your tests can build
inputs quickly and compare outputs easily. Read them, they are good examples!

Example (in a test):
    head = list_to_linked([1, 2, 3])        # 1 -> 2 -> 3
    assert linked_to_list(head) == [1, 2, 3]

    root = build_tree([2, 1, 3])            #     2
                                            #    / \
                                            #   1   3
    assert tree_to_list(root) == [2, 1, 3]
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Optional


# eq=False: nodes compare by identity (`is`), and the custom __repr__ shows
# only the value, so a list with a cycle never recurses forever.
@dataclass(eq=False)
class ListNode:
    """A node in a singly linked list. Compare lists with linked_to_list()."""

    val: int = 0
    next: Optional[ListNode] = None

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


@dataclass(eq=False)
class TreeNode:
    """A node in a binary tree. Compare trees with tree_to_list()."""

    val: int = 0
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def list_to_linked(values: list[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list. Returns the head (None if empty)."""
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def linked_to_list(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list back into a Python list. Do not call on a cyclic list."""
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order values, using None for missing nodes.

    This is the same format LeetCode uses, e.g. [3, 9, 20, None, None, 15, 7]:

            3
           / \\
          9   20
             /  \\
            15   7
    """
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        left = values[i] if i < len(values) else None
        if left is not None:
            node.left = TreeNode(left)
            queue.append(node.left)
        i += 1
        right = values[i] if i < len(values) else None
        if right is not None:
            node.right = TreeNode(right)
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    """Convert a binary tree to level-order values (trailing Nones trimmed)."""
    result: list[Optional[int]] = []
    queue: deque[Optional[TreeNode]] = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result
