"""
Challenge: Custom Exceptions
Level:     06 - Errors and Parsing
Topics:    defining exception classes, inheritance, exception attributes
Source:    Classic form-validation exercise

========================================================================
YOUR TASK
========================================================================
Two parts:

- Part 1: finish the exception class `ValidationError` (declared below)
  by giving it an `__init__` that stores which input was bad. Its
  subclasses `AgeError` and `EmailError` need no changes.
- Part 2: write `validate_user(name, age, email)`. It checks the three
  inputs and raises the right exception for the first bad one. If all
  three are fine, it returns the cleaned values in a dict.

    validate_user("  Ada ", 36, "Ada@Example.com")
        ->  {'name': 'Ada', 'age': 36, 'email': 'ada@example.com'}

========================================================================
BACKGROUND: WHY CUSTOM EXCEPTIONS?
========================================================================
Built-in exceptions like ValueError are generic. Your own exception
classes let callers catch exactly the problems they care about:

    try:
        validate_user(name, age, email)
    except AgeError:
        print("Please check your age")
    except ValidationError as err:      # any OTHER validation problem
        print(f"Problem with {err.field}")

An exception class is just a class that inherits from `Exception`,
either directly or through another class. ("Inherits from" means "is a
more specific kind of": the new class gets all the parent class's code
for free.) Inheritance forms a HIERARCHY, like a family tree:

    Exception
     +-- ValidationError      <- base for all of this module's errors
          +-- AgeError        <- bad age
          +-- EmailError      <- bad email

An `except` clause catches the class it names AND all of that class's
children. So `except ValidationError` also catches AgeError, because
AgeError inherits from ValidationError. But `except AgeError` does NOT
catch EmailError: they are siblings, not parent and child.

Python uses the FIRST `except` clause that matches. That's why, in the
code above, the more specific AgeError comes before ValidationError.

A custom exception can also carry extra data as attributes. Once you
have written Part 1, this works:

    err = ValidationError("name", "name must not be blank")
    err.field      # -> 'name'
    err.message    # -> 'name must not be blank'
    str(err)       # -> 'name must not be blank'

========================================================================
THE RULES
========================================================================
For Part 1, the exception classes must:
1. Give ValidationError an `__init__(self, field, message)` that:
   - stores `field` (the name of the bad input: "name", "age" or
     "email") as `self.field`
   - stores `message` as `self.message`
   - calls `super().__init__(message)` (the parent class's
     `__init__`), so that `str(err) == message`
2. Leave AgeError and EmailError with NO extra code. They inherit
   ValidationError's `__init__`, so their bodies stay as just the
   docstring.
3. Keep the hierarchy: ValidationError inherits from Exception, and
   AgeError and EmailError inherit from ValidationError. (They are
   already declared that way.)

For Part 2, `validate_user` must:
4. Check name, then age, then email, IN THAT ORDER. Raise on the FIRST
   problem found, and report only that one.
5. name: raise ValidationError with field "name" unless `name` is a
   str that is still non-empty after `.strip()`.
   Use plain ValidationError for name problems. There's no NameError
   subclass, and don't create one: `NameError` is already a built-in
   Python exception!
6. age: raise AgeError with field "age" unless `age` is an int (and
   NOT a bool) between 0 and 150 inclusive (0 and 150 are both
   allowed).
7. email: raise EmailError with field "email" unless ALL of these are
   true:
   - it is a str containing exactly ONE "@"
   - the part before the "@" (the "local part") is not empty
   - the part after the "@" (the "domain") contains at least one ".",
     and does not start or end with "."
   - it has no spaces anywhere
8. Give every raised error `.field` and `.message` attributes. The
   message text is up to you, but it should say what's wrong, like
   "age must be between 0 and 150, got 200". (Tests should check the
   exception TYPE and `.field`, not the exact message.)
9. If everything is fine, return a NEW dict:
   {"name": <name, stripped>, "age": age, "email": <email, lowercased>}

You can assume:
- Nothing about the types: `name`, `age` and `email` can be any value.
  Checking them is the whole job.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    validate_user("  Ada ", 36, "Ada@Example.com")
        ->  {'name': 'Ada', 'age': 36, 'email': 'ada@example.com'}
        The name is stripped and the email is lowercased.

    validate_user("Bob", -1, "bob@example.com")
        ->  raises AgeError: age must be between 0 and 150, got -1
        The age is below 0. (Your message wording may differ.)

    validate_user("Bob", 30, "bob-at-example.com")
        ->  raises EmailError, and err.field is "email"
        There is no "@". `except ValidationError as err` would catch
        it too, because EmailError is a kind of ValidationError.

    validate_user("", -1, "x")
        ->  raises ValidationError, and err.field is "name"
        All three inputs are bad, but the name is checked first.

========================================================================
EDGE CASES TO TEST
========================================================================
- Valid input returns the cleaned dict (stripped name, lowercase
  email)
- Hierarchy: issubclass(AgeError, ValidationError) and
  issubclass(EmailError, ValidationError) are True. But
  issubclass(AgeError, EmailError) is False
- `pytest.raises(ValidationError)` also catches an AgeError
- Bad names: "", "   " and None -> ValidationError with field "name"
- Age boundaries: 0 and 150 are OK. -1, 151, True and 30.0 -> AgeError
- Emails: "a@b.c" is OK. Each of these -> EmailError: "",
  "no-at-sign", "a@@b.com", "a@b@c.com", "@b.com", "a@bcom", "a@.com",
  "a@com.", "a b@c.com"
- Order: a bad name AND a bad age -> the error is about the name
- `excinfo.value.field` is the right field name

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. A custom __init__:
       def __init__(self, field: str, message: str) -> None:
           self.field = field
           ...
           super().__init__(message)
2. Raising: `raise AgeError("age", f"age must be ..., got {age}")`.
3. `email.count("@") == 1` checks for exactly one "@".
4. `local, _, domain = email.partition("@")` splits the email into the
   part before the "@", the "@" itself, and the part after it.
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
- Write `validate_user_all(...)`, which collects EVERY problem and
  raises one `MultipleValidationErrors` containing a list of them.
  (Python 3.11+ also has a built-in `ExceptionGroup` for this: look it
  up!)
- Add a `__repr__` (the method behind repr()) to ValidationError that
  shows the field.
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
