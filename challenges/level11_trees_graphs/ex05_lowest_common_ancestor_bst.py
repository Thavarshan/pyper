r"""
Challenge: Lowest Common Ancestor of a Binary Search Tree
Level:     11 - Trees and Graphs
Topics:    binary search trees, using the BST ordering to prune the search
Source:    LeetCode #235 "Lowest Common Ancestor of a Binary Search Tree"

========================================================================
PROBLEM
========================================================================
You are given the `root` of a binary search tree (BST) and two values,
`p` and `q`, that are both stored somewhere in the tree. Return the VALUE
of their LOWEST COMMON ANCESTOR (LCA).

Definitions:
    - An ANCESTOR of a node is any node on the path from the root down to
      it - and a node counts as an ancestor of ITSELF.
    - A COMMON ancestor of p and q is an ancestor of both.
    - The LOWEST common ancestor is the common ancestor furthest from the
      root (deepest in the tree).

Reminder - BST: for every node, all values in the left subtree are
smaller and all values in the right subtree are larger. Values are unique.

                 6
              /     \
             2       8
            / \     / \
           0   4   7   9
              / \
             3   5

    p=2, q=8  -> 6   (they are on different sides of 6)
    p=2, q=4  -> 2   (2 is an ancestor of 4, and of itself)
    p=3, q=5  -> 4
    p=0, q=5  -> 2

Use the BST property! At any node, compare p and q with its value:
    - both smaller  -> the LCA must be in the left subtree
    - both larger   -> the LCA must be in the right subtree
    - otherwise (they split, or one of them equals the node) -> this node
      IS the LCA

For easy testing, return the LCA's `.val` (an int), not the node.

========================================================================
EXAMPLES
========================================================================
    >>> from challenges.common.structures import build_tree
    >>> root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    >>> lowest_common_ancestor(root, 2, 8)
    6
    >>> lowest_common_ancestor(root, 2, 4)
    2
    >>> lowest_common_ancestor(root, 3, 5)
    4

========================================================================
CONSTRAINTS
========================================================================
- The tree is a valid BST with 2 to 100_000 unique int values.
- `p` and `q` are both guaranteed to exist in the tree; p may be larger
  or smaller than q, and p may equal q (then the answer is p).
- Return an int (the node's value), not a TreeNode.
- Do not modify the tree.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(h), where h is the height - you walk ONE path down, never
         exploring both subtrees.
- Space: O(1) iterative (O(h) if recursive).

========================================================================
EDGE CASES TO TEST
========================================================================
- p and q on different sides of the root -> root value
- One node is an ancestor of the other -> that node's value
- p == q -> p
- Argument order does not matter: (p, q) and (q, p) give the same answer
- p or q is the root itself -> root value
- Both deep in the same subtree

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start at the root and walk downwards - you never need to go back up.
2. At each node there are three cases (see PROBLEM). Two of them move you
   down; one of them stops.
3. `if p < node.val and q < node.val: node = node.left`
4. A simple `while True:` loop works because both values are guaranteed
   to exist, so you always stop at the answer.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Turning tail recursion into a `while` loop
- Chained comparisons: `a < x < b`
- `min()` / `max()` to normalise p and q so p <= q

========================================================================
STRETCH GOALS
========================================================================
- LCA in a general binary tree with no ordering (LeetCode #236) - needs a
  full DFS.
- Raise ValueError if p or q is not in the tree (you'd need to verify
  existence along the way).
"""

from __future__ import annotations

from challenges.common.structures import TreeNode


def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> int:
    """Return the value of the lowest common ancestor of p and q in a BST.

    Args:
        root: The root of a valid binary search tree (not None).
        p: A value guaranteed to be in the tree.
        q: A value guaranteed to be in the tree.

    Returns:
        The value of the deepest node that is an ancestor of both p and q
        (a node counts as its own ancestor).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
