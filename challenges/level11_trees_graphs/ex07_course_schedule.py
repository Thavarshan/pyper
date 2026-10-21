r"""
Challenge: Course Schedule (I and II)
Level:     11 - Trees and Graphs
Topics:    directed graphs, adjacency lists, cycle detection, topological sort
Source:    LeetCode #207 "Course Schedule" and #210 "Course Schedule II"

========================================================================
YOUR TASK
========================================================================
There are `num_courses` courses, numbered 0 to num_courses - 1. Each
pair `[course, prereq]` in `prerequisites` means "you must finish
`prereq` before you can take `course`". Write two functions:

- `can_finish(num_courses, prerequisites)`: RETURNS True if you can
  finish ALL the courses in some order, False if not. (LeetCode #207)
- `find_order(num_courses, prerequisites)`: RETURNS one order in which
  you could take all the courses, or [] if it is impossible.
  (LeetCode #210)

    can_finish(2, [[1, 0]])  ->  True      (take 0, then 1)
    find_order(2, [[1, 0]])  ->  [0, 1]

========================================================================
COURSES AS A GRAPH
========================================================================
Draw each course as a dot (a NODE). Draw each pair [course, prereq] as
an arrow prereq -> course, meaning "prereq comes before course". A
graph whose edges are one-way arrows like this is a DIRECTED graph.

    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

            0
           / \
          v   v
          1   2          valid orders: [0, 1, 2, 3] or [0, 2, 1, 3]
           \ /
            v
            3

An order where every arrow points forward is called a TOPOLOGICAL
ORDER. It is impossible exactly when the arrows form a CYCLE (a loop
that leads back to where it started). For example [[0, 1], [1, 0]]:
0 needs 1 and 1 needs 0, so neither can go first.

KAHN'S ALGORITHM finds a topological order using breadth-first search
(BFS: process things in the order they become ready, using a queue).
    - The IN-DEGREE of a course is how many prerequisites it still
      needs (how many arrows point INTO it).
    - Put every course with in-degree 0 into a queue. Nothing blocks
      them.
    - Repeatedly take a course from the front of the queue and add it
      to the order. For each course that depends on it, subtract 1 from
      that course's in-degree. If it drops to 0, it is now unblocked:
      add it to the queue.
    - If the order ends up containing every course, you succeeded. If
      some courses never reach in-degree 0, they are stuck in a cycle.

Walk-through for the 4-course example above:

    in-degrees: course 0 -> 0, 1 -> 1, 2 -> 1, 3 -> 2
    start: queue [0]
    take 0: order [0]           1 and 2 drop to 0   queue [1, 2]
    take 1: order [0, 1]        3 drops to 1        queue [2]
    take 2: order [0, 1, 2]     3 drops to 0        queue [3]
    take 3: order [0, 1, 2, 3]  nothing depends on 3, queue []
    4 courses in the order, so it worked.

And for the cycle [[0, 1], [1, 0]]: both courses start with in-degree
1, so the queue starts empty. The order stays [], which is shorter than
2 courses, so it is impossible.

========================================================================
THE RULES
========================================================================
Your functions must:
1. can_finish: return True if some order satisfies every prerequisite,
   otherwise False.
2. find_order: return a list that contains every course exactly once,
   where each prereq comes before the courses that need it. ANY valid
   order is accepted.
3. find_order: return [] if no valid order exists.
4. Treat a pair [a, a] (a course that requires itself) as a cycle, so
   it is impossible.
5. When num_courses is 0: can_finish returns True and find_order
   returns [].
6. Raise ValueError (in both functions) if any course number in
   `prerequisites` is outside 0 to num_courses - 1.
7. Not change (mutate) `prerequisites`.

You can assume:
- num_courses is an int from 0 to 2_000.
- `prerequisites` has 0 to 5_000 pairs. Each pair is a list of two
  ints, and no pair appears twice.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    can_finish(2, [[1, 0]])            ->  True
        Take 0, then 1.

    can_finish(2, [[1, 0], [0, 1]])    ->  False
        0 needs 1 and 1 needs 0: a cycle.

    find_order(2, [[1, 0]])            ->  [0, 1]
        The only valid order: 0 must come before 1.

    find_order(2, [[1, 0], [0, 1]])    ->  []
        Impossible, because of the cycle.

    sorted(find_order(3, []))          ->  [0, 1, 2]
        No prerequisites, so any arrangement of 0, 1, 2 is valid.
        Sorting the result lets the test compare one exact list.

TESTING "ANY VALID ORDER": many correct answers can exist, so do NOT
assert `find_order(...) == [0, 1, 2, 3]` for the diamond above. A
correct solution might return [0, 2, 1, 3]. Instead, check the
PROPERTIES of the result:
    - It contains every course exactly once:
      sorted(order) == list(range(num_courses))
    - For every [course, prereq] pair, prereq comes BEFORE course:
      position[prereq] < position[course], where `position` is a dict
      mapping each course to its index in the order.
Write a small helper in your test file that does these checks. For
graphs with exactly one valid order (such as a chain) you may compare
directly.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(V + E), where V is the number of courses and E the number of
         prerequisite pairs. Each course and each pair is handled a
         fixed number of times.
- Space: O(V + E) for the adjacency list (see hint 1) and the in-degree
         counts.

========================================================================
EDGE CASES TO TEST
========================================================================
- No prerequisites: can_finish(3, []) -> True, and find_order(3, [])
  returns some arrangement of [0, 1, 2]
- A simple chain [[1, 0], [2, 1], [3, 2]] -> find_order(4, ...) is
  exactly [0, 1, 2, 3] (the only valid order)
- Two-course cycle [[1, 0], [0, 1]] -> False / []
- Longer cycle 0 -> 1 -> 2 -> 0, [[1, 0], [2, 1], [0, 2]] with 3 courses
  -> False / []
- Self-loop: can_finish(1, [[0, 0]]) -> False, find_order(1, [[0, 0]])
  -> []
- A cycle in one part while other courses are fine:
  4 courses, [[1, 0], [3, 2], [2, 3]] -> still False / []
- Diamond shape (pictured above) -> check with the property helper
- num_courses = 0: can_finish(0, []) -> True, find_order(0, []) -> []
- Out-of-range course number: can_finish(2, [[2, 0]]) -> raises
  ValueError, and the same for find_order (and for -1)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Build an ADJACENCY LIST (a dict mapping each course to the courses
   that depend on it): `graph = {c: [] for c in range(num_courses)}`,
   and for each [course, prereq] do graph[prereq].append(course).
2. Build `indegree = [0] * num_courses`. Each pair adds 1 to
   indegree[course].
3. Queue every course with indegree 0 (use collections.deque).
4. Pop, append to `order`, decrement neighbours' in-degrees, enqueue the
   ones that hit 0.
5. At the end, `len(order) == num_courses` means success. can_finish can
   simply return `bool(find_order(...))`, except when num_courses is 0!
   (find_order returns [] then, and bool([]) is False.)

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
- Detect cycles with depth-first search (DFS) and three colours
  instead of Kahn's algorithm: white = not visited yet, grey = on the
  path you are exploring right now, black = finished. Reaching a grey
  node again means you found a cycle.
- Return the courses involved in a cycle when it's impossible.
- Make find_order deterministic (always the same answer for the same
  input): always pick the smallest available course next (use heapq
  instead of a deque).
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
