"""
Challenge: Inventory with Dataclasses
Level:     08 - Classes
Topics:    @dataclass, __post_init__, composition, dicts of objects
Source:    Classic OOP exercise

========================================================================
YOUR TASK
========================================================================
Finish two classes for a shop's stock list. `Item` is a dataclass (its
fields are provided). `Inventory` holds many Items. Fill in:

- `Item.__post_init__()`: check the name, price and quantity
- `Inventory.__init__()`: start with no items
- `add_item(item)`: add an Item, or add to the stock of an existing one
- `remove_item(name, qty)`: take `qty` units of an item out of stock
- `get(name)`: return the stored Item, or None
- `__len__()`: makes `len(inv)` give the number of distinct items
- `total_value()`: return the sum of price * quantity
- `low_stock(threshold)`: return sorted names of items running low
- `most_valuable()`: return the Item worth the most in total

    inv = Inventory()
    inv.add_item(Item("apple", 0.5, 10))
    inv.total_value()    # -> 5.0

========================================================================
WHAT A "DATACLASS" IS
========================================================================
A DATACLASS is a class whose main job is to hold data. Writing
`@dataclass` above a class with typed fields makes Python write
__init__, __repr__ and __eq__ for you:

    @dataclass
    class Point:
        x: int
        y: int

    Point(1, 2)                   # __init__ was generated
    repr(Point(1, 2))             # -> 'Point(x=1, y=2)'
    Point(1, 2) == Point(1, 2)    # -> True   (__eq__ was generated)

Because Python writes __init__ for you, you can't put your checks in
it. Instead, a dataclass calls a method named `__post_init__(self)`
right after the generated __init__ finishes. That's where the checks
go.

========================================================================
THE RULES
========================================================================
Your code must:

Item (a dataclass, fields provided)
1. Use the provided @dataclass Item. Do not hand-write its __init__.
   Put all the checks in __post_init__.
2. `name`: raise TypeError if it is not a str. Raise ValueError if it
   is empty or only whitespace (spaces, tabs and so on).
3. `price`: raise TypeError if it is not an int or float. Raise
   ValueError if it is negative. 0 is fine.
4. `quantity`: raise TypeError if it is not an int. Raise ValueError if
   it is negative. 0 is fine.
5. For price and quantity, `True`/`False` count as NOT numbers, so they
   raise TypeError. (bool is a subclass of int in Python, so check for
   it explicitly.)

Inventory (a normal class)
6. `Inventory()` starts empty. Store the items in a dict keyed by name.
   Names are case-sensitive: "Apple" and "apple" are different items.
7. `add_item(item)` adds an Item and returns None. Raise TypeError if
   `item` is not an Item.
8. If an item with the same name already exists, `add_item` INCREASES
   its quantity by item.quantity and keeps the EXISTING price.
9. Store your own copy of the Item. Don't rely on the caller leaving
   the Item they passed in unchanged. The simplest way is to store a
   new Item built from its fields.
10. `remove_item(name, qty)` lowers the named item's quantity by `qty`
    and returns None. Check the name FIRST, so an unknown name is
    always KeyError, whatever `qty` is. Then:
    - unknown name -> raise KeyError
    - `qty` not a positive int -> raise ValueError
    - `qty` greater than the stock -> raise ValueError, and nothing
      changes
    - if the quantity reaches exactly 0, delete the item from the
      inventory entirely
11. `get(name)` returns the stored Item, or None if there is none.
12. `len(inventory)` returns the number of DISTINCT items.
13. `total_value()` returns the sum of price * quantity over all items,
    and 0 when empty.
14. `low_stock(threshold)` returns the names of items whose quantity is
    STRICTLY LESS than `threshold` (an item with exactly `threshold`
    is not included), as a list sorted alphabetically.
15. `most_valuable()` returns the Item with the highest price *
    quantity (its total stock value), or None if the inventory is
    empty. On a tie, return the one whose name comes first
    alphabetically.
16. Use only the standard library.

You can assume:
- Money is stored as plain floats. Compare total_value() in tests with
  pytest.approx.

========================================================================
EXAMPLES
========================================================================
A short script. Each `# ->` comment shows what that line returns.

    inv = Inventory()
    inv.add_item(Item("apple", 0.5, 10))
    inv.add_item(Item("pear", 0.75, 2))
    inv.add_item(Item("apple", 9.99, 5))   # merges: 10 + 5 apples,
                                           # price stays 0.5
    inv.get("apple")
    # -> Item(name='apple', price=0.5, quantity=15)
    inv.total_value()        # -> 9.0   (0.5 * 15 + 0.75 * 2)
    inv.low_stock(5)         # -> ['pear']   (2 < 5, but 15 is not)
    inv.most_valuable().name # -> 'apple'    (worth 7.5, pear 1.5)
    inv.remove_item("pear", 2)   # pear reaches 0, so it is deleted
    len(inv)                 # -> 1
    inv.remove_item("kiwi", 1)   # raises KeyError

========================================================================
EDGE CASES TO TEST
========================================================================
- Item's repr and == come from the dataclass for free:
  Item("a", 1, 1) == Item("a", 1, 1)
- Item("", 1, 1), Item("x", -1, 1), Item("x", 1, -1) -> raise
  ValueError
- Item("x", "1", 1), Item("x", 1, 1.5) -> raise TypeError
- Adding the same name twice adds up the quantities and keeps the
  first price
- add_item("apple") -> raises TypeError
- remove_item with an unknown name -> raises KeyError
- remove_item with qty 0, a negative qty, or more than is in stock ->
  raises ValueError, and the quantity is unchanged
- Removing the exact quantity deletes the item: get() then returns
  None and len() goes down by 1
- Inventory().total_value() == 0
- low_stock returns sorted names, uses strict "<", and returns [] if
  nothing is low
- Inventory().most_valuable() is None. On a tie it picks the
  alphabetically first name: with Item("b", 2, 1) and Item("a", 1, 2)
  (both worth 2) it returns the "a" item

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. In Inventory.__init__: `self._items: dict[str, Item] = {}`.
2. `dataclasses.replace(item)` or
   `Item(item.name, item.price, item.quantity)` makes a copy for
   storage.
3. total_value:
   `sum(i.price * i.quantity for i in self._items.values())`.
4. low_stock: build the names with a list comprehension, then
   `sorted()` them.
5. most_valuable:
   `min(items, key=lambda i: (-(i.price * i.quantity), i.name))`
   picks the highest value first (the minus sign turns "biggest" into
   "smallest"), then the alphabetically first name. Or loop and keep
   the best so far.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- @dataclass and the methods it generates
- __post_init__ for validation
- Composition: an Inventory HAS Items (rather than IS a kind of Item)
- Dicts keyed by name for fast lookup
- sorted(), min() and max() with key functions and tie-breaking
- Returning None to mean "nothing found"

========================================================================
STRETCH GOALS
========================================================================
- Make Item frozen (`@dataclass(frozen=True)`, so its fields can't be
  changed after creation) and update Inventory to replace items
  instead of mutating (changing) them.
- Add `update_price(name, price)`.
- Add `to_dict()` / `from_dict()` using `dataclasses.asdict`, and save
  the inventory to JSON.
- Add __contains__ so `"apple" in inventory` works.
"""

