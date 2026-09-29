"""Tests for challenges/level02_strings/ex06_caesar_cipher.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level02_strings/test_ex06_caesar_cipher.py -v
"""

import pytest

from challenges.level02_strings.ex06_caesar_cipher import encrypt, decrypt


# TODO: write your tests. Example to get you started:
#
# def test_wraps_around_the_alphabet():
#     assert encrypt("xyz", 3) == "abc"
#
# def test_round_trip():
#     assert decrypt(encrypt("Hello, World!", 7), 7) == "Hello, World!"
