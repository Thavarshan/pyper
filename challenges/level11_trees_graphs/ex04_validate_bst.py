r"""
Challenge: Validate Binary Search Tree
Level:     11 - Trees and Graphs
Topics:    binary search trees, recursion with bounds, in-order traversal
Source:    LeetCode #98 "Validate Binary Search Tree"

========================================================================
YOUR TASK
========================================================================
Write `is_valid_bst(root)`. It RETURNS True if the binary tree is a
valid binary search tree (BST), and False otherwise.

    is_valid_bst(build_tree([2, 1, 3]))  ->  True

========================================================================
WHAT A "BINARY SEARCH TREE" IS
========================================================================
A BST is a binary tree that follows an ordering rule at EVERY node:
    - every value in its LEFT subtree is STRICTLY LESS than the node's
      value
    - every value in its RIGHT subtree is STRICTLY GREATER than the
      node's value
(A SUBTREE is a child together with everything below it.)

"Strictly" means equal values are NOT allowed. A tree that contains the
same value twice is never a valid BST here.

            5                       5
           / \                     / \
          3   8     valid         3   8     INVALID
         / \   \                 / \
        1   4   9               1   6       6 is in 5's LEFT subtree,
                                            but 6 > 5!

THE TRAP (right-hand tree): checking only "left child < node < right
child" at each node is NOT enough. 6 is a fine right child of 3, but it
breaks the rule for 5, higher up. Every node must respect the limits
set by ALL of its ancestors (the nodes above it on the path from the
root).

Two classic ways to check:

1. Bounds. Pass an allowed range (low, high) down the tree. The root
   may be anything. Going LEFT, the node's value becomes the new upper
   limit. Going RIGHT, it becomes the new lower limit. Here is the
   right-hand tree above:

       check 5 in (-inf, +inf)  -> ok
       check 3 in (-inf, 5)     -> ok    (left of 5: must be < 5)
       check 1 in (-inf, 3)     -> ok    (left of 3: must be < 3)
       check 6 in (3, 5)        -> FAIL  (right of 3, but still left of 5)

2. In-order traversal. Visit the left subtree, then the node, then the
   right subtree. For a valid BST this visits the values in strictly
   increasing order. The valid tree gives 1, 3, 4, 5, 8, 9. The invalid
   one gives 1, 3, 6, 5, 8 (6 then 5 goes down).

========================================================================
THE RULES
========================================================================
Your function must:
1. Return True if every node's left subtree holds only smaller values
   and its right subtree only larger values. Otherwise return False.
2. Return False if any value appears twice (duplicates are never
   allowed, on either side).
3. Return True for an empty tree (`root` is None).
4. Not change (mutate) the tree.

You can assume:
- `root` is a TreeNode or None.
- The tree has 0 to 10_000 nodes.
- Node values are ints, possibly very large or very negative. So don't
  use a made-up "sentinel" number (a special stand-in value) like -999
  to mean "no limit": a real node could hold a smaller value.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    is_valid_bst(build_tree([2, 1, 3]))                      ->  True
        1 is less than 2, and 3 is greater than 2.

    is_valid_bst(build_tree([5, 1, 4, None, None, 3, 6]))    ->  False
        4 is the RIGHT child of 5, but 4 is less than 5.

    is_valid_bst(build_tree([5, 3, 8, 1, 6]))                ->  False
        The trap tree pictured above: 6 sits left of 5.

    is_valid_bst(build_tree([2, 2, 2]))                      ->  False
        Duplicates are not allowed.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). Visit each of the n nodes once.
- Space: O(h), where h is the height of the tree. That is the deepest
         the recursion goes: one waiting call per level.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty tree: is_valid_bst(None) -> True
- Single node: build_tree([1]) -> True
- Duplicate value as a child: [2, 2] -> False, and [2, None, 2] -> False
- The "grandchild" trap: [5, 3, 8, 1, 6] -> False
- A valid larger BST: [8, 4, 12, 2, 6, 10, 14] -> True
- Very large and very negative values: [-(2**40), None, 2**40] -> True

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Write a helper `check(node, low, high)` that answers "is this subtree
   a BST whose values all lie strictly between low and high?"
2. Use `None` to mean "no limit" (or `float("-inf")` / `float("inf")`,
   minus and plus infinity).
3. Base case (the simple case that stops the recursion): an empty node
   is valid.
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
- Solve it with an in-order traversal generator (a function that uses
  `yield` to hand out values one at a time) and check that each value
  is greater than the previous one.
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
