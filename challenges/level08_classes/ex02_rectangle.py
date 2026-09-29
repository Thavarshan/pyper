"""
Challenge: Rectangle
Level:     08 - Classes
Topics:    property setters with validation, __eq__, __repr__, @classmethod
Source:    Classic OOP exercise

========================================================================
PROBLEM
========================================================================
Build a `Rectangle` class that always stays valid - it should be
impossible to give it a zero, negative or non-numeric size, either when
you create it OR when you change it later.

A PROPERTY SETTER lets you run code whenever someone assigns to an
attribute. With it, `rect.width = -3` can raise an error instead of
silently storing bad data:

    @property
    def width(self): ...            # runs on:  rect.width
    @width.setter
    def width(self, value): ...     # runs on:  rect.width = value

Requirements:

    Rectangle(width, height)
        Both must be int or float and > 0.
        Non-number (including bool) -> TypeError; <= 0 -> ValueError.
        __init__ should assign through the setters (self.width = width)
        so the validation lives in ONE place.

    .width / .height     Readable and writable properties with the same
                         validation as __init__. A failed assignment
                         leaves the old value in place.

    .area()              width * height
    .perimeter()         2 * (width + height)
    .is_square()         True if width == height

    Rectangle.square(size)
        A CLASSMETHOD - an alternative constructor called on the class
        itself, not an instance. Returns Rectangle(size, size).
        A classmethod receives the class as `cls`, so write
        `return cls(size, size)` (this also works for subclasses).

    r1 == r2             True when both are Rectangles with equal width
                         AND equal height. Rectangle(2, 3) is NOT equal
                         to Rectangle(3, 2). Comparing with a
                         non-Rectangle (e.g. a tuple) must return False -
                         to get that, __eq__ should `return NotImplemented`
                         for other types.

    repr(r)              Exactly:  Rectangle(width=2, height=3)
                         i.e. f"Rectangle(width={w!r}, height={h!r})"
                         so floats show as e.g. Rectangle(width=2.5, height=1)

Note: defining __eq__ makes Python set __hash__ to None, so Rectangles
can't go in sets or be dict keys. That's fine (they are mutable).

========================================================================
EXAMPLES
========================================================================
    >>> r = Rectangle(3, 4)
    >>> r.area(), r.perimeter(), r.is_square()
    (12, 14, False)
    >>> r.width = 4
    >>> r.is_square()
    True
    >>> Rectangle.square(5)
    Rectangle(width=5, height=5)
    >>> Rectangle(2, 3) == Rectangle(2, 3)
    True
    >>> r.height = 0
    Traceback (most recent call last):
        ...
    ValueError: ...

========================================================================
CONSTRAINTS
========================================================================
- width and height: int or float, > 0. bool is rejected (TypeError),
  even though bool is technically a subclass of int.
- Validation must also happen on later assignment, not just __init__.
- __eq__ returns NotImplemented for non-Rectangle operands (so `==`
  ends up False).

========================================================================
EDGE CASES TO TEST
========================================================================
- Area/perimeter with int and float sizes (use pytest.approx for floats)
- Rectangle(0, 5), Rectangle(5, -1) -> ValueError
- Rectangle("3", 4), Rectangle(True, 4) -> TypeError
- Setting an invalid width after creation raises AND keeps the old value
- is_square after changing a side
- Rectangle.square(3) == Rectangle(3, 3) and is_square() is True
- Rectangle.square(0) -> ValueError
- Rectangle(2, 3) != Rectangle(3, 2); Rectangle(2, 3) != (2, 3)
- repr for ints and floats

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Store the real values in `self._width` / `self._height`. The
   property getter returns `self._width`; the setter validates then
   assigns `self._width = value`.
2. Validate first, assign last - that's how a failed assignment keeps
   the old value.
3. Write one helper, e.g. `_validate(name, value)`, and call it from
   both setters.
4. Reject bools explicitly: `isinstance(value, bool)` must be checked
   BEFORE `isinstance(value, (int, float))`.
5. __eq__:
       if not isinstance(other, Rectangle):
           return NotImplemented
       return (self.width, self.height) == (other.width, other.height)

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- @property with @x.setter
- @classmethod and `cls` - alternative constructors
- __eq__ and NotImplemented; why __hash__ becomes None
- __repr__ and the `!r` conversion
- Class invariants: keeping an object valid at all times

========================================================================
STRETCH GOALS
========================================================================
- Add `scale(factor)` returning a NEW Rectangle scaled by `factor`.
- Add `__lt__` comparing by area and use `sorted()` on rectangles, or
  use functools.total_ordering.
- Make the class immutable (no setters, with `__slots__`) and add
  `__hash__` so rectangles can go in a set.
- Add a `contains(other)` method: can `other` fit inside `self`?
"""


class Rectangle:
    """A rectangle with validated positive width and height."""

    def __init__(self, width: float, height: float) -> None:
        """Create a rectangle.

        Args:
            width: Positive int or float.
            height: Positive int or float.

        Raises:
            TypeError: If a side is not an int/float (or is a bool).
            ValueError: If a side is zero or negative.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @property
    def width(self) -> float:
        """The rectangle's width."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @width.setter
    def width(self, value: float) -> None:
        """Set the width after validating it.

        Raises:
            TypeError: If `value` is not an int/float (or is a bool).
            ValueError: If `value` is zero or negative.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @property
    def height(self) -> float:
        """The rectangle's height."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @height.setter
    def height(self, value: float) -> None:
        """Set the height after validating it.

        Raises:
            TypeError: If `value` is not an int/float (or is a bool).
            ValueError: If `value` is zero or negative.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    @classmethod
    def square(cls, size: float) -> "Rectangle":
        """Alternative constructor: a rectangle with equal sides.

        Args:
            size: Length of each side. Same rules as width/height.

        Returns:
            A new instance of `cls` with width == height == size.

        Raises:
            TypeError: If `size` is not an int/float (or is a bool).
            ValueError: If `size` is zero or negative.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def area(self) -> float:
        """Return width * height."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def perimeter(self) -> float:
        """Return 2 * (width + height)."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def is_square(self) -> bool:
        """Return True if width equals height."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """Rectangles are equal when width and height both match.

        Returns:
            True/False for Rectangle operands; NotImplemented otherwise.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __repr__(self) -> str:
        """Return e.g. "Rectangle(width=2, height=3)"."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError
