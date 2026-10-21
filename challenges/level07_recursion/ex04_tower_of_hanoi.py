"""
Challenge: Tower of Hanoi
Level:     07 - Recursion
Topics:    recursion with multiple calls, lists of tuples, default arguments
Source:    Classic puzzle (Edouard Lucas, 1883)

========================================================================
YOUR TASK
========================================================================
Write `hanoi(n, source="A", target="C", spare="B")`. It RETURNS the list
of moves that solves the Tower of Hanoi puzzle for `n` discs. Each move
is a tuple `(from_peg, to_peg)`. Write it recursively (the function
calls itself).

    hanoi(2)  ->  [('A', 'B'), ('A', 'C'), ('B', 'C')]

========================================================================
THE PUZZLE
========================================================================
There are three pegs, named "A", "B" and "C". Peg "A" holds a stack of
`n` discs, largest at the bottom, smallest on top. The goal is to move
the whole stack to peg "C". The rules of the puzzle:

    1. Move only ONE disc at a time.
    2. A move takes the TOP disc from one peg and puts it on top of
       another peg.
    3. Never place a bigger disc on top of a smaller disc.

The move ("A", "C") means "take the top disc of A and put it on C".

THE STANDARD RECURSIVE ALGORITHM. Your output must follow it exactly,
so there is only one correct move list for each n:

    To move n discs from `source` to `target`, using `spare`:
        1. Move the top n-1 discs from `source` to `spare`
           (using `target` as the spare peg).
        2. Move the 1 remaining (largest) disc from `source` to
           `target`.
        3. Move the n-1 discs from `spare` to `target`
           (using `source` as the spare peg).
    Base case: n == 0 means no moves at all (an empty list).

Walk-through for n = 2 (small disc on top of big disc, both on A):

    step 1: move the small disc  A -> B    ('A', 'B')   (n-1 = 1 disc)
    step 2: move the big disc    A -> C    ('A', 'C')
    step 3: move the small disc  B -> C    ('B', 'C')   (n-1 = 1 disc)

This always makes exactly 2**n - 1 moves, which is the fewest possible.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a list of moves, following the standard algorithm above
   exactly.
2. Make each move a tuple of two peg-name strings (not a list, not a
   single string).
3. Use the peg names it is given: `source`, `target` and `spare`.
4. Return [] when `n` is 0.
5. Raise `TypeError` if `n` is not an int.
6. Raise `ValueError` if `n` is negative.
7. Raise `ValueError` if `source`, `target` and `spare` are not three
   DIFFERENT names.
8. Be recursive.

You can assume:
- 0 <= n <= 20 in normal use. 2**20 - 1 is about a million moves.
- Peg names are strings.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    hanoi(1)  ->  [('A', 'C')]
        One disc goes straight from A to C.

    hanoi(2)  ->  [('A', 'B'), ('A', 'C'), ('B', 'C')]
        See the walk-through above.

    hanoi(3)  ->  [('A', 'C'), ('A', 'B'), ('C', 'B'), ('A', 'C'),
                   ('B', 'A'), ('B', 'C'), ('A', 'C')]
        The first 3 moves shift 2 discs from A to B (with C as spare),
        then the big disc goes A -> C, then the last 3 moves shift the
        2 discs from B to C (with A as spare).

    hanoi(1, source="X", target="Y", spare="Z")  ->  [('X', 'Y')]
        Custom peg names appear in the output.

    hanoi(-1)                ->  raises ValueError
        A negative number of discs makes no sense.

    hanoi(2, "A", "A", "B")  ->  raises ValueError
        The peg names must all be different.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(2**n). You must output 2**n - 1 moves, and there is no
  faster way. Each extra disc DOUBLES the work.
- Space: O(n) for the call stack. At most n calls are waiting at once,
  one per disc. The output list itself is O(2**n).

========================================================================
EDGE CASES TO TEST
========================================================================
- n = 0 -> []
- n = 1 -> [("A", "C")]
- n = 2 and n = 3 -> exactly the lists in EXAMPLES
- len(hanoi(n)) == 2**n - 1 for several n (parametrize n over 0..10)
- Custom peg names: hanoi(1, source="X", target="Y", spare="Z")
  -> [("X", "Y")]
- VALIDITY: replay the moves on three lists and check that no bigger
  disc ever lands on a smaller one, and that all discs end on the
  target peg
- n = -1 -> raises ValueError
- n = 2.0 -> raises TypeError
- Duplicate peg names: hanoi(2, "A", "A", "B") -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Trust the recursion: assume hanoi(n - 1, ...) already works and
   returns the right moves. You only have to combine them.
2. The answer for n is:
   moves(n-1 discs: source -> spare) + [(source, target)]
   + moves(n-1 discs: spare -> target)
3. Pay close attention to which peg is the spare in each recursive
   call. Swapping them is the classic bug.
4. You can join lists with `+`, or pass one shared list down to a
   helper and `append` to it (faster for big n).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Recursion with TWO recursive calls (a "recursion tree")
- Default parameter values and keyword arguments
- Tuples as small fixed records, lists of tuples
- Simulating a process in a test to check correctness
- Why the move count grows exponentially (doubles with each disc:
  2**n - 1)

========================================================================
STRETCH GOALS
========================================================================
- Write a helper `simulate(n, moves)` that returns the final state of
  the three pegs, and use it in your tests.
- Return moves as `(disc_number, from_peg, to_peg)` triples.
- Write an iterative (loop-based) solution and test that it produces
  the same moves.
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
