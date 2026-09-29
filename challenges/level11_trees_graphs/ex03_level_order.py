r"""
Challenge: Binary Tree Level Order Traversal
Level:     11 - Trees and Graphs
Topics:    breadth-first search, queues, collections.deque
Source:    LeetCode #102 "Binary Tree Level Order Traversal"

========================================================================
PROBLEM
========================================================================
Given the `root` of a binary tree, return the values of its nodes grouped
by LEVEL (row), top to bottom. Within each level, list the values from
left to right.

            3                 level 0 -> [3]
           / \
          9   20              level 1 -> [9, 20]
             /  \
            15   7            level 2 -> [15, 7]

    result: [[3], [9, 20], [15, 7]]

The return type is `list[list[int]]`: one inner list per level. An empty
tree returns an empty list [].

This is BREADTH-FIRST SEARCH (BFS). Instead of diving deep (DFS), BFS
visits all nodes at distance 1, then all at distance 2, and so on. It
uses a QUEUE - first in, first out, like a line at a shop: you add
children to the BACK and take the next node from the FRONT.

In Python, use `collections.deque` for queues. `deque.popleft()` is O(1).
A plain list's `pop(0)` has to shift every other element, which is O(n).

To group by level, notice that at the start of each round the queue holds
EXACTLY the nodes of one level. Record `len(queue)`, pop that many, and
push their children for the next round:

    queue: [3]          -> level [3],       push 9, 20
    queue: [9, 20]      -> level [9, 20],   push 15, 7
    queue: [15, 7]      -> level [15, 7],   push nothing
    queue: []           -> done

========================================================================
EXAMPLES
========================================================================
    >>> from challenges.common.structures import build_tree
    >>> level_order(build_tree([3, 9, 20, None, None, 15, 7]))
    [[3], [9, 20], [15, 7]]

    >>> level_order(build_tree([1]))
    [[1]]

    >>> level_order(None)
    []

========================================================================
CONSTRAINTS
========================================================================
- The tree has 0 to 2_000 nodes.
- -1000 <= node value <= 1000.
- Empty tree -> [].
- Do not modify the tree.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n)
- Space: O(w) where w is the widest level (the queue), plus O(n) output.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty tree -> []
- Single node -> [[value]]
- Left-leaning chain [1, 2, None, 3] -> [[1], [2], [3]]
- A level with gaps: [1, 2, 3, None, 4, None, 5] -> [[1], [2, 3], [4, 5]]
- Negative and duplicate values
- Number of inner lists equals the tree's max depth

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Handle the empty tree first: return [].
2. `queue = deque([root])` starts the BFS.
3. `while queue:` - each iteration of this outer loop handles ONE level.
4. Inside, `for _ in range(len(queue)):` popleft a node, append its value
   to the current level list, and append its non-None children to the
   queue.
5. After the inner loop, append the level list to the result.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `from collections import deque`: append, popleft, len
- Why `list.pop(0)` is slow (O(n)) and deque.popleft() is fast (O(1))
- `_` as a throwaway loop variable
- Nested lists as return values: `list[list[int]]`

========================================================================
STRETCH GOALS
========================================================================
- Zigzag level order (LeetCode #103): alternate left->right, right->left.
- Right side view (LeetCode #199): the last value of each level.
- Solve it with DFS instead, passing the depth down and appending to
  result[depth].
"""

from __future__ import annotations

from challenges.common.structures import TreeNode


def level_order(root: TreeNode | None) -> list[list[int]]:
    """Return the tree's values grouped by level, top to bottom.

    Args:
        root: The root of the tree, or None for an empty tree.

    Returns:
        A list of levels; each level is a list of values from left to
        right. An empty tree returns [].
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
