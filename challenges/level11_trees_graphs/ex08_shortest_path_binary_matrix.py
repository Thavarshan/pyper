r"""
Challenge: Shortest Path in Binary Matrix
Level:     11 - Trees and Graphs
Topics:    BFS for shortest paths, grids, 8-directional movement
Source:    LeetCode #1091 "Shortest Path in Binary Matrix"

========================================================================
YOUR TASK
========================================================================
Write `shortest_path_binary_matrix(grid)`. The grid is a square of ints
where 0 is an open cell and 1 is a wall. RETURN the length of the
shortest path from the top-left cell to the bottom-right cell through
open cells, or -1 if there is no such path.

    shortest_path_binary_matrix([[0, 1], [1, 0]])  ->  2

========================================================================
HOW MOVES AND LENGTHS WORK, AND WHY BFS FINDS THE SHORTEST
========================================================================
From any cell you may move in all 8 directions: up, down, left, right
AND the four diagonals:

        (r-1,c-1) (r-1,c) (r-1,c+1)
        (r,  c-1)  [r,c]  (r,  c+1)
        (r+1,c-1) (r+1,c) (r+1,c+1)

The path LENGTH is the number of CELLS on it, counting both the start
cell (0, 0) and the end cell (n-1, n-1). So [[0]] has a path of length
1: the start is already the end.

    grid:                       path (marked *):
    [0, 0, 0]                   [*, *, 0]
    [1, 1, 0]                   [1, 1, *]
    [1, 1, 0]                   [1, 1, *]
                                -> length 4

Use breadth-first search (BFS). BFS uses a queue (first in, first out)
and explores cells in order of distance from the start: first every
cell 1 step away, then every cell 2 steps away, and so on. So the FIRST
time BFS reaches the target, it got there by a shortest route.
(Depth-first search, DFS, would find A path, but not necessarily the
shortest one.) Store each cell's distance with it in the queue as
(row, col, distance).

Here is the distance BFS gives each open cell in the grid above
(# is a wall):

    [1, 2, 3]
    [#, #, 3]          (1, 2) gets 3: one diagonal step from (0, 1)
    [#, #, 4]          the target (2, 2) gets 4 -> the answer

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the number of cells on the shortest path from (0, 0) to
   (n-1, n-1), moving in any of the 8 directions through 0 cells only.
2. Return -1 if no such path exists. That includes when the start cell
   or the end cell is a wall.
3. Raise ValueError if `grid` is empty ([]).
4. Not change (mutate) `grid`. Track visited cells in a set (or use a
   copy).

You can assume:
- Apart from [], the grid is square: n x n, with n from 1 to 100.
- Every cell is the int 0 or 1 (ints, not strings, unlike the islands
  challenge).

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    shortest_path_binary_matrix([[0, 1], [1, 0]])                  ->  2
        One diagonal step: (0, 0) then (1, 1). Two cells.

    shortest_path_binary_matrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]])  ->  4
        The grid pictured above.

    shortest_path_binary_matrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]])  ->  -1
        The start cell is a wall.

    shortest_path_binary_matrix([[0]])                              ->  1
        The start is the end: a path of one cell.

    shortest_path_binary_matrix([])  ->  raises ValueError

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n^2), where n is the side length (so n^2 is the number of
         cells). Each cell goes into the queue at most once.
- Space: O(n^2) for the visited set and the queue.

========================================================================
EDGE CASES TO TEST
========================================================================
- 1x1 grids: [[0]] -> 1, and [[1]] -> -1
- Start cell is a wall: [[1, 0], [0, 0]] -> -1
- End cell is a wall: [[0, 0], [0, 1]] -> -1
- A diagonal-only route: [[0, 1], [1, 0]] -> 2
- A route that must wind around walls -> 13 for
      [[0, 1, 0, 0, 0],
       [0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0],
       [0, 1, 0, 1, 0],
       [0, 0, 0, 1, 0]]
- Completely blocked middle: [[0, 0, 0], [1, 1, 1], [0, 0, 0]] -> -1
- The grid is unchanged afterwards (compare it with a copy made by
  copy.deepcopy before the call)
- [] -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Check the special cases first: empty grid, start or end is 1.
2. Build the list of 8 direction offsets: every (dr, dc) with dr and dc
   in (-1, 0, 1), except (0, 0).
3. queue = deque([(0, 0, 1)]) and visited = {(0, 0)}.
4. Pop (r, c, d). If (r, c) is the target, return d. Otherwise push every
   neighbour that is inside the grid, open and not yet visited, with
   distance d + 1. Mark it visited when you push it.
5. If the queue empties without reaching the target, return -1.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- BFS with `collections.deque` and distance tracking
- Generating offsets with a comprehension:
  `[(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]`
- Bounds checks with chained comparisons: `0 <= nr < n`
- Why BFS (not DFS) gives shortest paths in unweighted graphs (graphs
  where every step costs the same)

========================================================================
STRETCH GOALS
========================================================================
- Return the actual path as a list of (row, col) tuples (keep a `parent`
  dict and walk it backwards from the target).
- Support rectangular (non-square) grids.
- Allow only 4-directional movement via a parameter.
- Try A* search with a Chebyshev-distance heuristic using heapq. (A* is
  BFS that explores the most promising cells first. The heuristic is
  its guess of the remaining distance. Chebyshev distance,
  max(rows apart, cols apart), is the number of moves needed when
  diagonal moves are allowed and there are no walls.)
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
