"""Tests for challenges/level08_classes/ex01_bank_account.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level08_classes/test_ex01_bank_account.py -v
"""

import pytest

from challenges.level08_classes.ex01_bank_account import BankAccount, InsufficientFundsError


# TODO: write your tests. Example to get you started:
#
# def test_deposit_returns_new_balance():
#     acct = BankAccount("Alice", 100)
#     assert acct.deposit(50) == 150
#
# def test_overdraw_raises():
#     acct = BankAccount("Alice", 10)
#     with pytest.raises(InsufficientFundsError):
#         acct.withdraw(20)
