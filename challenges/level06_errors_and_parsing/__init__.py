"""Level 06 - Errors and Parsing.

Goal: write code that fails loudly and helpfully on bad input, recovers
gracefully where it should, and turns messy text into clean data.
("Parsing" means reading text and turning it into structured values,
like turning "1, 2, 3" into the list [1, 2, 3].)

Concepts covered:
- try / except / else / finally, and catching specific exceptions
- Raising exceptions with helpful messages (ValueError, TypeError, ...)
- Defining your own exception classes, and exception hierarchies
  (families of exceptions where one class inherits from another)
- Adding extra attributes to exceptions (e.g. a line number or field)
- Re-raising and exception chaining (`raise ... from ...`, which keeps
  the original error attached to the new one)
- Input validation: checking early and failing fast
- String parsing: split, strip, partition, str.isdigit, character loops
- Small state machines for parsing (e.g. quoted CSV fields)
- Testing errors with pytest.raises(..., match=...) and excinfo
"""
