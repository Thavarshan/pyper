"""
Challenge: Bank Transfer
Level:     13 - Concurrency
Topics:    several locks, deadlock, lock ordering, check-then-act races,
           contextlib.ExitStack
Source:    Classic bank-account deadlock exercise

========================================================================
YOUR TASK
========================================================================
The `Account` class below is PROVIDED: each account has an id, a
balance and its own lock. Write two functions that are safe to call
from many threads at once:

- `transfer(source, target, amount)` moves `amount` from `source` to
  `target`, holding BOTH accounts' locks, and never deadlocks.
- `total_balance(accounts)` adds up all the balances while holding
  every account's lock, so it sees one consistent moment.

    a = Account(1, 100)
    b = Account(2, 50)
    transfer(a, b, 30)
    a.balance, b.balance      # -> (70, 80)
    total_balance([a, b])     # -> 150

========================================================================
BACKGROUND: DEADLOCK
========================================================================
A transfer changes TWO accounts, so it must hold both locks: no other
thread may touch either account halfway through. The obvious code is
"lock the source, then lock the target". That code can freeze forever.

Picture two threads moving money in opposite directions at the same
moment. Thread 1 runs transfer(a, b, ...) and thread 2 runs
transfer(b, a, ...):

    thread 1                        thread 2
    lock a          (got it)
                                    lock b          (got it)
    lock b ... waiting for 2
                                    lock a ... waiting for 1

Each thread holds one lock and waits for the lock the OTHER one holds.
Neither can ever move on. This is a DEADLOCK: the threads are stuck
for good, with no error message and no crash. The program just hangs.

    thread 1 --holds--> [a] <--wants-- thread 2
    thread 1 --wants--> [b] <--holds-- thread 2

THE FIX: always take the locks in the SAME ORDER, whichever direction
the money goes. Here: the account with the smaller `account_id`
first. Now both threads above try to lock `a` first. One gets it. The
other waits while holding NOTHING, so it can't block anyone. The
winner takes `b` too, finishes, and releases both. Then the other
thread goes. A circle of waiting can never form.

The same reason means you must reject `source is target` BEFORE
locking anything. Locking one account's lock twice from the same
thread also hangs forever, because a `threading.Lock` can't be taken
again by the thread that already holds it.

========================================================================
BACKGROUND: CHECK-THEN-ACT
========================================================================
This looks careful, but it's a race:

    if source.balance >= amount:       # CHECK (no lock held)
        with ...both locks...:
            source.balance -= amount   # ACT

An account holds 50. Two threads each want to take 50. Both CHECK
before either ACTs: "50 >= 50? yes" and "50 >= 50? yes". Then both
subtract, and the balance ends at -50. The check was true when it ran,
but it was out of date by the time the thread acted on it.

The fix: do the check INSIDE the locks, right next to the change.
While you hold the locks, no other thread can change the balance
between your check and your update.

========================================================================
THE RULES
========================================================================
`transfer(source, target, amount)` must:
1. Raise `ValueError` if `amount <= 0`.
2. Raise `ValueError` if `source is target` (the very same account
   object). Check this BEFORE taking any lock.
3. Lock BOTH accounts, always in increasing `account_id` order (the
   lower id first), whichever way the money moves.
4. Inside the locks, check the funds. If `source.balance < amount`,
   raise `ValueError("insufficient funds")` and change nothing.
5. Otherwise subtract `amount` from `source.balance`, add it to
   `target.balance`, and return None.
6. Release both locks before returning, whether the transfer worked
   or raised. (A `with` block does this for you.)

`total_balance(accounts)` must:
7. Lock every account in increasing `account_id` order, add up all
   the balances, then release every lock. Release them even if
   something goes wrong while summing.
8. Return 0 for an empty list.
9. Not change the order of the caller's list.

You can assume:
- Every `account_id` is a unique int.
- An account appears at most once in the list passed to
  `total_balance`.
- `amount` is an int.

========================================================================
EXAMPLES
========================================================================
Each line runs one call. `# ->` shows what it returns.

    a = Account(1, 100)
    b = Account(2, 50)
    transfer(a, b, 30)
    a.balance, b.balance      # -> (70, 80)
    transfer(b, a, 500)       # -> raises ValueError("insufficient funds")
    a.balance, b.balance      # -> (70, 80)   nothing changed
    transfer(a, b, 0)         # -> raises ValueError (amount must be > 0)
    transfer(a, a, 10)        # -> raises ValueError (same account)
    total_balance([b, a])     # -> 150
    total_balance([])         # -> 0

========================================================================
EDGE CASES TO TEST
========================================================================
- Moving the whole balance works: Account(1, 10) -> Account(2, 0),
  amount 10 -> balances (0, 10)
- Money can move from a higher id to a lower id:
  transfer(Account(2, 10), Account(1, 0), 4) -> balances 6 and 4
- amount 0 or negative -> ValueError, balances unchanged
- Same account -> ValueError (and no hang)
- Insufficient funds -> ValueError("insufficient funds"), balances
  unchanged. Check the message with
  `pytest.raises(ValueError, match="insufficient funds")`.
- The locks are free again after a transfer, both after success and
  after an error: `account.lock.locked()` is False.
- total_balance([]) -> 0
- total_balance releases every lock, even on an error. Give one
  account a balance of "oops" (a string): summing raises TypeError,
  and afterwards no lock is held.
- No deadlock: two threads, one doing 1_000 transfers of 1 from a to
  b, the other 1_000 transfers of 1 from b to a, both accounts
  starting at 1_000. Join each with `t.join(timeout=5)` and
  `assert not t.is_alive()`. The total is still 2_000. Wrap the test
  in `sys.setswitchinterval(1e-6)` (and restore the old value in a
  `finally:`). Without it, Python switches threads so rarely that
  even the broken "source first" version usually gets lucky. With
  it, the broken version deadlocks most of the time.
- Ten threads each try to move 10 out of an account holding 50:
  exactly 5 succeed and 5 get "insufficient funds". The balance ends
  at 0 and never goes below 0. Collect the outcomes in a list (append
  under a lock of your own), and start the threads together with
  `threading.Barrier(10, timeout=5)` (each thread calls
  `barrier.wait()` first) so they really compete.
- Never let a test hang: always join with a timeout, and
  `@pytest.mark.timeout(10)` (pytest-timeout is installed) is a
  good safety net for a whole test.

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Do the two ValueError checks first, before any locking.
2. Put the two accounts in id order:
   `first, second = sorted([source, target], key=lambda acc: acc.account_id)`.
   Then nest two `with` blocks: `with first.lock:` and, inside it,
   `with second.lock:`. Inside both, keep using `source` and `target`
   for the money: `first`/`second` are only for the locking order.
3. The funds check and the two balance updates all go inside the
   inner `with` block. Raising there is fine: leaving a `with` block
   by an exception still releases the lock.
4. total_balance has to hold a variable number of locks, so you can't
   write a fixed number of nested `with` blocks.
   `contextlib.ExitStack` solves this: it is ONE `with` block that
   you can keep adding context managers to, and it releases all of
   them (in reverse order) when the block ends:

       with contextlib.ExitStack() as stack:
           for acc in sorted(accounts, key=lambda acc: acc.account_id):
               stack.enter_context(acc.lock)
           ...every lock is held here...
       ...every lock is released here, even after an error...

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Deadlock, and the lock ordering rule that prevents it
- Check-then-act races, and keeping the check and the change under the
  same lock
- `sorted(..., key=...)` with a lambda
- Nested `with` blocks, and `contextlib.ExitStack` for a variable
  number of them
- `lock.locked()` for checking a lock is free in tests
- `threading.Barrier` for making threads start at the same moment

========================================================================
STRETCH GOALS
========================================================================
- Write a test that DEMONSTRATES the deadlock. Make an
  `unordered_transfer` that locks the source, calls
  `time.sleep(0.1)`, then locks the target. Run a->b and b->a in two
  threads created with `daemon=True` (a daemon thread doesn't stop
  Python from exiting, so pytest can still finish while they're
  stuck). Join each with `timeout=1`, then assert BOTH are still
  alive.
- Another way to avoid deadlock is "back off and retry": lock the
  source, then try `target.lock.acquire(timeout=0.01)`. If that
  returns False, release the source lock, sleep a tiny random time,
  and start again. Remember to release the target lock when you're
  done (try/finally). Compare it with lock ordering: which is simpler
  to get right?
- Add `transfer_many(transfers)` that applies a list of
  (source, target, amount) moves all-or-nothing: lock every account
  involved (in id order), check everything, then apply.
"""

