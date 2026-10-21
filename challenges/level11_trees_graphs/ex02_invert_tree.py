r"""
Challenge: Invert Binary Tree
Level:     11 - Trees and Graphs
Topics:    binary trees, recursion, in-place mutation
Source:    LeetCode #226 "Invert Binary Tree"

========================================================================
YOUR TASK
========================================================================
Write `invert_tree(root)`. It turns a binary tree into its mirror image
by swapping the left and right child of EVERY node. It changes the tree
it was given and RETURNS the same root.

    tree_to_list(invert_tree(build_tree([2, 1, 3])))  ->  [2, 3, 1]

========================================================================
WHAT "INVERT" MEANS
========================================================================
Picture holding the tree up to a mirror. Everything on the left ends
up on the right, at every level:

            4                       4
          /   \                   /   \
         2     7      ----->     7     2
        / \   / \               / \   / \
       1   3 6   9             9   6 3   1

    level order:  [4, 2, 7, 1, 3, 6, 9]  ->  [4, 7, 2, 9, 6, 3, 1]

("Level order" means reading the tree row by row, left to right.
`build_tree` turns such a list into a tree, and `tree_to_list` turns a
tree back into a list. Both live in `challenges.common.structures`.)

Swapping only the root's two children is not enough. Look at the bottom
row: 1 and 3 swapped places too, and so did 6 and 9.

You do this IN PLACE: change the `.left` and `.right` pointers of the
nodes you were given. Do not build new TreeNode objects.

========================================================================
THE RULES
========================================================================
Your function must:
1. Swap the `.left` and `.right` children of every node in the tree.
2. Change (mutate) the existing nodes. Do not create new TreeNode
   objects.
3. Return the same root object that was passed in, so
   `invert_tree(root) is root` is True. This lets the caller write
   either `root = invert_tree(root)` or just `invert_tree(root)`.
4. Return None for an empty tree (`root` is None).

You can assume:
- `root` is a TreeNode or None.
- The tree has 0 to 100 nodes (you can test bigger balanced trees).
- Node values are ints.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    tree_to_list(invert_tree(build_tree([4, 2, 7, 1, 3, 6, 9])))
        ->  [4, 7, 2, 9, 6, 3, 1]
        The tree pictured above, mirrored at every level.

    tree_to_list(invert_tree(build_tree([2, 1, 3])))  ->  [2, 3, 1]
        The root's two children swap places.

    invert_tree(None)                                 ->  None
        An empty tree stays empty.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). Each of the n nodes is visited once.
- Space: O(h), where h is the height of the tree. That is the deepest
         the recursion goes: one waiting call per level.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty tree: invert_tree(None) -> None
- Single node: build_tree([1]) -> still [1]
- Only a left child: [1, 2] -> [1, None, 2]
  (2 moves from the left side to the right side)
- Perfect tree of 7 nodes: [4, 2, 7, 1, 3, 6, 9] -> [4, 7, 2, 9, 6, 3, 1]
- The returned node is the same object as the input root
  (`invert_tree(root) is root` -> True)
- Inverting twice gives back the original tree:
  [4, 2, 7, 1, 3, 6, 9] -> [4, 2, 7, 1, 3, 6, 9]

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Base case (the simple case that stops the recursion): an empty tree
   inverted is still empty.
2. For one node, swapping is a single tuple assignment:
   node.left, node.right = node.right, node.left
3. After (or before) swapping, invert both subtrees (each child and
   everything below it) recursively.
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
- Write an iterative version (a loop, no recursion) using a deque as a
  queue (BFS, row by row) or a list as a stack (DFS, deep first).
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
