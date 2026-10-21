r"""
Challenge: Binary Tree Level Order Traversal
Level:     11 - Trees and Graphs
Topics:    breadth-first search, queues, collections.deque
Source:    LeetCode #102 "Binary Tree Level Order Traversal"

========================================================================
YOUR TASK
========================================================================
Write `level_order(root)`. It RETURNS the tree's values grouped by
level (row), top to bottom, as a list of lists. Inside each level, the
values go from left to right.

    level_order(build_tree([3, 9, 20, None, None, 15, 7]))
        ->  [[3], [9, 20], [15, 7]]

========================================================================
HOW TO WALK A TREE ROW BY ROW (BFS)
========================================================================
            3                 level 0 -> [3]
           / \
          9   20              level 1 -> [9, 20]
             /  \
            15   7            level 2 -> [15, 7]

    result: [[3], [9, 20], [15, 7]]

(`build_tree` from `challenges.common.structures` builds this tree from
the list [3, 9, 20, None, None, 15, 7]: values row by row, with None
for a missing child.)

Visiting a tree row by row is called BREADTH-FIRST SEARCH (BFS). It
visits everything 1 step from the root, then everything 2 steps away,
and so on. (Its opposite, depth-first search or DFS, dives all the way
down one path before trying the next.)

BFS uses a QUEUE: first in, first out, like a line at a shop. You add
children to the BACK and take the next node from the FRONT. In Python,
use `collections.deque` for queues. `deque.popleft()` is O(1): it takes
the same tiny time however long the queue is. A plain list's `pop(0)`
has to shift every other item along by one, which is O(n): the longer
the list, the slower it gets.

To group by level, notice that at the start of each round the queue
holds EXACTLY the nodes of one level. Record `len(queue)`, pop that
many nodes, and push their children for the next round:

    queue: [3]          -> level [3],       push 9, 20
    queue: [9, 20]      -> level [9, 20],   push 15, 7
    queue: [15, 7]      -> level [15, 7],   push nothing
    queue: []           -> done

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a `list[list[int]]`: one inner list per level, top level
   first.
2. List the values inside each level from left to right.
3. Return an empty list [] for an empty tree (`root` is None).
4. Not change (mutate) the tree.

You can assume:
- `root` is a TreeNode or None.
- The tree has 0 to 2_000 nodes.
- Each node value is an int from -1000 to 1000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    level_order(build_tree([3, 9, 20, None, None, 15, 7]))
        ->  [[3], [9, 20], [15, 7]]
        The tree pictured above, one list per row.

    level_order(build_tree([1]))  ->  [[1]]
        One node, so one level holding one value.

    level_order(None)             ->  []
        An empty tree has no levels.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). Each of the n nodes goes in and out of the queue once.
- Space: O(w), where w is the number of nodes in the widest level (the
         most the queue ever holds), plus O(n) for the result list.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty tree: level_order(None) -> []
- Single node: build_tree([7]) -> [[7]]
- Left-leaning chain: [1, 2, None, 3] -> [[1], [2], [3]]
- A level with gaps: [1, 2, 3, None, 4, None, 5] -> [[1], [2, 3], [4, 5]]
  (4 is the right child of 2, and 5 is the right child of 3)
- Negative and duplicate values: [-1, 5, 5, -3] -> [[-1], [5, 5], [-3]]
- The number of inner lists equals the tree's max depth (for example,
  3 for [3, 9, 20, None, None, 15, 7])

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Handle the empty tree first: return [].
2. `queue = deque([root])` starts the BFS.
3. `while queue:`. Each pass of this outer loop handles ONE level.
4. Inside, `for _ in range(len(queue)):` popleft a node, append its value
   to the current level list, and append its non-None children to the
   queue.
5. After the inner loop, append the level list to the result.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `from collections import deque`: append, popleft, len
- Why `list.pop(0)` is slow (O(n)) and deque.popleft() is fast (O(1))
- `_` as a throwaway loop variable (a name for a value you don't use)
- Nested lists as return values: `list[list[int]]`

========================================================================
STRETCH GOALS
========================================================================
- Zigzag level order (LeetCode #103): alternate left->right, right->left.
- Right side view (LeetCode #199): the last value of each level.
- Solve it with DFS (recursion) instead: pass the depth down and append
  each value to result[depth].
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
