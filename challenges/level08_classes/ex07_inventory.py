"""
Challenge: Inventory with Dataclasses
Level:     08 - Classes
Topics:    @dataclass, __post_init__, composition, dicts of objects
Source:    Classic OOP exercise

========================================================================
PROBLEM
========================================================================
A DATACLASS is a class whose main job is to hold data. Writing
`@dataclass` above a class with typed fields makes Python generate
__init__, __repr__ and __eq__ for you automatically:

    @dataclass
    class Point:
        x: int
        y: int

    Point(1, 2)               # __init__ generated
    repr(Point(1, 2))         # "Point(x=1, y=2)"
    Point(1, 2) == Point(1, 2)  # True - __eq__ generated

Because __init__ is generated, you can't put validation in it. Instead
dataclasses call a method named `__post_init__(self)` right after the
generated __init__ finishes - that's where validation goes.

Part 1 - Item (a dataclass, fields provided below):
    name: str       non-empty (after stripping whitespace) -> else ValueError
    price: float    int or float (not bool), >= 0 -> else TypeError /
                    ValueError
    quantity: int   int (not bool), >= 0 -> else TypeError / ValueError
    Implement the checks in __post_init__. Non-str name -> TypeError.

Part 2 - Inventory (a normal class):
    Inventory()                 Starts empty. Stores items in a dict keyed
                                by name (names are case-sensitive).

    .add_item(item)             Add an Item. If an item with the same
                                name already exists, INCREASE its
                                quantity by item.quantity and keep the
                                EXISTING price. Non-Item argument ->
                                TypeError. Returns None.
                                Store your own copy (or be careful): later
                                changes to the passed-in Item object
                                should not be relied on. It's simplest to
                                store a new Item built from its fields.

    .remove_item(name, qty)     Decrease the named item's quantity by
                                `qty`.
                                - Unknown name -> KeyError
                                - qty not a positive int -> ValueError
                                - qty greater than the stock -> ValueError
                                  (nothing changes)
                                Check the name first, so an unknown name
                                is always KeyError whatever `qty` is.
                                - If quantity reaches exactly 0, delete
                                  the item from the inventory entirely.

    .get(name)                  Return the stored Item, or None if
                                missing.

    len(inventory)              Number of DISTINCT items (implement
                                __len__).

    .total_value()              Sum of price * quantity over all items
                                (0 when empty). Compare with approx.

    .low_stock(threshold)       Names of items whose quantity is
                                STRICTLY LESS than `threshold`, returned
                                as a list sorted alphabetically.

    .most_valuable()            The Item with the highest price * quantity
                                (its total stock value), or None if the
                                inventory is empty. Ties: return the one
                                whose name comes first alphabetically.

========================================================================
EXAMPLES
========================================================================
    >>> inv = Inventory()
    >>> inv.add_item(Item("apple", 0.5, 10))
    >>> inv.add_item(Item("pear", 0.75, 2))
    >>> inv.add_item(Item("apple", 9.99, 5))     # merges, keeps price 0.5
    >>> inv.get("apple")
    Item(name='apple', price=0.5, quantity=15)
    >>> inv.total_value()
    9.0
    >>> inv.low_stock(5)
    ['pear']
    >>> inv.most_valuable().name
    'apple'
    >>> inv.remove_item("pear", 2)
    >>> len(inv)
    1

========================================================================
CONSTRAINTS
========================================================================
- Use the provided @dataclass Item; do not hand-write its __init__.
- Item validation lives in __post_init__.
- All ordering in results is alphabetical where a list of names is
  returned.
- Only stdlib.

========================================================================
EDGE CASES TO TEST
========================================================================
- Item repr/equality come from the dataclass for free
- Item("", 1, 1), Item("x", -1, 1), Item("x", 1, -1) -> ValueError
- Item("x", "1", 1), Item("x", 1, 1.5) -> TypeError
- Adding the same name twice merges quantity and keeps the first price
- add_item("apple") -> TypeError
- remove_item on unknown name -> KeyError
- remove_item with qty 0, negative qty, or more than in stock ->
  ValueError, and the quantity is unchanged
- Removing the exact quantity deletes the item (get returns None,
  len decreases)
- total_value() of an empty inventory == 0
- low_stock returns sorted names, uses strict "<", and [] if none
- most_valuable() is None when empty; tie broken alphabetically

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. In Inventory.__init__: `self._items: dict[str, Item] = {}`.
2. `dataclasses.replace(item)` or `Item(item.name, item.price,
   item.quantity)` makes a copy for storage.
3. total_value: `sum(i.price * i.quantity for i in self._items.values())`.
4. low_stock: build the names with a list comprehension, then `sorted()`.
5. most_valuable: `min(items, key=lambda i: (-(i.price * i.quantity),
   i.name))` picks highest value, then alphabetical name. Or loop and
   keep the best so far.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- @dataclass and the methods it generates
- __post_init__ for validation
- Composition: an Inventory HAS Items
- Dicts keyed by name for fast lookup
- sorted(), min()/max() with key functions and tie-breaking
- Returning None to mean "nothing found"

========================================================================
STRETCH GOALS
========================================================================
- Make Item frozen (`@dataclass(frozen=True)`) and update Inventory to
  replace items instead of mutating them.
- Add `update_price(name, price)`.
- Add `to_dict()` / `from_dict()` using `dataclasses.asdict` and save
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
