"""
Challenge: Valid Parentheses
Level:     10 - Data Structures
Topics:    stacks, dicts as lookup tables, string iteration
Source:    LeetCode #20 "Valid Parentheses"

========================================================================
YOUR TASK
========================================================================
Write `is_valid(s)`. `s` is a string of brackets. Return True if the
brackets are "balanced" (every bracket is closed properly, in the
right order), otherwise False.

    is_valid("{[()]}")  ->  True

========================================================================
WHAT "BALANCED" MEANS
========================================================================
The string uses only these six characters:

    (  )  [  ]  {  }

A string is balanced when all three of these are true:

    1. Every opening bracket is closed by a closing bracket of the
       SAME kind: "(" by ")", "[" by "]", "{" by "}".
    2. Brackets close in the right order: the most recently opened
       bracket that is still open must be closed first.
       "([])" is fine. "([)]" is not: the "[" was opened last, so it
       must be closed before the ")".
    3. No closing bracket appears without a matching opener before it.

========================================================================
WHAT A STACK IS
========================================================================
A STACK is a "last in, first out" collection, like a pile of plates.
You push (add) onto the top and pop (remove) from the top. That is
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
THE RULES
========================================================================
Your function must:
1. Return True if `s` is balanced (rules 1 to 3 above), otherwise
   False.
2. Return True for the empty string "" (there is nothing to balance).

You can assume:
- `s` is a str containing only the characters "()[]{}".
- 0 <= len(s) <= 10_000.
- You do not need to handle other characters. You may treat them as
  invalid input, but the tests will not rely on that.

========================================================================
EXAMPLES
========================================================================
Each line shows a call, then what it should return.

    is_valid("()")      ->  True
        One pair, opened and closed.

    is_valid("()[]{}")  ->  True
        Three pairs, one after another.

    is_valid("([)]")    ->  False
        "[" was opened last, but ")" tries to close first.

    is_valid("{[()]}")  ->  True
        Pairs nested inside each other, each closed in order.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(n): look at each character once, no loop inside a loop.
- Space: O(n): in the worst case ("((((((") the stack holds every
  character.

========================================================================
EDGE CASES TO TEST
========================================================================
- ""        -> True (nothing to balance)
- "("       -> False (never closed)
- ")"       -> False (closing with an empty stack: don't crash!)
- "(]"      -> False (wrong kind)
- "([)]"    -> False (right kinds, wrong order)
- "((()))"  -> True (deep nesting)
- Any odd-length string, like "(()" -> False (it can never be
  balanced, because brackets come in pairs)

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
   opener, return False. Otherwise pop and continue.
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
- Ignore any non-bracket characters, so "a(b[c]d)e" -> True.
- Write `first_error_index(s) -> int`. It returns the index of the
  first character that breaks balance, -1 if `s` is balanced, or
  len(s) if some openers are never closed.
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
