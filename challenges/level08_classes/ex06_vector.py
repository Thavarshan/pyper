"""
Challenge: 2D Vector with Operator Overloading
Level:     08 - Classes
Topics:    magic / dunder methods, operator overloading, NotImplemented
Source:    Classic OOP exercise (inspired by "Fluent Python", ch. 1)

========================================================================
YOUR TASK
========================================================================
Write a `Vector2D(x, y)` class: a 2D vector (an arrow from the origin
(0, 0) to the point (x, y)) that works with Python's normal operators.
Fill in:

- `__init__(x, y)`: check and store x and y
- `__add__` / `__sub__`: make `v + w` and `v - w` work
- `__mul__` / `__rmul__`: make `v * 3` and `3 * v` work
- `__abs__`: make `abs(v)` give the vector's length
- `__eq__` / `__hash__`: make `==` work, and allow use in sets
- `__repr__`: describe it, as in "Vector2D(3, 4)"
- `dot(w)`: return the dot product (a number)
- `normalized()`: return a vector of length 1 in the same direction

    Vector2D(3, 4) + Vector2D(1, 1)    # -> Vector2D(4, 5)

========================================================================
WHAT "OPERATOR OVERLOADING" MEANS
========================================================================
MAGIC METHODS (also called DUNDER methods, from "Double UNDERscore")
are specially named methods that Python calls behind the scenes when
you use built-in syntax on your objects:

    v + w      calls  v.__add__(w)
    v - w      calls  v.__sub__(w)
    v * 3      calls  v.__mul__(3)
    3 * v      calls  (3).__mul__(v) first. int doesn't know about
               Vectors, so it returns NotImplemented, and Python then
               tries v.__rmul__(3)   ("r" = reflected, right-hand side)
    abs(v)     calls  v.__abs__()
    v == w     calls  v.__eq__(w)
    repr(v)    calls  v.__repr__()

Defining these is called OPERATOR OVERLOADING. It lets your own types
feel like built-in ones.

When an operator method gets something it doesn't support, it should
`return NotImplemented`. That is a special built-in value, NOT the
NotImplementedError exception, and you return it, not raise it. Python
then tries the other operand's method. If nothing works, Python raises
TypeError for you. So `Vector2D(1, 2) + 5` ends up raising TypeError.

Some vector maths:

    MAGNITUDE (length):  sqrt(x**2 + y**2)
                         abs(Vector2D(3, 4)) = sqrt(9 + 16) = 5.0
    DOT PRODUCT:         v.x * w.x + v.y * w.y
                         Vector2D(3, 4).dot(Vector2D(1, 0)) = 3 + 0 = 3
                         It is 0 when the arrows are at right angles.
    NORMALIZED:          same direction, length 1: divide x and y by the
                         magnitude. Vector2D(3, 4) -> Vector2D(0.6, 0.8)

========================================================================
THE RULES
========================================================================
Your class must:

Creating
1. Accept x and y only as int or float. Anything else, including
   `True`/`False`, raises `TypeError`. (bool is a subclass of int in
   Python, so check for it explicitly.)
2. Store them as attributes `.x` and `.y`.
3. Treat vectors as immutable (never changed after creation):
   operations always return NEW vectors and never change self or the
   other operand.

Operators
4. `v + w` returns Vector2D(v.x + w.x, v.y + w.y).
5. `v - w` returns Vector2D(v.x - w.x, v.y - w.y).
6. `v * k` and `k * v` return Vector2D(v.x * k, v.y * k), where k is
   an int or float (not bool). This is "scalar multiplication"
   (scaling by a plain number). Multiplying by another Vector2D is NOT
   supported, so it ends in TypeError (use dot() for that).
7. `abs(v)` returns the magnitude as a float.
8. `v == w` is True when x and y are both equal.
9. Every operator method returns `NotImplemented` (it does not raise)
   for an operand type it doesn't support. Python then turns that into
   TypeError for the user, or False for `==`.
10. `__hash__` returns hash((x, y)), so equal vectors have equal hashes
    and vectors can go in sets and be dict keys. (Defining __eq__
    alone would make Python switch hashing off.)
11. `repr(v)` returns exactly f"Vector2D({x!r}, {y!r})", such as
    Vector2D(3, 4) or Vector2D(1.5, -2).

Methods
12. `v.dot(w)` returns v.x * w.x + v.y * w.y. If w is not a Vector2D,
    raise `TypeError`.
13. `v.normalized()` returns a NEW vector Vector2D(x / |v|, y / |v|),
    where |v| is the magnitude. The zero vector Vector2D(0, 0) has no
    direction, so for it raise
    ValueError("cannot normalize the zero vector").

You can assume:
- Float results are not exact. Compare them in tests with
  pytest.approx (for example on .x and .y).

========================================================================
EXAMPLES
========================================================================
A short script. Each `# ->` comment shows what that line returns.

    v = Vector2D(3, 4)
    v + Vector2D(1, 1)       # -> Vector2D(4, 5)
    v - Vector2D(1, 1)       # -> Vector2D(2, 3)
    v * 2                    # -> Vector2D(6, 8)
    2 * v                    # -> Vector2D(6, 8)   (uses __rmul__)
    abs(v)                   # -> 5.0
    v.dot(Vector2D(1, 0))    # -> 3
    v.normalized()           # -> Vector2D(0.6, 0.8)
    v                        # -> Vector2D(3, 4)   (unchanged)

    v + 5                    # raises TypeError
    Vector2D(0, 0).normalized()   # raises ValueError

========================================================================
EDGE CASES TO TEST
========================================================================
- Adding or subtracting the zero vector changes nothing:
  v + Vector2D(0, 0) == v
- v - v == Vector2D(0, 0)
- Both v * 3 and 3 * v work and are equal
- v * 0 gives the zero vector, and v * -1 flips the direction:
  Vector2D(3, 4) * -1 == Vector2D(-3, -4)
- v + 5, v * v and v * "2" -> raise TypeError
- abs(Vector2D(0, 0)) == 0.0 and abs(Vector2D(-3, -4)) == 5.0
- The dot product of perpendicular (right-angled) vectors is 0:
  Vector2D(1, 2).dot(Vector2D(-2, 1)) == 0
- normalized() has magnitude about 1 (use pytest.approx), and the
  original vector is unchanged
- Vector2D(0, 0).normalized() -> raises ValueError
- Vector2D(1, 2) == Vector2D(1, 2), but != Vector2D(2, 1) and
  != (1, 2)
- Equal vectors have equal hashes, and {Vector2D(1, 2), Vector2D(1, 2)}
  has length 1
- Exact repr: repr(Vector2D(3, 4)) -> "Vector2D(3, 4)",
  repr(Vector2D(1.5, -2)) -> "Vector2D(1.5, -2)"
- Vector2D("1", 2) and Vector2D(True, 2) -> raise TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start each operator with a type check:
       if not isinstance(other, Vector2D):
           return NotImplemented
2. For scalar multiplication, check for a number that isn't a bool.
3. __rmul__ can simply `return self.__mul__(scalar)`, because
   3 * v and v * 3 give the same answer. Call the method directly
   rather than writing `self * scalar`: the method hands
   NotImplemented straight back, while `self * scalar` would raise
   TypeError itself (rule 9 says operator methods return
   NotImplemented instead of raising).
4. `math.hypot(x, y)` works out sqrt(x**2 + y**2) accurately.
5. In normalized(), work out the magnitude once and check it for zero
   before dividing.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Magic / dunder methods and operator overloading
- Reflected operators (__rmul__, __radd__)
- NotImplemented vs NotImplementedError
- __eq__ together with __hash__
- Immutability by convention (nothing stops changes, but you agree
  not to make any)
- math.hypot / math.sqrt

========================================================================
STRETCH GOALS
========================================================================
- Add __neg__ (-v), __truediv__ (v / k) and __bool__ (so the zero
  vector is falsy: treated as False by `if`).
- Add __iter__ so `x, y = v` works (tuple unpacking).
- Enforce true immutability with __slots__ and read-only properties.
- Add `angle()` returning the direction in radians (math.atan2).
"""

