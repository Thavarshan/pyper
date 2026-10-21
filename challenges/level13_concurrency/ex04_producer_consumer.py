"""
Challenge: Producer / Consumer
Level:     13 - Concurrency
Topics:    queue.Queue, worker threads, sentinel values, producer/consumer
Source:    Classic concurrency pattern (see the example in the `queue` docs)

========================================================================
YOUR TASK
========================================================================
Write `process_with_workers(items, worker, num_workers=4)`. It calls
`worker(item)` on every item, using a fixed team of `num_workers`
threads that share one queue of jobs. It RETURNS the results in the
same order as `items`.

    process_with_workers([1, 2, 3, 4], lambda x: x * 10, num_workers=2)
        ->  [10, 20, 30, 40]

========================================================================
BACKGROUND: WORKER THREADS AND A QUEUE
========================================================================
A THREAD is a separate line of work that runs alongside the rest of
your program. While one thread waits (for a web page, a file, or
`time.sleep`), the others carry on. That's how 8 jobs that each wait
0.2 seconds can finish in 0.4 seconds instead of 1.6.

One thread per item is fine for 5 items, but not for 10_000. The usual
answer is a fixed team of WORKER threads that share a to-do list:

    PRODUCER  --put-->  [ job | job | job | ... ]  --get-->  worker 1
    (your function)          the queue             --get-->  worker 2
                                                   --get-->  worker 3

The side that adds jobs is the PRODUCER. The workers that take jobs off
the queue and do them are the CONSUMERS. That's the whole
"producer/consumer" pattern.

`queue.Queue` is the to-do list. It is THREAD-SAFE: many threads can
put and get at the same moment without breaking it. (It has a lock
inside, so you don't need one of your own.)

    import queue
    q = queue.Queue()
    q.put("a")        # add to the back
    q.put("b")
    q.get()           # -> 'a'   take from the front (oldest first)
    q.get()           # -> 'b'
    q.get()           # BLOCKS: waits right here until something is put

That last line matters most. `get()` on an empty queue BLOCKS (waits,
doing nothing) until an item arrives. It doesn't return None and it
doesn't raise. So how does a worker know when to go home?

STOPPING WORKERS WITH A SENTINEL

A sentinel (a special stand-in value, also called a "poison pill")
is a job that means "no more work, stop now". Make one with
`object()`: a brand-new object that is not equal to anything else, so
it can't be mistaken for a real job. Test for it with `is` ("is this
that exact object?").

After all the real jobs, put ONE sentinel PER WORKER. Each worker
stops after taking one, so every worker gets exactly one:

    STOP = object()
    the queue for 3 items and 2 workers:

        (0, 'a')  (1, 'b')  (2, 'c')  STOP  STOP

Each real job carries its index (its position in `items`), because the
workers finish in any order. The index tells a worker where in the
results list its answer belongs.

A TRAP: CHECKING empty() FIRST

This looks like a neater way to stop:

    while not q.empty():     # step 1: "good, one job is left"
        job = q.get()        # step 2: ...but another worker took it

Between step 1 and step 2, another thread can take the last job. Then
`get()` waits forever for a job that never comes, and your program
hangs. Checking something shared and then acting on it as two separate
steps is a classic RACE CONDITION (a bug that depends on the exact
timing of the threads). The sentinel avoids it: a worker only ever
calls `get()`, which is one safe step.

========================================================================
THE RULES
========================================================================
Your function must:
1. Raise `ValueError` if `num_workers < 1`. Check this first, so it
   happens even when `items` is empty.
2. Return [] when `items` is empty.
3. Use a `queue.Queue`. Put an `(index, item)` pair on it for every
   item, then one sentinel per worker. Make the sentinel with
   `object()`.
4. Start `num_workers` threads. Each one loops: `get()` a job, stop if
   it is the sentinel, otherwise call `worker(item)` and store the
   result at `index`.
5. Start ALL the threads first, then join (wait for) ALL of them.
6. Return a NEW list of results in the same order as `items`, one
   result per item.
7. Call `worker` exactly once per item. At most `num_workers` calls of
   `worker` run at the same time.
8. Leave no threads running: every worker thread has finished when the
   function returns.
9. Not change `items`.
10. Not use `concurrent.futures` (that's ex06), `asyncio` or
    `multiprocessing`.

You can assume:
- `items` is a list and `num_workers` is an int.
- `worker` never raises an exception. (Handling that is a stretch
  goal.)
- `worker` is safe to call from several threads at once.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    process_with_workers([1, 2, 3, 4], lambda x: x * 10, num_workers=2)
        ->  [10, 20, 30, 40]
        2 workers share 4 jobs. The results are in input order, even
        if the workers finish out of order.

    process_with_workers(["a", "bb", "ccc"], len)  ->  [1, 2, 3]
        The default is 4 workers. More workers than items is fine: once
        the jobs run out, each worker takes its sentinel and stops.

    process_with_workers([], len)                  ->  []

    process_with_workers([1, 2], len, num_workers=0)  ->  raises ValueError

And a timed one:

    import time

    def slow_double(x):
        time.sleep(0.2)
        return x * 2

    process_with_workers(list(range(8)), slow_double, num_workers=4)
        ->  [0, 2, 4, 6, 8, 10, 12, 14]
        It takes about 0.4 s: 4 jobs at a time, so 2 rounds of 0.2 s.
        One thread on its own would take 1.6 s.

========================================================================
EDGE CASES TO TEST
========================================================================
- Order is kept even when the FIRST item finishes LAST. With a worker
  that sleeps `x * 0.05` seconds and returns x:
  process_with_workers([3, 2, 1], that_worker, num_workers=3)
  -> [3, 2, 1]
- It runs in parallel: the 8 x 0.2 s example above takes less than
  0.8 s. Time it with `time.perf_counter()` and use a generous margin.
  Never assert an exact time.
- The limit holds: it can't be faster than 2 rounds, so the same
  example takes at least 0.35 s.
- At most `num_workers` at once. Make the worker count how many calls
  are running right now (a shared counter changed under a
  `threading.Lock`) and record the highest value seen. 12 items that
  each sleep 0.05 s with num_workers=3 -> the highest is 3.
- num_workers=1: `worker` is called in input order (record the calls
  in a list: it equals `items`).
- More workers than items: 3 items, num_workers=10 -> correct results.
- Every item is processed exactly once: 50 items -> the recorded calls,
  sorted, equal `items`. (`list.append` is safe to call from several
  threads, but `count += 1` is NOT.)
- No threads left over: take `set(threading.enumerate())` before the
  call. Afterwards, no thread outside that set is still in
  `threading.enumerate()`.
- Empty list -> []
- num_workers = 0 or -1 -> raises ValueError (also with an empty list)
- `items` is unchanged after the call
- Add `@pytest.mark.timeout(10)` above your tests (pytest-timeout is
  installed). If a worker never gets its sentinel, the test then fails
  instead of freezing pytest forever.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Set up three things first: `results = [None] * len(items)`,
   `q = queue.Queue()` and `STOP = object()`.
2. `for pair in enumerate(items): q.put(pair)` puts every
   (index, item) pair. Then put `STOP` once per worker.
3. Write the worker loop as an inner function. It is a closure (an
   inner function that can use the outer function's variables), so it
   can see q, STOP, results and worker:

       def run():
           while True:
               job = q.get()
               if job is STOP:
                   return
               index, item = job
               ...

4. Make the threads with `threading.Thread(target=run)` (pass `run`
   itself, no parentheses). Keep them in a list. Start them all in one
   loop, then join them all in a SECOND loop. If you start and join in
   the same loop, the first worker does every job on its own while the
   others haven't even started.
5. Several threads writing into `results` is safe here. Each index is
   written by exactly one thread, and nobody reads the list until
   every thread has been joined.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `threading.Thread(target=...)`, `.start()` and `.join()`
- `queue.Queue`: `put()`, and `get()` blocking until there's an item
- Sentinel objects made with `object()`, and the `is` operator
- `enumerate()` to get (index, item) pairs
- Closures (inner functions that use the outer function's variables)
- Race conditions, and why "check, then act" is dangerous with threads

========================================================================
STRETCH GOALS
========================================================================
- Use a bounded queue, `queue.Queue(maxsize=2)`: `put()` then blocks
  while the queue is full. Run the producer in its own thread, so it
  feeds jobs while the workers run. This is how you'd handle a huge or
  endless stream of items without holding them all in memory.
- Look up `q.task_done()` and `q.join()`. They let the producer wait
  until every job is DONE (not just taken), without joining threads.
- Handle a `worker` that raises. Right now the exception kills that
  one worker thread: Python prints a traceback, the caller never sees
  the error, and that item's result stays None. Catch it inside the
  thread, keep going, and re-raise the error for the earliest item
  after all the threads are joined.
- Compare your code with ex06's `ThreadPoolExecutor`, which does all
  of this for you.
"""

from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")
R = TypeVar("R")


def process_with_workers(items: list[T], worker: Callable[[T], R], num_workers: int = 4) -> list[R]:
    """Call `worker` on every item using a pool of threads fed by a queue.

    Args:
        items: The items to process. Not modified.
        worker: A one-argument function to call on each item.
        num_workers: How many worker threads to start. Must be >= 1.

    Returns:
        A new list with worker(item) for every item, in input order.

    Raises:
        ValueError: If num_workers < 1.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