import contextlib  # for you to use in your implementation
import threading


class Account:
    """A bank account with its own lock.

    Attributes:
        account_id: A unique int that identifies the account. Use it to
            decide the locking order.
        balance: The current balance, an int.
        lock: A threading.Lock that guards this account's balance.

    This class is PROVIDED for you - you don't need to change it. Create
    one with Account(1, 100): its account_id is 1 and its balance is 100.
    """

    def __init__(self, account_id: int, balance: int = 0) -> None:
        self.account_id = account_id
        self.balance = balance
        self.lock = threading.Lock()


def transfer(source: Account, target: Account, amount: int) -> None:
    """Move `amount` from `source` to `target`, safely across threads.

    Both accounts' locks are taken in increasing account_id order, and the
    funds check happens while they are held.

    Args:
        source: The account to take money from.
        target: The account to put money into.
        amount: How much to move. Must be > 0.

    Raises:
        ValueError: If amount <= 0, if source is target, or (with the
            message "insufficient funds") if source.balance < amount.
            Balances are unchanged in every error case.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def total_balance(accounts: list[Account]) -> int:
    """Return the sum of all balances, holding every account's lock.

    The locks are taken in increasing account_id order and are all
    released before returning, even if an error occurs.

    Args:
        accounts: The accounts to add up. Not modified.

    Returns:
        The total balance (0 for an empty list).
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
