"""
Challenge: Caesar Cipher
Level:     02 - Strings
Topics:    ord(), chr(), modulo arithmetic, str.isupper(), building strings
Source:    Classic cryptography exercise

========================================================================
YOUR TASK
========================================================================
Write two functions:

    encrypt(text, shift)  moves every letter FORWARD `shift` places in
                          the alphabet.
    decrypt(text, shift)  undoes encrypt by moving every letter
                          BACKWARD `shift` places.

    encrypt("Hello, World!", 3)  ->  'Khoor, Zruog!'

========================================================================
WHAT A "CAESAR CIPHER" IS
========================================================================
The Caesar cipher is one of the oldest ways to hide a message. Each
letter is replaced by the letter a fixed number of places (the SHIFT)
further along the alphabet. With a shift of 3:

    A -> D,  B -> E,  ...,  W -> Z,  X -> A,  Y -> B,  Z -> C

Notice how it WRAPS AROUND: after Z it starts again at A. Like a clock,
26 steps bring you back to where you started. So a shift of 26 changes
nothing, and a shift of 29 is the same as a shift of 3 (29 = 26 + 3).
A negative shift moves backward: a shift of -1 turns "a" into "z".

========================================================================
THE RULES
========================================================================
Your functions must:
1. Shift only the 26 English letters A-Z and a-z.
2. Keep each letter's case: upper-case stays upper, lower-case stays
   lower.
3. Copy everything else through UNCHANGED: digits, spaces,
   punctuation, accented letters and emoji.
4. Accept ANY int as `shift`, with wrap-around: negative shifts move
   backward, and 0 or 26 leave the text unchanged
   (encrypt(text, 0) == text and encrypt(text, 26) == text). A shift
   bigger than 26 wraps too: 29 acts like 3.
5. Return a new string of the SAME length as `text`.
6. Make `decrypt` undo `encrypt`: decrypt(encrypt(text, k), k) == text
   for any k.
7. Make encrypt(text, -k) give the same result as decrypt(text, k).

You can assume:
- `text` is a str. It may be empty.
- `shift` is an int.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    encrypt("abc", 1)            ->  'bcd'
        Each letter moves one place forward.

    encrypt("Hello, World!", 3)  ->  'Khoor, Zruog!'
        Letters move 3 places and keep their case. The comma, space
        and "!" stay as they are.

    encrypt("xyz", 3)            ->  'abc'
        x, y and z run past the end of the alphabet and wrap around
        to a, b and c.

    decrypt("Khoor, Zruog!", 3)  ->  'Hello, World!'
        Moving 3 places backward undoes the encryption.

========================================================================
EDGE CASES TO TEST
========================================================================
- Empty string: encrypt("", 5) -> ''
- Wrap-around at the end of the alphabet: encrypt("z", 1) -> 'a' and
  encrypt("Z", 1) -> 'A'
- Negative shift: encrypt("a", -1) -> 'z'
- Shift of 0 and shift of 26: encrypt("Hi!", 0) -> 'Hi!' and
  encrypt("Hi!", 26) -> 'Hi!'
- Large shifts behave like shift % 26 (the remainder after dividing by
  26): encrypt("abc", 27) -> 'bcd', encrypt("abc", 52) -> 'abc', and
  encrypt("abc", 1000) -> 'mno' (1000 % 26 is 12)
- Case is kept in mixed-case text: encrypt("AbC", 1) -> 'BcD'
- Digits, spaces and punctuation are unchanged:
  encrypt("a1 b!", 5) -> 'f1 g!'
- Round trip: decrypt(encrypt(t, k), k) == t for several k, such as
  -30, 0, 3 and 1000

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
   `"a" <= ch <= "z"` to test for plain lower-case letters. Don't use
   ch.isalpha(), which is True for accented letters too.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `ord()` and `chr()`: characters are numbers underneath
- Modulo (`%`, the remainder) for wrap-around arithmetic (clocks,
  alphabets, circular lists)
- Comparing characters with < and > (they compare by code point)
- `str.isupper()` / `str.islower()`
- Building strings with a list and "".join()

========================================================================
STRETCH GOALS
========================================================================
- Solve it with `str.maketrans()` and `str.translate()` (build a table
  saying which letter becomes which, then apply it in one go).
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
