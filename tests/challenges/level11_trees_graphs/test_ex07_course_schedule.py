"""Tests for challenges/level11_trees_graphs/ex07_course_schedule.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

find_order may return ANY valid order, so check properties of the result
rather than comparing with one exact list (see the helper below).

Run just this file:
    pytest tests/challenges/level11_trees_graphs/test_ex07_course_schedule.py -v
"""

import pytest

from challenges.level11_trees_graphs.ex07_course_schedule import can_finish, find_order


# TODO: write your tests. Example to get you started:
#
# def assert_valid_order(order, num_courses, prerequisites):
#     """Fail unless `order` is a valid topological order."""
#     assert sorted(order) == list(range(num_courses))   # every course once
#     position = {course: i for i, course in enumerate(order)}
#     for course, prereq in prerequisites:
#         assert position[prereq] < position[course]
#
# def test_diamond_has_valid_order():
#     prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
#     assert_valid_order(find_order(4, prereqs), 4, prereqs)
#
# def test_cycle_is_impossible():
#     assert can_finish(2, [[1, 0], [0, 1]]) is False
#     assert find_order(2, [[1, 0], [0, 1]]) == []
