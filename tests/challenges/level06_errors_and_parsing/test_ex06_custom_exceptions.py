"""Tests for challenges/level06_errors_and_parsing/ex06_custom_exceptions.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level06_errors_and_parsing/test_ex06_custom_exceptions.py -v
"""

import pytest

from challenges.level06_errors_and_parsing.ex06_custom_exceptions import (
    ValidationError,
    AgeError,
    EmailError,
    validate_user,
)


# TODO: write your tests. Example to get you started:
#
# def test_hierarchy():
#     assert issubclass(AgeError, ValidationError)
#
# def test_bad_age_raises_age_error_with_field():
#     with pytest.raises(AgeError) as excinfo:
#         validate_user("Bob", 200, "bob@example.com")
#     assert excinfo.value.field == "age"
