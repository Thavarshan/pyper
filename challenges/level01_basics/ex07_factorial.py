"""
Challenge: Factorial
Level:     01 - Basics
Topics:    loops, accumulators, isinstance(), TypeError vs ValueError
Source:    Classic beginner exercise

========================================================================
YOUR TASK
========================================================================
Write `factorial(n)`. It returns n! (say "n factorial"): all the whole
numbers from 1 up to `n` multiplied together. Use a loop, and reject
inputs that are the wrong type or a negative number.

    factorial(5)  ->  120

========================================================================
WHAT "FACTORIAL" MEANS
========================================================================
    5! = 5 * 4 * 3 * 2 * 1 = 120
    1! = 1
    0! = 1      (by definition: multiplying no numbers at all gives 1,
                 the "empty product")

There are two different kinds of "wrong" input:

    - Wrong TYPE  (5.0, "5", None, True)  ->  raise TypeError
    - Wrong VALUE (a negative int like -3) ->  raise ValueError

About bools: in Python, `bool` is a subclass of `int` (a special kind
of int), so `isinstance(True, int)` is True and `True + True == 2`.
Passing a bool to factorial is almost certainly a bug, so this
challenge DECIDES to reject bools with TypeError.

========================================================================
THE RULES
========================================================================
Your function must:
1. Compute n! with a LOOP (an "iterative" solution). Do not use
   `math.factorial`, and do not use recursion (a function calling
   itself). Recursion comes in a later level.
2. Return an int. Python ints grow without limit, so factorial(100)
   works.
3. Return 1 for both 0 and 1.
4. Raise TypeError if `n` is not an int. That includes 5.0: it is a
   float, so it raises TypeError even though it is "whole".
5. Raise TypeError if `n` is a bool (True or False).
6. Raise ValueError if `n` is a negative int.
7. Check the type BEFORE the value, so factorial("x") raises your own
   clear TypeError, not a confusing error from comparing "x" with 0.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    factorial(5)     ->  120
        5 * 4 * 3 * 2 * 1.

    factorial(0)     ->  1
        0! is 1 by definition.

    factorial(10)    ->  3628800
        10 * 9 * 8 * ... * 1. Factorials grow very fast.

    factorial(-3)    ->  raises ValueError
        Right type, wrong value.

    factorial(5.0)   ->  raises TypeError
        A float, not an int.

    factorial(True)  ->  raises TypeError
        Bools are rejected, even though Python treats them as ints.

========================================================================
EDGE CASES TO TEST
========================================================================
- factorial(0) -> 1 and factorial(1) -> 1
- A small value: factorial(5) -> 120
- A larger value: factorial(20) -> 2432902008176640000
- Matches math.factorial(n) for every n in range(30). (math.factorial
  is fine to use in TESTS, just not in your solution.)
- A negative number: factorial(-1) -> raises ValueError
- factorial(5.0), factorial("5") and factorial(None)
  -> raise TypeError
- factorial(True) and factorial(False) -> raise TypeError
  (our decision about bools)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with `result = 1` (not 0: multiplying by 0 ruins everything).
2. Loop `for i in range(2, n + 1):` and do `result *= i`.
3. `isinstance(n, int)` checks the type. Because bool is a subclass of
   int, you ALSO need `isinstance(n, bool)` to reject bools.
4. Order your checks: bool/type first, then negative, then compute.
5. Notice that 0 and 1 need no special case if your loop starts at 2.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- The accumulator pattern with multiplication (`*=`)
- `isinstance()` and class inheritance (bool is an int!)
- TypeError vs ValueError: which one describes the problem?
- Python's arbitrary-precision integers (ints with no size limit)
- Using `pytest.raises` to check exceptions

========================================================================
STRETCH GOALS
========================================================================
- Rewrite it with a `while` loop.
- Write it using `functools.reduce` and `operator.mul`. (`reduce`
  combines a list into one value by applying a two-argument function
  over and over: here, multiplying.)
- Write `count_trailing_zeros(n)`: how many zeros are at the end of n!?
  (Hint: count factors of 5, without computing n!.)
"""


def factorial(n: int) -> int:
    """Return n! computed iteratively.

    Args:
        n: A non-negative integer (bools are not accepted).

    Returns:
        The product 1 * 2 * ... * n, with factorial(0) == 1.

    Raises:
        TypeError: If `n` is not an int, or is a bool.
        ValueError: If `n` is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
