r"""
Challenge: Validate Binary Search Tree
Level:     11 - Trees and Graphs
Topics:    binary search trees, recursion with bounds, in-order traversal
Source:    LeetCode #98 "Validate Binary Search Tree"

========================================================================
PROBLEM
========================================================================
Given the `root` of a binary tree, return True if it is a valid BINARY
SEARCH TREE (BST), otherwise False.

What is a BST? A binary tree where, for EVERY node:
    - every value in its LEFT subtree is STRICTLY LESS than the node's value
    - every value in its RIGHT subtree is STRICTLY GREATER than the node's
      value
    - both subtrees are themselves BSTs

"Strictly" means duplicates are NOT allowed: a tree containing the same
value twice is never a valid BST here.

            5                       5
           / \                     / \
          3   8     valid         3   8     INVALID
         / \   \                 / \
        1   4   9               1   6       6 is in 5's LEFT subtree,
                                            but 6 > 5!

The trap (right-hand tree): checking only "left child < node < right
child" at each node is NOT enough. 6 is a fine right child of 3, but it
breaks the rule for the ancestor 5. Every node must respect the limits
set by ALL of its ancestors.

Two classic approaches:
    1. Bounds: pass down an allowed range (low, high). The root may be
       anything; going left, the node's value becomes the new upper
       bound; going right, it becomes the new lower bound.
    2. In-order traversal (left, node, right) of a valid BST visits values
       in strictly increasing order.

========================================================================
EXAMPLES
========================================================================
    >>> from challenges.common.structures import build_tree
    >>> is_valid_bst(build_tree([2, 1, 3]))
    True

    >>> is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6]))
    False

    >>> is_valid_bst(build_tree([5, 3, 8, 1, 6]))
    False

    >>> is_valid_bst(build_tree([2, 2, 2]))
    False

========================================================================
CONSTRAINTS
========================================================================
- The tree has 0 to 10_000 nodes.
- Node values are ints, possibly very large or very negative (so don't
  use magic sentinel numbers like -999 for bounds).
- An empty tree (None) is a valid BST -> True.
- Do not modify the tree.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n)
- Space: O(h) recursion stack, h = height.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty tree -> True
- Single node -> True
- Duplicate value as a child: [2, 2] or [2, None, 2] -> False
- The "grandchild" trap: [5, 3, 8, 1, 6] -> False
- A valid larger BST, e.g. [8, 4, 12, 2, 6, 10, 14] -> True
- Very large / negative values, e.g. [-(2**40), None, 2**40] -> True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Write a helper `check(node, low, high)` that answers "is this subtree
   a BST whose values all lie strictly between low and high?"
2. Use `None` to mean "no bound" (or `float("-inf")` / `float("inf")`).
3. Base case: an empty node is valid.
4. If node.val <= low or node.val >= high -> False.
5. Otherwise recurse: check(node.left, low, node.val) and
   check(node.right, node.val, high).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Nested helper functions (a def inside a def)
- `float("inf")` and `float("-inf")` compare correctly with any int
- Default arguments for the initial bounds
- Generators: an in-order traversal written with `yield` / `yield from`

========================================================================
STRETCH GOALS
========================================================================
- Solve it with an in-order traversal generator and check each value is
  greater than the previous one.
- Allow a flag `allow_duplicates_left=True` where equal values may go in
  the left subtree.
- Find the k-th smallest value in a BST (LeetCode #230).
"""

from __future__ import annotations

from challenges.common.structures import TreeNode


def is_valid_bst(root: TreeNode | None) -> bool:
    """Return True if the tree is a strict binary search tree.

    Args:
        root: The root of the tree, or None for an empty tree.

    Returns:
        True if every node's left subtree holds only smaller values and
        its right subtree only larger values (no duplicates anywhere),
        otherwise False. An empty tree returns True.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
