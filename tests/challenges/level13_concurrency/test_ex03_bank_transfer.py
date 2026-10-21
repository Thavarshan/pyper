"""Tests for challenges/level13_concurrency/ex03_bank_transfer.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level13_concurrency/test_ex03_bank_transfer.py -v
"""

import pytest

from challenges.level13_concurrency.ex03_bank_transfer import Account, total_balance, transfer


# TODO: write your tests. Example to get you started:
#
# import sys
# import threading
#
# def test_example():
#     a, b = Account(1, 100), Account(2, 50)
#     transfer(a, b, 30)
#     assert (a.balance, b.balance) == (70, 80)
#     assert total_balance([a, b]) == 150
#
# def test_insufficient_funds_changes_nothing():
#     a, b = Account(1, 10), Account(2, 0)
#     with pytest.raises(ValueError, match="insufficient funds"):
#         transfer(a, b, 50)
#     assert (a.balance, b.balance) == (10, 0)
#
# @pytest.mark.timeout(10)  # fail instead of hanging forever
# def test_opposite_directions_do_not_deadlock():
#     a, b = Account(1, 1_000), Account(2, 1_000)
#
#     def move(source, target):
#         for _ in range(1_000):
#             transfer(source, target, 1)
#
#     old = sys.getswitchinterval()
#     sys.setswitchinterval(1e-6)  # switch threads very often
#     try:
#         t1 = threading.Thread(target=move, args=(a, b))
#         t2 = threading.Thread(target=move, args=(b, a))
#         t1.start()
#         t2.start()
#         t1.join(timeout=5)  # never wait forever
#         t2.join(timeout=5)
#     finally:
#         sys.setswitchinterval(old)
#     assert not t1.is_alive() and not t2.is_alive()  # both finished
#     assert a.balance + b.balance == 2_000
