r"""
Challenge: Course Schedule (I and II)
Level:     11 - Trees and Graphs
Topics:    directed graphs, adjacency lists, cycle detection, topological sort
Source:    LeetCode #207 "Course Schedule" and #210 "Course Schedule II"

========================================================================
PROBLEM
========================================================================
There are `num_courses` courses, numbered 0 to num_courses - 1. Some
courses have prerequisites. You get them as `prerequisites`, a list of
PAIRS `[course, prereq]`, meaning "to take `course` you must first
finish `prereq`".

Write two functions:

1. `can_finish(num_courses, prerequisites) -> bool`
   Can you finish ALL the courses in some order? (LeetCode #207)

2. `find_order(num_courses, prerequisites) -> list[int]`
   Return an order in which you could take all the courses, or an empty
   list [] if it is impossible. (LeetCode #210)

Model this as a DIRECTED GRAPH: each course is a node and each pair
[course, prereq] is an arrow prereq -> course ("prereq comes before
course").

    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

            0
           / \
          v   v
          1   2          valid orders: [0, 1, 2, 3] or [0, 2, 1, 3]
           \ /
            v
            3

It is impossible exactly when the graph contains a CYCLE, e.g.
[[0, 1], [1, 0]]: 0 needs 1 and 1 needs 0 - neither can go first.

An order where every arrow points forward is called a TOPOLOGICAL ORDER.
KAHN'S ALGORITHM finds one with BFS:
    - The IN-DEGREE of a course = how many prerequisites it still needs.
    - Put every course with in-degree 0 into a queue (nothing blocks it).
    - Repeatedly take a course from the queue, add it to the order, and
      for each course that depends on it, decrement that course's
      in-degree; if it drops to 0, it's now unblocked - enqueue it.
    - If the order ends up containing all courses -> success. If some
      courses never reach in-degree 0, they are stuck in a cycle.

TESTING "ANY VALID ORDER": many correct answers can exist, so do NOT
assert `find_order(...) == [0, 1, 2, 3]` - a correct solution might
return [0, 2, 1, 3]. Instead, check the PROPERTIES of the result:
    - it has length num_courses and contains every course exactly once
      (sorted(order) == list(range(num_courses)))
    - for every [course, prereq] pair, prereq appears BEFORE course
      (position[prereq] < position[course], where position maps each
      course to its index in the order)
Write a small helper in your test file that does these checks. For
graphs with exactly one valid order (e.g. a chain) you may compare
directly.

========================================================================
EXAMPLES
========================================================================
    >>> can_finish(2, [[1, 0]])
    True
    >>> can_finish(2, [[1, 0], [0, 1]])
    False
    >>> find_order(2, [[1, 0]])
    [0, 1]
    >>> find_order(2, [[1, 0], [0, 1]])
    []
    >>> sorted(find_order(3, []))    # any permutation of 0, 1, 2 is valid
    [0, 1, 2]

========================================================================
CONSTRAINTS
========================================================================
- 0 <= num_courses <= 2_000.
- 0 <= len(prerequisites) <= 5_000.
- For valid input, every pair has two ints in range [0, num_courses);
  no duplicate pairs.
- A pair [a, a] (a course requiring itself) is a cycle -> impossible.
- num_courses = 0 -> can_finish is True and find_order returns [].
- Do not mutate `prerequisites`.
- If a course number is out of range, raise ValueError.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(V + E) - V courses, E prerequisite pairs.
- Space: O(V + E) for the adjacency list and in-degree counts.

========================================================================
EDGE CASES TO TEST
========================================================================
- No prerequisites -> True, and find_order returns a permutation of all courses
- A simple chain 0 -> 1 -> 2 -> 3 -> exactly one valid order
- Two-course cycle and a longer cycle 0 -> 1 -> 2 -> 0 -> False / []
- Self-loop [[0, 0]] -> False / []
- A cycle in one part while other courses are fine -> still False / []
- Diamond shape (example above) -> check with the property helper
- num_courses = 0
- Out-of-range course number -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Build an adjacency list: `graph = {c: [] for c in range(num_courses)}`
   and for each [course, prereq] do graph[prereq].append(course).
2. Build `indegree = [0] * num_courses`; each pair adds 1 to
   indegree[course].
3. Queue every course with indegree 0 (use collections.deque).
4. Pop, append to `order`, decrement neighbours' in-degrees, enqueue the
   ones that hit 0.
5. At the end: `len(order) == num_courses` means success. can_finish can
   simply return `bool(find_order(...))` - except when num_courses is 0!

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Adjacency lists with dict / `collections.defaultdict(list)`
- `[0] * n` to create a list of counters
- `collections.deque` for Kahn's BFS
- Unpacking pairs in a loop: `for course, prereq in prerequisites:`
- Testing properties instead of exact outputs

========================================================================
STRETCH GOALS
========================================================================
- Detect cycles with DFS and three colours (white = unvisited, grey = on
  the current path, black = done) instead of Kahn's algorithm.
- Return the courses involved in a cycle when it's impossible.
- Make find_order deterministic: always pick the smallest available course
  next (use heapq instead of a deque).
"""


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """Return True if all courses can be completed.

    Args:
        num_courses: Number of courses, labelled 0..num_courses - 1.
        prerequisites: Pairs [course, prereq] meaning prereq must be taken
            before course. Not modified.

    Returns:
        True if there is an order that satisfies every prerequisite
        (i.e. the prerequisite graph has no cycle), otherwise False.

    Raises:
        ValueError: If any course number is outside 0..num_courses - 1.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """Return one valid order to take all courses, or [] if impossible.

    Args:
        num_courses: Number of courses, labelled 0..num_courses - 1.
        prerequisites: Pairs [course, prereq] meaning prereq must be taken
            before course. Not modified.

    Returns:
        A list containing every course exactly once, where each prereq
        appears before the courses that need it. Any valid order is
        accepted. Returns [] if no valid order exists (or num_courses is 0).

    Raises:
        ValueError: If any course number is outside 0..num_courses - 1.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
