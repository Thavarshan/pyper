"""
Challenge: Custom Exceptions
Level:     06 - Errors and Parsing
Topics:    defining exception classes, inheritance, exception attributes
Source:    Classic form-validation exercise

========================================================================
WHY CUSTOM EXCEPTIONS?
========================================================================
Built-in exceptions like ValueError are generic. Your own exception
classes let callers catch exactly the problems they care about:

    try:
        validate_user(name, age, email)
    except AgeError:
        print("Please check your age")
    except ValidationError as err:      # any OTHER validation problem
        print(f"Problem with {err.field}")

An exception class is just a class that inherits (directly or
indirectly) from `Exception`. Inheritance forms a HIERARCHY: because
AgeError inherits from ValidationError, `except ValidationError` also
catches AgeError, but `except AgeError` does NOT catch EmailError.

    Exception
     +-- ValidationError      <- base for all of this module's errors
          +-- AgeError        <- bad age
          +-- EmailError      <- bad email

========================================================================
PROBLEM
========================================================================
Part 1 - finish the exception classes below.

The three classes are already declared (so imports work), but they are
empty. Give ValidationError an `__init__(self, field, message)` that:
- stores `field` (the name of the bad input: "name", "age" or "email")
  as `self.field`
- stores `message` as `self.message`
- calls `super().__init__(message)` so `str(err) == message`

AgeError and EmailError need NO extra code: they inherit ValidationError's
`__init__`. (Their bodies can stay as just the docstring.)

Part 2 - `validate_user(name, age, email)`

Check the inputs IN THIS ORDER and raise on the FIRST problem found.
If everything is fine, return a dict
`{"name": <stripped name>, "age": age, "email": <lowercased email>}`.

name  (raise ValidationError with field "name"):
    - must be a str; after `.strip()` it must be non-empty.

age   (raise AgeError with field "age"):
    - must be an int, and NOT a bool.
    - must be between 0 and 150 inclusive.

email (raise EmailError with field "email"):
    - must be a str containing exactly ONE "@".
    - the part before "@" (local part) must be non-empty.
    - the part after "@" (domain) must contain at least one "." and must
      not start or end with ".".
    - no spaces anywhere.

The message text is up to you, but should say what's wrong (e.g.
"age must be between 0 and 150, got 200"). Tests should check the
exception TYPE and the `.field` attribute, not the exact message.

========================================================================
EXAMPLES
========================================================================
    >>> validate_user("  Ada ", 36, "Ada@Example.com")
    {'name': 'Ada', 'age': 36, 'email': 'ada@example.com'}

    >>> validate_user("Bob", -1, "bob@example.com")
    Traceback (most recent call last):
    ...
    AgeError: age must be between 0 and 150, got -1

    >>> try:
    ...     validate_user("Bob", 30, "bob-at-example.com")
    ... except ValidationError as err:
    ...     print(type(err).__name__, err.field)
    EmailError email

========================================================================
CONSTRAINTS
========================================================================
- ValidationError inherits from Exception; AgeError and EmailError
  inherit from ValidationError.
- Every raised error has `.field` and `.message` attributes.
- Check name, then age, then email; report only the first problem.
- Name problems raise plain ValidationError (there's no NameError
  subclass - and don't create one: `NameError` is already a built-in
  Python exception!).
- Return a NEW dict with the cleaned values.

========================================================================
EDGE CASES TO TEST
========================================================================
- Valid input returns the cleaned dict (stripped name, lowercase email)
- Hierarchy: issubclass(AgeError, ValidationError) and
  issubclass(EmailError, ValidationError) are True;
  issubclass(AgeError, EmailError) is False
- `pytest.raises(ValidationError)` also catches an AgeError
- Empty / whitespace-only name, non-str name (e.g. None)
- Age boundaries: 0 and 150 OK; -1 and 151 fail; True and 30.0 fail
- Emails: "a@b.c" OK; "", "no-at-sign", "a@@b.com", "a@b@c.com",
  "@b.com", "a@bcom", "a@.com", "a@com.", "a b@c.com" all fail
- Order: bad name AND bad age -> the error is about the name
- `excinfo.value.field` is the right field name

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Custom __init__:
       def __init__(self, field: str, message: str) -> None:
           self.field = field
           ...
           super().__init__(message)
2. Raising: `raise AgeError("age", f"age must be ..., got {age}")`.
3. `email.count("@") == 1` checks for exactly one "@".
4. `local, _, domain = email.partition("@")` splits it.
5. Write one small helper per field (_check_name, _check_age, ...) to
   keep validate_user short.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Defining classes and inheritance
- Custom exception hierarchies and catching a base class
- `__init__`, `self`, and `super().__init__(...)`
- Exception attributes and `str(exc)`
- Order of `except` clauses (most specific first)
- `pytest.raises(...) as excinfo` and `excinfo.value`

========================================================================
STRETCH GOALS
========================================================================
- `validate_user_all(...)` that collects EVERY problem and raises one
  `MultipleValidationErrors` containing a list of them. (Python 3.11+
  also has the built-in `ExceptionGroup` - look it up!)
- Add a `__repr__` to ValidationError showing the field.
- Add a PhoneError for an optional `phone` argument.
"""

from typing import Any


class ValidationError(Exception):
    """Base class for all validation errors in this module.

    Attributes (to add):
        field: Name of the invalid input ("name", "age" or "email").
        message: Human-readable description of the problem.
    """

    # TODO: add __init__(self, field: str, message: str) that stores
    # self.field and self.message and calls super().__init__(message).


class AgeError(ValidationError):
    """Raised when the age is not a valid int in the range 0..150."""

    # Nothing to add: inherits __init__ from ValidationError.


class EmailError(ValidationError):
    """Raised when the email address is malformed."""

    # Nothing to add: inherits __init__ from ValidationError.


def validate_user(name: Any, age: Any, email: Any) -> dict[str, Any]:
    """Validate user details and return them cleaned.

    Args:
        name: Must be a non-blank str.
        age: Must be an int (not bool) from 0 to 150 inclusive.
        email: Must be a str like "local@domain.tld" (see module docs).

    Returns:
        {"name": stripped name, "age": age, "email": lowercased email}

    Raises:
        ValidationError: With field "name" if the name is invalid.
        AgeError: With field "age" if the age is invalid.
        EmailError: With field "email" if the email is invalid.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
