"""
Challenge: Gather and Time Out
Level:     13 - Concurrency
Topics:    async/await, the event loop, asyncio.gather, asyncio.wait_for
Source:    Classic asyncio exercise

========================================================================
YOUR TASK
========================================================================
Write two async functions:

- `gather_in_order(funcs)` runs several async jobs AT THE SAME TIME and
  returns their results as a list, in the same order as `funcs`.
- `with_timeout(func, seconds, default)` runs one async job, but gives
  up after `seconds`. It returns the job's result if it finished in
  time, otherwise it cancels the job and returns `default`.

    async def fetch_one():
        await asyncio.sleep(0.2)     # pretend to wait for a web page
        return 1

    asyncio.run(gather_in_order([fetch_one, fetch_one, fetch_one]))
    # -> [1, 1, 1], after about 0.2 seconds in total (not 0.6)

========================================================================
BACKGROUND: ASYNC AND AWAIT
========================================================================
asyncio lets ONE thread juggle many jobs that spend most of their time
waiting (for the network, a database, a timer). It is the same idea
as threads for I/O-bound work, without the threads.

An "async function" is defined with `async def`. Calling it does NOT
run it. It just creates a coroutine object: a paused job, ready to go.

    async def hello():
        print("hi")
        return 42

    c = hello()     # prints NOTHING. c is a coroutine object.

Something has to run it. `asyncio.run(c)` starts an "event loop" (the
scheduler that runs coroutines), runs `c` until it finishes, and gives
back its result: here it prints "hi" and returns 42. Inside another
async function you write `await c` instead, which means "run this and
wait for its result".

The important part is that every `await` is a place where a coroutine
may PAUSE and let the event loop run a different one. Jobs take turns
at each `await`. That is how one thread does many things "at once":

    job A: start ... await asyncio.sleep(1) .................. done
    job B:   start ... await asyncio.sleep(1) ................ done
    job C:     start ... await asyncio.sleep(1) .............. done
           |<----------- about 1 second in total ----------->|

While A is sleeping, the loop runs B, then C. All three sleeps overlap.

The flip side: a coroutine only lets others run when it awaits. If it
calls the ordinary `time.sleep(1)`, it holds on to the only thread and
the WHOLE loop freezes for a second. Inside async code always use
`await asyncio.sleep(...)`, never `time.sleep(...)`.

Two tools from asyncio do the work in this challenge:

- `await asyncio.gather(c1, c2, c3)` runs the coroutines at the same
  time and returns a list of their results, in the order you passed
  them (NOT the order they finished in).
- `await asyncio.wait_for(c, timeout=2.0)` runs `c`, but if it isn't
  done after 2 seconds, it CANCELS it and raises
  `asyncio.TimeoutError`. Cancelling means asyncio throws
  `asyncio.CancelledError` into the coroutine at the `await` where it
  is paused, so it stops there (its `finally:` blocks still run).
  (On Python 3.11+ `asyncio.TimeoutError` is just another name for the
  built-in `TimeoutError`. Catching `asyncio.TimeoutError` works on
  every version.)

Why do the functions take `funcs` (async functions with no arguments)
instead of ready-made coroutines? Because a coroutine object can be
awaited only ONCE, and creating one you never await gives a
"coroutine ... was never awaited" warning. Taking a function lets
YOUR code decide when, and whether, to create the coroutine, by
calling func(). Such a function that builds the thing you need is
called a "factory".

========================================================================
THE RULES
========================================================================
Your functions must:
1. Both be `async def` functions. The caller runs them with
   `asyncio.run(...)` or `await`.
2. `gather_in_order(funcs)`: call each function in `funcs` to get its
   coroutine, run all of them at the same time with `asyncio.gather`,
   and return their results as a list, in the same order as `funcs`.
3. If any job raises an exception, let it propagate (pass through to
   the caller). With several failures, the first one to happen is the
   one the caller sees.
4. When `funcs` is empty, return [].
5. `with_timeout(func, seconds, default)`: raise ValueError if
   `seconds` is negative. 0 is allowed.
6. Otherwise run func() with `asyncio.wait_for`. If it finishes within
   `seconds`, return its result.
7. If it takes longer, make sure it is cancelled (wait_for does this
   for you), catch `asyncio.TimeoutError` and return `default`.
8. Let any other exception from func() propagate.
9. Don't use `time.sleep` anywhere, and don't use threads.

You can assume:
- Every item in `funcs`, and `func`, is an async function that takes
  no arguments.

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

    asyncio.run(gather_in_order([make_job(i, 0.2) for i in range(5)]))
        -> [0, 1, 2, 3, 4]   after about 0.2 s, not 1.0 s
        All five sleeps happen at the same time.

    asyncio.run(gather_in_order([make_job("slow", 0.3),
                                 make_job("fast", 0.0)]))
        -> ['slow', 'fast']
        "fast" finishes first, but results follow the order of funcs.

    asyncio.run(gather_in_order([]))
        -> []

    asyncio.run(with_timeout(make_job("ok", 0.05), 1.0, "late"))
        -> 'ok'      it finished in time

    asyncio.run(with_timeout(make_job("ok", 5), 0.1, "late"))
        -> 'late'    after about 0.1 s: the job was cancelled

    asyncio.run(with_timeout(make_job("ok", 0), -1, "late"))
        -> raises ValueError

========================================================================
EDGE CASES TO TEST
========================================================================
- Timing: 5 jobs that each sleep 0.2 s finish in well under 1.0 s
  (assert elapsed < 0.6)
- Order: jobs that finish in a different order still come back in
  the order of `funcs`, e.g. delays 0.3, 0.0, 0.1 -> results in that
  same order
- Exception: a job that raises KeyError makes gather_in_order raise
  KeyError
- Empty list -> []
- with_timeout returns the job's result when it is fast enough
- with_timeout returns `default` for a slow job, and returns soon
  (elapsed < 1.0 for a 5 s job with seconds=0.1)
- The slow job really is cancelled: it sees asyncio.CancelledError
  (see the tips below)
- with_timeout with a negative `seconds` -> ValueError
- An exception raised inside func() passes through with_timeout

Testing tips:
- Write plain `def test_...():` functions and call
  `asyncio.run(...)` inside them. You don't need any pytest plugin.
- Measure time with `time.perf_counter()` before and after, and
  assert with a generous margin (`< 0.6`, never `== 0.2`). Computers
  are sometimes slow for a moment, so exact timings make flaky tests
  (tests that sometimes pass and sometimes fail).
- To prove cancellation, let the slow job record what happened in a
  list that the test can check afterwards:

      events = []

      async def slow():
          try:
              await asyncio.sleep(5)
          except asyncio.CancelledError:
              events.append("cancelled")
              raise                       # always re-raise it!

      assert asyncio.run(with_timeout(slow, 0.1, None)) is None
      assert events == ["cancelled"]

- `@pytest.mark.timeout(10)` (from pytest-timeout) makes a test fail
  instead of hanging forever if something gets stuck.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. You make the coroutines with a list comprehension:
   `[func() for func in funcs]`. Nothing runs yet at this point.
2. `asyncio.gather` takes the coroutines as separate arguments, not
   as one list. Unpack the list with a star: `gather(*coros)`.
3. gather already returns the results in argument order. Wrap the
   result in `list(...)` to be sure you return a real list.
4. In with_timeout, check `seconds` BEFORE you call func(). Otherwise
   you create a coroutine that never gets awaited, and Python warns
   about it.
5. The shape of with_timeout:

       try:
           return await asyncio.wait_for(func(), timeout=seconds)
       except asyncio.TimeoutError:
           return default

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `async def`, `await` and coroutine objects
- The event loop and `asyncio.run`
- Cooperative multitasking: jobs only switch at an `await`
- Why `time.sleep` blocks the loop and `asyncio.sleep` doesn't
- `asyncio.gather`, `asyncio.wait_for`, cancellation and
  `asyncio.CancelledError`
- Unpacking a list into arguments with `*`

========================================================================
STRETCH GOALS
========================================================================
- Try `asyncio.gather(..., return_exceptions=True)`. Failed jobs then
  show up as exception objects in the result list instead of being
  raised.
- Put `time.sleep(0.2)` inside the jobs instead of `asyncio.sleep`
  and time gather_in_order again. Five jobs now take about 1 s: the
  loop was frozen.
- On Python 3.11+, rewrite with_timeout with `async with
  asyncio.timeout(seconds):`, and gather_in_order with
  `asyncio.TaskGroup`.
- Use `asyncio.create_task` to start a job, do something else, then
  `await` the task later.
"""

from collections.abc import Awaitable, Callable
from typing import TypeVar

R = TypeVar("R")


async def gather_in_order(funcs: list[Callable[[], Awaitable[R]]]) -> list[R]:
    """Run every job at the same time and return the results in order.

    Args:
        funcs: Async functions that take no arguments. Each is called once
            to create its coroutine.

    Returns:
        A list of results, in the same order as `funcs` ([] if empty).

    Raises:
        Exception: Whatever exception a job raises is propagated.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


async def with_timeout(
    func: Callable[[], Awaitable[R]], seconds: float, default: R
) -> R:
    """Run func(), giving up after `seconds`.

    Args:
        func: An async function that takes no arguments.
        seconds: How long to wait, in seconds. 0 is allowed.
        default: What to return if func() takes too long.

    Returns:
        func()'s result if it finished in time, otherwise `default` (the
        slow job is cancelled).

    Raises:
        ValueError: If seconds < 0.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
