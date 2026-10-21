"""Level 05 - Functions, Deeper.

Goal: treat functions as ordinary values that you can pass around,
return and wrap. Along the way, learn the idioms that make Python code
short and expressive: comprehensions, flexible arguments, closures,
generators and decorators.

Concepts covered:
- Functions are objects: you can pass them as arguments and return
  them from other functions
- Higher-order functions (functions that take or return functions)
- lambda expressions (small one-line functions with no name)
- List, dict and set comprehensions (including nested ones)
- *args and **kwargs: accepting any number of arguments
- Closures (inner functions that remember the outer function's
  variables) and the `nonlocal` keyword
- Generators: `yield`, laziness (making each value only when it is
  asked for), infinite sequences, next(), islice()
- Decorators (functions that wrap other functions to add behaviour):
  the @ syntax, functools.wraps, decorator factories
- Function attributes (values stored on a function object, such as
  func.cache or func.calls)
- typing helpers from collections.abc: Callable, Iterable, Iterator
"""
