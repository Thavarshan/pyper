"""
Challenge: Flexible Sum
Level:     05 - Functions, Deeper
Topics:    *args, **kwargs, isinstance, repr, string formatting
Source:    Classic *args/**kwargs exercise

========================================================================
YOUR TASK
========================================================================
Write two functions that accept ANY number of arguments:

- `flexible_sum(*args, **kwargs)` adds up all the numbers it is given,
  whether they are passed by position or by name.
- `describe_call(*args, **kwargs)` returns a string that shows exactly
  what it was called with.

    flexible_sum(1, 2.5, bonus=10)    ->  13.5
    describe_call(1, "a", flag=True)
        ->  "args=(1, 'a'); kwargs={flag=True}"

========================================================================
BACKGROUND: *ARGS, **KWARGS AND REPR
========================================================================
Normally a function has a fixed list of parameters. Two special
parameters let a function accept ANY number of arguments:

    def f(*args, **kwargs):
        print(args, kwargs)

- `*args` collects all the extra POSITIONAL arguments (the ones passed
  without a name) into a TUPLE.
- `**kwargs` collects all the extra KEYWORD arguments (the ones
  written name=value) into a DICT that maps each name to its value.

    f(1, 2, x=3)    prints   (1, 2) {'x': 3}
    f()             prints   () {}

The names `args` and `kwargs` are only a convention. The `*` and `**`
are what matter.

`repr(value)` gives the "developer" text form of a value: the way
Python shows it at the interactive prompt. For strings, that includes
the quotes:

    repr("hi")    is   "'hi'"     (compare str("hi"), which is "hi")
    repr(3)       is   "3"
    repr(None)    is   "None"

========================================================================
THE RULES
========================================================================
For `flexible_sum`, your function must:
1. Return the sum of ALL positional values and ALL keyword values.
2. Accept only numbers: values of type `int` or `float`.
3. Reject `bool` values, even though Python counts `True` as an int
   (`isinstance(True, int)` is True!).
4. Raise `TypeError` if any value is not allowed. The message must
   include the bad value's repr, for example "not a number: 'hello'".
   (Hint 5 tests for the words "not a number".)
5. Return 0 when called with no arguments at all.
6. Return an int if every value was an int, and a float if any value
   was a float. (Plain `+` does this for you.)

For `describe_call`, your function must:
7. Return a string in exactly this format, character for character:

       args=<A>; kwargs=<K>

8. Build <A> from the reprs of the positional arguments, joined by
   ", " and wrapped in parentheses: (1, 'a', None). With no positional
   arguments it is ().
9. Write a single positional argument as (1), with NO trailing comma.
   So you can't simply use repr(args), which gives (1,).
10. Build <K> from each keyword argument written as name=repr(value),
    joined by ", " and wrapped in curly braces: {x=1, y='hi'}. With no
    keyword arguments it is {}.
11. List the keyword arguments in the order they were passed. (`kwargs`
    is a normal dict, and dicts remember the order things were added,
    so this happens naturally.)

You can assume:
- Callers may pass any number of positional and keyword arguments, of
  any type.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    flexible_sum(1, 2, 3)             ->  6
        All ints, so the result is an int.

    flexible_sum(1, 2.5, bonus=10)    ->  13.5
        The keyword value 10 counts too. 2.5 is a float, so the
        result is a float.

    flexible_sum()                    ->  0
        No arguments at all.

    flexible_sum(1, "2")
        ->  raises TypeError: not a number: '2'
        "2" is a string, not a number. The message shows its repr,
        quotes included.

    describe_call(1, "a", flag=True)
        ->  "args=(1, 'a'); kwargs={flag=True}"
        Each value is shown with its repr, so "a" keeps its quotes.

    describe_call()                   ->  'args=(); kwargs={}'
        Nothing passed: empty parentheses and empty braces.

    describe_call(42)                 ->  'args=(42); kwargs={}'
        One argument, and no trailing comma after 42.

========================================================================
EDGE CASES TO TEST
========================================================================
- No arguments: flexible_sum() -> 0, describe_call() ->
  'args=(); kwargs={}'
- Only keyword arguments: flexible_sum(a=1, b=2) -> 3
- Negative numbers and floats: flexible_sum(-1, 0.5) -> -0.5
- A bool anywhere: flexible_sum(1, True) -> TypeError
- None, a str or a list as a value -> TypeError
- Unpacking into the call: flexible_sum(*[1, 2], **{"x": 3}) -> 6
- A single positional arg has no trailing comma:
  describe_call(42) -> 'args=(42); kwargs={}'
- String values show their quotes:
  describe_call(name="Bob") -> "args=(); kwargs={name='Bob'}"

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Inside the function, `args` is a tuple and `kwargs` is a dict. Loop
   over `args` and over `kwargs.values()`.
2. Check for bool FIRST with `isinstance(v, bool)`. Then check the
   type with `isinstance(v, (int, float))`. A tuple of types means
   "any of these".
3. `", ".join(...)` only joins strings, so turn each value into a
   string with `repr(x)` first.
4. For kwargs: `f"{name}={value!r}"`. The `!r` inside an f-string
   means "use repr()".
5. `pytest.raises(TypeError, match="not a number")` checks the
   message.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `*args` and `**kwargs` in a function DEFINITION (packing: gathering
  arguments into a tuple or dict)
- `*` and `**` in a function CALL (unpacking: spreading a list or dict
  out into separate arguments)
- `isinstance()` with a tuple of types, and the bool-is-an-int gotcha
- `repr()` vs `str()`, and `!r` in f-strings
- `str.join()`
- `pytest.raises(..., match=...)`

========================================================================
STRETCH GOALS
========================================================================
- Accept `decimal.Decimal` and `fractions.Fraction` too (hint:
  `numbers.Number`) while still rejecting bool.
- Give describe_call a `func_name` keyword-only argument (one that can
  only be passed by name, because it comes after `*args`) and produce
  "greet(1, x=2)"-style output.
- Write `call_with(func, *args, **kwargs)`, which forwards (passes on)
  everything to `func`. Decorators use this pattern later in this
  level.
"""


def flexible_sum(*args: int | float, **kwargs: int | float) -> int | float:
    """Sum every positional and keyword argument.

    Args:
        *args: Any number of int/float values.
        **kwargs: Any number of name=int/float values.

    Returns:
        The total of all values (0 if there are none).

    Raises:
        TypeError: If any value is not an int or float, or is a bool.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def describe_call(*args: object, **kwargs: object) -> str:
    """Describe the arguments this function was called with.

    Args:
        *args: Any positional arguments.
        **kwargs: Any keyword arguments.

    Returns:
        A string formatted exactly as "args=(A); kwargs={K}" - see the
        module docstring for the precise rules.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
