"""
Challenge: Safe Counter
Level:     13 - Concurrency
Topics:    race conditions, threading.Lock, the `with` statement, the GIL
Source:    Classic race-condition exercise

========================================================================
YOUR TASK
========================================================================
Write a class `SafeCounter`: a number that many threads can change at
the same time without losing any updates. Write these methods:

    SafeCounter(start=0)     create a counter holding `start`
    increment(amount=1)      add `amount`
    decrement(amount=1)      subtract `amount`
    value                    a property: the current number

Then write `increment_many(counter, num_threads, increments_per_thread)`.
It starts `num_threads` threads, and each one calls
`counter.increment()` `increments_per_thread` times.

    c = SafeCounter()
    increment_many(c, 8, 10_000)
    c.value    # -> 80000, every single time

========================================================================
BACKGROUND: WHY `+= 1` IS NOT SAFE
========================================================================
`self._value += 1` looks like one step, but Python really does three:

    1. READ  the current value
    2. ADD   1 to it
    3. WRITE the new value back

Python can pause one thread and run another BETWEEN any two of these
steps. Here two threads both increment a counter that holds 5:

    stored   thread A           thread B
    5        read 5
    5                           read 5
    5        add: 5 + 1 = 6
    5                           add: 5 + 1 = 6
    6        write 6
    6                           write 6      <- A's +1 is lost!

Two increments ran, but the counter only went up by 1. This is a RACE
CONDITION: the result depends on the exact timing of the threads. It
is a nasty bug, because the code works most of the time and fails at
random.

"But Python has the GIL!" CPython (the usual Python) has a Global
Interpreter Lock: only one thread runs Python code at any moment. That
doesn't help here. Python can still switch threads between step 1 and
step 3, which is exactly what the table shows. Python 3.13 also has
an optional, experimental "free-threaded" build with no GIL at all,
where threads truly run at the same moment and races get even easier
to hit.

Honest warning: on CPython 3.10 to 3.12, a bare `self._value += 1`
very rarely loses an update in practice, because of where Python
chooses to switch threads. Rarely is not never. Nothing guarantees it,
other versions behave differently, and real code usually does more
work between the read and the write. So your tests may pass even
WITHOUT a lock. The lock is what makes the right answer certain.

To SEE a race when you experiment:
- Put `time.sleep(0)` between the read and the write. It tells Python
  "switch to another thread now".
- `sys.setswitchinterval(1e-6)` makes Python switch threads every
  microsecond instead of every 5 milliseconds, so races show up far
  more often. It affects the whole program, so save the old value
  with `sys.getswitchinterval()` and put it back in a `finally:`.

THE FIX: A LOCK

A `threading.Lock` lets only ONE thread at a time into a block of
code. Any other thread that arrives waits until the first one leaves:

    self._lock = threading.Lock()   # make it ONCE, in __init__

    with self._lock:      # acquire: wait until no one else holds it
        self._value += 1  # only one thread at a time runs this
                          # release: automatic when the block ends,
                          # even if an exception is raised

Now read, add and write happen together, with no other thread in the
middle. Always use `with` rather than calling `acquire()` and
`release()` yourself: if you forget the release, or an exception
skips it, every other thread waits forever.

========================================================================
THE RULES
========================================================================
Your class must:
1. `SafeCounter(start=0)`: start the stored value at `start`, and
   create ONE `threading.Lock` for this counter.
2. `increment(amount=1)`: add `amount` to the value. Return None.
3. `decrement(amount=1)`: subtract `amount` from the value. Return
   None. The value is allowed to go below 0.
4. Raise `ValueError` from `increment` or `decrement` if `amount` is
   negative, and leave the value unchanged. An `amount` of 0 is fine
   and does nothing.
5. `value`: a read-only property (use `@property`) that returns the
   current value as an int.
6. Do every read AND every write of the stored value inside
   `with self._lock:` (one lock for everything, including the read in
   `value`). Reading under the lock too means you never see a
   half-finished update, and it keeps the rule simple: "touch the
   data, hold the lock".

Your function `increment_many` must:
7. Raise `ValueError` if `num_threads` or `increments_per_thread` is
   negative. 0 is fine and does nothing.
8. Start `num_threads` threads. Each one calls `counter.increment()`
   (with no argument) `increments_per_thread` times.
9. Start ALL the threads first, then join ALL of them, and only then
   return (None).

You can assume:
- `start`, `amount`, `num_threads` and `increments_per_thread` are
  ints.

========================================================================
EXAMPLES
========================================================================
Each line runs one call. `# ->` shows what it returns.

    c = SafeCounter()
    c.value             # -> 0
    c.increment()
    c.increment(5)
    c.value             # -> 6
    c.decrement(2)
    c.value             # -> 4
    c.decrement(10)
    c.value             # -> -6    (going below 0 is allowed)
    c.increment(-1)     # -> raises ValueError (value stays -6)

    c2 = SafeCounter(10)
    increment_many(c2, 3, 10)
    c2.value            # -> 40    (10 + 3 threads x 10 increments)

    increment_many(c2, -1, 5)   # -> raises ValueError

========================================================================
EDGE CASES TO TEST
========================================================================
- A new counter: SafeCounter().value -> 0, SafeCounter(10).value -> 10
- amount 0 changes nothing: SafeCounter(3), then increment(0) and
  decrement(0) -> value 3
- Negative amounts raise ValueError and leave the value as it was
- decrement below zero: SafeCounter().decrement(5) -> value -5
- `value` is read-only: `c.value = 5` raises AttributeError (that is
  what a @property with no setter does)
- increment_many(SafeCounter(), 8, 10_000) -> value 80_000. Run it
  with `sys.setswitchinterval(1e-6)` (and restore it after) to make
  the test as tough as possible.
- increment_many with 0 threads, or 0 increments per thread -> value
  unchanged
- increment_many with a negative count -> ValueError
- Many threads incrementing by 3 and others decrementing by 2 at the
  same time: 4 threads x 10_000 x (+3) and 4 threads x 10_000 x (-2)
  -> value 40_000
- Never let a test hang: join with `t.join(timeout=5)`, then
  `assert not t.is_alive()`. pytest-timeout is installed, so you can
  also mark a test with `@pytest.mark.timeout(10)`.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. In __init__, store `self._value = start` and
   `self._lock = threading.Lock()`.
2. In increment: check `amount` first and raise if it's negative.
   Then `with self._lock:` and add.
3. The property is a method with `@property` above it. Inside, return
   the value from within `with self._lock:`. Returning from inside a
   `with` block still releases the lock.
4. increment_many: write a small inner function that loops
   `increments_per_thread` times calling `counter.increment()`. Make a
   list of `num_threads` threads with it as the target. Start each
   one, then join each one.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Race conditions and "read, modify, write"
- `threading.Lock` and the `with` statement (a context manager: an
  object that does setup on entry and cleanup on exit)
- The GIL (Global Interpreter Lock), and why it doesn't make your code
  thread-safe
- `@property` for read-only attributes
- `sys.setswitchinterval` / `sys.getswitchinterval` for experiments
- try/finally to always restore a global setting

========================================================================
STRETCH GOALS
========================================================================
- Write an `UnsafeCounter` with no lock, whose increment does
  `current = self._value`, then `time.sleep(0)`, then
  `self._value = current + amount`. Write a test showing that 4
  threads x 1_000 increments ends BELOW 4_000. Then remove the
  `time.sleep(0)` and see how much harder the race is to catch, even
  with `sys.setswitchinterval(1e-6)`.
- `Lock` vs `RLock`: add a method `add_twice(amount)` that holds the
  lock and calls `self.increment(amount)` twice. With a `Lock` it
  hangs forever: the thread waits for a lock that it holds itself.
  That's a DEADLOCK (threads stuck waiting, forever). Switch to
  `threading.RLock` (a re-entrant lock: the thread that holds it may
  take it again) and it works. To test the hang safely, run it in a
  thread made with `daemon=True` (so Python can still exit while it's
  stuck), join with a timeout, and assert the thread is still alive.
"""

import threading  # for you to use in your implementation


class SafeCounter:
    """An integer counter that is safe to change from many threads."""

    def __init__(self, start: int = 0) -> None:
        """Create a counter.

        Args:
            start: The initial value.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def increment(self, amount: int = 1) -> None:
        """Add `amount` to the counter, holding the lock.

        Args:
            amount: How much to add. Must be >= 0.

        Raises:
            ValueError: If amount < 0.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def decrement(self, amount: int = 1) -> None:
        """Subtract `amount` from the counter, holding the lock.

        Args:
            amount: How much to subtract. Must be >= 0.

        Raises:
            ValueError: If amount < 0.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @property
    def value(self) -> int:
        """The current value, read while holding the lock.

        Returns:
            The current value.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError


def increment_many(counter: SafeCounter, num_threads: int, increments_per_thread: int) -> None:
    """Increment `counter` from many threads at the same time.

    Starts `num_threads` threads, and each calls counter.increment()
    `increments_per_thread` times. Returns once every thread has finished.

    Args:
        counter: The counter to increment.
        num_threads: How many threads to start. Must be >= 0.
        increments_per_thread: How many increments each thread does.
            Must be >= 0.

    Raises:
        ValueError: If num_threads or increments_per_thread is negative.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
