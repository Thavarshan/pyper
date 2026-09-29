"""Level 04 - Dictionaries and Sets.

Goal: learn to reach for a dict or a set whenever you need fast lookups,
counting, grouping or de-duplication, and understand why they turn many
O(n^2) "compare everything with everything" solutions into O(n) ones.

Concepts covered:
- Creating dicts and sets, literal syntax ({} vs set())
- Looking up, inserting and updating keys; `in` membership tests
- dict.get(), dict.setdefault(), dict.items(), dict.keys(), dict.values()
- collections.Counter and collections.defaultdict
- Hashing: why keys/set members must be immutable (str, int, tuple)
- Set operations: union (|), intersection (&), difference (-)
- Dicts remember insertion order (Python 3.7+)
- Sorting with key functions, e.g. sorted(items, key=lambda kv: ...)
- Classic "hash map" interview patterns (two sum, anagrams, first unique)
"""
