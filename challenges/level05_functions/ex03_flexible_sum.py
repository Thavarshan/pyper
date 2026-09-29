"""
Challenge: Flexible Sum
Level:     05 - Functions, Deeper
Topics:    *args, **kwargs, isinstance, repr, string formatting
Source:    Classic *args/**kwargs exercise

========================================================================
PROBLEM
========================================================================
Normally a function has a fixed list of parameters. Python lets a
function accept ANY number of arguments using two special parameters:

    def f(*args, **kwargs): ...

- `*args` collects all extra POSITIONAL arguments into a TUPLE.
- `**kwargs` collects all extra KEYWORD arguments (name=value) into a
  DICT mapping name -> value.

    f(1, 2, x=3)   ->   args == (1, 2)   kwargs == {"x": 3}

(The names `args`/`kwargs` are only a convention; the `*` and `**` are
what matter.)

Part 1 - `flexible_sum(*args, **kwargs)`

Return the sum of ALL positional values and ALL keyword values.
- Only numbers are allowed: `int` and `float`.
- `bool` is NOT allowed, even though in Python `True` is technically an
  int (isinstance(True, int) is True!). Treat bools as invalid.
- If any value is not a number, raise `TypeError` whose message names
  the offending value's repr, e.g. "not a number: 'hello'".
- With no arguments at all, return 0.
- The result is an int if every value was an int; if any value was a
  float, the result is a float (this happens naturally with `+`).

Part 2 - `describe_call(*args, **kwargs)`

Return a string that describes exactly how the function was called,
in this precise format:

    "args=<A>; kwargs=<K>"

where
- <A> is the positional arguments' reprs joined by ", " and wrapped in
  parentheses:  (1, 'a', None)   and for no args:  ()
  NOTE: a single arg is shown as (1) with NO trailing comma - so do not
  simply use repr(args).
- <K> is each keyword argument written as name=repr(value), joined by
  ", " and wrapped in curly braces, in the order they were passed:
  {x=1, y='hi'}   and for no kwargs:  {}

"repr" is the developer-facing text form of a value: repr("hi") is
"'hi'" (with quotes), repr(3) is "3", repr(None) is "None".

========================================================================
EXAMPLES
========================================================================
    >>> flexible_sum(1, 2, 3)
    6

    >>> flexible_sum(1, 2.5, bonus=10)
    13.5

    >>> flexible_sum()
    0

    >>> flexible_sum(1, "2")
    Traceback (most recent call last):
    ...
    TypeError: not a number: '2'

    >>> describe_call(1, "a", flag=True)
    "args=(1, 'a'); kwargs={flag=True}"

    >>> describe_call()
    'args=(); kwargs={}'

    >>> describe_call(42)
    'args=(42); kwargs={}'

========================================================================
CONSTRAINTS
========================================================================
- flexible_sum accepts any number of positional and keyword arguments.
- Valid values: instances of int or float, but NOT bool.
- Invalid values -> `TypeError` (message must contain repr(value)).
- describe_call must produce the format above character-for-character.
- Keyword arguments keep the order in which they were passed (kwargs is
  a normal dict, so it remembers insertion order).

========================================================================
EDGE CASES TO TEST
========================================================================
- No arguments                         -> 0 / 'args=(); kwargs={}'
- Only keyword arguments: flexible_sum(a=1, b=2) -> 3
- Negative numbers and floats
- A bool anywhere: flexible_sum(1, True) -> TypeError
- None, a str, a list as a value       -> TypeError
- Unpacking into the call: flexible_sum(*[1, 2], **{"x": 3}) -> 6
- describe_call with a single positional arg -> no trailing comma
- describe_call with string values shows quotes: {name='Bob'}

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Inside the function, `args` is a tuple and `kwargs` is a dict -
   loop over `args` and over `kwargs.values()`.
2. Check type with `isinstance(v, (int, float))`, and check for bool
   first with `isinstance(v, bool)`.
3. `", ".join(...)` only joins strings, so convert with `repr(x)` first.
4. For kwargs: `f"{name}={value!r}"` - the `!r` inside an f-string
   means "use repr()".
5. `pytest.raises(TypeError, match="not a number")` checks the message.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `*args` and `**kwargs` in a function DEFINITION (packing)
- `*` and `**` in a function CALL (unpacking)
- `isinstance()` with a tuple of types, and the bool-is-an-int gotcha
- `repr()` vs `str()`, and `!r` in f-strings
- `str.join()`
- `pytest.raises(..., match=...)`

========================================================================
STRETCH GOALS
========================================================================
- Accept `decimal.Decimal` and `fractions.Fraction` too (hint:
  `numbers.Number`) while still rejecting bool.
- Make describe_call accept a `func_name` keyword-only argument (after
  `*args`) and produce "greet(1, x=2)"-style output.
- Write `call_with(func, *args, **kwargs)` that forwards everything to
  `func` - the pattern decorators use later in this level.
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
