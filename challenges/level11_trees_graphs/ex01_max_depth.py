r"""
Challenge: Maximum Depth of Binary Tree
Level:     11 - Trees and Graphs
Topics:    binary trees, recursion, depth-first search
Source:    LeetCode #104 "Maximum Depth of Binary Tree"

========================================================================
PROBLEM
========================================================================
Given the `root` of a binary tree, return its MAXIMUM DEPTH: the number
of nodes along the longest path from the root down to a leaf (a node
with no children).

A binary tree is a set of `TreeNode` objects, each with a `.val`, a
`.left` child and a `.right` child (children may be None). We describe
trees in tests using "level order" lists, reading row by row, left to
right, with None marking a missing child - `build_tree` understands this
format:

    build_tree([3, 9, 20, None, None, 15, 7])

            3            depth 1
           / \
          9   20         depth 2
             /  \
            15   7       depth 3        -> max depth = 3

Note: depth counts NODES, not edges. A single node has depth 1; an empty
tree (root is None) has depth 0.

This is the perfect first recursion-on-trees problem. The depth of a tree
is 1 (for the root) plus the larger of the depths of its two subtrees.

========================================================================
EXAMPLES
========================================================================
    >>> from challenges.common.structures import build_tree
    >>> max_depth(build_tree([3, 9, 20, None, None, 15, 7]))
    3

    >>> max_depth(build_tree([1, None, 2]))
    2

    >>> max_depth(None)
    0

========================================================================
CONSTRAINTS
========================================================================
- The tree has 0 to 10_000 nodes.
- Node values are ints (they do not matter for this problem).
- Empty tree -> 0.
- Do not modify the tree.
- A recursive solution is fine for balanced trees; a completely lopsided
  tree of 10_000 nodes would exceed Python's recursion limit (see stretch).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n) - visit every node once.
- Space: O(h) where h is the height (the recursion stack).

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty tree (None) -> 0
- Single node -> 1
- Only left children (a "linked list" leaning left) -> number of nodes
- Only right children -> number of nodes
- Perfect tree of 7 nodes -> 3
- Unbalanced tree where the deepest leaf is on the right

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. What is the depth of an empty tree? That is your base case.
2. Trust the recursion: assume max_depth(root.left) already gives the
   correct depth of the left subtree.
3. Combine: 1 + max(left_depth, right_depth).
4. For an iterative version, BFS level by level with a deque and count
   the levels.

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
- Write an iterative version using BFS (count levels).
- Write an iterative DFS version with an explicit stack of (node, depth).
- Minimum depth (LeetCode #111) - careful, it is NOT just min() instead
  of max()!
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
