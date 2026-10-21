"""
Challenge: Bank Account
Level:     08 - Classes
Topics:    classes, __init__, methods, @property, custom exceptions, __repr__
Source:    Classic OOP exercise

========================================================================
YOUR TASK
========================================================================
Write a `BankAccount` class that holds an owner's name, a balance and a
history of deposits and withdrawals. Fill in:

- `__init__(owner, balance=0.0)`: set up a new account
- `balance`: read-only property, the current balance
- `transactions`: read-only property, a copy of the history
- `deposit(amount)`: add money, return the NEW balance
- `withdraw(amount)`: take money out, return the NEW balance
- `__repr__()`: describe the account, as in
  "BankAccount(owner='Alice', balance=150.00)"

    acct = BankAccount("Alice", 100)
    acct.deposit(50)    # -> 150

========================================================================
WHAT A CLASS IS
========================================================================
A CLASS is a blueprint for making objects. An OBJECT (or INSTANCE) is
one thing built from that blueprint, with its own data. `BankAccount`
is the class. "Alice's account" and "Bob's account" are two separate
instances, each with its own balance.

Inside a class, METHODS are functions that belong to the object. Their
first parameter is always `self`: the particular object the method was
called on. `acct.deposit(50)` is really `BankAccount.deposit(acct, 50)`.

A PROPERTY looks like a plain attribute from outside (`acct.balance`,
no brackets), but runs a method behind the scenes. A property with no
"setter" is READ-ONLY: `acct.balance = 5` raises AttributeError, and
Python does that for you.

A CUSTOM EXCEPTION is just a class that inherits from Exception (or
one of its subclasses). `InsufficientFundsError` is provided below. It
inherits from ValueError, so `except ValueError` also catches it.

========================================================================
THE RULES
========================================================================
Your class must:

Creating an account: BankAccount(owner, balance=0.0)
1. Store `owner` in a plain attribute `.owner`.
2. Raise `ValueError` if `owner` is not a str, or is empty or only
   whitespace (spaces, tabs and so on).
3. Raise `TypeError` if the starting `balance` is not an int or float.
   `True` and `False` count as NOT numbers here. (bool is a subclass
   of int in Python, so `isinstance(True, int)` is True. Check for
   bool explicitly.)
4. Raise `ValueError` if the starting `balance` is negative. 0 is fine.

Reading the account
5. `.balance` is a read-only property returning the current balance.
   Assigning to it (`acct.balance = 5`) raises AttributeError.
6. `.transactions` is a read-only property returning a list of the
   successful transactions, oldest first, as tuples:
   ("deposit", amount) or ("withdraw", amount).
   - The starting balance is NOT a transaction.
   - Failed operations are NOT recorded.
   - Return a COPY of the internal list, so outside code cannot
     tamper with the history.

Moving money
7. `.deposit(amount)` adds `amount` to the balance and returns the NEW
   balance.
8. `.withdraw(amount)` subtracts `amount` and returns the NEW balance.
   Withdrawing the exact balance (down to 0) is allowed.
9. If `amount` is more than the balance, `withdraw` raises
   `InsufficientFundsError` and changes nothing: the balance and the
   history stay as they were.
10. For both deposit and withdraw: raise `TypeError` if `amount` is not
    an int or float (again, bools are rejected), and raise `ValueError`
    if `amount` is zero or negative.

Showing the account
11. `repr(acct)` returns exactly
    f"BankAccount(owner={owner!r}, balance={balance:.2f})"
    For example: BankAccount(owner='Alice', balance=150.00)
    (`!r` puts quotes around the name, `:.2f` shows 2 decimal places.)

You can assume:
- Amounts are plain numbers. No need for Decimal. Compare floats in
  tests with pytest.approx.

========================================================================
EXAMPLES
========================================================================
A short script. Each `# ->` comment shows what that line returns.

    acct = BankAccount("Alice", 100)
    acct.deposit(50)          # -> 150
    acct.withdraw(30)         # -> 120
    acct.balance              # -> 120
    acct.transactions         # -> [('deposit', 50), ('withdraw', 30)]
    repr(acct)
    # -> "BankAccount(owner='Alice', balance=120.00)"

    acct.withdraw(1000)       # raises InsufficientFundsError
    acct.balance              # -> 120   (unchanged)

    acct.deposit(0)           # raises ValueError (must be > 0)
    acct.deposit("10")        # raises TypeError  (not a number)
    acct.balance = 999        # raises AttributeError (read-only)

========================================================================
EDGE CASES TO TEST
========================================================================
- A new account with the default balance: BankAccount("Bob").balance
  == 0 and .transactions == []
- deposit and withdraw return the new balance
- Withdraw exactly the full balance -> balance becomes 0
- Withdraw more than the balance -> raises InsufficientFundsError, and
  the balance and the history are unchanged afterwards
- deposit(0), deposit(-5), withdraw(0) -> raise ValueError
- deposit("10") -> raises TypeError
- `acct.balance = 999` -> raises AttributeError
- Changing the returned transactions list (for example appending to
  it) does not change acct.transactions
- repr with a float balance: repr(BankAccount("Al", 10.5))
  -> "BankAccount(owner='Al', balance=10.50)"
- Two accounts are independent: depositing into one doesn't touch the
  other
- BankAccount("", 10) and BankAccount("Bob", -1) -> raise ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Store the balance in a "private" attribute like `self._balance`.
   The leading underscore is a convention meaning "internal, don't
   touch from outside".
2. A read-only property:
       @property
       def balance(self) -> float:
           return self._balance
3. Put the amount checks in a small helper method, such as
   `_check_amount(amount)`, so deposit and withdraw share them.
4. Check for insufficient funds BEFORE changing anything.
5. Create the history as `self._transactions = []` inside __init__,
   NOT as a class attribute (written directly under `class`).
   Otherwise every account shares the same list! Return
   `list(self._transactions)` from the property to hand out a copy.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `class`, `__init__`, `self`, instance attributes
- Methods vs functions
- `@property` for computed or read-only attributes
- Custom exception classes and exception inheritance
- `__repr__` and f-string format specs (`:.2f`, `!r`)
- Class attributes vs instance attributes (the shared-list trap)

========================================================================
STRETCH GOALS
========================================================================
- Add `transfer(other, amount)` that withdraws from self and deposits
  into another account atomically (all or nothing: if any step fails,
  neither account changes).
- Add `__str__` returning a friendly message like
  "Alice's account: $120.00".
- Switch to `decimal.Decimal` to avoid float rounding surprises
  (0.1 + 0.2 gives 0.30000000000000004 with floats).
- Add a SavingsAccount subclass with `add_interest(rate)`.
"""


