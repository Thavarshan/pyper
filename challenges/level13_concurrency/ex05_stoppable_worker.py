"""
Challenge: Stoppable Worker
Level:     13 - Concurrency
Topics:    threading.Event, daemon threads, join with a timeout, stopping
Source:    Common pattern for background jobs (heartbeats, polling)

========================================================================
YOUR TASK
========================================================================
Write a class `RepeatingWorker`. It runs a task over and over in a
background thread, every `interval` seconds, until you stop it. Write
these methods and properties:

    RepeatingWorker(task, interval)   set it up (nothing runs yet)
    start()                           start the background thread
    stop(timeout=None)                ask the thread to stop, then wait
                                      for it to end
    is_running                        True while the thread is alive
    runs                              how many times task() succeeded
    error                             the exception that stopped the
                                      worker, or None

    w = RepeatingWorker(lambda: print("tick"), interval=1.0)
    w.start()    # prints "tick" straight away, then once a second
    ...
    w.stop()     # returns at once, even in the middle of a wait

========================================================================
BACKGROUND: HOW TO STOP A THREAD
========================================================================
YOU CAN'T KILL A THREAD

Python has no `thread.kill()`. A thread ends only when the function it
runs returns. So stopping is COOPERATIVE: the main program raises a
"please stop" flag, and the thread checks the flag and returns by
itself.

threading.Event IS THAT FLAG

An Event is a thread-safe True/False flag that starts as False:

    import threading
    stop_event = threading.Event()
    stop_event.is_set()     # -> False
    stop_event.wait(5)      # waits 5 s, then -> False (timed out)
    stop_event.set()        # raise the flag (from any thread)
    stop_event.is_set()     # -> True
    stop_event.wait(5)      # -> True at once, because it is set

`wait(seconds)` waits until the flag is set OR the time runs out,
whichever comes first. It returns True if the flag is set. That makes
it a "sleep that can be woken up early". Compare this with
`time.sleep(60)`, which can't be interrupted: with sleep, stop() could
take up to a whole minute. With `wait(60)`, the thread wakes up the
moment stop() sets the flag:

    worker thread:  task() | wait(60) ...... woken! -> loop ends
    main thread:                     stop(): set() ^  then join()

join() AND join(timeout)

`t.join()` waits until thread `t` has ended. `t.join(timeout=2)` waits
at most 2 seconds and then returns anyway. It does NOT raise when time
runs out. Call `t.is_alive()` afterwards to find out whether the
thread really ended.

DAEMON THREADS

When your main program finishes, Python waits for every normal
thread to end before it exits. A forgotten worker that loops forever
would stop your program from EVER exiting. A daemon thread, made with
`threading.Thread(target=..., daemon=True)`, doesn't hold the program
open: Python just abandons it at exit. The catch: a daemon is cut off
in the middle of whatever it was doing, so don't use one for work that
must finish, such as saving a file.

TWO MORE THINGS ABOUT THREADS

- A thread can be started only ONCE. Calling `.start()` a second time
  on the same Thread raises `RuntimeError`. That's why a stopped
  RepeatingWorker can't be started again.
- An exception inside a thread never reaches the code that started
  it. The thread just ends, and Python prints a traceback. To report
  the error, catch it inside the thread and store it somewhere the
  main program can read (here, the `error` property).

========================================================================
THE RULES
========================================================================
Your class must:
1. `__init__`: raise `ValueError` if `interval <= 0`. Don't start
   anything yet.
2. `start()`: start ONE background thread with `daemon=True`.
3. Raise `RuntimeError` if `start()` is called a second time, even
   after `stop()`.
4. In the background thread, loop:
   a. call `task()`,
   b. add 1 to `runs`,
   c. wait `interval` seconds with `Event.wait(interval)`, so that
      `stop()` wakes it up at once. Never use `time.sleep`.
   d. If stop was asked for, end the thread. Otherwise go back to a.
   So the first run happens straight away, not after one interval.
5. If `task()` raises an exception: store it in `error`, don't count
   that run, and end the thread. The worker then counts as stopped.
6. `stop(timeout=None)`: set the stop flag and join the thread,
   passing `timeout` to `join()`. It returns None and doesn't raise
   when the timeout runs out. (The thread then ends by itself once the
   `task()` call it is in the middle of returns.)
7. Calling `stop()` before `start()` does nothing, and a later
   `start()` still works normally. Calling `stop()` again after a stop
   also does nothing.
8. `is_running` is True only between `start()` and the thread ending
   (because of `stop()` or an error). It is False before `start()`.
9. `runs` counts the `task()` calls that returned without raising. It
   is 0 before `start()`.
10. `error` is None, or the exception object that stopped the worker.

You can assume:
- `task` takes no arguments. Its return value is ignored.
- `interval` is an int or float, in seconds.
- Only one thread (your main code) calls start() and stop().

========================================================================
EXAMPLES
========================================================================
Each line runs one call. `# ->` shows the value you'd see.

    import time

    w = RepeatingWorker(lambda: None, interval=0.1)
    w.is_running     # -> False    nothing starts in __init__
    w.start()        # task runs now, then every 0.1 s
    w.is_running     # -> True
    time.sleep(0.35)
    w.stop()         # returns almost at once
    w.is_running     # -> False
    w.runs           # -> about 4  (at 0, 0.1, 0.2 and 0.3 s)
    w.start()        # -> raises RuntimeError (no restarting)

    slow = RepeatingWorker(lambda: None, interval=60)
    slow.start()
    slow.stop()      # returns in a moment, not after 60 s

    def broken():
        raise ValueError("boom")

    bad = RepeatingWorker(broken, interval=1)
    bad.start()
    # ...a moment later:
    bad.is_running   # -> False    the error ended the thread
    bad.error        # -> ValueError('boom')
    bad.runs         # -> 0        the failed run doesn't count

    RepeatingWorker(lambda: None, 0)   # -> raises ValueError

Threads are not exact clocks. In the first example, `runs` is
"about 4", so test it with a range such as `2 <= w.runs <= 6`.

========================================================================
EDGE CASES TO TEST
========================================================================
Things that happen "soon" in another thread need a little waiting
loop. Copy this helper into your test file:

    def wait_until(predicate, timeout=2.0):
        deadline = time.perf_counter() + timeout
        while time.perf_counter() < deadline:
            if predicate():
                return True
            time.sleep(0.01)
        return predicate()

- It runs straight away: interval=60, start(), then
  `wait_until(lambda: w.runs >= 1)` is True and `w.runs == 1`
- stop() is fast even with interval=60: it takes less than 0.5 s
  (time it with `time.perf_counter()`), and then is_running is False
- runs stops growing after stop: interval=0.01, wait until runs >= 3,
  stop(), save runs, sleep 0.1 s -> runs hasn't changed
- It really waits between runs: interval=0.1, let it run 0.35 s, stop
  -> 2 <= runs <= 6 (a loop that never waits would give thousands)
- start() twice -> raises RuntimeError
- start() after stop() -> raises RuntimeError
- stop() before start() -> no error, runs == 0, is_running is False,
  and a later start() still works (runs reaches 1)
- stop() twice -> no error
- A task that raises ValueError on its 3rd call ->
  `wait_until(lambda: not w.is_running)` is True, `w.error` is that
  exact exception object, and runs == 2
- interval 0 or -1 -> raises ValueError
- Nothing runs before start(): create a worker, sleep 0.1 s -> the
  task was never called and runs == 0
- It runs in a daemon background thread: inside the task, record
  `threading.current_thread().daemon` -> True
- Always call stop() at the end of a test (in a `try`/`finally`), so a
  worker can't keep running into the next test. Adding
  `@pytest.mark.timeout(10)` (pytest-timeout is installed) turns a
  hang into a failure.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. In __init__, store task and interval, plus
   `self._stop_event = threading.Event()`, `self._thread = None`,
   `self._runs = 0` and `self._error = None`.
2. You may add your own private helper method, for example
   `_loop(self)`, and run it with
   `threading.Thread(target=self._loop, daemon=True)`.
3. `self._thread is not None` tells you start() was already called.
   Use it in start() (raise) and in stop() (return early if it's None).
4. Because `wait()` returns True once the flag is set, the loop can be:

       while True:
           try:
               self._task()
           except Exception as exc:
               self._error = exc
               return
           self._runs += 1
           if self._stop_event.wait(self._interval):
               return

5. is_running: `self._thread is not None and self._thread.is_alive()`.
6. Only the worker thread changes `_runs` and `_error`, and the main
   thread only reads them. One writer and a few readers of a simple
   value is fine without a lock. Two threads both doing `+= 1` is not
   (see ex02).

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `threading.Event`: `set()`, `is_set()`, and `wait(timeout)` with its
  True/False return value
- Daemon threads, and what happens to threads when a program exits
- `Thread.is_alive()` and `Thread.join(timeout)`
- Cooperative stopping: why threads can't be killed from outside
- Catching exceptions inside a thread so they aren't lost
- `@property` for read-only attributes

========================================================================
STRETCH GOALS
========================================================================
- Measure the interval from the START of one run to the start of the
  next, so a slow task doesn't push every later run back. Use
  `time.monotonic()` (a clock that never jumps backwards) and wait
  only for the time that's left.
- Add `pause()` and `resume()` using a second Event.
- Read about `threading.Timer`. It runs a function once after a delay,
  can be cancelled, and is built on `Event.wait` just like yours.
- Instead of stopping on the first error, keep a list of errors and
  stop only after 3 failures in a row.
"""

from collections.abc import Callable


class RepeatingWorker:
    """Run a task repeatedly in a background thread until stopped."""

    def __init__(self, task: Callable[[], None], interval: float) -> None:
        """Set up the worker. Nothing runs until start() is called.

        Args:
            task: A no-argument function to call on every run.
            interval: Seconds to wait after each run. Must be > 0.

        Raises:
            ValueError: If interval <= 0.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def start(self) -> None:
        """Start the background daemon thread (the first run is immediate).

        Raises:
            RuntimeError: If start() has already been called, even if the
                worker has since been stopped.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def stop(self, timeout: float | None = None) -> None:
        """Ask the worker to stop, then wait for its thread to end.

        Does nothing if the worker was never started.

        Args:
            timeout: Most seconds to wait for the thread (passed to
                join()). None means wait as long as it takes.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @property
    def is_running(self) -> bool:
        """True between start() and the background thread ending.

        Returns:
            Whether the background thread is alive.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @property
    def runs(self) -> int:
        """How many times task() has completed without raising.

        Returns:
            The number of successful runs (0 before start()).
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @property
    def error(self) -> Exception | None:
        """The exception that stopped the worker, if any.

        Returns:
            The exception raised by task(), or None.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError
