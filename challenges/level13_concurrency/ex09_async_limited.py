"""
Challenge: Limit Async Concurrency
Level:     13 - Concurrency
Topics:    asyncio.Semaphore, asyncio.Queue, worker tasks, create_task
Source:    Classic "don't hammer the server" asyncio pattern

========================================================================
YOUR TASK
========================================================================
Write two async functions that run many async jobs, but never more
than a fixed number AT ONCE:

- `run_limited(funcs, limit)` runs the jobs in `funcs` with at most
  `limit` of them running at the same time, using a Semaphore.
- `async_worker_pool(items, worker, num_workers)` calls
  `worker(item)` for every item, using `num_workers` worker tasks
  that take items from a Queue.

Both return the results in the SAME ORDER as their input.

    asyncio.run(run_limited([job_a, job_b, job_c, job_d], 2))
    # -> [result_a, result_b, result_c, result_d]
    #    with never more than 2 jobs running at once

========================================================================
BACKGROUND: WHY LIMIT, AND TWO WAYS TO DO IT
========================================================================
With asyncio it is easy to start 10_000 jobs at once with
asyncio.gather. That is often a BAD idea. A web server may only
accept a few requests at a time from you (a "rate limit") and start
refusing the rest. Your computer may run out of open connections or
files. So you limit concurrency (how many jobs run at the same time).

Way 1: a Semaphore ("N permits").
A Semaphore is a counter of permits. `asyncio.Semaphore(3)` starts
with 3. A job takes a permit before it starts and gives it back when
it ends. When no permits are left, the next job WAITS at that line
until someone gives one back:

    semaphore = asyncio.Semaphore(3)

    async def run_one(func):
        async with semaphore:    # take a permit (wait if none left)
            return await func()  # the permit is given back after this,
                                 # even if func() raises

You still start ALL the jobs with gather, but only 3 at a time get
past the `async with` line. Six jobs that take 0.1 s each, limit 3:

    time  0.0 s     0.1 s     0.2 s
          [job 0   ][job 3   ]
          [job 1   ][job 4   ]
          [job 2   ][job 5   ]         about 0.2 s in total

Way 2: a worker pool (the asyncio version of a producer/consumer
queue). Put all the items in an `asyncio.Queue`, then start exactly N
worker tasks. Each worker loops: take an item from the queue,
process it, repeat. Only N workers exist, so at most N items are
processed at once.

    queue: [item0, item1, item2, item3, ...]
             |       |
          worker A  worker B      each takes the next item when free

`asyncio.create_task(coro)` starts a coroutine running in the
background as a "task" and gives you a handle to it, which you can
later `await` (or pass to asyncio.gather) to wait for it to finish.

Which design fits when?
- Semaphore: you already have a list of separate jobs. It's the
  shortest code.
- Worker pool: you have a stream of items that all need the SAME
  processing, items may keep arriving while workers run, or each
  worker needs its own setup (like one connection per worker).

A warning about WHERE to create the Semaphore and the Queue. They
remember the event loop (asyncio's scheduler) that first waits on
them. Every `asyncio.run(...)` starts a NEW loop. So if you create one
at the top of the module, the second `asyncio.run` that uses it can
fail with "RuntimeError: ... is bound to a different event loop".
Always create them INSIDE your async function.

========================================================================
THE RULES
========================================================================
Your functions must:
1. Both be `async def` functions. The caller runs them with
   `asyncio.run(...)` or `await`.
2. `run_limited(funcs, limit)`: raise ValueError if `limit` is less
   than 1.
3. Call each function in `funcs` to make its coroutine, and run them
   so that at most `limit` run at the same time. Use an
   `asyncio.Semaphore(limit)` created INSIDE `run_limited`.
4. Return the results as a list in the same order as `funcs`. When
   `funcs` is empty, return [].
5. If a job raises an exception, let it propagate (pass through to
   the caller).
6. `async_worker_pool(items, worker, num_workers)`: raise ValueError
   if `num_workers` is less than 1. When `items` is empty, return [].
7. Use an `asyncio.Queue` and exactly `num_workers` worker tasks
   started with `asyncio.create_task`. Each worker takes items from
   the queue and awaits `worker(item)`.
8. So at most `num_workers` calls of `worker` run at the same time.
9. Return the results as a list in the same order as `items`.
10. Make sure every worker task has finished before you return.
11. Don't use threads or `time.sleep`.

You can assume:
- Every item in `funcs` is an async function that takes no arguments.
- `worker` is an async function that takes one argument and never
  raises (handling that is a stretch goal).
- `items` may contain any values, including None.

========================================================================
EXAMPLES
========================================================================
Each example uses this helper, which makes a "job" that waits
`delay` seconds and then returns `value`:

    def make_job(value, delay):
        async def job():
            await asyncio.sleep(delay)
            return value
        return job

    asyncio.run(run_limited([make_job(i, 0.1) for i in range(6)], 3))
        -> [0, 1, 2, 3, 4, 5]   after about 0.2 s
        Two "rounds" of 3 jobs, as in the picture above.

    asyncio.run(run_limited([make_job("a", 0.15), make_job("b", 0.0),
                             make_job("c", 0.05)], 2))
        -> ['a', 'b', 'c']
        They finish in the order b, c, a, but results keep the order
        of funcs.

    asyncio.run(run_limited([], 3))   ->  []
    asyncio.run(run_limited([], 0))   ->  raises ValueError

    async def double(x):
        await asyncio.sleep(0.1)
        return x * 2

    asyncio.run(async_worker_pool([1, 2, 3, 4, 5, 6], double, 3))
        -> [2, 4, 6, 8, 10, 12]   after about 0.2 s

    asyncio.run(async_worker_pool([1, 2], double, 5))
        -> [2, 4]
        More workers than items is fine. The extra workers just stop.

    asyncio.run(async_worker_pool([1], double, 0))
        -> raises ValueError

========================================================================
EDGE CASES TO TEST
========================================================================
- The limit holds: track how many jobs are running (see the tips)
  and check that the maximum seen is <= limit
- The limit is actually used: with 10 jobs and limit 3, the maximum
  seen == 3 (not just 1, which would mean no concurrency at all)
- Timing: 6 jobs of 0.1 s with limit 3 take about 0.2 s
  (assert elapsed < 0.35)
- Order: jobs that finish out of order still come back in input order
- limit bigger than the number of jobs: 3 jobs, limit 10 -> all 3
  run at once (max seen == 3)
- limit=0 -> ValueError. Empty funcs -> []
- The same tests for async_worker_pool: max seen <= num_workers
  (== num_workers with enough items), timing, order
- async_worker_pool with more workers than items -> still correct
- async_worker_pool with falsy items, e.g. [None, 0, "", False]
  -> the worker is called for every one of them
- num_workers=0 -> ValueError. Empty items -> []

Testing tips:
- Write plain `def test_...():` functions and call
  `asyncio.run(...)` inside them. You don't need any pytest plugin.
- To measure "how many at once", let every job update a shared
  counter. asyncio runs in a single thread and only switches jobs at
  an `await`, so you don't need a lock for this. (With THREADS you
  would need a threading.Lock around the updates.)

      def test_limit_is_respected():
          running = 0
          max_running = 0

          def make_tracked_job(value):
              async def job():
                  nonlocal running, max_running
                  running += 1
                  max_running = max(max_running, running)
                  try:
                      await asyncio.sleep(0.05)
                      return value
                  finally:
                      running -= 1
              return job

          funcs = [make_tracked_job(i) for i in range(10)]
          assert asyncio.run(run_limited(funcs, 3)) == list(range(10))
          assert max_running == 3

  `nonlocal` only works because `running` and `max_running` live
  inside the test function. A small class with two attributes works
  too.
- Measure time with `time.perf_counter()` and assert with a generous
  margin, like `< 0.35` for something that should take 0.2 s.
- `@pytest.mark.timeout(10)` (from pytest-timeout) makes a test fail
  instead of hanging forever, for example if a worker never stops.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. run_limited: write a small inner async function `run_one(func)`
   that does `async with semaphore:` and returns `await func()`.
   Then gather `run_one(f)` for every f in funcs.
2. gather returns results in argument order, so the order rule comes
   for free in run_limited.
3. async_worker_pool: these hints stop the workers with sentinels (a
   special stand-in value that means "no more work"). Make one with
   `STOP = object()`. It is different from every other value, even
   None, so it can never be mistaken for a real item.
4. Put `(index, item)` pairs on the queue with `queue.put_nowait(...)`
   (fine here because the queue has no size limit), then put one STOP
   per worker. Each worker loops: `job = await queue.get()`. If
   `job is STOP`, return. Otherwise unpack it and store
   `await worker(item)` in `results[index]`.
5. Make `results = [None] * len(items)` before starting the workers.
   Every worker writes only to its own index, so the order comes out
   right whichever worker finishes first.
6. Start the workers with
   `tasks = [asyncio.create_task(work()) for _ in range(num_workers)]`
   and wait for all of them with `await asyncio.gather(*tasks)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `asyncio.Semaphore` and `async with`
- `asyncio.Queue`: `put_nowait`, `await get()`
- `asyncio.create_task` and tasks running in the background
- Sentinel values made with `object()`
- Why asyncio objects should be created inside the running loop
- Choosing between a semaphore and a worker pool

========================================================================
STRETCH GOALS
========================================================================
- Stop the workers a different way: instead of sentinels, call
  `queue.task_done()` after each item, `await queue.join()` (it waits
  until every item is done), then `task.cancel()` each worker.
- Handle a `worker` that raises: collect the exception and re-raise
  it after all the workers have stopped.
- Use a bounded queue, `asyncio.Queue(maxsize=2)`, with a separate
  producer task that does `await queue.put(...)`. The producer now
  waits whenever the workers fall behind.
- On Python 3.11+, rewrite async_worker_pool with
  `asyncio.TaskGroup`.
"""

from collections.abc import Awaitable, Callable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


async def run_limited(funcs: list[Callable[[], Awaitable[R]]], limit: int) -> list[R]:
    """Run the jobs with at most `limit` running at the same time.

    Args:
        funcs: Async functions that take no arguments. Each is called once.
        limit: The most jobs allowed to run at once. Must be >= 1.

    Returns:
        A list of results, in the same order as `funcs` ([] if empty).

    Raises:
        ValueError: If limit < 1.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


async def async_worker_pool(
    items: list[T], worker: Callable[[T], Awaitable[R]], num_workers: int
) -> list[R]:
    """Process every item with `num_workers` worker tasks sharing a Queue.

    Args:
        items: The items to process. Not modified.
        worker: An async function called once per item.
        num_workers: How many worker tasks to start. Must be >= 1.

    Returns:
        A list of worker(item) results, in the same order as `items`
        ([] if `items` is empty).

    Raises:
        ValueError: If num_workers < 1.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
