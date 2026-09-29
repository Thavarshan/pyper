"""
Challenge: Tower of Hanoi
Level:     07 - Recursion
Topics:    recursion with multiple calls, lists of tuples, default arguments
Source:    Classic puzzle (Edouard Lucas, 1883)

========================================================================
PROBLEM
========================================================================
There are three pegs, named "A", "B" and "C". On peg "A" sits a stack of
`n` discs, largest at the bottom, smallest on top. The goal is to move
the whole stack to peg "C". The rules:

    1. Move only ONE disc at a time.
    2. A move takes the TOP disc from one peg and puts it on top of
       another peg.
    3. Never place a bigger disc on top of a smaller disc.

Write `hanoi(n, source="A", target="C", spare="B")` that returns the
list of moves needed. Each move is a tuple `(from_peg, to_peg)`, e.g.
("A", "C") means "move the top disc of A onto C".

THE STANDARD RECURSIVE ALGORITHM (your output must follow it exactly,
so the move list is fully deterministic):

    To move n discs from `source` to `target` using `spare`:
        1. Move the top n-1 discs from `source` to `spare`
           (using `target` as the spare).
        2. Move the 1 remaining (largest) disc from `source` to `target`.
        3. Move the n-1 discs from `spare` to `target`
           (using `source` as the spare).
    Base case: n == 0 -> no moves at all (empty list).

This always produces exactly 2**n - 1 moves, which is the minimum
possible.

========================================================================
EXAMPLES
========================================================================
    >>> hanoi(1)
    [('A', 'C')]

    >>> hanoi(2)
    [('A', 'B'), ('A', 'C'), ('B', 'C')]

    >>> hanoi(3)
    [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')]

    >>> hanoi(1, source="X", target="Y", spare="Z")
    [('X', 'Y')]

========================================================================
CONSTRAINTS
========================================================================
- `n` is an int, 0 <= n <= 20 (2**20 - 1 is about a million moves).
- If `n` is negative, raise `ValueError`.
- If `n` is not an int, raise `TypeError`.
- Peg names are strings; `source`, `target` and `spare` must be three
  DIFFERENT names, otherwise raise `ValueError`.
- Return a list of tuples of two strings (not lists, not strings).
- Must be recursive.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(2**n) - you must output 2**n - 1 moves, there is no faster
  way.
- Space: O(n) call stack depth (plus the O(2**n) output list).

========================================================================
EDGE CASES TO TEST
========================================================================
- n = 0 -> []
- n = 1 -> [("A", "C")]
- n = 2 and n = 3 -> exactly the sequences in EXAMPLES
- len(hanoi(n)) == 2**n - 1 for several n (parametrize n in 0..10)
- Custom peg names are used in the output
- VALIDITY: simulate the moves on three lists and check no bigger disc
  ever lands on a smaller one and all discs end on the target peg
- n = -1 -> ValueError; n = 2.0 -> TypeError
- Duplicate peg names, e.g. hanoi(2, "A", "A", "B") -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Trust the recursion: assume hanoi(n - 1, ...) already works and
   returns the right moves. You just have to combine them.
2. The answer for n is:
   moves(n-1 discs: source -> spare) + [(source, target)]
   + moves(n-1 discs: spare -> target)
3. Pay close attention to which peg is the spare in each recursive
   call - swapping them is the classic bug.
4. You can join lists with `+`, or pass one shared list down to a helper
   and `append` to it (more efficient for big n).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Recursion with TWO recursive calls (a "recursion tree")
- Default parameter values and keyword arguments
- Tuples as small fixed records, lists of tuples
- Simulating a process in a test to check correctness
- Why the move count grows exponentially (2**n - 1)

========================================================================
STRETCH GOALS
========================================================================
- Write a helper `simulate(n, moves)` that returns the final state of
  the three pegs, and use it in your tests.
- Return moves as `(disc_number, from_peg, to_peg)` triples.
- Write an iterative solution and test it produces the same moves.
"""


def hanoi(
    n: int, source: str = "A", target: str = "C", spare: str = "B"
) -> list[tuple[str, str]]:
    """Return the moves that solve Tower of Hanoi for `n` discs.

    Must be implemented recursively using the standard algorithm
    described in the module docstring (move n-1 to spare, move largest
    to target, move n-1 from spare to target).

    Args:
        n: Number of discs. Must be >= 0.
        source: Name of the peg the discs start on.
        target: Name of the peg the discs must end on.
        spare: Name of the helper peg.

    Returns:
        A list of 2**n - 1 moves, each a (from_peg, to_peg) tuple.

    Raises:
        TypeError: If `n` is not an int.
        ValueError: If `n` is negative or the peg names are not distinct.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
