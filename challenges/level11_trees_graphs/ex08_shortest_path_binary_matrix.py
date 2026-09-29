r"""
Challenge: Shortest Path in Binary Matrix
Level:     11 - Trees and Graphs
Topics:    BFS for shortest paths, grids, 8-directional movement
Source:    LeetCode #1091 "Shortest Path in Binary Matrix"

========================================================================
PROBLEM
========================================================================
You get an n x n grid of ints, where 0 is an open cell and 1 is a wall.
Find the length of the SHORTEST path from the top-left cell (0, 0) to
the bottom-right cell (n-1, n-1), moving only through 0 cells.

From any cell you may move in all 8 directions - up, down, left, right
AND the four diagonals:

        (r-1,c-1) (r-1,c) (r-1,c+1)
        (r,  c-1)  [r,c]  (r,  c+1)
        (r+1,c-1) (r+1,c) (r+1,c+1)

The path LENGTH is the number of CELLS visited, including both the start
and the end cell. If no such path exists (including when the start or
end cell is a wall), return -1.

Input representation: `grid` is a `list[list[int]]` of 0s and 1s (ints,
not strings - unlike the islands challenge).

    grid:                       path (marked *):
    [0, 0, 0]                   [*, *, 0]
    [1, 1, 0]                   [1, 1, *]
    [1, 1, 0]                   [1, 1, *]
                                -> length 4

Why BFS? BFS explores cells in order of distance from the start: first
all cells 1 step away, then 2 steps, and so on. So the FIRST time BFS
reaches the target, it has done so by a shortest route. (DFS would find
A path, but not necessarily the shortest.) Store the distance alongside
each cell in the queue: (row, col, distance).

The grid must NOT be mutated - track visited cells in a set (or a copy).

========================================================================
EXAMPLES
========================================================================
    >>> shortest_path_binary_matrix([[0, 1], [1, 0]])
    2

    >>> shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]])
    4

    >>> shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]])
    -1

    >>> shortest_path_binary_matrix([[0]])
    1

========================================================================
CONSTRAINTS
========================================================================
- The grid is square: n x n with 1 <= n <= 100.
- Every cell is the int 0 or 1.
- An empty grid [] -> raise ValueError.
- Do not mutate `grid`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2) - each cell is enqueued at most once.
- Space: O(n^2) for the visited set and queue.

========================================================================
EDGE CASES TO TEST
========================================================================
- 1x1 grid [[0]] -> 1; [[1]] -> -1
- Start cell is a wall -> -1
- End cell is a wall -> -1
- A diagonal-only route: [[0, 1], [1, 0]] -> 2
- A route that must wind around walls
- Completely blocked middle -> -1
- The grid is unchanged afterwards
- [] -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Check the special cases first: empty grid, start or end is 1.
2. Build the list of 8 direction offsets: every (dr, dc) with dr and dc
   in (-1, 0, 1), except (0, 0).
3. queue = deque([(0, 0, 1)]) and visited = {(0, 0)}.
4. Pop (r, c, d). If (r, c) is the target, return d. Otherwise push every
   in-bounds, open, unvisited neighbour with distance d + 1 (mark visited
   when pushing).
5. If the queue empties without reaching the target, return -1.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- BFS with `collections.deque` and distance tracking
- Generating offsets with a comprehension:
  `[(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]`
- Bounds checks with chained comparisons: `0 <= nr < n`
- Why BFS (not DFS) gives shortest paths in unweighted graphs

========================================================================
STRETCH GOALS
========================================================================
- Return the actual path as a list of (row, col) tuples (keep a `parent`
  dict and walk it backwards from the target).
- Support rectangular (non-square) grids.
- Allow only 4-directional movement via a parameter.
- Try A* search with a Chebyshev-distance heuristic using heapq.
"""


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    """Return the length of the shortest clear 8-directional path.

    Args:
        grid: An n x n grid of 0 (open) and 1 (wall) ints. Not modified.

    Returns:
        The number of cells on the shortest path from (0, 0) to
        (n-1, n-1), counting both ends, or -1 if no path exists.

    Raises:
        ValueError: If `grid` is empty.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
