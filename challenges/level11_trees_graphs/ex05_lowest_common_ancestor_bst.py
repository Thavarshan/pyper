r"""
Challenge: Lowest Common Ancestor of a Binary Search Tree
Level:     11 - Trees and Graphs
Topics:    binary search trees, using the BST ordering to prune the search
Source:    LeetCode #235 "Lowest Common Ancestor of a Binary Search Tree"

========================================================================
YOUR TASK
========================================================================
Write `lowest_common_ancestor(root, p, q)`. `root` is the top of a
binary search tree (BST), and `p` and `q` are two values stored in it.
Return the VALUE (an int) of their lowest common ancestor: the deepest
node that has both p and q at or below it.

    lowest_common_ancestor(build_tree([6, 2, 8, 0, 4, 7, 9]), 2, 8)  ->  6

========================================================================
WHAT "LOWEST COMMON ANCESTOR" MEANS
========================================================================
    - An ANCESTOR of a node is any node on the path from the root down
      to it. A node also counts as an ancestor of ITSELF.
    - A COMMON ancestor of p and q is an ancestor of both.
    - The LOWEST common ancestor (LCA) is the common ancestor furthest
      from the root (the deepest one in the tree).

A BST follows an ordering rule: for every node, all values in its left
subtree are smaller, and all values in its right subtree are larger.
(A subtree is a child together with everything below it.) Values are
unique.

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

Use the ordering rule! Start at the root. At each node, compare p and q
with the node's value:
    - both smaller  -> the LCA must be in the left subtree: go left
    - both larger   -> the LCA must be in the right subtree: go right
    - otherwise (one is smaller and one is larger, or one of them
      equals the node) -> this node IS the LCA

Walk-through for p=3, q=5:

    at 6:  3 and 5 are both smaller  -> go left
    at 2:  3 and 5 are both larger   -> go right
    at 4:  3 is smaller, 5 is larger -> stop, the answer is 4

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the LCA's `.val` (an int), NOT the TreeNode itself. This
   keeps testing easy.
2. Give the same answer whichever order p and q come in.
3. Return p when p equals q.
4. Not change (mutate) the tree.

You can assume:
- `root` is a valid BST (never None) with 2 to 100_000 unique int
  values. A tree that big can be very tall, so a `while` loop is safer
  than recursion here (deep recursion crashes with RecursionError).
- `p` and `q` are both in the tree. p may be larger or smaller than q,
  and p may equal q.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return. All use the tree
pictured above:

    root = build_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])

    lowest_common_ancestor(root, 2, 8)  ->  6
        2 is to the left of 6 and 8 is to the right, so they split at 6.

    lowest_common_ancestor(root, 2, 4)  ->  2
        4 is below 2, and 2 counts as its own ancestor.

    lowest_common_ancestor(root, 3, 5)  ->  4
        See the walk-through above.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(h), where h is the height of the tree. You walk ONE path
         down and never explore both subtrees.
- Space: O(1) with a loop: only a variable or two, however big the tree
         is. (O(h) if you use recursion, one waiting call per level.)

========================================================================
EDGE CASES TO TEST
========================================================================
Using the tree pictured above:
- p and q on different sides of the root: (2, 8) -> 6
- One node is an ancestor of the other: (2, 4) -> 2
- p == q: (5, 5) -> 5
- Argument order does not matter: (8, 2) -> 6, the same as (2, 8)
- p or q is the root itself: (6, 3) -> 6
- Both deep in the same subtree: (0, 3) -> 2, and (7, 9) -> 8

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start at the root and walk downwards. You never need to go back up.
2. At each node there are three cases (see the background above). Two of
   them move you down. One of them stops.
3. `if p < node.val and q < node.val: node = node.left`
4. A simple `while True:` loop works. Both values are guaranteed to be in
   the tree, so you always stop at the answer.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Turning tail recursion (a function whose last step is calling
  itself) into a `while` loop
- Chained comparisons: `a < x < b`
- `min()` / `max()` to normalise p and q so p <= q

========================================================================
STRETCH GOALS
========================================================================
- LCA in a general binary tree with no ordering (LeetCode #236). This
  needs a full depth-first search (DFS) of both subtrees.
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
