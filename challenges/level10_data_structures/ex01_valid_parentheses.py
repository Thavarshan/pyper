"""
Challenge: Valid Parentheses
Level:     10 - Data Structures
Topics:    stacks, dicts as lookup tables, string iteration
Source:    LeetCode #20 "Valid Parentheses"

========================================================================
PROBLEM
========================================================================
You are given a string made up only of the six bracket characters

    (  )  [  ]  {  }

Decide whether the brackets are "balanced". A string is balanced when:

    1. Every opening bracket is eventually closed by a closing bracket
       of the SAME kind: "(" by ")", "[" by "]", "{" by "}".
    2. Brackets close in the correct order: the most recently opened,
       still-unclosed bracket must be the first one to be closed.
       "([])" is fine, but "([)]" is not - the "[" was opened last, so
       it must be closed before the ")".
    3. No closing bracket appears without a matching opener before it.

Return True if the string is balanced, False otherwise.

What is a STACK? A stack is a "last in, first out" collection - think of
a pile of plates. You push onto the top and pop from the top. That is
exactly rule 2: the last bracket opened is the first one that must be
closed. Watch the stack while scanning "{[()]}":

    char   action         stack (top on the right)
    ----   ------------   ------------------------
     {     push           {
     [     push           { [
     (     push           { [ (
     )     pop "(" ok     { [
     ]     pop "[" ok     {
     }     pop "{" ok     (empty)  -> balanced!

========================================================================
EXAMPLES
========================================================================
    >>> is_valid("()")
    True

    >>> is_valid("()[]{}")
    True

    >>> is_valid("([)]")
    False

    >>> is_valid("{[()]}")
    True

========================================================================
CONSTRAINTS
========================================================================
- `s` is a str containing only the characters "()[]{}".
- 0 <= len(s) <= 10_000.
- The empty string counts as balanced -> True.
- You do not need to handle other characters (you may treat them as
  invalid input, but tests will not rely on that).

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n) - look at each character once.
- Space: O(n) - in the worst case ("((((((") the stack holds every char.

========================================================================
EDGE CASES TO TEST
========================================================================
- ""        -> True (nothing to balance)
- "("       -> False (never closed)
- ")"       -> False (closing with an empty stack - don't crash!)
- "(]"      -> False (wrong kind)
- "([)]"    -> False (right kinds, wrong order)
- "((()))"  -> True (deep nesting)
- An odd-length string can never be balanced

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. A Python list is a stack: `.append()` to push, `.pop()` to pop,
   `stack[-1]` to peek at the top.
2. Opening brackets always get pushed. Closing brackets are where the
   checking happens.
3. A dict like {")": "(", "]": "[", "}": "{"} maps each closer to the
   opener it needs, so you avoid a long if/elif chain.
4. On a closer: if the stack is empty OR the top is not the matching
   opener -> return False. Otherwise pop and continue.
5. After the loop, the string is balanced only if the stack is empty.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- Using a `list` as a stack (append / pop / [-1])
- Dicts as lookup tables instead of if/elif chains
- `in` for membership tests on dicts (checks keys) and strings
- Truthiness: `if not stack:` is True when the list is empty
- Early `return` to stop as soon as you know the answer

========================================================================
STRETCH GOALS
========================================================================
- Ignore any non-bracket characters so "a(b[c]d)e" -> True.
- Write `first_error_index(s) -> int` returning the index of the first
  character that breaks balance (or -1 if balanced / len(s) if some
  openers are never closed).
"""


def is_valid(s: str) -> bool:
    """Return True if the brackets in `s` are balanced.

    Args:
        s: A string made only of the characters "()[]{}".

    Returns:
        True if every bracket is closed by the same kind in the correct
        order, otherwise False. The empty string returns True.
    """
    # TODO: implement me, then make your tests pass.
    raise NotImplementedError
