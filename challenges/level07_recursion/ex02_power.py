"""
Challenge: Fast Power (Exponentiation by Squaring)
Level:     07 - Recursion
Topics:    recursion, divide and conquer, negative exponents, floats
Source:    LeetCode #50 "Pow(x, n)"

========================================================================
YOUR TASK
========================================================================
Write `power(base, exp)`. It returns `base` raised to the whole-number
power `exp`, the same as `base ** exp`, but WITHOUT using `**`, `pow()`
or `math.pow()`. Write it recursively, using the fast "halving" trick
explained below.

    power(2, 10)  ->  1024

========================================================================
WHAT "FAST POWER" MEANS
========================================================================
The obvious approach multiplies `base` by itself `exp` times. For
exp = 10**9 that is a billion multiplications. Done recursively, it
also needs a billion calls waiting on the stack, far past Python's
limit of about 1000.

Instead, use DIVIDE AND CONQUER: split a problem into smaller pieces,
solve the pieces (often recursively), then combine the answers.

For powers, the key observation is:

    x^10 = (x^5)^2        ->  work out x^5 ONCE, then square it
    x^5  = x * (x^2)^2    ->  odd exponent: pull out one extra x

In general, with half = x^(exp // 2):

    if exp is even:  x^exp = half * half
    if exp is odd:   x^exp = half * half * x

Each step HALVES the exponent, so exp = 1_000_000 needs only about 20
recursive calls. This is called "exponentiation by squaring" or "fast
exponentiation".

Two more facts you need:

- Negative exponents: x^(-n) is 1 / x^n. For example
  2^-2 = 1 / 2^2 = 1/4 = 0.25.
- Zero exponent: anything to the power 0 is 1. By convention 0^0 is
  also 1, the same as Python's `0 ** 0`.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return `base` raised to the power `exp`.
2. Return 1 when `exp` is 0, for every base, including 0.
3. Handle a negative `exp` by returning 1 / base^|exp|. The result is
   then a float.
4. Raise `ZeroDivisionError` when `base` is 0 and `exp` is negative
   (0^-1 would mean 1/0).
5. Raise `TypeError` when `exp` is not an int.
6. Be recursive and use the halving trick, so the recursion depth is
   about log2(|exp|) (the number of times you can halve |exp| before
   reaching 0). Do not do `exp` separate multiplications.
7. Not use `**`, `pow()` or `math.pow()`.

For an int base and an exp of 0 or more, the result may be an int or a
float. Compare results with `==` or `pytest.approx`.

You can assume:
- `base` is an int or a float.
- -2**31 <= exp <= 2**31 - 1. This is LeetCode's range, meant for
  float bases. With an INT base keep your test exponents modest:
  power(2, 2**31 - 1) is an integer hundreds of megabytes long and
  would take ages.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    power(2, 10)     ->  1024
        2 multiplied by itself 10 times.

    power(2.0, -2)   ->  0.25
        Negative exponent: 1 / 2^2 = 1/4.

    power(5, 0)      ->  1
        Anything to the power 0 is 1.

    power(-3, 3)     ->  -27
        (-3) * (-3) * (-3). An odd number of negatives stays negative.

    power(0, -1)     ->  raises ZeroDivisionError
        It would mean 1 / 0.

========================================================================
COMPLEXITY TARGET
========================================================================
"log |exp|" is roughly how many times you can halve |exp| before you
reach 0. For exp = 1_000_000 that is about 20.

- Time:  O(log |exp|) multiplications. Each call halves the exponent
  and does one or two multiplications.
- Space: O(log |exp|) for the call stack. At the deepest point about
  log2(|exp|) calls are waiting on the stack.

========================================================================
EDGE CASES TO TEST
========================================================================
- exp = 0: power(5, 0) -> 1, and power(0, 0) -> 1
- exp = 1: power(7, 1) -> 7 (the base itself)
- base = 0, exp > 0: power(0, 5) -> 0
- base = 0, exp < 0: power(0, -1) -> raises ZeroDivisionError
- Negative base, odd and even exponent: power(-2, 3) -> -8,
  power(-2, 4) -> 16
- Negative exponent: power(2, -3) == pytest.approx(0.125)
- Fractional base: power(0.5, 3) == pytest.approx(0.125)
- A huge exponent that would crash a one-multiplication-per-call
  version: power(1.0000001, 10**7) == pytest.approx(1.0000001 ** 10**7)
- A non-int exponent: power(2, 2.5) -> raises TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Deal with a negative exponent first: power(base, -n) is
   1 / power(base, n). In Python, dividing by 0 already raises
   ZeroDivisionError, but checking for base == 0 yourself makes the
   intent clear.
2. Base case: exp == 0 -> return 1.
3. Work out `half = power(base, exp // 2)` ONCE and store it in a
   variable. Writing `power(base, exp // 2) * power(base, exp // 2)`
   calls the function twice and throws away all the speed-up.
4. Use `exp % 2 == 1` (or `exp % 2 != 0`) to test for odd.
5. Floats are not exact. In tests, compare floats with
   `pytest.approx(expected)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Divide and conquer recursion
- Why storing an in-between result in a variable matters
- int vs float arithmetic, `ZeroDivisionError`
- `pytest.approx` for comparing floating-point numbers
- `@pytest.mark.parametrize` to test many (base, exp) pairs at once

========================================================================
STRETCH GOALS
========================================================================
- Write a parametrized test (one test run once per input pair) that
  compares `power(b, e)` with `b ** e` for a grid of bases and
  exponents.
- Write an iterative (loop-based) version using the binary digits of
  `exp`.
- Add a `mod` parameter: power_mod(base, exp, mod) returns
  (base ** exp) % mod for ints, keeping the numbers small at each step.
"""


def power(base: float, exp: int) -> float:
    """Return `base` raised to the integer power `exp`, recursively.

    Uses fast exponentiation (divide and conquer): O(log |exp|) steps.

    Args:
        base: The number to raise. Int or float.
        exp: The integer exponent. May be negative or zero.

    Returns:
        base ** exp. power(x, 0) == 1 for every x (including 0).

    Raises:
        ZeroDivisionError: If `base` is 0 and `exp` is negative.
        TypeError: If `exp` is not an int.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
