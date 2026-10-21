"""
Challenge: Shapes - Inheritance and Abstract Base Classes
Level:     08 - Classes
Topics:    inheritance, abc.ABC, @abstractmethod, super(), polymorphism
Source:    Classic OOP exercise

========================================================================
YOUR TASK
========================================================================
Finish a small family of shape classes that all share one abstract
parent, `Shape` (provided). Fill in:

- `Shape.describe()`: a text summary, written ONCE, used by all shapes
- `Circle(radius)`: `__init__`, `area()`, `perimeter()`
- `Square(side)`: `__init__`, `area()`, `perimeter()`
- `Triangle(a, b, c)`: `__init__`, `area()`, `perimeter()`
- `total_area(shapes)`: a function that adds up the areas of many shapes

    Square(2).describe()
    # -> 'Square with area 4.00 and perimeter 8.00'

========================================================================
BACKGROUND: INHERITANCE, ABSTRACT CLASSES, POLYMORPHISM
========================================================================
INHERITANCE lets one class (the SUBCLASS or "child") reuse and extend
another (the BASE CLASS or "parent"). `class Circle(Shape):` means "a
Circle is a kind of Shape". It gets all of Shape's methods for free and
can add or override (replace) its own.

An ABSTRACT BASE CLASS (ABC) is a parent that describes WHAT every
subclass must be able to do, without saying HOW. Methods marked
`@abstractmethod` have no real code in the parent. A subclass that
forgets to write them cannot be created: Python raises TypeError when
you try. You also can't create a plain `Shape()` directly.

POLYMORPHISM means code can treat different subclasses the same way.
`total_area(shapes)` just calls `shape.area()` on each item. It doesn't
care whether the item is a Circle, a Square or a Triangle.

HERON'S FORMULA gives a triangle's area from its three sides:

    s    = (a + b + c) / 2                 (the "semi-perimeter")
    area = sqrt(s * (s-a) * (s-b) * (s-c))

    For sides 3, 4, 5:  s = 6
                        area = sqrt(6 * 3 * 2 * 1) = sqrt(36) = 6

THE TRIANGLE INEQUALITY: three lengths only make a triangle if each
side is strictly less than the sum of the other two. 1, 1, 5 fails
(5 is not less than 1 + 1), so the two short sides can't meet. 1, 2, 3
fails too (3 is not LESS than 1 + 2): the sides would lie flat, with
zero area. Such a flat triangle is called "degenerate".

========================================================================
THE RULES
========================================================================
Your code must:

Shape (abstract, provided)
1. Keep Shape abstract: `Shape()` raises TypeError. The stub already
   does this, thanks to ABC + @abstractmethod.
2. `describe()` is written ONCE in Shape and inherited, not copied into
   each subclass. It returns exactly
   f"{type(self).__name__} with area {a:.2f} and perimeter {p:.2f}"
   where a and p are the shape's area and perimeter. `:.2f` rounds to
   2 decimal places: "Square with area 4.00 and perimeter 8.00".

Circle(radius)
3. area = pi * radius**2, perimeter (the circumference) =
   2 * pi * radius. Use math.pi.

Square(side)
4. area = side**2, perimeter = 4 * side.

Triangle(a, b, c), the three side lengths
5. perimeter = a + b + c, area by Heron's formula (see above).
6. Raise `ValueError` if the sides break the triangle inequality:
   you need a < b + c, b < a + c AND c < a + b. Degenerate (flat)
   triangles such as 1, 2, 3 are rejected too.

Every subclass
7. Raise `TypeError` if a dimension is not an int or float. `True`
   and `False` count as NOT numbers (bool is a subclass of int in
   Python, so check for it explicitly).
8. Raise `ValueError` if a dimension is 0 or less.
9. Store the dimensions as public attributes named like the
   constructor parameters: `circle.radius`, `square.side`,
   `triangle.a`, `triangle.b`, `triangle.c`.

total_area(shapes)
10. Return the sum of area() for every shape in the iterable (anything
    you can loop over). An empty iterable gives 0.

General
11. Use only the standard library (math).

You can assume:
- Results are floats. Compare them in tests with pytest.approx.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    Square(2).describe()  ->  'Square with area 4.00 and perimeter 8.00'
        2 * 2 = 4 and 4 * 2 = 8, shown with 2 decimal places.

    round(Circle(1).area(), 5)  ->  3.14159
        pi * 1**2 is pi.

    Triangle(3, 4, 5).area()  ->  6.0
        Heron's formula, worked through above.

    total_area([Square(2), Triangle(3, 4, 5)])  ->  10.0
        4 + 6.0.

    Shape()  ->  raises TypeError
        Python says "Can't instantiate abstract class Shape ...".

========================================================================
EDGE CASES TO TEST
========================================================================
- Shape() -> raises TypeError
- A subclass, defined in your test, that doesn't write area() can't be
  created: calling it raises TypeError
- Circle(1): area == pytest.approx(math.pi),
  perimeter == pytest.approx(2 * math.pi)
- Square(0) and Circle(-1) -> raise ValueError
- Square("2") -> raises TypeError
- Triangle(3, 4, 5): area == 6, perimeter == 12
- Triangle(1, 2, 3) (degenerate) and Triangle(1, 1, 5) -> raise
  ValueError
- describe() uses the right class name for each subclass:
  Circle(1).describe() -> 'Circle with area 3.14 and perimeter 6.28'
- isinstance(Circle(1), Shape) is True
- total_area([]) == 0, and total_area of a mix of shapes is the sum of
  their areas

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. describe() can call self.area() and self.perimeter(). Python runs
   the SUBCLASS's version. That's polymorphism in action.
2. `type(self).__name__` gives the class name as a string ("Circle").
3. Put the shared number checks in a module-level helper function (or
   a method on Shape) so the subclasses don't repeat them.
4. For Heron's formula use `math.sqrt`.
5. total_area: `sum(shape.area() for shape in shapes)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Inheritance and method overriding
- `abc.ABC` and `@abstractmethod`
- Polymorphism and "duck typing" (if it has an area() method, you can
  use it as a shape)
- `type(obj).__name__`, `isinstance`, `issubclass`
- `super().__init__()` (calls the parent's __init__, useful if Shape
  grows its own)
- math.pi, math.sqrt

========================================================================
STRETCH GOALS
========================================================================
- Add Rectangle(width, height) and make Square a subclass of it.
  Discuss: is that a good idea? (Look up the "Liskov substitution
  principle": a subclass should work anywhere its parent does.)
- Add `__repr__` to each shape, such as "Circle(radius=1)".
- Add `__lt__` (the `<` operator) so shapes sort by area with
  sorted([...]).
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

