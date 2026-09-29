"""Tests for challenges/level10_data_structures/ex04_linked_list_cycle.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

WARNING: never call linked_to_list() on a list that has a cycle - it will
loop forever. Build the list with list_to_linked(), THEN create the cycle
by re-pointing the last node's .next by hand.

Run just this file:
    pytest tests/challenges/level10_data_structures/test_ex04_linked_list_cycle.py -v
"""

import pytest

from challenges.common.structures import ListNode, list_to_linked
from challenges.level10_data_structures.ex04_linked_list_cycle import has_cycle


# TODO: write your tests. Example to get you started:
#
# def make_cycle(values, pos):
#     """Build a linked list and point the tail back at index `pos`."""
#     head = list_to_linked(values)
#     nodes = []
#     node = head
#     while node is not None:
#         nodes.append(node)
#         node = node.next
#     nodes[-1].next = nodes[pos]   # the tail now points back into the list
#     return head
#
# def test_cycle_detected():
#     head = make_cycle([3, 2, 0, -4], pos=1)   # -4 -> 2
#     assert has_cycle(head) is True
#
# def test_no_cycle():
#     assert has_cycle(list_to_linked([1, 2, 3])) is False
#
# def test_single_node_self_loop():
#     node = ListNode(1)
#     node.next = node
#     assert has_cycle(node) is True
