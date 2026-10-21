"""
Challenge: Stack
Level:     08 - Classes
Topics:    classes wrapping a list, LIFO, __len__, __iter__, IndexError
Source:    Classic data structure

========================================================================
YOUR TASK
========================================================================
Write a `Stack` class that keeps its items in a Python list. The last
item you put in is the first one you take out. Fill in:

- `__init__(items=None)`: create a stack, optionally with starting items
- `push(item)`: put `item` on top, return None
- `pop()`: remove and return the top item
- `peek()`: return the top item WITHOUT removing it
- `is_empty()`: return True if there are no items
- `__len__()`: makes `len(stack)` give the number of items
- `__iter__()`: makes `for x in stack` go from TOP to BOTTOM
- `__repr__()`: describe it, as in "Stack([1, 2, 3])"

    s = Stack([1, 2, 3])
    s.pop()     # -> 3

========================================================================
WHAT A "STACK" IS
========================================================================
A STACK is a collection where the last item added is the first one
removed: "Last In, First Out" (LIFO). Think of a pile of plates. You
put plates on the top and take them off the top.

    push(1), push(2), push(3)      top -> [3]
                                          [2]
                                          [1]
    pop() -> 3, then pop() -> 2, then pop() -> 1

"DUNDER" (double-underscore) methods like __len__ and __iter__ are
hooks that Python calls for built-in operations: `len(s)` calls
`s.__len__()`, and `for x in s` calls `s.__iter__()`.

========================================================================
THE RULES
========================================================================
Your class must:

Creating
1. `Stack()` creates an empty stack.
2. `Stack(items)` takes any iterable (anything you can loop over, such
   as a list, tuple or generator) and pushes its items in order, so
   the LAST one ends up on top: Stack([1, 2, 3]).peek() == 3.
3. Not modify the iterable it was given.
4. Give each Stack its own list. Two stacks never share items.

Using
5. `push(item)` puts `item` on top and returns None.
6. `pop()` removes and returns the top item. On an empty stack it
   raises IndexError("pop from empty stack").
7. `peek()` returns the top item without removing it. On an empty
   stack it raises IndexError("peek from empty stack").
8. `is_empty()` returns True if there are no items.
9. `len(stack)` returns the number of items.
10. Iterating (`for x in stack`, `list(stack)`) goes from TOP to
    BOTTOM and does not change the stack: list(Stack([1, 2, 3])) ==
    [3, 2, 1].
11. `repr(stack)` returns exactly Stack([1, 2, 3]), with the items
    listed BOTTOM to TOP (the order you'd pass to the constructor to
    rebuild it). An empty stack gives Stack([]).
12. push, pop, peek, is_empty and len must all be O(1): they take the
    same tiny amount of time however many items are stored. Use the
    END of the list as the top, because list.append and list.pop are
    O(1) there.

You can assume:
- Items can be any Python object, including None.

========================================================================
EXAMPLES
========================================================================
A short script. Each `# ->` comment shows what that line returns.

    s = Stack()
    s.is_empty()        # -> True
    s.push("a")
    s.push("b")
    s.peek()            # -> 'b'
    len(s)              # -> 2
    list(s)             # -> ['b', 'a']   (top first)
    s.pop()             # -> 'b'
    repr(s)             # -> "Stack(['a'])"

    Stack([1, 2, 3]).peek()   # -> 3   (the last item is on top)
    Stack().pop()             # raises IndexError: pop from empty stack

========================================================================
EDGE CASES TO TEST
========================================================================
- A new stack: is_empty() is True, len(s) == 0, list(s) == []
- pop() and peek() on an empty stack -> raise IndexError with the
  messages "pop from empty stack" and "peek from empty stack"
- Push then pop returns the same object (`popped is item`)
- LIFO order over several pushes and pops: push 1, 2, 3 -> pops give
  3, 2, 1
- peek doesn't change len
- Pushing None works, and is_empty() is then False
- Iteration goes top to bottom and leaves the stack intact (len is the
  same afterwards)
- Stack([1, 2, 3]): the top is 3, and the original list is still
  [1, 2, 3] after pushing more items onto the stack
- Two stacks don't share items
- repr: Stack() -> "Stack([])", Stack([1, 2, 3]) -> "Stack([1, 2, 3])"

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. In __init__: `self._items = list(items) if items is not None else []`.
   `list(...)` makes a copy, so you never modify the caller's list.
2. Never use a mutable default argument like `items=[]`. That one list
   would be shared by every Stack. Use `None` as the default.
3. The top of the stack is `self._items[-1]`.
4. For __iter__, `return reversed(self._items)`, or write a generator
   (a function that uses `yield`).
5. Check `if not self._items:` before popping or peeking.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Wrapping a built-in type to give it a smaller, clearer interface
  (composition and encapsulation)
- __len__, __iter__, __repr__
- The mutable default argument trap
- `reversed()` and generators
- Raising built-in exceptions with helpful messages

========================================================================
STRETCH GOALS
========================================================================
- Add `__bool__` so `if stack:` works. (Hint: __len__ already does
  this, because Python treats an object with length 0 as False. Write
  a test proving it.)
- Add a `max_size` option that raises OverflowError when full.
- Use your Stack to solve LeetCode #20 "Valid Parentheses".
- Implement a MinStack (LeetCode #155) with an O(1) `get_min()`.
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
