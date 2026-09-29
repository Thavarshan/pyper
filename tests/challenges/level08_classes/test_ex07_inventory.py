"""Tests for challenges/level08_classes/ex07_inventory.py

Write your tests here first, run them and watch them fail, then implement
the solution until they pass. The "EDGE CASES TO TEST" section of the
challenge file lists good cases to cover.

Run just this file:
    pytest tests/challenges/level08_classes/test_ex07_inventory.py -v
"""

import pytest

from challenges.level08_classes.ex07_inventory import Inventory, Item


# TODO: write your tests. Example to get you started:
#
# def test_adding_same_name_merges_quantity():
#     inv = Inventory()
#     inv.add_item(Item("apple", 0.5, 10))
#     inv.add_item(Item("apple", 0.5, 5))
#     assert inv.get("apple").quantity == 15
#
# def test_remove_unknown_item_raises_key_error():
#     with pytest.raises(KeyError):
#         Inventory().remove_item("ghost", 1)