from dataclasses import dataclass


@dataclass
class Item:
    """A product in stock."""

    name: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        """Validate the fields right after the generated __init__.

        Raises:
            TypeError: If name is not a str, price is not an int/float,
                or quantity is not an int (bools rejected for numbers).
            ValueError: If name is empty/whitespace, or price or
                quantity is negative.
        """
        # TODO: implement validation here, then make your tests pass.
        raise NotImplementedError


class Inventory:
    """A collection of Items keyed by name."""

    def __init__(self) -> None:
        """Create an empty inventory."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def add_item(self, item: Item) -> None:
        """Add an item, merging quantity if the name already exists.

        When merging, the existing price is kept.

        Args:
            item: The Item to add.

        Raises:
            TypeError: If `item` is not an Item.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def remove_item(self, name: str, qty: int) -> None:
        """Remove `qty` units of the named item.

        The item is deleted entirely when its quantity reaches 0.

        Args:
            name: The item's name (case-sensitive).
            qty: How many units to remove. Positive int.

        Raises:
            KeyError: If no item has that name.
            ValueError: If `qty` is not a positive int, or is greater
                than the quantity in stock (nothing is changed).
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def get(self, name: str) -> Item | None:
        """Return the stored Item with this name, or None."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of distinct items."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def total_value(self) -> float:
        """Return the sum of price * quantity for every item (0 if empty)."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def low_stock(self, threshold: int) -> list[str]:
        """Return names of items with quantity < threshold, sorted A-Z."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def most_valuable(self) -> Item | None:
        """Return the item with the highest price * quantity, or None.

        Ties are broken by name, alphabetically first wins.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError
