"""
Challenge: Container With Most Water
Level:     12 - Algorithms
Topics:    two pointers, greedy reasoning
Source:    LeetCode #11 "Container With Most Water"

========================================================================
YOUR TASK
========================================================================
Write `max_area(height)`. Each number in `height` is a vertical wall,
and wall i stands at position x = i. Pick TWO walls to hold water
between them. RETURN the most water any pair of walls can hold.

    max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])  ->  49

========================================================================
HOW MUCH WATER A PAIR HOLDS
========================================================================
Two walls i and j (with i < j), together with the ground, make a
container. The water it holds is

    width  * (height of the SHORTER wall)
    (j - i) * min(height[i], height[j])

Water spills over the shorter wall, so the taller one doesn't help.

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

    walls 1 and 8: width 8 - 1 = 7, shorter height 7 -> 7 * 7 = 49

TWO POINTERS: instead of trying every pair (O(n^2), a loop inside a
loop), keep two indexes. Start with the widest container: left = 0,
right = n - 1. Each step, move ONE pointer inwards: always the one at
the SHORTER wall.

Why is that safe? Every other container that uses the shorter wall is
narrower, and its water level can never rise above that short wall. So
none of them can beat the one you just measured. The short wall is
"used up": drop it.

The first few steps on the example:

    left=0 (1), right=8 (7):  8 * 1 =  8   left is shorter: left += 1
    left=1 (8), right=8 (7):  7 * 7 = 49   right is shorter: right -= 1
    left=1 (8), right=7 (3):  6 * 3 = 18   right is shorter: right -= 1
    ... and so on until the pointers meet. The best seen is 49.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return the largest (j - i) * min(height[i], height[j]) over all
   pairs of walls i < j.
2. Return 0 when there are fewer than 2 walls (no container possible).
3. Not change (mutate) `height`.

You can assume:
- `height` is a list of 0 to 100_000 ints.
- Each height is from 0 to 10_000.
- With up to 100_000 walls, checking every pair is too slow for big
  inputs: aim for one pass with two pointers.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])  ->  49
        Walls 1 and 8, pictured above.

    max_area([1, 1])                       ->  1
        Width 1, height 1.

    max_area([4, 3, 2, 1, 4])              ->  16
        The two outer walls: width 4, height 4.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n). Each step moves one pointer inwards, so there are fewer
         than n steps.
- Space: O(1). Just a few variables, however long the list is.

========================================================================
EDGE CASES TO TEST
========================================================================
- [] -> 0, and [5] -> 0
- Two walls: [3, 7] -> 3 (width 1 * the shorter height 3)
- Walls of height 0 hold nothing: [0, 5] -> 0
- The best pair is the two outermost walls: [4, 3, 2, 1, 4] -> 16
- The best pair is two tall neighbours in the middle: [1, 9, 9, 1] -> 9
- All equal heights -> (n - 1) * h, for example [4, 4, 4, 4] -> 12

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Brute force: try every pair i < j (O(n^2)). Useful for checking your
   fast answer in tests.
2. left, right = 0, len(height) - 1, and best = 0.
3. While left < right: compute the area and update best.
4. Then move whichever pointer points at the shorter wall (if they are
   equal, moving either is fine).

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
- Trapping Rain Water (LeetCode #42), a harder cousin.
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
