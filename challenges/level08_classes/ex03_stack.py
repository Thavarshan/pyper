"""
Challenge: Stack
Level:     08 - Classes
Topics:    classes wrapping a list, LIFO, __len__, __iter__, IndexError
Source:    Classic data structure

========================================================================
PROBLEM
========================================================================
A STACK is a collection where the last item added is the first one
removed - "Last In, First Out" (LIFO). Think of a stack of plates: you
put plates on top and take them off the top.

    push(1), push(2), push(3)      top -> [3]
                                          [2]
                                          [1]
    pop() -> 3, then pop() -> 2 ...

Build a `Stack` class (storing items in a Python list internally):

    Stack()               Create an empty stack.
    Stack(items)          Optional: an iterable of starting items,
                          pushed in order (so the LAST one is on top).
                          Stack([1, 2, 3]).peek() == 3.
                          The given iterable must not be modified.

    .push(item)           Put `item` on top. Returns None.
    .pop()                Remove and return the top item.
                          Empty stack -> IndexError("pop from empty stack").
    .peek()               Return the top item WITHOUT removing it.
                          Empty stack -> IndexError("peek from empty stack").
    .is_empty()           True if there are no items.
    len(stack)            Number of items (implement __len__).
    iter(stack)           Iterate from TOP to BOTTOM without removing
                          anything (implement __iter__). So
                          list(Stack([1, 2, 3])) == [3, 2, 1].
    repr(stack)           Exactly:  Stack([1, 2, 3])  - items listed
                          BOTTOM to TOP (the order you'd pass to the
                          constructor to rebuild it). Empty: Stack([])

Items can be any Python object, including None.

"Dunder" (double-underscore) methods like __len__ and __iter__ are hooks
Python calls for built-in operations: `len(s)` calls `s.__len__()`,
`for x in s` calls `s.__iter__()`.

========================================================================
EXAMPLES
========================================================================
    >>> s = Stack()
    >>> s.is_empty()
    True
    >>> s.push("a"); s.push("b")
    >>> s.peek()
    'b'
    >>> len(s)
    2
    >>> list(s)
    ['b', 'a']
    >>> s.pop()
    'b'
    >>> s
    Stack(['a'])

========================================================================
CONSTRAINTS
========================================================================
- push, pop, peek, is_empty and len must all be O(1) (use the END of
  the list as the top: list.append / list.pop are O(1) there).
- pop/peek on an empty stack raise IndexError (messages above).
- Iterating must not change the stack.
- Each Stack instance has its own list (no sharing between instances).

========================================================================
EDGE CASES TO TEST
========================================================================
- New stack: is_empty() True, len 0, list(s) == []
- pop() and peek() on an empty stack -> IndexError
- Push then pop returns the same object
- LIFO order over several pushes/pops
- peek doesn't change len
- Pushing None works and is_empty() is then False
- Iteration order is top to bottom and leaves the stack intact
- Stack([1, 2, 3]) - top is 3; the original list is unchanged
- Two stacks don't share items
- repr for empty and non-empty stacks

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. In __init__: `self._items = list(items) if items is not None else []`.
   `list(...)` makes a copy, so you never modify the caller's list.
2. Never use a mutable default argument like `items=[]` - that one list
   would be shared by every Stack. Use `None` as the default.
3. The top of the stack is `self._items[-1]`.
4. For __iter__, `return reversed(self._items)` or write a generator
   with `yield`.
5. Check `if not self._items:` before popping or peeking.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Wrapping a built-in type to give it a smaller, clearer interface
  (composition / encapsulation)
- __len__, __iter__, __repr__
- The mutable default argument trap
- `reversed()` and generators
- Raising built-in exceptions with helpful messages

========================================================================
STRETCH GOALS
========================================================================
- Add `__bool__` so `if stack:` works (hint: __len__ already does this -
  write a test proving it).
- Add a `max_size` option that raises OverflowError when full.
- Use your Stack to solve LeetCode #20 "Valid Parentheses".
- Implement a MinStack (LeetCode #155) with O(1) `get_min()`.
"""

from collections.abc import Iterable, Iterator
from typing import Any


class Stack:
    """A last-in, first-out (LIFO) stack."""

    def __init__(self, items: Iterable[Any] | None = None) -> None:
        """Create a stack, optionally pre-filled.

        Args:
            items: Optional iterable of starting items, pushed in order
                (the last item ends up on top). Not modified.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def push(self, item: Any) -> None:
        """Put `item` on top of the stack."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def pop(self) -> Any:
        """Remove and return the top item.

        Raises:
            IndexError: If the stack is empty.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def peek(self) -> Any:
        """Return the top item without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Return True if the stack has no items."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of items on the stack."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __iter__(self) -> Iterator[Any]:
        """Iterate over items from top to bottom, without removing them."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __repr__(self) -> str:
        """Return e.g. "Stack([1, 2, 3])" with items bottom to top."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError
