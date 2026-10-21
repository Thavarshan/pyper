"""
Challenge: Thread Pool
Level:     13 - Concurrency
Topics:    concurrent.futures, ThreadPoolExecutor, Future, as_completed
Source:    Standard-library `concurrent.futures` patterns

========================================================================
YOUR TASK
========================================================================
Write two functions with `concurrent.futures.ThreadPoolExecutor`:

- `parallel_map(func, items, max_workers=4)` works like
  `[func(x) for x in items]`, but runs up to `max_workers` calls at the
  same time. Results come back in input order.
- `fastest(funcs)` runs every zero-argument function at once and
  RETURNS the result of the first one to finish without an error.

    parallel_map(lambda x: x * x, [1, 2, 3])   ->  [1, 4, 9]
    fastest([slow_server, fast_server])        ->  what fast_server returns

========================================================================
BACKGROUND: THREAD POOLS AND FUTURES
========================================================================
In ex04 you built a pool of worker threads by hand, with a queue and
sentinels. `concurrent.futures` does all of that for you.

THE EXECUTOR

    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(pow, 2, 10)   # schedule pow(2, 10)
        future.result()                        # -> 1024

`ThreadPoolExecutor(max_workers=3)` keeps a pool of up to 3 worker
threads. `submit(func, *args)` hands it one job and returns AT ONCE,
without waiting for the job. When the `with` block ends, the pool shuts
down, and it WAITS for every job to finish first.

A FUTURE

`submit()` gives you a Future: a box that will hold the job's result
once the job is done. Think of it as an IOU.

    future.done()        True once the job has finished (or failed)
    future.result()      waits for the job, then returns its value.
                         If the job raised, result() raises that same
                         exception here, in your thread.
    future.exception()   waits for the job, then returns the
                         exception it raised, or None if it worked.
                         It does not raise.
    future.cancel()      cancels a job that hasn't started yet. A job
                         that is already running can't be cancelled.

THREE WAYS TO GET RESULTS

    executor.submit(func, x)    one job, one Future
    executor.map(func, items)   like the built-in map(): results in
                                INPUT order. It's lazy (it hands out
                                results only as you loop over it), so
                                wrap it in list().
    as_completed(futures)       loops over Futures in the order they
                                FINISH, fastest first

    import time
    from concurrent.futures import as_completed

    def nap(seconds):
        time.sleep(seconds)
        return seconds

    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(nap, s) for s in (0.3, 0.1, 0.2)]
        [f.result() for f in as_completed(futures)]  # -> [0.1, 0.2, 0.3]

WHEN THREADS HELP

Threads help when the work is mostly WAITING: for a network reply, a
database or a disk. That kind of work is called "I/O-bound" (I/O means
input/output). While one thread waits, the others run. In these
challenges `time.sleep` stands in for that waiting.

Threads don't speed up number-crunching ("CPU-bound" work) in normal
Python. The GIL (Global Interpreter Lock) lets only one thread run
Python code at a time. ex07 uses processes for that kind of work.

DON'T WAIT FOR THE LOSERS

fastest() should return as soon as it has a winner. A `with` block
gets in the way: leaving it waits for EVERY job, including slow ones
whose results you no longer need. So for fastest(), create the
executor without `with`, and when you're done call:

    executor.shutdown(wait=False, cancel_futures=True)

`wait=False` means "don't wait for the jobs". `cancel_futures=True`
drops jobs that are still waiting in the queue and haven't started.
Jobs that are already RUNNING keep running in the background until
they finish, because Python can't stop a thread from outside. (Python
still waits for them before the whole program exits.) In fastest()
every job starts at once, so nothing is queued, but cancelling queued
work is a good habit for pools with fewer workers than jobs.

========================================================================
THE RULES
========================================================================
`parallel_map` must:
1. Raise `ValueError` if `max_workers < 1`. Check this first, so it
   happens even when `items` is empty.
2. Return [] when `items` is empty.
3. Use `ThreadPoolExecutor(max_workers=max_workers)` in a `with`
   block, so at most `max_workers` calls run at the same time.
4. Return a NEW list with `func(item)` for every item, in input order.
5. Let an exception from `func` propagate (pass through to the
   caller), unchanged.
6. Not change `items`.

`fastest` must:
7. Raise `ValueError` if `funcs` is empty.
8. Run all the functions at the same time, with
   `ThreadPoolExecutor(max_workers=len(funcs))`.
9. Return the result of the FIRST function to finish without raising.
   Use `as_completed`. Skip the functions that raised.
10. Raise `RuntimeError("all functions failed")` if every one of them
    raised.
11. Return as soon as it has a winner, without waiting for the slower
    functions. Don't use a `with` block. Call
    `executor.shutdown(wait=False, cancel_futures=True)` instead, both
    after a win and after "all functions failed".

You can assume:
- `items` and `funcs` are lists, and `max_workers` is an int.
- Every function in `funcs` takes no arguments.
- `func` is safe to call from several threads at once.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    parallel_map(lambda x: x * x, [1, 2, 3])   ->  [1, 4, 9]

    parallel_map(len, [])                      ->  []

    parallel_map(lambda x: 1 / x, [1, 0, 2])   ->  raises ZeroDivisionError
        The error happens in a worker thread, but it reaches YOU.

    parallel_map(len, ["a"], max_workers=0)    ->  raises ValueError

    def slow(x):
        time.sleep(0.2)
        return x

    parallel_map(slow, [1, 2, 3, 4, 5], max_workers=5)  ->  [1, 2, 3, 4, 5]
        All 5 run at the same time: about 0.2 s, not 1.0 s.

For fastest(), this helper makes test functions. It is a function that
builds and returns a new function (a closure):

    def sleeper(seconds, value):
        def f():
            time.sleep(seconds)
            return value
        return f

    def broken():
        raise ValueError("server down")

    fastest([sleeper(0.3, "slow"), sleeper(0.05, "fast")])  ->  'fast'

    fastest([sleeper(1.0, "slow"), sleeper(0.05, "fast")])  ->  'fast'
        After about 0.05 s. It does NOT wait the full 1.0 s.

    fastest([broken, sleeper(0.1, "ok")])   ->  'ok'
        broken finishes first, but it raised, so it is skipped.

    fastest([broken, broken])   ->  raises RuntimeError("all functions failed")

    fastest([])                 ->  raises ValueError

========================================================================
EDGE CASES TO TEST
========================================================================
Time things with `time.perf_counter()` and always leave a generous
margin. Never assert an exact time.

parallel_map:
- Order is kept even when the FIRST item finishes LAST: with a func
  that sleeps `x * 0.05` s and returns x,
  parallel_map(that_func, [3, 2, 1], max_workers=3) -> [3, 2, 1]
- Calls run at the same time: 5 items that each sleep 0.2 s with
  max_workers=5 -> takes less than 0.6 s
- The default is 4 workers: 8 items that each sleep 0.2 s -> takes
  between 0.35 s and 0.8 s (2 rounds of 4)
- At most `max_workers` at once: make func count how many calls are
  running right now (a shared counter changed under a
  `threading.Lock`) and record the highest value seen. 12 items that
  each sleep 0.05 s with max_workers=3 -> the highest is 3.
- An exception propagates: `pytest.raises(ZeroDivisionError)` around
  parallel_map(lambda x: 1 / x, [1, 0, 2])
- Empty list -> []
- max_workers = 0 or -3 -> raises ValueError (also with an empty list)

fastest:
- It doesn't wait for the losers: [sleeper(1.0, "slow"),
  sleeper(0.05, "fast")] -> 'fast' in less than 0.5 s
- It skips failures: [broken, sleeper(0.1, "ok")] -> 'ok'
- All fail -> `pytest.raises(RuntimeError, match="all functions failed")`
- Empty list -> raises ValueError
- One function -> its result: fastest([lambda: 42]) -> 42
- A winner that returns None still wins: fastest([lambda: None]) ->
  None. So don't use "the result is None" to mean "it failed".
- They all run at once: two functions that sleep 0.2 s then raise,
  plus sleeper(0.3, "ok") -> 'ok' in less than 0.5 s (one at a time
  would take 0.7 s)
- Add `@pytest.mark.timeout(10)` above your tests (pytest-timeout is
  installed), so a hang fails instead of freezing pytest.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. parallel_map fits in a few lines:

       with ThreadPoolExecutor(max_workers=max_workers) as executor:
           return list(executor.map(func, items))

   `list()` matters. It collects every result before the `with` block
   ends, and it re-raises an error from `func`. (If several calls
   raise, you get the error of the earliest item.)
2. ThreadPoolExecutor raises its own ValueError for max_workers=0,
   but only once you create one. Check `max_workers` yourself at the
   top, before anything else.
3. fastest: `executor = ThreadPoolExecutor(max_workers=len(funcs))`,
   then `futures = [executor.submit(f) for f in funcs]`.
4. Loop with `for future in as_completed(futures):`. Inside, check
   `future.exception() is None`. If so, return `future.result()`.
   as_completed only hands you finished futures, so neither call
   waits.
5. Put the loop in `try:` and the shutdown call in `finally:`. A
   `finally` block runs whether you return a winner or raise the
   RuntimeError.
6. If the loop ends without returning, every function failed. Raise
   the RuntimeError there.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `concurrent.futures.ThreadPoolExecutor`: `submit()`, `map()`,
  `shutdown()`
- Future objects: `result()`, `exception()`, `done()`, `cancel()`
- `as_completed()`: results in the order they finish
- `try`/`finally` for clean-up that must always happen
- I/O-bound vs CPU-bound work, and the GIL

========================================================================
STRETCH GOALS
========================================================================
- Give fastest() a `timeout` argument: `as_completed(futures,
  timeout=...)` raises `concurrent.futures.TimeoutError` (the same as
  the built-in TimeoutError on Python 3.11+) if nothing finishes in
  time.
- When every function fails, attach the last error:
  `raise RuntimeError("all functions failed") from last_error`. The
  traceback then shows both errors.
- Write parallel_map with `submit()` and a list of futures instead of
  `map()`, and check that the order still holds.
- Read about `concurrent.futures.wait(futures,
  return_when=FIRST_COMPLETED)`, another way to wait for a winner.
- Compare with your hand-built pool in ex04. What does the executor
  give you for free?
"""

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


def parallel_map(func: Callable[[T], R], items: list[T], max_workers: int = 4) -> list[R]:
    """Return [func(item) for item in items], running calls on a thread pool.

    Args:
        func: A one-argument function to call on each item.
        items: The items to process. Not modified.
        max_workers: Most calls to run at the same time. Must be >= 1.

    Returns:
        A new list of results, in input order.

    Raises:
        ValueError: If max_workers < 1.
        Exception: Whatever `func` raises is passed on unchanged.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def fastest(funcs: list[Callable[[], R]]) -> R:
    """Run all funcs at once and return the first successful result.

    Args:
        funcs: Zero-argument functions to race against each other.

    Returns:
        The return value of the first function to finish without raising.

    Raises:
        ValueError: If funcs is empty.
        RuntimeError: "all functions failed", if every function raised.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
