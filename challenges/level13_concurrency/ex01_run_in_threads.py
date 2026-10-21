"""
Challenge: Run in Threads
Level:     13 - Concurrency
Topics:    threading.Thread, start() and join(), collecting results,
           passing exceptions back to the caller
Source:    Classic threading exercise

========================================================================
YOUR TASK
========================================================================
Write `run_in_threads(func, inputs)`. It calls `func(item)` for every
item in `inputs`, each call in its OWN thread, all at the same time.
It waits for every thread to finish and returns the results as a list,
in the same order as `inputs`.

    run_in_threads(lambda x: x * 2, [1, 2, 3])  ->  [2, 4, 6]

========================================================================
BACKGROUND: WHAT A THREAD IS
========================================================================
Normally your program does one thing at a time, line by line. A
THREAD is a second (or third, or tenth) line of work running inside
the same program, alongside the main one. All threads share the same
variables.

Threads are most useful when the work spends its time WAITING: for a
web page, a file, a database or a timer. While one thread waits, the
others carry on. In this level `time.sleep(0.2)` stands in for "wait
0.2 seconds for the network".

Creating and running a thread takes three steps:

    import threading

    def greet(name):
        print("hello", name)

    t = threading.Thread(target=greet, args=("ann",))
    t.start()     # the thread starts running greet("ann")...
                  # ...while this line carries on straight away
    t.join()      # wait here until the thread has finished

- `target` is the function to run. Pass the function itself, with no
  parentheses.
- `args` is a TUPLE of arguments for it. A one-item tuple needs the
  trailing comma: `("ann",)`.
- `start()` returns immediately. The work happens in the background.
- `join()` BLOCKS (waits, doing nothing else) until that thread ends.

THE CLASSIC MISTAKE: starting and joining in the same loop.

    for item in inputs:          # WRONG: one at a time!
        t = threading.Thread(target=func, args=(item,))
        t.start()
        t.join()                 # waits before the next one starts

Each thread finishes before the next one even begins, so nothing runs
at the same time. With 5 calls that each take 0.2 s, this takes 1.0 s.
The fix is two loops: start ALL the threads first, then join ALL of
them. Then the 5 calls overlap and the total is about 0.2 s:

    seconds:  0.0       0.2       0.4       0.6       0.8       1.0
    wrong:    [ call 1 ][ call 2 ][ call 3 ][ call 4 ][ call 5 ]
    right:    [ call 1 ]
              [ call 2 ]
              [ call 3 ]
              [ call 4 ]
              [ call 5 ]

TWO THINGS A THREAD WON'T DO FOR YOU:

1. It doesn't hand back a return value. `t.join()` always returns
   None, and whatever `target` returned is thrown away. So your thread
   must STORE its result somewhere you can read later, such as a slot
   in a list.

2. It doesn't pass exceptions back to you. If `target` raises an
   exception, that thread just dies and Python prints a traceback.
   Neither `start()` nor `join()` raises anything, and your main code
   carries on as if all went well. (Under pytest, the traceback shows
   up as a PytestUnhandledThreadExceptionWarning instead.) So your
   thread must CATCH the exception and store it, and the main thread
   re-raises it later.

========================================================================
THE RULES
========================================================================
Your function must:
1. Create one `threading.Thread` per item in `inputs`.
2. Start ALL the threads, and only then join ALL of them, so the calls
   run at the same time.
3. Return a NEW list where position i holds `func(inputs[i])`. Keep
   the input order, whatever order the threads happen to finish in.
4. If `func` raises in any thread: first wait for ALL the threads to
   finish, then re-raise the exception in the caller. If several
   calls raised, re-raise the one from the EARLIEST input (lowest
   index), not the one that happened first in time.
5. Return [] for an empty `inputs` (and start no threads).
6. Not use `concurrent.futures`, `multiprocessing` or `asyncio`. The
   point is to use `threading.Thread` directly.

You can assume:
- `func` takes exactly one argument.
- `inputs` is a list. Don't change it.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    run_in_threads(lambda x: x * 2, [1, 2, 3])  ->  [2, 4, 6]

    run_in_threads(str.upper, ["a", "b"])       ->  ["A", "B"]

    run_in_threads(lambda x: x, [])             ->  []
        No inputs, no threads.

    def slow_double(x):
        time.sleep(0.2)
        return x * 2

    run_in_threads(slow_double, [1, 2, 3, 4, 5])  ->  [2, 4, 6, 8, 10]
        Takes about 0.2 seconds, not 1.0, because the calls overlap.

    def check(x):
        if x < 0:
            raise ValueError(f"negative: {x}")
        return x

    run_in_threads(check, [5, -1, -2])
        ->  raises ValueError("negative: -1")
        Both -1 and -2 fail. -1 has the lower index, so its error wins.

========================================================================
EDGE CASES TO TEST
========================================================================
- The calls overlap: 5 calls that each sleep 0.2 s finish in under
  0.6 s in total. Time it with `time.perf_counter()`. Use a generous
  limit like `< 0.6`, never `== 0.2`, because computers vary.
- Order is kept when threads finish out of order. Make input 0 sleep
  longest and the last input sleep shortest: the result is still in
  input order.
- Empty inputs -> []
- A single input: run_in_threads(str, [7]) -> ["7"]
- Each call gets its own thread: record
  `threading.current_thread().name` inside `func`. You get one
  distinct name per input, and none of them is the main thread's
  name, `threading.main_thread().name`.
- `func` is called exactly once per input.
- Results can be None: run_in_threads(lambda x: None, [1, 2]) ->
  [None, None]
- The earliest error wins: inputs [1, 2, 3, 4], where 4 raises
  straight away and 2 sleeps 0.2 s and then raises KeyError ->
  KeyError is raised, even though 4 failed first.
- All threads finish before the error is raised: inputs
  ["boom", "slow"], where "boom" raises at once and "slow" sleeps
  0.3 s and then appends to a `done` list. Once pytest.raises has
  caught the error, `done == ["slow"]`.
- No threads are left running afterwards: `threading.active_count()`
  is the same before and after the call.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Make two lists the same length as the inputs, filled in up front:
   `results = [None] * len(inputs)` and `errors = [None] * len(inputs)`.
   Each thread writes only to its OWN slot (its index), so threads
   never write to the same place.
2. Write a small inner function, say `worker(index, item)`. Inside a
   try block, store `func(item)` in `results[index]`. In
   `except Exception as exc`, store `exc` in `errors[index]` instead.
   Use `worker` as each thread's target, with `args=(i, item)`.
3. Build the threads with `enumerate(inputs)`. Keep them in a list,
   then loop over it once to start each one and again to join each
   one.
4. After joining, loop over `errors` from the start. The first one
   that isn't None is the earliest input's error: `raise` it. If none
   failed, return `results`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `threading.Thread(target=..., args=(...,))`, `.start()`, `.join()`
- Why `join()` returns None, and storing results in a shared list
- Inner functions (closures) that write into the outer function's
  list. Changing a list's item doesn't need `nonlocal`.
- Catching an exception, storing it, and re-raising it later with
  `raise exc`
- `threading.current_thread().name` and `threading.active_count()`
- Testing without hanging: `t.join(timeout=5)` followed by
  `assert not t.is_alive()`. pytest-timeout is installed too, so
  `@pytest.mark.timeout(10)` on a test fails it instead of letting it
  hang forever.

========================================================================
STRETCH GOALS
========================================================================
- Name your threads: `threading.Thread(..., name=f"worker-{i}")`.
  Print `threading.current_thread().name` inside `func` to watch the
  calls interleave.
- Compare with the standard library's ready-made version:
  `concurrent.futures.ThreadPoolExecutor().map(func, inputs)`. You'll
  meet it properly later in this level.
- Look up `threading.excepthook`: the function Python calls when an
  exception escapes a thread. Replace it with your own function and
  record the errors instead of printing them.
"""

import threading  # for you to use in your implementation
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


def run_in_threads(func: Callable[[T], R], inputs: list[T]) -> list[R]:
    """Call func(item) for every item, each in its own thread, at once.

    Args:
        func: A one-argument function to run for each item.
        inputs: The items to process. Not modified.

    Returns:
        A new list of results in the same order as `inputs`
        ([] if `inputs` is empty).

    Raises:
        Exception: Whatever `func` raised, re-raised after every thread
            has finished. If several calls raised, the one from the
            lowest index is re-raised.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
