"""Level 04 - Dictionaries and Sets.

Goal: learn to reach for a dict or a set whenever you need fast lookups,
counting, grouping or removing duplicates. Understand why they turn
many "compare everything with everything" solutions into much faster
ones: from O(n^2), where the work grows with the SQUARE of the input
size, to O(n), where it grows in step with the input size.

Concepts covered:
- Creating dicts and sets, and the literal syntax ({} is an empty
  dict, set() is an empty set)
- Looking up, inserting and updating keys, and `in` membership tests
- dict.get(), dict.setdefault(), dict.items(), dict.keys(), dict.values()
- collections.Counter and collections.defaultdict
- Hashing: why dict keys and set members must be immutable
  (unchangeable), like str, int and tuple
- Set operations: union (|), intersection (&), difference (-)
- Dicts remember insertion order (Python 3.7+)
- Sorting with key functions (a function that says what to sort by),
  e.g. sorted(items, key=lambda kv: ...)
- Classic "hash map" interview patterns (two sum, anagrams, first
  unique). "Hash map" is the general name for what Python calls a dict.
"""