class InsufficientFundsError(ValueError):
    """Raised when a withdrawal is larger than the available balance.

    Provided for you - no need to change it.
    """


class BankAccount:
    """A simple bank account with a balance and transaction history."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        """Create a new account.

        Args:
            owner: The account holder's name. Non-empty string.
            balance: Starting balance, must be >= 0.

        Raises:
            TypeError: If `balance` is not an int or float (bools rejected).
            ValueError: If `owner` is not a non-empty string or `balance`
                is negative.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @property
    def balance(self) -> float:
        """The current balance (read-only)."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @property
    def transactions(self) -> list[tuple[str, float]]:
        """A copy of the successful transactions, oldest first.

        Each entry is ("deposit", amount) or ("withdraw", amount).
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def deposit(self, amount: float) -> float:
        """Add money to the account.

        Args:
            amount: The amount to add. Must be > 0.

        Returns:
            The new balance.

        Raises:
            TypeError: If `amount` is not an int or float.
            ValueError: If `amount` is zero or negative.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def withdraw(self, amount: float) -> float:
        """Take money out of the account.

        Args:
            amount: The amount to remove. Must be > 0 and <= balance.

        Returns:
            The new balance.

        Raises:
            TypeError: If `amount` is not an int or float.
            ValueError: If `amount` is zero or negative.
            InsufficientFundsError: If `amount` is greater than the
                balance. The account is left unchanged.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __repr__(self) -> str:
        """Return e.g. "BankAccount(owner='Alice', balance=150.00)"."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError
