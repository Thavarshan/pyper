"""
Challenge: Rectangle
Level:     08 - Classes
Topics:    property setters with validation, __eq__, __repr__, @classmethod
Source:    Classic OOP exercise

========================================================================
YOUR TASK
========================================================================
Write a `Rectangle` class that always stays valid: it must be
impossible to give it a zero, negative or non-number size, either when
you create it OR when you change it later. Fill in:

- `__init__(width, height)`: create a rectangle
- `width` / `height`: properties you can read AND set, with checks
- `area()`: return width * height
- `perimeter()`: return 2 * (width + height)
- `is_square()`: return True if width == height
- `Rectangle.square(size)`: build a size-by-size rectangle
- `__eq__(other)`: make `==` compare width and height
- `__repr__()`: describe it, as in "Rectangle(width=2, height=3)"

    r = Rectangle(3, 4)
    r.area()        # -> 12
    r.width = -3    # raises ValueError, and r.width stays 3

========================================================================
BACKGROUND: SETTERS, CLASSMETHODS AND __eq__
========================================================================
A PROPERTY SETTER lets you run code whenever someone assigns to an
attribute. With it, `rect.width = -3` can raise an error instead of
quietly storing bad data:

    @property
    def width(self): ...            # runs on:  rect.width
    @width.setter
    def width(self, value): ...     # runs on:  rect.width = value

A CLASSMETHOD is a method you call on the class itself, not on an
instance: `Rectangle.square(5)`. It receives the class as its first
parameter, named `cls`. A common use is an "alternative constructor",
another way to build an object. Writing `return cls(size, size)`
(rather than `Rectangle(size, size)`) means it also builds the right
type for subclasses.

`__eq__` decides what `r1 == r2` means. Without it, two separate
Rectangle objects are never equal, even with the same sides. When
`__eq__` gets something it doesn't know how to compare (say, a tuple),
it should `return NotImplemented` (a special built-in value, not an
error). Python then tries the other side, and finally falls back to
False.

========================================================================
THE RULES
========================================================================
Your class must:

Sizes
1. Accept only an int or float for width and height. Anything else,
   including `True`/`False`, raises `TypeError`. (bool is a subclass
   of int in Python, so `isinstance(True, int)` is True. Check for
   bool explicitly.)
2. Raise `ValueError` for a width or height of 0 or less.
3. Apply these checks both in `Rectangle(width, height)` and on later
   assignment (`r.width = value`, `r.height = value`).
4. Leave the old value in place when an assignment fails.
5. In `__init__`, assign through the setters (`self.width = width`) so
   the checks live in ONE place.

Methods
6. `area()` returns width * height.
7. `perimeter()` returns 2 * (width + height).
8. `is_square()` returns True if width == height, else False.
9. `Rectangle.square(size)` is a classmethod that returns
   `cls(size, size)`. A bad size raises the same errors as above.

Comparing and showing
10. `r1 == r2` is True when both are Rectangles with equal width AND
    equal height. Rectangle(2, 3) is NOT equal to Rectangle(3, 2).
11. For a non-Rectangle `other` (such as a tuple), `__eq__` returns
    `NotImplemented`, so `==` ends up False.
12. `repr(r)` returns exactly f"Rectangle(width={w!r}, height={h!r})",
    for example Rectangle(width=2, height=3). Floats show as they are:
    Rectangle(width=2.5, height=1).

Note: defining __eq__ makes Python set __hash__ to None. So Rectangles
can't go in sets or be dict keys. That's fine, because they are
mutable (they can change after creation).

========================================================================
EXAMPLES
========================================================================
A short script. Each `# ->` comment shows what that line returns.

    r = Rectangle(3, 4)
    r.area()                              # -> 12
    r.perimeter()                         # -> 14
    r.is_square()                         # -> False

    r.width = 4
    r.is_square()                         # -> True

    Rectangle.square(5)
    # -> Rectangle(width=5, height=5)
    Rectangle(2, 3) == Rectangle(2, 3)    # -> True
    Rectangle(2, 3) == Rectangle(3, 2)    # -> False
    Rectangle(2, 3) == (2, 3)             # -> False (not a Rectangle)

    r.height = 0                          # raises ValueError
    r.height                              # -> 4  (old value kept)
    Rectangle("3", 4)                     # raises TypeError

========================================================================
EDGE CASES TO TEST
========================================================================
- Area and perimeter with ints and floats: Rectangle(2.5, 1.5).area()
  == pytest.approx(3.75), .perimeter() == pytest.approx(8.0)
- Rectangle(0, 5) and Rectangle(5, -1) -> raise ValueError
- Rectangle("3", 4) and Rectangle(True, 4) -> raise TypeError
- Setting an invalid width after creation raises AND keeps the old
  value
- is_square changes after changing a side: Rectangle(3, 4), then
  width = 4 -> is_square() is True
- Rectangle.square(3) == Rectangle(3, 3), and its is_square() is True
- Rectangle.square(0) -> raises ValueError
- Rectangle(2, 3) != Rectangle(3, 2), and Rectangle(2, 3) != (2, 3)
- repr for ints and floats: repr(Rectangle(2, 3)) ->
  "Rectangle(width=2, height=3)", repr(Rectangle(2.5, 1)) ->
  "Rectangle(width=2.5, height=1)"

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Store the real values in `self._width` and `self._height`. The
   property getter returns `self._width`. The setter checks the value,
   then assigns `self._width = value`.
2. Check first, assign last. That's how a failed assignment keeps the
   old value.
3. Write one helper, such as `_validate(name, value)`, and call it
   from both setters.
4. Reject bools explicitly. `isinstance(True, (int, float))` is True,
   so a check for (int, float) alone lets bools through. Add an
   `isinstance(value, bool)` check as well.
5. __eq__:
       if not isinstance(other, Rectangle):
           return NotImplemented
       return (self.width, self.height) == (other.width, other.height)

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- @property with @x.setter
- @classmethod and `cls`: alternative constructors
- __eq__ and NotImplemented, and why __hash__ becomes None
- __repr__ and the `!r` conversion (use repr() on the value)
- Class invariants: rules that keep an object valid at all times

========================================================================
STRETCH GOALS
========================================================================
- Add `scale(factor)` returning a NEW Rectangle scaled by `factor`.
- Add `__lt__` (the `<` operator) comparing by area and use `sorted()`
  on rectangles, or use functools.total_ordering (which fills in the
  other comparisons for you).
- Make the class immutable (unchangeable: no setters, with
  `__slots__`) and add `__hash__` so rectangles can go in a set.
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
