r"""
Challenge: Validate Password
Level:     06 - Errors and Parsing
Topics:    input validation, str methods, any(), collecting errors
Source:    Classic validation exercise

========================================================================
YOUR TASK
========================================================================
Many sign-up forms tell you EVERY password rule you broke at once,
instead of one at a time. Write `validate_password(pw)`. It checks a
password against five rules and returns a list of the names of every
rule it fails. An empty list means the password is valid. Then write
`is_strong(pw)`, which returns True only when no rule fails.

    validate_password("abc")
        ->  ['too_short', 'no_uppercase', 'no_digit', 'no_symbol']

========================================================================
THE RULES
========================================================================
These are the five password rules. Each has an EXACT name, and the
returned list must use this order:

    Order  Rule name        Fails when...
    -----  ---------------  -------------------------------------------
    1      "too_short"      len(pw) < 8
    2      "no_uppercase"   there is no uppercase letter (str.isupper)
    3      "no_lowercase"   there is no lowercase letter (str.islower)
    4      "no_digit"       there is no digit character (str.isdigit)
    5      "no_symbol"      there is no "symbol": no character from
                            string.punctuation, which is
                            !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

Your functions must:
1. `validate_password`: return a `list[str]` with the name of every
   rule that `pw` fails, each name at most once, in the table order.
2. Return [] when the password passes every rule.
3. Treat exactly 8 characters as long enough (the rule is "< 8").
4. Allow spaces in passwords, but NOT count a space as a symbol.
5. `is_strong`: return True if the password passes every rule, else
   False. Return a real bool, and reuse `validate_password` to decide.
6. Both functions: raise `TypeError` if `pw` is not a str (for example
   None or 12345678). The message is up to you.

You can assume:
- When `pw` is a str, it may contain any characters.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    validate_password("Abcdef1!")     ->  []
        8 characters, with an uppercase letter, a lowercase letter, a
        digit and a symbol.

    validate_password("abc")
        ->  ['too_short', 'no_uppercase', 'no_digit', 'no_symbol']
        Only the lowercase rule passes. The names come in table order.

    validate_password("PASSWORD123")  ->  ['no_lowercase', 'no_symbol']
        Long enough, with uppercase letters and digits, but no
        lowercase letter and no symbol.

    is_strong("Tr0ub4dor&3")          ->  True
        It passes all five rules ("&" is the symbol).

    is_strong("password")             ->  False
        validate_password gives a non-empty list for it.

========================================================================
EDGE CASES TO TEST
========================================================================
- A valid password -> []
- Empty string "" -> all five rule names, in table order
- The length boundary: "Abcde1!" (7 characters) -> ['too_short'], and
  "Abcdef1!" (8 characters) -> []
- One rule broken at a time (one test per rule)
- A space is not a symbol: "Abcdefg1 " -> ['no_symbol']
- The returned names always come in table order
- None or an int -> TypeError
- is_strong agrees with validate_password on several inputs

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Start with `failures = []` and append a name for every failed
   check. If you check in table order, you get the right output order
   for free.
2. `any(ch.isupper() for ch in pw)` is True if at least one character
   is uppercase.
3. `import string`, then test `ch in string.punctuation` for symbols.
4. is_strong is a one-liner: `return not validate_password(pw)`. (An
   empty list is falsy, meaning `if` treats it as False, so
   `not []` is True.) Comparing with `== []` works too.
5. Type check: `if not isinstance(pw, str): raise TypeError(...)`.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- str methods: isupper, islower, isdigit
- `any()` / `all()` with generator expressions
- The `string` module constants
- Collecting all errors vs failing fast on the first one
- Guard clauses (early checks at the top of a function) and
  `isinstance` type checks
- `@pytest.mark.parametrize` (runs one test with many inputs): perfect
  for testing each rule

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
