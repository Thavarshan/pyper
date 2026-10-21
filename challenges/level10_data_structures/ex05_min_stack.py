"""
Challenge: Min Stack
Level:     10 - Data Structures
Topics:    stacks, class design, trading space for time, O(1) operations
Source:    LeetCode #155 "Min Stack"

========================================================================
YOUR TASK
========================================================================
Write a class `MinStack`. It works like a normal stack, but it can
also tell you the SMALLEST value currently in it, instantly. Write
these methods:

    MinStack()   create an empty stack
    push(val)    put `val` on top
    pop()        remove the top value AND return it
    top()        return the top value without removing it
    get_min()    return the smallest value currently in the stack
    __len__()    return how many values are in the stack (so len(s)
                 works)

========================================================================
THE TRICK: REMEMBER THE MINIMUM AT EVERY LEVEL
========================================================================
A STACK is "last in, first out", like a pile of plates: you add to and
remove from the top only.

The hard part: when you pop the current minimum, what is the NEW
minimum? You cannot afford to search for it. The trick is to remember,
for every position in the stack, what the minimum was at that moment:

    push 5    values: [5]          mins: [5]
    push 3    values: [5, 3]       mins: [5, 3]
    push 7    values: [5, 3, 7]    mins: [5, 3, 3]     get_min() -> 3
    pop -> 7  values: [5, 3]       mins: [5, 3]        get_min() -> 3
    pop -> 3  values: [5]          mins: [5]           get_min() -> 5

This is a classic "trade space for time" move: store a bit extra so
you never need to recompute.

========================================================================
THE RULES
========================================================================
Your class must:
1. Run EVERY method in O(1) time (constant time: the same speed no
   matter how many values are stored). So no loops over the stack,
   and no calling min() on a list.
2. Return None from `push`.
3. Return the removed top value from `pop`.
4. Raise `IndexError` from `pop`, `top` and `get_min` on an EMPTY
   stack. That's the same error Python raises for `[].pop()`.

You can assume:
- Values are ints. Negative and duplicate values are allowed.
- There are up to 30_000 operations in total.

========================================================================
EXAMPLES
========================================================================
Each line runs one call. `# ->` shows what it returns.

    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    s.get_min()     # -> -3
    s.pop()         # -> -3   (removes -3)
    s.top()         # -> 0
    s.get_min()     # -> -2   (-3 is gone, so -2 is smallest)
    len(s)          # -> 2

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(1) for every method: no loops, just a few list operations.
- Space: O(n) for n stored values (plus the extra minimums).

========================================================================
EDGE CASES TO TEST
========================================================================
- A fresh stack: len(s) is 0, and pop(), top() and get_min() each
  raise IndexError
- Push one value: top() and get_min() both return it
- Duplicate minimums: push 1, push 1, pop -> get_min() is still 1
- Push in decreasing order (5, 3, 1), then pop everything, checking
  get_min() each time: 1, then 3, then 5
- Push in increasing order (1, 3, 5): get_min() stays 1, the first
  value
- After popping everything, the stack behaves as empty again (pop,
  top and get_min raise IndexError)

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with a plain list as the underlying stack. push, pop and top
   are then easy.
2. get_min is the hard one. What if you kept a SECOND list alongside
   the first?
3. When you push `val`, also push `min(val, current_min)` onto the
   second list (or just `val` if the stack was empty).
4. When you pop, pop from both lists. The new top of the second list
   is the new minimum.
5. For IndexError you can simply let `list.pop()` / `list[-1]` raise
   it. Or check `if not self._stack:` and raise it yourself with a
   message.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Writing a class: `__init__`, instance attributes, methods, `self`
- The `__len__` dunder ("double underscore") method, so `len(obj)`
  works
- Leading underscore (`self._items`) means "private by convention"
- Raising built-in exceptions: `raise IndexError("pop from empty stack")`
- Storing tuples: one list of (value, min_so_far) pairs also works

========================================================================
STRETCH GOALS
========================================================================
- Use ONE list of (value, current_min) tuples instead of two lists.
- Add `get_max()`, also in O(1).
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
