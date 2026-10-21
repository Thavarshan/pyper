"""Level 13 - Concurrency.

Goal: make a program do several things at once, safely. You will start
and stop threads, protect shared data with locks, avoid deadlocks, pass
work between threads with queues, use thread and process pools, and
write async code with asyncio.

Concurrency vs parallelism
    CONCURRENCY means several tasks are in progress at the same time,
    taking turns. PARALLELISM means they are literally running at the
    same instant, on different CPU cores. A cook juggling three pans is
    concurrent. Three cooks each with one pan are parallel.

Why bother?
    Most programs spend a lot of time WAITING: for a web page, a file or
    a database. While one task waits, another can run. That is the big
    win for "I/O-bound" work (I/O = input/output, meaning network, disk
    and the like). In these challenges `time.sleep()` or
    `asyncio.sleep()` stands in for that waiting.

    "CPU-bound" work, such as heavy maths, never waits. It only gets
    faster if it runs on several CPU cores at once.

Threads
    A THREAD is a separate line of execution inside your program. All
    threads share the same memory, so they can all see the same lists,
    dicts and objects. That is convenient, and it's also the danger.

        import threading
        t = threading.Thread(target=some_function, args=(1, 2))
        t.start()     # begins running some_function(1, 2) in the background
        t.join()      # waits here until it has finished

The GIL (Global Interpreter Lock)
    The standard Python interpreter (CPython) lets only ONE thread run
    Python code at any instant. Threads still help with I/O-bound work,
    because a thread that is waiting gives up the GIL so another can run.
    They do NOT speed up CPU-bound work. For that, use separate PROCESSES
    (challenge 07), each with its own interpreter and its own GIL.
    Python 3.13 added an optional "free-threaded" build without a GIL,
    but the normal build still has one.

Race conditions and locks
    When two threads change the same data at the same time, updates can
    get lost. That's a RACE CONDITION: the result depends on who wins
    the race. It may only go wrong once in a thousand runs, which makes
    it hard to find. A LOCK (`threading.Lock`) lets only one thread at a
    time into a block of code:

        with lock:
            balance += amount     # only one thread at a time in here

Deadlock
    Two threads each hold a lock the other one needs, so both wait
    forever. The usual cure is to always take locks in the same order.

Queues
    `queue.Queue` is a thread-safe line of waiting work. Producer
    threads put items in, and consumer (worker) threads take them out.
    No extra locks are needed.

Pools
    `concurrent.futures` gives you a ready-made POOL of worker threads
    (`ThreadPoolExecutor`) or processes (`ProcessPoolExecutor`). You hand
    it jobs, and it hands back FUTURES: placeholders for results that
    will be ready later.

asyncio
    A different style: ONE thread, with many tasks that politely take
    turns. A task runs until it reaches `await` (usually while waiting
    for I/O), and then another task gets a go. Functions are written
    with `async def`, and you start the whole thing with `asyncio.run()`.

Which one should I use?
    Waiting on I/O, a handful of tasks        -> threads or a thread pool
    Waiting on I/O, thousands of connections  -> asyncio
    Heavy computation (CPU-bound)             -> processes

Testing concurrent code
    - Prove things run at the same time with timing. For example, five
      0.2 s sleeps should finish in well under 1 s. Always leave a
      generous margin (assert `< 0.6`, never `== 0.2`), because computers
      are sometimes slow for reasons outside your control.
    - Never let a test hang forever. Join threads with a timeout
      (`t.join(timeout=5)`, then `assert not t.is_alive()`). pytest-timeout
      is installed, so a test can also carry `@pytest.mark.timeout(10)`.
      Every test also has a 60-second safety limit set in pyproject.toml.
    - A passing test doesn't prove there's no race. Bugs may appear only
      rarely. Run the test many times, and reason about your locks.
"""
