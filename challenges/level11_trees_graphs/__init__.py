r"""Level 11 - Trees and Graphs.

Goal: learn to think about data shaped like a tree or a network, and the
two basic ways to explore it: depth-first and breadth-first search.

Binary trees
    A binary tree is made of nodes. Each node holds a value and has at
    most two children, `left` and `right` (either may be None). The top
    node is the ROOT. Nodes with no children are LEAVES. The DEPTH of a
    tree is the number of nodes on the longest root-to-leaf path. A
    SUBTREE is a child together with everything below it.

            3          <- root (depth 1)
           / \
          9   20       <- depth 2
             /  \
            15   7     <- leaves (depth 3)

    Almost every tree problem is solved by recursion (a function that
    calls itself): "solve the problem for the left subtree, solve it for
    the right subtree, then combine the two answers with the current
    node". The base case (the simple case that stops the recursion) is
    nearly always "the node is None". `TreeNode`, `build_tree` and
    `tree_to_list` live in `challenges.common.structures`.

Binary search trees (BST)
    A BST is a binary tree with an ordering rule: for EVERY node, all
    values in its left subtree are smaller and all values in its right
    subtree are larger. That rule lets you find a value by going left or
    right at each step, like a binary search.

Depth-first search (DFS)
    DFS goes as deep as possible down one path before backing up and
    trying the next. Recursion gives you DFS naturally: Python's call
    stack remembers where to come back to. You can also keep your own
    stack in a list.

Breadth-first search (BFS)
    BFS explores in "rings": first everything 1 step away, then 2 steps,
    and so on. It uses a QUEUE (first in, first out, like a line at a
    shop). In Python use `collections.deque`: its `popleft()` is O(1)
    (equally fast however long the queue is), whereas `list.pop(0)` is
    O(n) (it shifts every other item, so it gets slower as the list
    grows). Because BFS visits nodes in order of distance, it finds
    SHORTEST paths in unweighted graphs (graphs where every step costs
    the same).

Graphs and grids
    A graph is a set of nodes (also called vertices) joined by edges
    (connections). Trees are a special kind of graph with no cycles
    (no loops leading back to where you started). A grid is a graph too:
    each cell is a node connected to its neighbours. Graphs can have
    cycles, so when exploring one you must remember which nodes you have
    already VISITED (usually with a `set`), or you will loop forever. A
    common way to store a graph is an ADJACENCY LIST: a dict mapping each
    node to a list of its neighbours.

Topological sort
    In a directed graph (one where edges are one-way arrows), an edge
    A -> B can mean "A must come before B". A topological order lists
    every node so that all edges point forward. One exists only if the
    graph has no cycle. Kahn's algorithm finds one with BFS: repeatedly
    take a node that has no remaining prerequisites.
"""
