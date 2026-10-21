"""
Challenge: FizzBuzz
Level:     01 - Basics
Topics:    loops, conditionals, the modulo operator (%), building lists
Source:    Classic interview warm-up (also LeetCode #412 "Fizz Buzz")

========================================================================
YOUR TASK
========================================================================
Write `fizzbuzz(n)`. It returns a list of strings, one for each number
from 1 up to and including `n`. Multiples of 3 become "Fizz", multiples
of 5 become "Buzz", multiples of both become "FizzBuzz", and every
other number becomes itself as a string.

    fizzbuzz(5)  ->  ['1', '2', 'Fizz', '4', 'Buzz']

========================================================================
WHAT "DIVISIBLE BY" MEANS
========================================================================
A number is divisible by 3 when dividing it by 3 leaves no remainder.
Python's remainder operator is `%`:

    9 % 3    is 0, so 9 is divisible by 3
    10 % 3   is 1, so 10 is not

So `9 % 3 == 0` is True and `10 % 3 == 0` is False.

========================================================================
THE RULES
========================================================================
Your function must:
1. Return a list with one string for each number from 1 to `n`
   (including `n`), in order. So the list has exactly `n` items.
2. Use "FizzBuzz" for a number divisible by 3 AND by 5.
3. Use "Fizz" for a number divisible by 3 only.
4. Use "Buzz" for a number divisible by 5 only.
5. Use the number itself as a string for any other number: 7 becomes
   "7". Every item is a str, never an int.
6. Return an empty list [] when `n` is 0.
7. Raise ValueError when `n` is negative (it makes no sense to count up
   to a negative number).

You can assume:
- `n` is an int.
- For normal input, `n` is between 0 and 10_000.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    fizzbuzz(5)       ->  ['1', '2', 'Fizz', '4', 'Buzz']
        3 is divisible by 3 and 5 is divisible by 5. The rest stay as
        numbers, written as strings.

    fizzbuzz(15)[-1]  ->  'FizzBuzz'
        [-1] picks the last item. 15 is divisible by both 3 and 5.

    fizzbuzz(1)       ->  ['1']
        Just the number 1, as a string.

    fizzbuzz(-1)      ->  raises ValueError
        You cannot count up to a negative number.

========================================================================
EDGE CASES TO TEST
========================================================================
- fizzbuzz(0)       -> []
- fizzbuzz(1)       -> ['1']
- fizzbuzz(3)[-1]   -> 'Fizz'
- fizzbuzz(5)[-1]   -> 'Buzz'
- fizzbuzz(15)[-1]  -> 'FizzBuzz'
- The length always equals n: len(fizzbuzz(100)) -> 100
- Every item is a str, not an int: fizzbuzz(2) -> ['1', '2']
  (not [1, 2])
- fizzbuzz(-1)      -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `range(1, n + 1)` gives you 1, 2, ..., n. `range` stops BEFORE its
   second argument, which is why you need `n + 1`.
2. Order matters: check "divisible by both" FIRST. If you check "by 3"
   first, 15 will return "Fizz" and never reach the "FizzBuzz" branch.
3. "Divisible by 3 and 5" is the same as "divisible by 15".
4. `str(7)` turns the int 7 into the string "7".

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `for x in range(...)` loops
- `if / elif / else` chains and why their order matters
- The `%` (modulo, the remainder) operator
- Creating a list with `[]` and adding to it with `.append()`
- Raising exceptions: `raise ValueError("message")`
- Type hints: `list[str]` means "a list whose items are strings"

========================================================================
STRETCH GOALS
========================================================================
- Rewrite your solution as a single list comprehension (a one-line way
  to build a list: [... for i in range(...)]).
- Generalise it: `fizzbuzz_custom(n, rules)` where `rules` is a dict like
  {3: "Fizz", 5: "Buzz", 7: "Bazz"}, so 105 -> "FizzBuzzBazz".
"""


def fizzbuzz(n: int) -> list[str]:
    """Return the FizzBuzz sequence for the numbers 1..n.

    Args:
        n: How many numbers to generate. Must be >= 0.

    Returns:
        A list of length `n` where each item is "Fizz", "Buzz",
        "FizzBuzz", or the number itself as a string.

    Raises:
        ValueError: If `n` is negative.
    """
    if n < 0:
        raise ValueError(f"{n} cannot be a negative integer")

    return [determine_word(num) for num in range(1, n+1)]


def determine_word(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def fizzbuzz_custom(num: int, rules: dict[int, str]) -> list[str]:
    if num < 0:
        raise ValueError(f"{num} cannot be a negative integer")

    results: list[str] = []

    for num in range(1, num + 1):
        final_word = ""
        for divisor, word in rules.items():
            if num % divisor == 0:
                final_word += word

        if final_word != "":
            results.append(final_word)
        else:
            results.append(str(num))

    return results
