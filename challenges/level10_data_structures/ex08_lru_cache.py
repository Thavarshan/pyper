"""
Challenge: LRU Cache
Level:     10 - Data Structures
Topics:    hash maps, collections.OrderedDict, doubly linked lists, class design
Source:    LeetCode #146 "LRU Cache"

========================================================================
YOUR TASK
========================================================================
Write a class `LRUCache`: a small key -> value store with a size
limit. When it is full, it throws away the entry that was used least
recently. Write these methods:

    LRUCache(capacity)   create a cache holding at most `capacity`
                         entries
    get(key)             return the value for `key`, or -1 if the key
                         isn't stored
    put(key, value)      store `value` under `key` (insert or update)
    __len__()            return how many entries are stored (so
                         len(cache) works)

========================================================================
WHAT AN "LRU CACHE" IS
========================================================================
A CACHE is a small, fast store that keeps recently used results, so
you don't have to recompute or re-fetch them. It has limited room.
When it is full and something new arrives, it must EVICT (throw away)
an existing entry.

An "LRU" cache evicts the Least Recently Used entry: the one that has
gone the longest without being read (get) or written (put).

Walk-through with capacity 2. The "order" column lists keys from least
recent (LEFT) to most recent (right):

    put(1, 1)    cache {1:1}          order: 1
    put(2, 2)    cache {1:1, 2:2}     order: 1 2
    get(1) -> 1                       order: 2 1     (1 is now most recent)
    put(3, 3)    full! evict 2        order: 1 3
    get(2) -> -1                      (2 was evicted)
    put(4, 4)    full! evict 1        order: 3 4
    get(1) -> -1
    get(3) -> 3                       order: 4 3
    get(4) -> 4                       order: 3 4

========================================================================
TWO WAYS TO GET O(1)
========================================================================
O(1) means constant time: the same speed however many entries are
stored, so you never loop over the entries.

1. `collections.OrderedDict`: a dict that remembers the order keys
   were added, with two O(1) extras:
       od.move_to_end(key)       mark key as most recent (moves it
                                 to the right end)
       od.popitem(last=False)    remove and return the OLDEST
                                 (leftmost) entry
   Together these make an LRU cache in a few lines.

2. Hash map + doubly linked list (how OrderedDict works inside). Keep
   nodes in a doubly linked list ordered by recency. Each node has a
   `.prev` and a `.next`. A dict maps key -> node, so you can find any
   node in O(1). Because the list is DOUBLY linked (each node knows
   the one before it too), you can unlink that node in O(1) without
   walking the list:

       dict: {1: node1, 3: node3}

       head <-> [key 1] <-> [key 3] <-> tail
       (LRU end)                   (MRU end)

   LRU means least recently used, MRU means most recently used.
   "head" and "tail" are dummy sentinel nodes (special stand-in nodes
   that hold no data), so an empty list is never a special case.
   To "use" a key: unlink its node and re-insert it just before tail.
   To evict: unlink head.next and delete its key from the dict.

Solve it with approach 1 first. Approach 2 is the stretch goal.

========================================================================
THE RULES
========================================================================
Your class must:
1. Raise `ValueError` from `__init__` if capacity < 1.
2. get(key): return the stored value, or -1 if `key` is not present.
   A successful get counts as a "use": it makes the key the MOST
   recently used.
3. A get MISS (key not present) does not change the recency order.
4. put(key, value): insert or update key -> value, and return None.
   This also counts as a use.
5. If putting a NEW key would go over the capacity, first evict the
   least recently used key.
6. Updating an EXISTING key never evicts anything.
7. Run both `get` and `put` in O(1) time on average.

You can assume:
- `capacity` is an int.
- Keys and values are ints, and values are >= 0. So -1 clearly means
  "missing".
- There are up to 200_000 calls in total, so a solution that loops
  over the entries on every call will be too slow.

========================================================================
EXAMPLES
========================================================================
Each line runs one call. `# ->` shows what it returns.

    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)        # -> 1    (1 is now most recent)
    cache.put(3, 3)     # full: evicts key 2, the least recent
    cache.get(2)        # -> -1   (2 was evicted)
    len(cache)          # -> 2

    LRUCache(0)         # -> raises ValueError

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(1) average for get and put: a dict lookup plus a fixed
         number of moves, no loops.
- Space: O(capacity): never more than `capacity` entries are stored.

========================================================================
EDGE CASES TO TEST
========================================================================
- get on an empty cache: LRUCache(2).get(1) -> -1
- capacity = 1: every new key evicts the previous one. put(1, 1),
  put(2, 2), then get(1) -> -1 and get(2) -> 2
- put on an existing key updates its value AND makes it most recent.
  It does not evict anything or change len(). With capacity 2:
  put(1, 1), put(2, 2), put(1, 10), put(3, 3) -> get(1) is 10 and
  get(2) is -1 (2 was the least recent)
- A get makes a key "fresh", so a different key is evicted next (see
  the examples: get(1) saves 1, and 2 is evicted)
- len() never goes above capacity
- LRUCache(0) -> raises ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Store `self._capacity` and `self._data = OrderedDict()` in
   __init__.
2. get: if the key is missing, return -1. Otherwise move_to_end(key)
   and return the value.
3. put for an existing key: update the value and move_to_end.
4. put for a new key: add it (it goes to the end automatically). Then,
   if len > capacity, popitem(last=False).
5. Stretch version: write a tiny `_Node` class with key, value, prev
   and next. Helper methods `_remove(node)` and `_add_to_end(node)`
   keep the get/put code short.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `collections.OrderedDict`: move_to_end, popitem(last=False)
- Plain dicts also keep insertion order (Python 3.7+) but lack
  move_to_end
- `functools.lru_cache`: the built-in decorator that uses this idea
- Doubly linked lists and sentinel nodes
- `__slots__` for lightweight node classes (it fixes the attribute
  names up front, which saves memory)

========================================================================
STRETCH GOALS
========================================================================
- Implement it WITHOUT OrderedDict: a plain dict + your own doubly
  linked list (approach 2). Your existing tests should pass unchanged.
- Add `peek(key)` that returns the value without updating recency.
- Implement an LFU (Least Frequently Used) cache (LeetCode #460): it
  evicts the key used the fewest times.
"""


class LRUCache:
    """A fixed-capacity cache that evicts the least recently used key."""

    def __init__(self, capacity: int) -> None:
        """Create an empty cache.

        Args:
            capacity: Maximum number of entries to hold. Must be >= 1.

        Raises:
            ValueError: If capacity < 1.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def get(self, key: int) -> int:
        """Return the value for `key` and mark it most recently used.

        Args:
            key: The key to look up.

        Returns:
            The stored value, or -1 if `key` is not in the cache.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def put(self, key: int, value: int) -> None:
        """Insert or update `key` and mark it most recently used.

        If adding a new key makes the cache exceed its capacity, the least
        recently used key is evicted first.

        Args:
            key: The key to store.
            value: The value to associate with `key`.
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError

    def __len__(self) -> int:
        """Return the number of entries currently in the cache.

        Returns:
            The current size (always <= capacity).
        """
        # TODO: implement me, then make your tests pass.
        raise NotImplementedError
