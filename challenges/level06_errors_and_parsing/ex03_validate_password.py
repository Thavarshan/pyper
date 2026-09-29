"""
Challenge: Validate Password
Level:     06 - Errors and Parsing
Topics:    input validation, str methods, any(), collecting errors
Source:    Classic validation exercise

========================================================================
PROBLEM
========================================================================
Many sign-up forms check passwords against a set of rules and tell you
EVERY rule you broke at once (instead of one at a time). Write
`validate_password(pw)` that returns a list of the names of every rule
the password fails. An empty list means the password is valid.

The rules, their EXACT names, and the order they must appear in the
returned list:

    Order  Rule name        Fails when...
    -----  ---------------  -------------------------------------------
    1      "too_short"      len(pw) < 8
    2      "no_uppercase"   there is no uppercase letter (str.isupper)
    3      "no_lowercase"   there is no lowercase letter (str.islower)
    4      "no_digit"       there is no digit character (str.isdigit)
    5      "no_symbol"      there is no "symbol", i.e. no character
                            from string.punctuation:
                            !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~

Notes:
- Spaces are allowed in passwords but do NOT count as symbols.
- Always return the failed names in the table order above.

Then write `is_strong(pw)` that returns True if the password passes
every rule, else False. It must reuse `validate_password`.

If `pw` is not a str (e.g. None or 12345678), raise `TypeError` from
BOTH functions.

========================================================================
EXAMPLES
========================================================================
    >>> validate_password("Abcdef1!")
    []

    >>> validate_password("abc")
    ['too_short', 'no_uppercase', 'no_digit', 'no_symbol']

    >>> validate_password("PASSWORD123")
    ['no_lowercase', 'no_symbol']

    >>> is_strong("Tr0ub4dor&3")
    True

    >>> is_strong("password")
    False

========================================================================
CONSTRAINTS
========================================================================
- Return type is `list[str]`, rule names exactly as in the table, in
  table order, each at most once.
- Exactly 8 characters is long enough (the rule is "< 8").
- Non-str input -> `TypeError` (message is up to you).
- is_strong returns a real bool.

========================================================================
EDGE CASES TO TEST
========================================================================
- A valid password -> []
- Empty string "" -> all five rule names
- Exactly 7 chars vs exactly 8 chars (boundary!)
- Only one rule broken each time (one test per rule)
- A space is not a symbol: "Abcdefg1 " -> ["no_symbol"]
- Order of the returned names always matches the table
- None / int input -> TypeError
- is_strong agrees with validate_password on several inputs

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with `failures = []` and append a name for every failed check.
   Checking in table order gives you the right output order for free.
2. `any(ch.isupper() for ch in pw)` is True if at least one character
   is uppercase.
3. `import string` and test `ch in string.punctuation` for symbols.
4. is_strong is a one-liner: `return not validate_password(pw)` (an
   empty list is falsy) or `== []`.
5. Type check: `if not isinstance(pw, str): raise TypeError(...)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- str methods: isupper, islower, isdigit
- `any()` / `all()` with generator expressions
- The `string` module constants
- Collecting all errors vs failing fast on the first one
- Guard clauses and `isinstance` type checks
- `@pytest.mark.parametrize` - perfect for testing each rule

========================================================================
STRETCH GOALS
========================================================================
- Make the rules data-driven: a list of (name, check_function) pairs,
  so adding a rule means adding one line.
- Add a "common_password" rule that fails for anything in a small set
  like {"password1!", "Qwerty123!"} (compare case-insensitively).
- Add "no_repeats": fails if any character appears 3+ times in a row.
"""


def validate_password(pw: str) -> list[str]:
    """Return the names of every password rule that pw fails.

    Args:
        pw: The password to check.

    Returns:
        A list of rule names in this order (only the failed ones):
        "too_short", "no_uppercase", "no_lowercase", "no_digit",
        "no_symbol". Empty if the password is valid.

    Raises:
        TypeError: If pw is not a str.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def is_strong(pw: str) -> bool:
    """Return True if pw passes every rule in validate_password.

    Args:
        pw: The password to check.

    Returns:
        True if there are no failed rules, else False.

    Raises:
        TypeError: If pw is not a str.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
