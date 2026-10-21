"""
Challenge: Count Primes in Parallel
Level:     13 - Concurrency
Topics:    CPU-bound work, the GIL, processes, ProcessPoolExecutor
Source:    Classic "split the work into chunks" exercise

========================================================================
YOUR TASK
========================================================================
Write two functions:

- `count_primes(start, stop)` counts the prime numbers n with
  start <= n < stop, the ordinary way, one number at a time.
- `count_primes_parallel(limit, workers=4)` counts the primes below
  `limit` by splitting the numbers into `workers` chunks and counting
  each chunk in a SEPARATE PROCESS at the same time, then adding up
  the counts.

    count_primes(0, 10)            ->  4      (2, 3, 5 and 7)
    count_primes_parallel(100, 4)  ->  25

========================================================================
BACKGROUND: WHY PROCESSES AND NOT THREADS?
========================================================================
Some programs are slow because they WAIT (for a web page, a file, a
database). That is called I/O-bound work, and threads help with it:
while one thread waits, another can run.

Counting primes is different. The computer never waits, it just
calculates. That is called CPU-bound work. For CPU-bound Python code,
threads do NOT make it faster, because of the GIL.

The GIL (Global Interpreter Lock) is a lock inside the normal Python
interpreter. Only the thread holding it can run Python code. So even
on a computer with 8 cores, 4 threads doing maths take turns, and
only ONE of them runs at any moment:

    threads:    [T1][T2][T3][T4][T1][T2]...   one at a time, in turns
    processes:  P1 [==========]               every process has its
                P2 [==========]               own interpreter and its
                P3 [==========]               own GIL, so they really
                P4 [==========]               run at the same time

(Python 3.13 has an optional "free-threaded" build with no GIL. With
it, threads can speed up CPU work too. The normal build still has the
GIL.)

A process is a whole separate running Python program. The
`concurrent.futures` module gives you a pool of them:

    from concurrent.futures import ProcessPoolExecutor

    with ProcessPoolExecutor(max_workers=4) as executor:
        future = executor.submit(count_primes, 0, 500)   # starts work
        future.result()                                  # -> 95

`submit(func, arg1, arg2)` sends one job to a free worker process and
gives you back a "future": a ticket you can exchange for the answer
later with `.result()`. `executor.map(func, list1, list2)` is a
shortcut that calls func(list1[0], list2[0]), func(list1[1],
list2[1]), ... and gives the results back in order.

Processes come with some rules that threads don't have:

- They don't share memory. Each process has its own copy of
  everything. The arguments you send and the results you get back are
  copied between processes by "pickling" them (turning them into bytes
  and back again).
- So the function you send must be picklable. Python pickles a
  function by its NAME, and the worker process looks that name up
  again. This only works for a function defined at the TOP LEVEL of a
  module (not inside another function), and never for a lambda.
  Sending one gives an error like "Can't pickle <function <lambda>
  ...>" or "Can't pickle local object ...".
- Starting processes and copying data to them takes time. For a
  small job, the parallel version is SLOWER than the plain one. It
  only pays off when each chunk has plenty of work.
- On Windows and macOS (and on Linux from Python 3.14), each worker
  process starts by IMPORTING your main script again. If you run this
  file as a script, put the code that creates the pool under

      if __name__ == "__main__":
          print(count_primes_parallel(1_000_000))

  so that importing it doesn't start another pool. Without the guard
  you get a RuntimeError. Tests run through pytest, and code that is
  only imported, don't need it.

========================================================================
THE RULES
========================================================================
Your functions must:
1. `count_primes(start, stop)`: return how many primes n there are
   with start <= n < stop (`stop` itself is NOT included).
2. Decide whether n is prime by trial division: try dividing n by
   2, 3, 4, ... up to the square root of n. If none of them divides
   it evenly, n is prime.
3. Treat numbers below 2 (0, 1 and negatives) as not prime.
4. When start >= stop, return 0.
5. `count_primes_parallel(limit, workers=4)`: return how many primes
   are below `limit` (0 <= n < limit).
6. Raise ValueError if `limit` is negative or `workers` is less than 1.
7. Split range(0, limit) into exactly `workers` back-to-back chunks.
   Together they must cover every number EXACTLY ONCE: no gaps, no
   overlaps. Some chunks may be empty when there are more workers than
   numbers.
8. Count every chunk in a worker process using
   `ProcessPoolExecutor(max_workers=workers)`, inside a `with` block.
   Send it `count_primes` itself (not a lambda or a nested function).
9. Add up the chunk counts and return the total.

You can assume:
- All arguments are ints.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    count_primes(0, 10)    ->  4
        The primes below 10 are 2, 3, 5 and 7.

    count_primes(10, 20)   ->  4
        11, 13, 17 and 19.

    count_primes(-5, 3)    ->  1
        Only 2. Negative numbers, 0 and 1 are not prime.

    count_primes(10, 3)    ->  0
        start >= stop, so there is nothing to count.

    count_primes_parallel(1_000, 4)  ->  168
        Chunks [0, 250), [250, 500), [500, 750), [750, 1000).
        Their counts are 53, 42, 37 and 36, and 53 + 42 + 37 + 36 = 168.

    count_primes_parallel(5, workers=8)  ->  2
        More workers than numbers: most chunks are empty, which is
        fine. The primes below 5 are 2 and 3.

    count_primes_parallel(-1)  ->  raises ValueError

========================================================================
EDGE CASES TO TEST
========================================================================
- Known counts with count_primes_parallel:
  below 10 -> 4, below 100 -> 25, below 1_000 -> 168,
  below 100_000 -> 9_592
- workers=1 gives the same answer: count_primes_parallel(1_000, 1)
  -> 168
- More workers than numbers: count_primes_parallel(5, workers=8) -> 2
- Tiny limits: limit 0, 1 and 2 -> 0, limit 3 -> 1
- The parallel answer matches the plain one for many limits and
  worker counts, e.g. count_primes_parallel(97, 7) ==
  count_primes(0, 97)
- count_primes with start >= stop -> 0
- count_primes with a range that starts below 2: (-5, 3) -> 1
- Squares of primes are not prime: count_primes(25, 26) -> 0,
  count_primes(49, 50) -> 0 (checks that you divide up to AND
  including the square root)
- limit=-1 -> ValueError, workers=0 -> ValueError

Testing tips:
- Your test file imports count_primes from this module, so the
  worker processes can find it by name. Tests work as normal.
- Don't assert that the parallel version is faster. Timing depends
  on the machine and on how many cores it has, so such a test is
  flaky (sometimes passes, sometimes fails). Compare answers instead.
- A test that starts processes can take a while. Optionally guard it
  with `@pytest.mark.timeout(30)` (from pytest-timeout) so that it
  fails instead of hanging forever if something goes wrong.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Write and test count_primes first, without any processes. Get it
   right on its own before you go parallel.
2. For the square root test, `d * d <= n` avoids floats completely.
   Or use `math.isqrt(n)`, which gives the whole-number square root.
3. Chunk boundaries for the parallel version:

       bounds = [limit * i // workers for i in range(workers + 1)]

   For limit=10, workers=3 this gives [0, 3, 6, 10], so the chunks are
   [0, 3), [3, 6) and [6, 10). Chunk i runs from bounds[i] up to (not
   including) bounds[i + 1]. Each chunk's stop is the next chunk's
   start, so nothing is counted twice and nothing is skipped.
4. `executor.map(count_primes, starts, stops)` with
   starts = bounds[:-1] and stops = bounds[1:] calls count_primes once
   per chunk. Wrap it in sum(...). Do it INSIDE the `with` block.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- CPU-bound vs I/O-bound work
- The GIL, and why threads don't speed up CPU-heavy Python code
- `concurrent.futures.ProcessPoolExecutor`, `submit`, `map` and
  futures
- Pickling: how data and functions travel between processes
- `if __name__ == "__main__":` and why worker processes need it
- `math.isqrt` and integer division `//`

========================================================================
STRETCH GOALS
========================================================================
- Time it. Use time.perf_counter() to compare count_primes(0, limit)
  with count_primes_parallel(limit) for a big limit like 1_000_000,
  then for a small one like 1_000. Where does parallel start to win?
- Swap ProcessPoolExecutor for ThreadPoolExecutor and time it again.
  You should see no speed-up (unless you run the free-threaded 3.13
  build).
- The chunks are the same SIZE but not the same amount of WORK: big
  numbers take longer to test. Try splitting into many more chunks
  than workers (say 4 * workers) and see if it finishes sooner.
- Rewrite it with `multiprocessing.Pool` and its `starmap` method.
"""

def count_primes(start: int, stop: int) -> int:
    """Count the primes n with start <= n < stop, by trial division.

    Args:
        start: The first number to check (included). May be below 2.
        stop: Where to stop (NOT included).

    Returns:
        How many primes lie in [start, stop). 0 if start >= stop.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def count_primes_parallel(limit: int, workers: int = 4) -> int:
    """Count the primes below `limit` using several worker processes.

    Splits range(0, limit) into `workers` back-to-back chunks, counts each
    chunk with count_primes in a ProcessPoolExecutor, and adds the counts.

    Args:
        limit: Count the primes n with 0 <= n < limit.
        workers: How many chunks and worker processes to use.

    Returns:
        The number of primes below `limit`.

    Raises:
        ValueError: If limit < 0 or workers < 1.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
