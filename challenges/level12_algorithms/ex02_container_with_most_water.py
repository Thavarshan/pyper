"""
Challenge: Container With Most Water
Level:     12 - Algorithms
Topics:    two pointers, greedy reasoning
Source:    LeetCode #11 "Container With Most Water"

========================================================================
PROBLEM
========================================================================
You get a list `height` of non-negative ints. Imagine each value as a
vertical wall standing at x = i with that height. Pick TWO walls; together
with the ground they form a container. The water it holds is

    width  * (height of the SHORTER wall)
    (j - i) * min(height[i], height[j])

(Water spills over the shorter wall, so the taller one doesn't help.)
Return the maximum amount of water any pair of walls can hold.

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    8 |    #              #
    7 |    #~~~~~~~~~~~~~~#~~~~~#      <- water level = 7
    6 |    #  #           #     #
    5 |    #  #     #     #     #
    4 |    #  #     #  #  #     #
    3 |    #  #     #  #  #  #  #
    2 |    #  #  #  #  #  #  #  #
    1 | #  #  #  #  #  #  #  #  #
      +----------------------------
        0  1  2  3  4  5  6  7  8

    walls 1 and 8: width 7, shorter height 7 -> 49 (the answer)

TWO POINTERS: start with the widest container, left = 0, right = n - 1.
Then move ONE pointer inwards each step - always the one at the SHORTER
wall. Why is that safe? Moving the taller wall inwards can only make the
width smaller while the height stays limited by the same short wall, so
it can never do better. The short wall is "used up"; drop it.

========================================================================
EXAMPLES
========================================================================
    >>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    49

    >>> max_area([1, 1])
    1

    >>> max_area([4, 3, 2, 1, 4])
    16

========================================================================
CONSTRAINTS
========================================================================
- 0 <= len(height) <= 100_000.
- 0 <= height[i] <= 10_000 (ints).
- Fewer than 2 walls -> 0 (no container possible).
- Do not mutate `height`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n) - each step moves one pointer.
- Space: O(1).

========================================================================
EDGE CASES TO TEST
========================================================================
- [] and [5] -> 0
- Two walls -> width 1 * min height
- Walls of height 0 -> 0 contribution
- The best pair is the two outermost walls ([4, 3, 2, 1, 4] -> 16)
- The best pair is adjacent tall walls in the middle ([1, 9, 9, 1] -> 9)
- All equal heights -> (n - 1) * h

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Brute force: try every pair i < j (O(n^2)). Useful for checking your
   fast answer in tests.
2. left, right = 0, len(height) - 1; best = 0.
3. While left < right: compute the area and update best.
4. Then move whichever pointer points at the shorter wall (if equal,
   moving either is fine).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The two-pointer while loop: `while left < right:`
- Tuple unpacking for initialisation: `left, right = 0, len(h) - 1`
- Proving (informally) that a greedy move can't skip the best answer

========================================================================
STRETCH GOALS
========================================================================
- Also return the pair of indexes (i, j).
- Trapping Rain Water (LeetCode #42) - a harder cousin.
"""


def max_area(height: list[int]) -> int:
    """Return the most water any two walls can contain.

    Args:
        height: Wall heights; wall i stands at x = i. Not modified.

    Returns:
        The maximum of (j - i) * min(height[i], height[j]) over all i < j,
        or 0 if there are fewer than 2 walls.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
