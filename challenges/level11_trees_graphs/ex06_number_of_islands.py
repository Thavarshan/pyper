r"""
Challenge: Number of Islands
Level:     11 - Trees and Graphs
Topics:    grids as graphs, DFS/BFS flood fill, visited sets
Source:    LeetCode #200 "Number of Islands"

========================================================================
YOUR TASK
========================================================================
Write `num_islands(grid)`. The grid is a map where "1" is land and "0"
is water. RETURN how many islands there are. An island is a group of
land cells joined up, down, left or right (NOT diagonally).

    num_islands([["1", "1", "0"], ["0", "0", "1"]])  ->  2

========================================================================
WHAT THE GRID LOOKS LIKE, AND HOW TO COUNT
========================================================================
`grid` is a list of rows. Each row is a list of one-character STRINGS,
"1" or "0" (not the ints 1 and 0!). grid[r][c] is the cell in row r,
column c. Everything outside the grid counts as water.

         c=0  1   2   3   4
    r=0 [ 1   1   0   0   0 ]
    r=1 [ 1   1   0   0   0 ]        island A = the 2x2 block top-left
    r=2 [ 0   0   1   0   0 ]        island B = the single cell (2, 2)
    r=3 [ 0   0   0   1   1 ]        island C = (3, 3) and (3, 4)
                                     -> 3 islands

    (2, 2) and (3, 3) touch only diagonally, so they are separate.

Think of the grid as a GRAPH (dots joined by lines): every land cell is
a dot, joined to each land neighbour above, below, left and right. An
island is then one "connected component": a group of dots that are all
reachable from each other.

To count them, scan every cell in order. Whenever you find land you
have not VISITED yet, that's a new island: add 1 to the count. Then
FLOOD FILL from it: spread out through its land neighbours, and their
neighbours, and so on, marking every cell of that island as visited.
That way you never count the same island twice. For the grid above:

    (0, 0): new land  -> count = 1, mark (0,0) (0,1) (1,0) (1,1)
    (0, 1), (1, 0), (1, 1): already visited, skip
    (2, 2): new land  -> count = 2, mark (2,2)
    (3, 3): new land  -> count = 3, mark (3,3) (3,4)
    (3, 4): already visited, skip
    every other cell is water        -> answer 3

You can flood fill with depth-first search (DFS: recursion or a stack,
going deep first) or breadth-first search (BFS: a queue, spreading out
in rings). Both work here.

A common trick is to overwrite visited land with "0". Do NOT do that
here: it destroys the caller's grid. Use a `visited` set of (row, col)
tuples instead, or work on a copy.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the number of islands, as an int. Cells connect up, down,
   left and right only, never diagonally.
2. Return 0 for an empty grid ([]) or a grid of empty rows ([[]]).
3. Not change (mutate) `grid`. After the call it must look exactly as
   it did before.

You can assume:
- `grid` has 0 to 300 rows. All rows have the same length (0 to 300).
- Every cell is exactly "1" or "0" (strings).

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    num_islands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ])  ->  3
        The grid pictured above.

    num_islands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]])  ->  1
        The middle column joins the top row to the bottom row.

    num_islands([])  ->  0
        No cells, so no islands.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(rows * cols). Each cell is looked at only a few times.
- Space: O(rows * cols) in the worst case, for the visited set and the
         queue (or stack). That is when the whole grid is land.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty grids: [] -> 0, and [[]] -> 0
- All water: [["0", "0"], ["0", "0"]] -> 0
- All land: [["1", "1"], ["1", "1"]] -> 1
- Diagonal-only neighbours are separate islands:
  [["1", "0"], ["0", "1"]] -> 2
- A U-shaped island:
  [["1", "0", "1"], ["1", "0", "1"], ["1", "1", "1"]] -> 1
- A single row: [["1", "0", "1", "0", "1"]] -> 3
- A single column: [["1"], ["1"], ["0"], ["1"]] -> 2
- The grid is unchanged afterwards (compare it with a copy made by
  copy.deepcopy before the call)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Loop over every (r, c). Skip water and already-visited cells.
2. When you hit unvisited land: count += 1, then explore its whole island.
3. Exploring with BFS: a deque starting with (r, c). Pop a cell and look
   at its 4 neighbours (r+1, c), (r-1, c), (r, c+1), (r, c-1).
4. For each neighbour check that it is inside the grid
   (0 <= nr < rows and 0 <= nc < cols), is "1", and is not in visited.
   If so, add it to visited and to the queue.
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
- Return the area (number of cells) of the largest island
  (LeetCode #695).
- Write both a recursive DFS and an iterative BFS version.
- Solve it with a Union-Find (disjoint set) data structure: a structure
  that keeps track of which group each cell belongs to and can merge
  two groups quickly.
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
