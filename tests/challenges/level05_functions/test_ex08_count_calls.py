"""Tests for challenges/level05_functions/ex08_count_calls.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level05_functions/test_ex08_count_calls.py -v
"""

import pytest

from challenges.level05_functions.ex08_count_calls import count_calls, repeat


# TODO: write your tests. Example to get you started:
#
# def test_counts_calls():
#     @count_calls
#     def hello(name="world"):
#         return f"hi {name}"
#
#     assert hello.calls == 0
#     hello()
#     hello(name="ann")
#     assert hello.calls == 2
#
# def test_repeat_returns_list_of_results():
#     @repeat(3)
#     def one():
#         return 1
#     assert one() == [1, 1, 1]
#
# def test_repeat_negative_raises_at_decoration_time():
#     with pytest.raises(ValueError):
#         repeat(-1)