import math  # for you to use in your implementation


class Vector2D:
    """An immutable-by-convention 2D vector."""

    def __init__(self, x: float, y: float) -> None:
        """Create a vector.

        Args:
            x: Horizontal component (int or float, not bool).
            y: Vertical component (int or float, not bool).

        Raises:
            TypeError: If a component is not an int/float, or is a bool.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __add__(self, other: object) -> "Vector2D":
        """Return self + other, or NotImplemented for non-vectors."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __sub__(self, other: object) -> "Vector2D":
        """Return self - other, or NotImplemented for non-vectors."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __mul__(self, scalar: object) -> "Vector2D":
        """Return self scaled by a number, or NotImplemented otherwise."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __rmul__(self, scalar: object) -> "Vector2D":
        """Support `number * vector` (same result as vector * number)."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __abs__(self) -> float:
        """Return the magnitude sqrt(x**2 + y**2) as a float."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """Equal when both components match; NotImplemented for non-vectors."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __hash__(self) -> int:
        """Return hash((x, y)) so equal vectors hash equally."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __repr__(self) -> str:
        """Return e.g. "Vector2D(3, 4)"."""
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def dot(self, other: "Vector2D") -> float:
        """Return the dot product self.x * other.x + self.y * other.y.

        Raises:
            TypeError: If `other` is not a Vector2D.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def normalized(self) -> "Vector2D":
        """Return a new unit-length vector in the same direction.

        Raises:
            ValueError: If this is the zero vector.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

