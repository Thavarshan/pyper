"""
Challenge: Queue Using Two Stacks
Level:     08 - Classes
Topics:    FIFO vs LIFO, composing data structures, amortized analysis
Source:    LeetCode #232 "Implement Queue using Stacks"

========================================================================
YOUR TASK
========================================================================
Write a `MyQueue` class: a first-in, first-out queue built from TWO
Python lists, each used ONLY as a stack. Fill in:

- `__init__()`: create an empty queue
- `push(x)`: add x to the BACK of the queue, return None
- `pop()`: remove and return the item at the FRONT
- `peek()`: return the FRONT item without removing it
- `empty()`: return True if the queue has no items
- `__len__()`: makes `len(q)` give the number of items

    q = MyQueue()
    q.push(1)
    q.push(2)
    q.pop()     # -> 1   (first in, first out)

========================================================================
WHAT "QUEUE" AND "STACK" MEAN
========================================================================
A QUEUE is "First In, First Out" (FIFO), like a line at a shop: the
first person to join is the first to be served. A STACK (see ex03) is
the opposite: "Last In, First Out" (LIFO), like a pile of plates.

THE TRICK: keep an "in" stack for new items and an "out" stack for
items ready to leave. When you need the front of the queue and "out"
is empty, pop EVERYTHING from "in" and push it onto "out". Pouring one
stack into another reverses the order, so the oldest item ends up on
top of "out", exactly where you need it:

    push 1, 2, 3          in: [1, 2, 3]    out: []
    pop() needs front     in: []           out: [3, 2, 1]   (poured)
                          pop from out -> 1
    push 4                in: [4]          out: [3, 2]
    pop()                 out is not empty, so just pop from out -> 2

========================================================================
THE RULES
========================================================================
Your class must:
1. Store the items in exactly two lists, used ONLY as stacks. The only
   list operations allowed are:

       lst.append(x)          push onto the top (the end)
       lst.pop()              pop from the top (the end)   <- no pop(0)!
       lst[-1]                peek at the top
       len(lst), not lst      check the size, or whether it is empty

   `lst.pop(0)`, `lst.insert(0, x)`, slicing, `reversed` and
   `collections.deque` are NOT allowed. They would defeat the purpose.
2. `push(x)` adds x to the BACK of the queue and returns None.
3. `pop()` removes and returns the FRONT item. On an empty queue it
   raises IndexError("pop from empty queue").
4. `peek()` returns the FRONT item without removing it. On an empty
   queue it raises IndexError("peek from empty queue").
5. `empty()` returns True if the queue has no items.
6. `len(q)` returns the number of items.
7. push is O(1) (the same small cost however big the queue is). pop
   and peek are AMORTIZED O(1), explained below.

You can assume:
- Any Python object can be queued, including None.

========================================================================
EXAMPLES
========================================================================
A short script. Each `# ->` comment shows what that line returns.

    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.peek()                       # -> 1   (front, not removed)
    q.pop()                        # -> 1
    q.push(4)
    [q.pop(), q.pop(), q.pop()]    # -> [2, 3, 4]
    q.empty()                      # -> True
    q.pop()                        # raises IndexError
                                   # ("pop from empty queue")

========================================================================
COMPLEXITY: WHAT DOES "AMORTIZED O(1)" MEAN?
========================================================================
A single pop() can be slow: if "out" is empty and "in" holds n items,
you move all n of them. But each item moves from "in" to "out" at most
ONCE in its whole life. So over any run of n operations, the total
work is at most about 3n steps (push, move, pop for each item). The
AVERAGE cost per operation is then constant.

"Amortized O(1)" means exactly that: occasionally expensive, but cheap
on average over many calls. For example, 10_000 pushes then 10_000
pops move each item once: 10_000 moves in total, not 10_000 per pop.

If you moved the items back to "in" after every pop, you would lose
this, and every pop would be O(n) (its cost would grow with the number
of items).

========================================================================
EDGE CASES TO TEST
========================================================================
- A new queue: empty() is True, len(q) == 0
- pop() and peek() on an empty queue -> raise IndexError
- FIFO order: push 1, 2, 3 then pop three times -> 1, 2, 3
- Interleaved pushes and pops: push 1, push 2, pop, push 3, pop, pop
  -> the pops give 1, 2, 3
- peek doesn't remove: len is unchanged, and the next pop returns the
  same value
- Queueing None: push(None) -> len(q) == 1, empty() is False,
  pop() returns None
- A long run: 10_000 pushes then 10_000 pops returns 0..9999 in order
- Draining the queue fully makes empty() True again

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. In __init__: `self._in = []` and `self._out = []`.
2. push always appends to `self._in`.
3. Write a helper `_shift()`: if `self._out` is empty, pop every item
   from `self._in` and append it to `self._out`.
4. pop and peek: call `_shift()`, then check whether `self._out` is
   still empty. If it is, the whole queue is empty, so raise
   IndexError. Otherwise use `self._out.pop()` or `self._out[-1]`.
5. len is `len(self._in) + len(self._out)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- FIFO vs LIFO
- Building one data structure out of another (composition)
- Amortized analysis (average cost over many operations)
- Private helper methods (leading underscore)
- Why `list.pop(0)` is O(n) (every other item shifts down one place)
  and what `collections.deque` is for

========================================================================
STRETCH GOALS
========================================================================
- Reuse your Stack class from ex03 instead of raw lists.
- The reverse challenge: LeetCode #225 "Implement Stack using Queues".
- Use the `timeit` module to time 100_000 pushes + pops with
  `list.pop(0)`, with your MyQueue, and with `collections.deque`.
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
