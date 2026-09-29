"""
Challenge: Shapes - Inheritance and Abstract Base Classes
Level:     08 - Classes
Topics:    inheritance, abc.ABC, @abstractmethod, super(), polymorphism
Source:    Classic OOP exercise

========================================================================
PROBLEM
========================================================================
INHERITANCE lets one class (the SUBCLASS or "child") reuse and extend
another (the BASE CLASS or "parent"). `class Circle(Shape):` means
"a Circle is a kind of Shape" - it gets all of Shape's methods for free
and can add or override its own.

An ABSTRACT BASE CLASS (ABC) is a parent that describes WHAT every
subclass must be able to do, without saying HOW. Methods marked
`@abstractmethod` have no real implementation in the parent; any
subclass that forgets to implement them cannot be instantiated -
Python raises TypeError when you try. You also can't create a plain
`Shape()` directly.

POLYMORPHISM means code can treat different subclasses the same way:
`total_area(shapes)` just calls `shape.area()` on each item and doesn't
care whether it's a Circle, Square or Triangle.

Build:

    Shape (abstract, provided below)
        .area()         abstract - subclasses must implement
        .perimeter()    abstract - subclasses must implement
        .describe()     CONCRETE (implemented once, in Shape) returning:
                            "<ClassName> with area <A> and perimeter <P>"
                        with A and P rounded to 2 decimal places, i.e.
                        f"{type(self).__name__} with area {a:.2f} and perimeter {p:.2f}"
                        e.g. "Square with area 4.00 and perimeter 8.00"

    Circle(radius)
        area = pi * r**2, perimeter (circumference) = 2 * pi * r
        Use math.pi.

    Square(side)
        area = side**2, perimeter = 4 * side

    Triangle(a, b, c)   (the three side lengths)
        perimeter = a + b + c
        area via HERON'S FORMULA:
            s = (a + b + c) / 2          (the "semi-perimeter")
            area = sqrt(s * (s-a) * (s-b) * (s-c))
        The TRIANGLE INEQUALITY must hold: each side must be strictly
        less than the sum of the other two (a < b + c, b < a + c,
        c < a + b). Otherwise the sides can't form a triangle ->
        ValueError. (Sides like 1, 2, 3 are "degenerate" - flat, zero
        area - and are also rejected.)

    total_area(shapes)
        Return the sum of area() for every shape in the iterable.
        Empty iterable -> 0.

Validation for every subclass: each dimension must be an int or float
(not bool) -> else TypeError; and > 0 -> else ValueError.

Each subclass stores its dimensions as public attributes with the same
names as the constructor parameters: `circle.radius`, `square.side`,
`triangle.a`, `triangle.b`, `triangle.c`.

========================================================================
EXAMPLES
========================================================================
    >>> Square(2).describe()
    'Square with area 4.00 and perimeter 8.00'

    >>> round(Circle(1).area(), 5)
    3.14159

    >>> Triangle(3, 4, 5).area()
    6.0

    >>> total_area([Square(2), Triangle(3, 4, 5)])
    10.0

    >>> Shape()
    Traceback (most recent call last):
        ...
    TypeError: Can't instantiate abstract class Shape ...

========================================================================
CONSTRAINTS
========================================================================
- Shape must stay abstract: `Shape()` raises TypeError (this is
  already true in the stub thanks to ABC + @abstractmethod).
- describe() is written ONCE in Shape and inherited, not copied into
  each subclass.
- Floats: compare with pytest.approx.
- Only stdlib (math).

========================================================================
EDGE CASES TO TEST
========================================================================
- Shape() -> TypeError
- A subclass defined in your test that doesn't implement area() can't
  be instantiated (TypeError)
- Circle(1) area ~ pi, perimeter ~ 2*pi
- Square(0), Circle(-1) -> ValueError; Square("2") -> TypeError
- Triangle(3, 4, 5) area == 6, perimeter == 12
- Triangle(1, 2, 3) (degenerate) and Triangle(1, 1, 5) -> ValueError
- describe() uses the right class name for each subclass
- isinstance(Circle(1), Shape) is True
- total_area([]) == 0; total_area of a mix of shapes

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. describe() can call self.area() and self.perimeter() - Python will
   run the SUBCLASS's version. That's polymorphism in action.
2. `type(self).__name__` gives the class name as a string ("Circle").
3. Put the shared number validation in a module-level helper function
   (or a method on Shape) so the subclasses don't repeat it.
4. For Heron's formula use `math.sqrt`.
5. total_area: `sum(shape.area() for shape in shapes)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Inheritance and method overriding
- `abc.ABC` and `@abstractmethod`
- Polymorphism / "duck typing"
- `type(obj).__name__`, `isinstance`, `issubclass`
- `super().__init__()` (useful if Shape grows its own __init__)
- math.pi, math.sqrt

========================================================================
STRETCH GOALS
========================================================================
- Add Rectangle(width, height) and make Square a subclass of it.
  Discuss: is that a good idea? (Look up the "Liskov substitution
  principle".)
- Add `__repr__` to each shape, e.g. "Circle(radius=1)".
- Add `__lt__` so shapes sort by area: sorted([...]).
- Add a `scale(factor)` abstract method returning a new, scaled shape.
"""

import math  # for you to use in your implementation
from abc import ABC, abstractmethod
from collections.abc import Iterable


class Shape(ABC):
    """Abstract base class for 2D shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape. Subclasses must implement."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape. Subclasses must implement."""

    def describe(self) -> str:
        """Return e.g. "Square with area 4.00 and perimeter 8.00".

        Implemented once here; works for every subclass.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError


class Circle(Shape):
    """A circle defined by its radius."""

    def __init__(self, radius: float) -> None:
        """Create a circle.

        Args:
            radius: Positive int or float.

        Raises:
            TypeError: If `radius` is not an int/float (or is a bool).
            ValueError: If `radius` is zero or negative.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def area(self) -> float:
        """Return pi * radius**2."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def perimeter(self) -> float:
        """Return the circumference, 2 * pi * radius."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError


class Square(Shape):
    """A square defined by its side length."""

    def __init__(self, side: float) -> None:
        """Create a square.

        Args:
            side: Positive int or float.

        Raises:
            TypeError: If `side` is not an int/float (or is a bool).
            ValueError: If `side` is zero or negative.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def area(self) -> float:
        """Return side**2."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def perimeter(self) -> float:
        """Return 4 * side."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError


class Triangle(Shape):
    """A triangle defined by its three side lengths."""

    def __init__(self, a: float, b: float, c: float) -> None:
        """Create a triangle.

        Args:
            a: Length of the first side (positive).
            b: Length of the second side (positive).
            c: Length of the third side (positive).

        Raises:
            TypeError: If any side is not an int/float (or is a bool).
            ValueError: If any side is <= 0, or the sides break the
                triangle inequality (including degenerate triangles).
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def area(self) -> float:
        """Return the area using Heron's formula."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def perimeter(self) -> float:
        """Return a + b + c."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError


def total_area(shapes: Iterable[Shape]) -> float:
    """Return the combined area of all `shapes`.

    Args:
        shapes: Any iterable of Shape instances.

    Returns:
        The sum of each shape's area(); 0 for an empty iterable.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError

