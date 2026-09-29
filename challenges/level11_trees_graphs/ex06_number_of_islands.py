r"""
Challenge: Number of Islands
Level:     11 - Trees and Graphs
Topics:    grids as graphs, DFS/BFS flood fill, visited sets
Source:    LeetCode #200 "Number of Islands"

========================================================================
PROBLEM
========================================================================
You get a map as a 2D grid. Each cell is either land ("1") or water
("0"). An ISLAND is a group of land cells connected HORIZONTALLY or
VERTICALLY (up, down, left, right - NOT diagonally). Everything outside
the grid counts as water. Count the islands.

Input representation: `grid` is a `list[list[str]]` - a list of rows,
each row a list of one-character STRINGS "1" or "0" (not ints!).
grid[r][c] is the cell in row r, column c.

         c=0  1   2   3   4
    r=0 [ 1   1   0   0   0 ]
    r=1 [ 1   1   0   0   0 ]        island A = the 2x2 block top-left
    r=2 [ 0   0   1   0   0 ]        island B = the single cell (2, 2)
    r=3 [ 0   0   0   1   1 ]        island C = (3, 3) and (3, 4)
                                     -> 3 islands

    Note (2, 2) and (3, 3) touch only diagonally, so they are separate.

Think of the grid as a GRAPH: every land cell is a node, joined by an
edge to each land neighbour above/below/left/right. An island is a
"connected component". The count is: scan every cell; whenever you find
land you have not visited yet, that's a new island - increment the
counter and then FLOOD FILL (DFS or BFS) from it to mark every cell of
that island as visited, so you don't count it again.

IMPORTANT: your function must NOT mutate `grid`. (A common trick is to
overwrite visited land with "0", but that destroys the caller's data.
Use a `visited` set of (row, col) tuples, or work on a copy.)

========================================================================
EXAMPLES
========================================================================
    >>> num_islands([
    ...     ["1", "1", "0", "0", "0"],
    ...     ["1", "1", "0", "0", "0"],
    ...     ["0", "0", "1", "0", "0"],
    ...     ["0", "0", "0", "1", "1"],
    ... ])
    3

    >>> num_islands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]])
    1

    >>> num_islands([])
    0

========================================================================
CONSTRAINTS
========================================================================
- 0 <= number of rows <= 300; all rows have the same length (0..300).
- Every cell is exactly "1" or "0" (strings).
- An empty grid ([]) or a grid of empty rows ([[]]) -> 0.
- `grid` must be left unchanged after the call.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(rows * cols) - each cell is examined a constant number of times.
- Space: O(rows * cols) for the visited set / queue in the worst case.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty grid [] and [[]] -> 0
- All water -> 0
- All land -> 1
- Diagonal-only neighbours are separate islands: [["1","0"],["0","1"]] -> 2
- A snake-shaped / U-shaped island -> 1
- Single row and single column grids
- The grid is unchanged afterwards (compare against a deep copy)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Loop over every (r, c). Skip water and already-visited cells.
2. When you hit unvisited land: count += 1, then explore its whole island.
3. Exploring with BFS: a deque starting with (r, c); pop a cell, look at
   its 4 neighbours (r+1,c), (r-1,c), (r,c+1), (r,c-1).
4. For each neighbour check: inside the grid (0 <= nr < rows and
   0 <= nc < cols), is "1", and not in visited -> add to visited and queue.
5. Add a cell to `visited` when you PUSH it, not when you pop it, so it
   can't be queued twice.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Nested lists: `grid[r][c]`, `len(grid)`, `len(grid[0])`
- Sets of tuples: `visited.add((r, c))`
- A directions list: `for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):`
- `collections.deque` for BFS, or recursion for DFS
- `copy.deepcopy` (useful in your tests to check nothing was mutated)

========================================================================
STRETCH GOALS
========================================================================
- Return the area of the largest island (LeetCode #695).
- Write both a recursive DFS and an iterative BFS version.
- Solve it with a Union-Find (disjoint set) data structure.
"""


def num_islands(grid: list[list[str]]) -> int:
    """Count groups of "1" cells connected up/down/left/right.

    Args:
        grid: A rectangular grid of "1" (land) and "0" (water) strings.
            It is not modified.

    Returns:
        The number of islands (0 for an empty grid).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
