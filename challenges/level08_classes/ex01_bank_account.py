"""
Challenge: Bank Account
Level:     08 - Classes
Topics:    classes, __init__, methods, @property, custom exceptions, __repr__
Source:    Classic OOP exercise

========================================================================
PROBLEM
========================================================================
A CLASS is a blueprint for creating objects. An OBJECT (or INSTANCE) is
one thing built from that blueprint, with its own data. For example,
`BankAccount` is the class; "Alice's account" and "Bob's account" are
two separate instances, each with its own balance.

Inside a class, METHODS are functions that belong to the object. Their
first parameter is always `self` - the particular object the method was
called on. `acct.deposit(50)` is really `BankAccount.deposit(acct, 50)`.

Build a `BankAccount` class:

    BankAccount(owner, balance=0.0)
        - `owner`: the account holder's name, a non-empty str.
        - `balance`: the starting balance, a number >= 0 (default 0.0).
        - Invalid owner (not a str, or empty/whitespace only) ->
          ValueError. Negative starting balance -> ValueError.

    .owner              plain attribute holding the owner's name.

    .balance            READ-ONLY property returning the current balance.
                        Assigning to it (`acct.balance = 5`) must raise
                        AttributeError. (A @property with no setter
                        does this for you automatically.)

    .deposit(amount)    Add `amount` to the balance and return the NEW
                        balance. `amount` must be > 0, else ValueError.

    .withdraw(amount)   Subtract `amount` and return the NEW balance.
                        `amount` must be > 0, else ValueError.
                        If `amount` is more than the balance, raise
                        InsufficientFundsError and leave the balance
                        unchanged. Withdrawing the exact balance (to 0)
                        is allowed.

    .transactions       A read-only property returning a list of the
                        successful transactions in the order they
                        happened, as tuples:
                            ("deposit", amount) or ("withdraw", amount)
                        The starting balance is NOT a transaction.
                        Failed operations are NOT recorded.
                        Return a COPY of the internal list, so outside
                        code cannot tamper with the history.

    repr(acct)          Exactly:  BankAccount(owner='Alice', balance=150.00)
                        i.e. f"BankAccount(owner={owner!r}, balance={balance:.2f})"

A "custom exception" is just a class that inherits from Exception (or
one of its subclasses). `InsufficientFundsError` is provided below for
you - it inherits from ValueError, so `except ValueError` also catches
it.

========================================================================
EXAMPLES
========================================================================
    >>> acct = BankAccount("Alice", 100)
    >>> acct.deposit(50)
    150
    >>> acct.withdraw(30)
    120
    >>> acct.balance
    120
    >>> acct.transactions
    [('deposit', 50), ('withdraw', 30)]
    >>> acct
    BankAccount(owner='Alice', balance=120.00)
    >>> acct.withdraw(1000)
    Traceback (most recent call last):
        ...
    InsufficientFundsError: ...

========================================================================
CONSTRAINTS
========================================================================
- Amounts are int or float. Use plain numbers (no need for Decimal);
  compare floats in tests with pytest.approx.
- Zero or negative amounts -> ValueError (for deposit AND withdraw).
- Non-number amounts (e.g. "10") -> TypeError. `True`/`False` count as
  non-numbers here (bool is a subclass of int, so check for it explicitly).
  The same TypeError rule applies to the starting `balance`.
- Overdraw -> InsufficientFundsError; balance unchanged, nothing logged.
- `balance` and `transactions` are read-only properties.

========================================================================
EDGE CASES TO TEST
========================================================================
- New account with default balance: balance == 0 and transactions == []
- deposit/withdraw return the new balance
- Withdraw exactly the full balance -> balance 0
- Withdraw more than the balance -> InsufficientFundsError, and the
  balance and history are unchanged afterwards
- deposit(0), deposit(-5), withdraw(0) -> ValueError
- deposit("10") -> TypeError
- `acct.balance = 999` -> AttributeError
- Mutating the returned transactions list does not change the account
- repr formatting, including a float balance (e.g. 10.5 -> "10.50")
- Two accounts are independent (depositing into one doesn't touch the
  other)
- BankAccount("", 10) and BankAccount("Bob", -1) -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Store the balance in a "private" attribute like `self._balance`.
   The leading underscore is a convention meaning "internal - don't
   touch from outside".
2. A read-only property:
       @property
       def balance(self) -> float:
           return self._balance
3. Validate in a small helper method, e.g. `_check_amount(amount)`, so
   deposit and withdraw share the same checks.
4. Check for insufficient funds BEFORE changing anything.
5. Store the history in `self._transactions = []` (created in __init__,
   NOT as a class attribute - otherwise all accounts share one list!).
   Return `list(self._transactions)` from the property.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `class`, `__init__`, `self`, instance attributes
- Methods vs functions
- `@property` for computed / read-only attributes
- Custom exception classes and exception inheritance
- `__repr__` and f-string format specs (`:.2f`, `!r`)
- Class attributes vs instance attributes (the shared-list trap)

========================================================================
STRETCH GOALS
========================================================================
- Add `transfer(other, amount)` that withdraws from self and deposits
  into another account atomically (nothing changes if it fails).
- Add `__str__` returning a friendly message like
  "Alice's account: $120.00".
- Switch to `decimal.Decimal` to avoid float rounding (0.1 + 0.2).
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
