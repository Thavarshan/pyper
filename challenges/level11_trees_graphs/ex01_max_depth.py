r"""
Challenge: Maximum Depth of Binary Tree
Level:     11 - Trees and Graphs
Topics:    binary trees, recursion, depth-first search
Source:    LeetCode #104 "Maximum Depth of Binary Tree"

========================================================================
YOUR TASK
========================================================================
Write `max_depth(root)`. It takes the root (top node) of a binary tree
and RETURNS the tree's maximum depth: the number of nodes on the
longest path from the root down to a leaf.

    max_depth(build_tree([3, 9, 20, None, None, 15, 7]))  ->  3

========================================================================
WHAT "BINARY TREE" AND "DEPTH" MEAN
========================================================================
A binary tree is made of `TreeNode` objects. Each node has a `.val`
(its value), a `.left` child and a `.right` child. A child can be None,
which means "nothing there". The node at the top is the ROOT. A node
with no children is a LEAF.

Tests describe trees as "level order" lists: read the tree row by row,
left to right, and write None for a missing child. `build_tree` (from
`challenges.common.structures`) turns such a list into real nodes:

    build_tree([3, 9, 20, None, None, 15, 7])

            3            depth 1
           / \
          9   20         depth 2
             /  \
            15   7       depth 3

    The longest path is 3 -> 20 -> 15 (or 3 -> 20 -> 7): 3 nodes.

Depth counts NODES, not the lines between them. A single node has depth
1. An empty tree (root is None) has depth 0.

The key idea is recursion (a function that calls itself). A SUBTREE is
a child together with everything below it. The depth of a tree is 1
(for the root) plus the depth of its deeper subtree:

    depth(3)  = 1 + max(depth(9), depth(20))
              = 1 + max(1, 2)
              = 3

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the number of nodes on the longest root-to-leaf path, as an
   int.
2. Return 0 for an empty tree (`root` is None).
3. Not change (mutate) the tree.

You can assume:
- `root` is a TreeNode or None.
- The tree has 0 to 10_000 nodes.
- Node values are ints. They don't matter for this problem.

Note: a recursive solution is fine for balanced (bushy) trees. A
completely lopsided tree of 10_000 nodes is a chain 10_000 calls deep.
That is deeper than Python's default recursion limit (about 1_000), so
it would crash with RecursionError. See the stretch goals.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    max_depth(build_tree([3, 9, 20, None, None, 15, 7]))  ->  3
        The tree pictured above: 3 -> 20 -> 15 is 3 nodes long.

    max_depth(build_tree([1, None, 2]))                   ->  2
        1 has no left child. Its right child is 2. That is 2 nodes.

    max_depth(None)                                       ->  0
        An empty tree has no nodes at all.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). Visit each of the n nodes once.
- Space: O(h), where h is the height (the depth) of the tree. That is
         the most calls waiting on the recursion "stack" at once: one
         per level of the path you are currently on.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty tree (None) -> 0
- Single node, build_tree([1]) -> 1
- Only left children, build_tree([1, 2, None, 3, None, 4]) -> 4
  (a "linked list" leaning left: the answer is the number of nodes)
- Only right children, build_tree([1, None, 2, None, 3]) -> 3
- Perfect tree of 7 nodes, build_tree([1, 2, 3, 4, 5, 6, 7]) -> 3
- Unbalanced tree with the deepest leaf on the right,
  build_tree([1, 2, 3, None, None, None, 4, None, 5]) -> 4

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. What is the depth of an empty tree? That is your base case (the
   simple case that stops the recursion).
2. Trust the recursion: assume max_depth(root.left) already gives the
   correct depth of the left subtree.
3. Combine: 1 + max(left_depth, right_depth).
4. For a version without recursion, do a breadth-first search (BFS),
   which visits the tree one row at a time, using a deque. Count the
   rows.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Recursion on a recursive data structure
- The built-in `max()`
- `TreeNode | None` type hints
- `collections.deque` for the BFS alternative
- `sys.setrecursionlimit` and why deep recursion is risky in Python

========================================================================
STRETCH GOALS
========================================================================
- Write an iterative version (a loop, no recursion) using BFS: count
  the levels.
- Write an iterative depth-first (DFS) version: keep your own stack, a
  list of (node, depth) pairs, instead of using recursion.
- Minimum depth (LeetCode #111). Careful: it is NOT just min() instead
  of max()! For [1, None, 2], min() would give 1, but the only leaf is
  2, so the answer is 2.
"""

from __future__ import annotations

from challenges.common.structures import TreeNode


def max_depth(root: TreeNode | None) -> int:
    """Return the number of nodes on the longest root-to-leaf path.

    Args:
        root: The root of the tree, or None for an empty tree.

    Returns:
        The maximum depth (0 for an empty tree).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
