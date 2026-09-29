r"""Level 11 - Trees and Graphs.

Goal: learn to think about data shaped like a tree or a network, and the
two fundamental ways to explore it: depth-first and breadth-first search.

Binary trees
    A binary tree is made of nodes; each node holds a value and has at
    most two children, `left` and `right` (either may be None). The top
    node is the ROOT; nodes with no children are LEAVES. The DEPTH of a
    tree is the number of nodes on the longest root-to-leaf path.

            3          <- root (depth 1)
           / \
          9   20       <- depth 2
             /  \
            15   7     <- leaves (depth 3)

    Almost every tree problem is solved by recursion: "solve the problem
    for the left subtree, solve it for the right subtree, combine the two
    answers with the current node". The base case is nearly always "the
    node is None". `TreeNode`, `build_tree` and `tree_to_list` live in
    `challenges.common.structures`.

Binary search trees (BST)
    A BST is a binary tree with an ordering rule: for EVERY node, all
    values in its left subtree are smaller and all values in its right
    subtree are larger. That rule lets you find a value by going left or
    right at each step - like a binary search.

Depth-first search (DFS)
    DFS goes as deep as possible down one path before backing up and
    trying the next. Recursion gives you DFS naturally (the call stack
    remembers where to come back to); you can also use an explicit stack.

Breadth-first search (BFS)
    BFS explores in "rings": first everything 1 step away, then 2 steps,
    and so on. It uses a QUEUE (first in, first out). In Python use
    `collections.deque` - `popleft()` is O(1), whereas `list.pop(0)` is
    O(n). Because BFS visits nodes in order of distance, it finds SHORTEST
    paths in unweighted graphs.

Graphs and grids
    A graph is a set of nodes (vertices) joined by edges. Trees are a
    special kind of graph with no cycles. A grid is a graph too: each cell
    is a node connected to its neighbours. Graphs can have cycles, so when
    exploring one you must remember which nodes you have already VISITED
    (usually with a `set`) or you will loop forever. A common way to store
    a graph is an ADJACENCY LIST: a dict mapping each node to a list of its
    neighbours.

Topological sort
    In a directed graph where an edge A -> B means "A must come before B",
    a topological order lists every node so that all edges point forward.
    One exists only if the graph has no cycle. Kahn's algorithm (BFS on
    nodes with no remaining prerequisites) finds one.
"""
