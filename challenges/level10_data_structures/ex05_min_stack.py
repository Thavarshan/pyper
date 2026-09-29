"""
Challenge: Min Stack
Level:     10 - Data Structures
Topics:    stacks, class design, trading space for time, O(1) operations
Source:    LeetCode #155 "Min Stack"

========================================================================
PROBLEM
========================================================================
Design a class `MinStack` that behaves like a normal stack but can also
tell you the SMALLEST value currently in it - instantly.

It must support these methods, and EVERY one must run in O(1) time
(constant time - no loops over the stack, no calling min() on a list):

    MinStack()        create an empty stack
    push(val)         put `val` on top
    pop()             remove the top value AND return it
    top()             return the top value without removing it
    get_min()         return the smallest value currently in the stack
    __len__()         return how many values are in the stack (so len(s)
                      works)

The difficulty: when you pop the current minimum, what is the NEW
minimum? You cannot afford to search for it. The trick is to remember,
for every position in the stack, what the minimum was at that moment:

    push 5    values: [5]          mins: [5]
    push 3    values: [5, 3]       mins: [5, 3]
    push 7    values: [5, 3, 7]    mins: [5, 3, 3]     get_min() -> 3
    pop -> 7  values: [5, 3]       mins: [5, 3]        get_min() -> 3
    pop -> 3  values: [5]          mins: [5]           get_min() -> 5

This is a classic "trade space for time" move: store a bit extra so you
never need to recompute.

========================================================================
EXAMPLES
========================================================================
    >>> s = MinStack()
    >>> s.push(-2)
    >>> s.push(0)
    >>> s.push(-3)
    >>> s.get_min()
    -3
    >>> s.pop()
    -3
    >>> s.top()
    0
    >>> s.get_min()
    -2
    >>> len(s)
    2

========================================================================
CONSTRAINTS
========================================================================
- Values are ints (negative and duplicate values allowed).
- `push` returns None.
- `pop`, `top` and `get_min` on an EMPTY stack must raise `IndexError`
  (the same error Python raises for `[].pop()`).
- Up to 30_000 operations in total.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(1) for every method.
- Space: O(n) for n stored values.

========================================================================
EDGE CASES TO TEST
========================================================================
- A fresh stack: len is 0, and pop/top/get_min raise IndexError
- Push one value: top() and get_min() both return it
- Duplicate minimums: push 1, push 1, pop -> get_min() is still 1
- Push in decreasing order, then pop everything checking get_min() each time
- Push in increasing order: get_min() stays the first value
- After popping everything, the stack behaves as empty again (IndexError)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with a plain list as the underlying stack - push/pop/top are easy.
2. get_min is the hard one. What if you kept a SECOND list in parallel?
3. When you push `val`, also push `min(val, current_min)` onto the second
   list (or just `val` if the stack was empty).
4. When you pop, pop from both lists. The new top of the second list is
   the new minimum.
5. For IndexError you can simply let `list.pop()` / `list[-1]` raise it,
   or check `if not self._stack:` and raise it yourself with a message.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Writing a class: `__init__`, instance attributes, methods, `self`
- The `__len__` dunder method so `len(obj)` works
- Leading underscore (`self._items`) = "private by convention"
- Raising built-in exceptions: `raise IndexError("pop from empty stack")`
- Storing tuples: one list of (value, min_so_far) pairs also works

========================================================================
STRETCH GOALS
========================================================================
- Use ONE list of (value, current_min) tuples instead of two lists.
- Add `get_max()` also in O(1).
- Save space: only push onto the min-list when val <= current min.
"""


class MinStack:
    """A stack that can also report its minimum value in O(1) time."""

    def __init__(self) -> None:
        """Create an empty MinStack."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def push(self, val: int) -> None:
        """Push `val` onto the top of the stack.

        Args:
            val: The value to add.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def pop(self) -> int:
        """Remove and return the top value.

        Returns:
            The value that was on top.

        Raises:
            IndexError: If the stack is empty.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def top(self) -> int:
        """Return the top value without removing it.

        Returns:
            The value currently on top.

        Raises:
            IndexError: If the stack is empty.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def get_min(self) -> int:
        """Return the smallest value currently in the stack.

        Returns:
            The minimum value.

        Raises:
            IndexError: If the stack is empty.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of values in the stack.

        Returns:
            How many values are currently stored.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError
