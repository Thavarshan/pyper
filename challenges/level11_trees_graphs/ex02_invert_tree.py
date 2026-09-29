r"""
Challenge: Invert Binary Tree
Level:     11 - Trees and Graphs
Topics:    binary trees, recursion, in-place mutation
Source:    LeetCode #226 "Invert Binary Tree"

========================================================================
PROBLEM
========================================================================
Given the `root` of a binary tree, INVERT it - produce its mirror image -
by swapping the left and right child of EVERY node. Return the root.

            4                       4
          /   \                   /   \
         2     7      ----->     7     2
        / \   / \               / \   / \
       1   3 6   9             9   6 3   1

    level order:  [4, 2, 7, 1, 3, 6, 9]  ->  [4, 7, 2, 9, 6, 3, 1]

Do this IN PLACE: change the `.left` / `.right` pointers of the existing
nodes; do not build new TreeNode objects. Return the same root object you
were given (or None for an empty tree), so the caller can write
`root = invert_tree(root)` or just `invert_tree(root)`.

Note that swapping only the root's children is not enough - the swap
must happen at every level (look at the bottom row above).

========================================================================
EXAMPLES
========================================================================
    >>> from challenges.common.structures import build_tree, tree_to_list
    >>> tree_to_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9])))
    [4, 7, 2, 9, 6, 3, 1]

    >>> tree_to_list(invert_tree(build_tree([2, 1, 3])))
    [2, 3, 1]

    >>> invert_tree(None) is None
    True

========================================================================
CONSTRAINTS
========================================================================
- The tree has 0 to 100 nodes (you can test bigger balanced trees).
- Node values are ints.
- The tree is modified in place, and the returned object `is` the root
  that was passed in.
- Empty tree -> return None.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n) - every node is visited once.
- Space: O(h) recursion stack, h = height of the tree.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty tree -> None
- Single node -> unchanged
- Only a left child: [1, 2] -> [1, None, 2]
- Perfect tree of 7 nodes (the example above)
- The returned node is the same object as the input root (`is`)
- Inverting twice gives back the original tree

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Base case: an empty tree inverted is still empty.
2. For one node, swapping is a single tuple assignment:
   node.left, node.right = node.right, node.left
3. After (or before) swapping, invert both subtrees recursively.
4. Don't forget to `return root` at the end.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Tuple assignment to swap two values without a temp variable
- Mutating objects in place vs building new ones
- Functions that mutate AND return (like this one) vs functions that only
  mutate (like list.sort(), which returns None)

========================================================================
STRETCH GOALS
========================================================================
- Write an iterative version using a deque (BFS) or a list (DFS stack).
- Write `is_symmetric(root)` (LeetCode #101): is a tree its own mirror?
- Write `mirrored_copy(root)` that returns a NEW inverted tree and leaves
  the original untouched.
"""

from __future__ import annotations

from challenges.common.structures import TreeNode


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    """Mirror a binary tree in place by swapping every node's children.

    Args:
        root: The root of the tree, or None for an empty tree.

    Returns:
        The same root object (now inverted), or None if the tree is empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
