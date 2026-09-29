"""
Challenge: Queue Using Two Stacks
Level:     08 - Classes
Topics:    FIFO vs LIFO, composing data structures, amortized analysis
Source:    LeetCode #232 "Implement Queue using Stacks"

========================================================================
PROBLEM
========================================================================
A QUEUE is "First In, First Out" (FIFO) - like a line at a shop: the
first person to join is the first to be served. A STACK (see ex03) is
the opposite: Last In, First Out.

Your job: build a queue called `MyQueue` using ONLY two Python lists,
and use each list ONLY as a stack. That means the only list operations
you may use are:

    lst.append(x)      push onto the top (end)
    lst.pop()          pop from the top (end)     <- no pop(0)!
    lst[-1]            peek at the top
    len(lst) / not lst size / emptiness check

(`lst.pop(0)`, `lst.insert(0, x)`, slicing, `reversed`, and
`collections.deque` are NOT allowed - they would defeat the purpose.)

The trick: keep an "in" stack for new items and an "out" stack for
items ready to leave. When you need the front of the queue and the
"out" stack is empty, pop EVERYTHING from "in" and push it onto "out".
Pouring a stack into another reverses its order - so the oldest item
ends up on top of "out", exactly where you need it.

Methods:
    MyQueue()          Create an empty queue.
    .push(x)           Add x to the BACK of the queue. Returns None.
    .pop()             Remove and return the item at the FRONT.
                       Empty -> IndexError("pop from empty queue").
    .peek()            Return the FRONT item without removing it.
                       Empty -> IndexError("peek from empty queue").
    .empty()           True if the queue has no items.
    len(q)             Number of items (implement __len__).

========================================================================
EXAMPLES
========================================================================
    >>> q = MyQueue()
    >>> q.push(1); q.push(2); q.push(3)
    >>> q.peek()
    1
    >>> q.pop()
    1
    >>> q.push(4)
    >>> [q.pop(), q.pop(), q.pop()]
    [2, 3, 4]
    >>> q.empty()
    True

========================================================================
CONSTRAINTS
========================================================================
- Use exactly two lists, used only as stacks (see allowed operations).
- Any Python object can be queued, including None.
- pop/peek on an empty queue raise IndexError.
- push is O(1). pop and peek are AMORTIZED O(1) (explained below).

========================================================================
COMPLEXITY: WHAT DOES "AMORTIZED O(1)" MEAN?
========================================================================
One single pop() can be slow: if "out" is empty and "in" holds n items,
you move all n of them. But each item is moved from "in" to "out" at
most ONCE in its whole life. Over any sequence of n operations the
total work is at most about 3n steps (push, move, pop per item), so the
AVERAGE cost per operation is constant. "Amortized O(1)" means exactly
that: occasionally expensive, but cheap on average over many calls.

If you moved items back to "in" after every pop, you would lose this
and every pop would be O(n).

========================================================================
EDGE CASES TO TEST
========================================================================
- New queue: empty() True, len 0
- pop()/peek() on empty -> IndexError
- FIFO order for a simple push, push, push, pop, pop, pop sequence
- Interleaved pushes and pops (push 1, push 2, pop, push 3, pop, pop)
  still give 1, 2, 3
- peek doesn't remove (len unchanged, pop returns same value)
- Queueing None
- A long run (e.g. 10_000 pushes then pops) returns items in order
- Draining the queue fully makes empty() True again

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. In __init__: `self._in = []` and `self._out = []`.
2. push always appends to `self._in`.
3. Write a helper `_shift()`: if `self._out` is empty, pop every item
   from `self._in` and append it to `self._out`.
4. pop and peek: call `_shift()`, then check whether `self._out` is
   still empty (-> the whole queue is empty -> IndexError); otherwise
   use `self._out.pop()` / `self._out[-1]`.
5. len is `len(self._in) + len(self._out)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- FIFO vs LIFO
- Building one abstraction out of another (composition)
- Amortized analysis
- Private helper methods (leading underscore)
- Why `list.pop(0)` is O(n) and what `collections.deque` is for

========================================================================
STRETCH GOALS
========================================================================
- Reuse your Stack class from ex03 instead of raw lists.
- The reverse challenge: LeetCode #225 "Implement Stack using Queues".
- Time 100_000 pushes + pops with `list.pop(0)` vs your MyQueue vs
  `collections.deque` using the `timeit` module.
- Add `__iter__` (front to back) without changing the queue.
"""

from typing import Any


class MyQueue:
    """A FIFO queue built from two lists used strictly as stacks."""

    def __init__(self) -> None:
        """Create an empty queue."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def push(self, x: Any) -> None:
        """Add `x` to the back of the queue."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def pop(self) -> Any:
        """Remove and return the front item.

        Raises:
            IndexError: If the queue is empty.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def peek(self) -> Any:
        """Return the front item without removing it.

        Raises:
            IndexError: If the queue is empty.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def empty(self) -> bool:
        """Return True if the queue has no items."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of items in the queue."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError
