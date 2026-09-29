"""
Challenge: 2D Vector with Operator Overloading
Level:     08 - Classes
Topics:    magic / dunder methods, operator overloading, NotImplemented
Source:    Classic OOP exercise (inspired by "Fluent Python", ch. 1)

========================================================================
PROBLEM
========================================================================
MAGIC METHODS (also called DUNDER methods, from "Double UNDERscore")
are specially named methods Python calls behind the scenes when you use
built-in syntax on your objects:

    v + w      calls  v.__add__(w)
    v - w      calls  v.__sub__(w)
    v * 3      calls  v.__mul__(3)
    3 * v      calls  (3).__mul__(v) first - int doesn't know Vectors, so
               it returns NotImplemented and Python then tries
               v.__rmul__(3)   ("r" = reflected / right-hand side)
    abs(v)     calls  v.__abs__()
    v == w     calls  v.__eq__(w)
    repr(v)    calls  v.__repr__()

Defining these is called OPERATOR OVERLOADING. It lets your own types
feel like built-in ones.

When an operator method gets an operand it doesn't support, it should
`return NotImplemented` (a special built-in constant - NOT raise
NotImplementedError). Python then tries the other operand's method,
and if nothing works it raises TypeError for you. So
`Vector2D(1, 2) + 5` ends up raising TypeError.

Build `Vector2D(x, y)`, a 2D vector (an arrow from the origin to the
point (x, y)):

    Vector2D(x, y)     x and y are int or float (not bool), else
                       TypeError. Store them as attributes .x and .y.
                       Vectors are treated as immutable: operations
                       always return NEW vectors and never change self.

    v + w              Vector2D(v.x + w.x, v.y + w.y)
    v - w              Vector2D(v.x - w.x, v.y - w.y)
    v * k, k * v       Scalar multiplication: Vector2D(v.x * k, v.y * k)
                       where k is an int or float (not bool). Multiplying
                       by another Vector2D is NOT supported -> TypeError
                       (use dot() for that).
    abs(v)             MAGNITUDE (length): sqrt(x**2 + y**2), a float.
                       abs(Vector2D(3, 4)) == 5.0
    v == w             True when x and y are both equal. Comparing with
                       a non-Vector2D returns NotImplemented (-> False).
    repr(v)            Exactly:  Vector2D(3, 4)   or   Vector2D(1.5, -2)
                       i.e. f"Vector2D({x!r}, {y!r})"
    v.dot(w)           DOT PRODUCT: v.x * w.x + v.y * w.y (a number).
                       w must be a Vector2D, else TypeError.
    v.normalized()     A new vector pointing the same way with magnitude
                       1: Vector2D(x / |v|, y / |v|).
                       DECISION: the zero vector Vector2D(0, 0) has no
                       direction, so normalized() raises ValueError
                       ("cannot normalize the zero vector").

Because we define __eq__ and the vector is immutable-by-convention, also
define __hash__ as hash((x, y)) so vectors can be used in sets and as
dict keys.

========================================================================
EXAMPLES
========================================================================
    >>> v = Vector2D(3, 4)
    >>> v + Vector2D(1, 1)
    Vector2D(4, 5)
    >>> v - Vector2D(1, 1)
    Vector2D(2, 3)
    >>> v * 2
    Vector2D(6, 8)
    >>> 2 * v
    Vector2D(6, 8)
    >>> abs(v)
    5.0
    >>> v.dot(Vector2D(1, 0))
    3
    >>> v.normalized()
    Vector2D(0.6, 0.8)

========================================================================
CONSTRAINTS
========================================================================
- Components: int or float, never bool (TypeError).
- Operators return NotImplemented for unsupported operand types (so the
  user sees TypeError), they don't raise directly.
- Never modify self or the other operand.
- normalized() of the zero vector -> ValueError.
- Compare float results with pytest.approx (e.g. on .x and .y).

========================================================================
EDGE CASES TO TEST
========================================================================
- Adding / subtracting the zero vector changes nothing
- v - v == Vector2D(0, 0)
- Both v * 3 and 3 * v work and are equal
- v * 0 gives the zero vector; v * -1 flips direction
- v + 5, v * v, v * "2" -> TypeError
- abs of the zero vector is 0.0; abs(Vector2D(-3, -4)) == 5.0
- dot of perpendicular vectors is 0
- normalized() has magnitude ~1 and the original is unchanged
- Vector2D(0, 0).normalized() -> ValueError
- Vector2D(1, 2) == Vector2D(1, 2); != Vector2D(2, 1); != (1, 2)
- Equal vectors have equal hashes; {Vector2D(1, 2), Vector2D(1, 2)}
  has length 1
- repr exact format for ints and floats
- Vector2D("1", 2), Vector2D(True, 2) -> TypeError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start each operator with a type check:
       if not isinstance(other, Vector2D):
           return NotImplemented
2. For scalar multiplication, check for a number that isn't a bool.
3. __rmul__ can simply `return self * scalar` (i.e. call __mul__),
   because scalar multiplication is commutative.
4. `math.hypot(x, y)` computes sqrt(x**2 + y**2) accurately.
5. In normalized(), compute the magnitude once and check it for zero
   before dividing.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Magic / dunder methods and operator overloading
- Reflected operators (__rmul__, __radd__)
- NotImplemented vs NotImplementedError
- __eq__ together with __hash__
- Immutability by convention
- math.hypot / math.sqrt

========================================================================
STRETCH GOALS
========================================================================
- Add __neg__ (-v), __truediv__ (v / k) and __bool__ (zero vector is
  falsy).
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

