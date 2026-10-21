# Glossary

Plain-English meanings of terms that come up again and again in the
challenges. Each challenge also explains these the first time it uses them,
so you don't need to read this file front to back. Use it to look things up.

## Functions and values

**return vs print**
: `return` hands a value back to whoever called the function, so they can
  store it or test it. `print()` only shows text on the screen. The
  challenges almost always want you to `return`, and tests can only check
  what you return.

**argument / parameter**
: In `def greet(name):`, `name` is a *parameter* (the placeholder). In
  `greet("Ada")`, `"Ada"` is the *argument* (the actual value passed in).

**positional / keyword argument**
: `f(1, 2)` passes arguments by position. `f(a=1, b=2)` passes them by name
  (keyword).

**`*args` / `**kwargs`**
: `*args` collects any number of extra positional arguments into a tuple.
  `**kwargs` collects extra keyword arguments into a dict.

**type hint**
: A note such as `name: str` or `-> list[int]` saying what type a value
  should be. Python doesn't enforce it; it's documentation for you and your
  editor.

**callable**
: Anything you can call with `()`: a function, a lambda, a class, or an
  object with a `__call__` method.

**closure**
: A function defined inside another function that still remembers the outer
  function's variables after the outer function has returned.

**decorator**
: A function that takes a function and returns a new, usually wrapped,
  function. `@my_decorator` above a `def` is shorthand for
  `func = my_decorator(func)`.

**generator**
: A function that uses `yield` to hand back values one at a time, pausing
  between them, instead of building a whole list up front.

**pure function**
: A function whose result depends only on its arguments, and which changes
  nothing outside itself. The same input always gives the same output.

**side effect**
: Anything a function does besides returning a value, such as printing,
  changing a list it was given, or writing a file.

## Changing data

**mutate / mutable / immutable**
: To *mutate* is to change an object in place. Lists, dicts and sets are
  *mutable* (they can be changed). Strings, ints, floats and tuples are
  *immutable*: every "change" actually builds a new object.

**in place**
: Changing the original object instead of building a new one.
  `nums.sort()` sorts in place. `sorted(nums)` returns a new sorted list
  and leaves `nums` alone.

**"do not modify the input"**
: After your function runs, the list or dict the caller passed in must look
  exactly as it did before. Work on a copy, or build a new result.

**copy (shallow)**
: `nums[:]`, `list(nums)` or `nums.copy()` make a new list holding the
  *same* items. A change to the new list doesn't affect the old one.

## Truth and comparison

**truthy / falsy**
: How a value behaves inside `if`. *Falsy* values count as False: `0`,
  `0.0`, `""`, `[]`, `{}`, `set()`, `None`, `False`. Everything else is
  *truthy*. So `if not name:` is True when `name == ""`.

**`==` vs `is`**
: `==` asks "do these have equal values?". `is` asks "are these the very
  same object?". Two separate lists `[1] == [1]` is True, but `[1] is [1]`
  is False. Use `is` mainly for `None`: `if x is None:`.

**float imprecision**
: Computers store decimals in binary, so `0.1 + 0.2 == 0.3` is False. In
  tests, compare floats with `pytest.approx(...)`.

## Collections

**iterable**
: Anything you can loop over with `for`: lists, strings, tuples, dicts,
  sets, ranges, generators, files.

**hashable**
: Can be used as a dict key or stored in a set. Immutable built-in values
  (ints, strings, tuples of hashable things) are hashable. Lists, dicts and
  sets are not.

**index**
: An item's position in a sequence, counting from 0. Negative indexes count
  from the end: `nums[-1]` is the last item.

**slice**
: `nums[start:stop]` makes a new list from `start` up to (but not
  including) `stop`. Either end can be left out: `nums[:2]`, `nums[-2:]`.

**stable sort**
: A sort that keeps items with equal keys in their original relative
  order.

## Errors

**raise**
: Stop the function and signal an error: `raise ValueError("n must be >= 0")`.

**propagate**
: Let an exception pass through your function to the caller instead of
  catching it. If you don't write `try`/`except`, exceptions propagate
  automatically.

**custom exception**
: Your own error type, made by subclassing `Exception`:
  `class ConfigError(Exception): ...`.

## Algorithms

**Big-O (O(n), O(1), ...)**
: A rough measure of how the work grows as the input gets bigger, where *n*
  is the input size (for example the length of the list).
  - **O(1)**: constant. The same amount of work whatever the size.
  - **O(log n)**: halves the problem each step, like binary search.
  - **O(n)**: one pass over the input.
  - **O(n log n)**: good sorting algorithms such as merge sort.
  - **O(n²)**: a loop inside a loop over the input.
  - **O(2ⁿ)**: doubles with every extra item, such as listing all subsets.

  *Space* complexity is the same idea for extra memory. **O(1) space** means
  only a few variables, with no new list that grows with the input.

**recursion / base case**
: A function that calls itself on a smaller version of the problem. The
  *base case* is the smallest version, which it answers directly without
  calling itself. Without one, the calls never end.

**memoization / cache**
: Remembering answers you've already worked out so you never compute the
  same thing twice.

**dynamic programming (DP)**
: Solving a big problem by building it from answers to smaller,
  overlapping sub-problems, usually stored in a list or table.

**greedy**
: Always taking whatever looks best right now. It's fast, but it doesn't
  always give the best overall answer.

**two pointers / sliding window**
: Walking through a list with two positions at once, either from both ends
  inwards or as the start and end of a moving "window".

**sentinel**
: A special stand-in value that means "nothing yet" or "impossible", such
  as `-1`, `None` or `float("inf")`. Also a dummy node at the start or end
  of a linked list, so the code never has to handle an empty list
  separately.

**DFS / BFS**
: Two ways to explore a tree or graph. *Depth-first search* goes as deep as
  possible down one path before backing up. *Breadth-first search* explores
  everything 1 step away, then everything 2 steps away, and so on.

**idempotent**
: Doing it twice has the same effect as doing it once. Sorting an
  already-sorted list changes nothing.
