"""
Challenge: Fast Power (Exponentiation by Squaring)
Level:     07 - Recursion
Topics:    recursion, divide and conquer, negative exponents, floats
Source:    LeetCode #50 "Pow(x, n)"

========================================================================
PROBLEM
========================================================================
Write `power(base, exp)` that returns `base` raised to the whole-number
power `exp` - the same thing as `base ** exp` - WITHOUT using `**`,
`pow()` or `math.pow()`.

The naive approach multiplies `base` by itself `exp` times, which is
slow for a big exponent (a billion multiplications for exp = 10**9) and
would also blow the recursion limit. Instead use DIVIDE AND CONQUER:

    DIVIDE AND CONQUER means: split a problem into smaller pieces,
    solve the pieces (often recursively), then combine the answers.

For powers, the key observation is:

    x^10 = (x^5)^2          -> compute x^5 ONCE, then square it
    x^5  = x * (x^2)^2      -> odd exponent: pull out one x first

In general:
    if exp is even:  x^exp = half * half           where half = x^(exp // 2)
    if exp is odd:   x^exp = half * half * x

Each step HALVES the exponent, so exp = 1_000_000 needs only about 20
recursive calls. This is called "exponentiation by squaring" or "fast
exponentiation".

Negative exponents: x^(-n) == 1 / x^n. For example 2^-2 = 1/4 = 0.25.

Zero exponent: anything to the power 0 is 1 (and by convention
0^0 == 1, same as Python's `0 ** 0`).

========================================================================
EXAMPLES
========================================================================
    >>> power(2, 10)
    1024

    >>> power(2.0, -2)
    0.25

    >>> power(5, 0)
    1

    >>> power(-3, 3)
    -27

(Results for int bases with non-negative exponents may be int or
float; compare with `==` or `pytest.approx`. For negative exponents the
result is a float.)

========================================================================
CONSTRAINTS
========================================================================
- `base` is a float or int. `exp` is an int (may be negative).
- -2**31 <= exp <= 2**31 - 1  (LeetCode's range, meant for float bases;
  with an INT base keep test exponents modest - power(2, 2**31 - 1) is
  an integer hundreds of megabytes long and would take ages)
- If `base == 0` and `exp < 0`, raise `ZeroDivisionError` (it would mean
  dividing by zero: 0^-1 = 1/0).
- If `exp` is not an int, raise `TypeError`.
- Must be recursive and must use the halving strategy (recursion depth
  about log2(|exp|)), not exp repeated multiplications.
- Do not use `**`, `pow()` or `math.pow()`.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(log |exp|) multiplications.
- Space: O(log |exp|) for the call stack.

========================================================================
EDGE CASES TO TEST
========================================================================
- exp = 0            -> 1 (also power(0, 0) == 1)
- exp = 1            -> base
- base = 0, exp > 0  -> 0
- base = 0, exp < 0  -> ZeroDivisionError
- Negative base with odd / even exponent: power(-2, 3) == -8,
  power(-2, 4) == 16
- Negative exponent: power(2, -3) == pytest.approx(0.125)
- Fractional base: power(0.5, 3) == pytest.approx(0.125)
- A huge exponent that would crash a naive recursive version:
  power(1.0000001, 10**7) == pytest.approx(1.0000001 ** 10**7)
- exp = 2.5 -> TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Deal with a negative exponent first: power(base, -n) is
   1 / power(base, n). Check for base == 0 before dividing.
2. Base case: exp == 0 -> return 1.
3. Compute `half = power(base, exp // 2)` ONCE and store it in a
   variable. Writing `power(base, exp // 2) * power(base, exp // 2)`
   calls the function twice and throws away all the speed-up.
4. Use `exp % 2 == 1` (or `exp % 2 != 0`) to test for odd.
5. Floats are not exact. In tests compare floats with
   `pytest.approx(expected)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Divide and conquer recursion
- Why storing an intermediate result in a variable matters
- int vs float arithmetic, `ZeroDivisionError`
- `pytest.approx` for comparing floating-point numbers
- `@pytest.mark.parametrize` to test many (base, exp) pairs at once

========================================================================
STRETCH GOALS
========================================================================
- Write a parametrized test comparing `power(b, e)` with `b ** e` for a
  grid of bases and exponents.
- Write an iterative version using the binary digits of `exp`.
- Add a `mod` parameter: power_mod(base, exp, mod) returns
  (base ** exp) % mod for ints, keeping numbers small at each step.
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
