"""
Challenge: Caesar Cipher
Level:     02 - Strings
Topics:    ord(), chr(), modulo arithmetic, str.isupper(), building strings
Source:    Classic cryptography exercise

========================================================================
PROBLEM
========================================================================
The Caesar cipher is one of the oldest ways to hide a message. Each
letter is replaced by the letter a fixed number of positions (the SHIFT)
further along the alphabet. With a shift of 3:

    A -> D,  B -> E,  ...,  W -> Z,  X -> A,  Y -> B,  Z -> C

Notice how it WRAPS AROUND: after Z it starts again at A.

Write two functions:

1. `encrypt(text, shift)` shifts every letter FORWARD by `shift`.
2. `decrypt(text, shift)` undoes encrypt, shifting BACKWARD by `shift`,
   so that decrypt(encrypt(text, k), k) == text for any k.

Rules:
    - Only the 26 English letters A-Z / a-z are shifted.
    - CASE IS PRESERVED: upper-case stays upper, lower-case stays lower.
    - Everything else (digits, spaces, punctuation, accented letters,
      emoji) is copied through UNCHANGED.
    - `shift` may be ANY int: negative (shift backwards), 0 (no change),
      or larger than 26 (a shift of 29 is the same as a shift of 3).

========================================================================
EXAMPLES
========================================================================
    >>> encrypt("abc", 1)
    'bcd'

    >>> encrypt("Hello, World!", 3)
    'Khoor, Zruog!'

    >>> encrypt("xyz", 3)
    'abc'

    >>> decrypt("Khoor, Zruog!", 3)
    'Hello, World!'

========================================================================
CONSTRAINTS
========================================================================
- `text` is a str (may be empty). `shift` is an int.
- Return a new string of the SAME length as `text`.
- encrypt(text, -k) == decrypt(text, k).
- encrypt(text, 26) == text, and encrypt(text, 0) == text.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string -> ""
- Wrap-around at the end of the alphabet ("z" + 1 -> "a", "Z" + 1 -> "A")
- Negative shift ("a" - 1 -> "z")
- Shift of 0 and shift of 26 -> unchanged
- Large shifts (27, 52, 1000) behave like shift % 26
- Case preserved in mixed-case text
- Digits, spaces, punctuation unchanged
- Round trip: decrypt(encrypt(t, k), k) == t for several k

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. `ord("a")` gives the number (code point) of a character: 97.
   `chr(97)` goes back: "a". Letters are consecutive: ord("b") == 98.
2. For a lower-case letter, its position in the alphabet is
   ord(ch) - ord("a"), a number from 0 to 25.
3. new_position = (position + shift) % 26. In Python `%` always returns
   a non-negative result for a positive divisor, so negative shifts wrap
   correctly: (0 - 1) % 26 == 25.
4. decrypt can simply call encrypt with -shift.
5. Build a list of characters and "".join() it at the end. Use
   `"a" <= ch <= "z"` (not ch.isalpha(), which is True for accented
   letters too) to test for plain lower-case letters.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `ord()` and `chr()`: characters are numbers underneath
- Modulo for wrap-around arithmetic (clocks, alphabets, circular lists)
- Comparing characters with < and > (they compare by code point)
- `str.isupper()` / `str.islower()`
- Building strings with a list and "".join()

========================================================================
STRETCH GOALS
========================================================================
- Solve it with `str.maketrans()` and `str.translate()`.
- Write `crack(ciphertext) -> int` that guesses the shift by assuming
  the most common letter in English text is "e".
- Implement the Vigenere cipher, which uses a keyword instead of a
  single shift.
"""


def encrypt(text: str, shift: int) -> str:
    """Encrypt `text` with a Caesar cipher.

    Args:
        text: The message to encrypt.
        shift: How many positions to move each letter forward. May be
            negative or larger than 26.

    Returns:
        The encrypted text. Letters are shifted with wrap-around and keep
        their case; all other characters are unchanged.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError


def decrypt(text: str, shift: int) -> str:
    """Decrypt text that was encrypted with `encrypt(..., shift)`.

    Args:
        text: The encrypted message.
        shift: The shift that was used to encrypt it.

    Returns:
        The original text.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
