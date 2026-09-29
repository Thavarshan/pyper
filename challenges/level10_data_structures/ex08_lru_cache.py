"""
Challenge: LRU Cache
Level:     10 - Data Structures
Topics:    hash maps, collections.OrderedDict, doubly linked lists, class design
Source:    LeetCode #146 "LRU Cache"

========================================================================
PROBLEM
========================================================================
A CACHE is a small, fast store that keeps recently used results so you
don't have to recompute or re-fetch them. Because it has limited room,
when it is full and something new arrives, it must EVICT (throw away)
an existing entry. An "LRU" cache evicts the Least Recently Used entry -
the one that has gone the longest without being read or written.

Design a class `LRUCache` with:

    LRUCache(capacity)   create a cache holding at most `capacity` entries
    get(key)             return the value stored for `key`, or -1 if the
                         key is not present. A successful get counts as a
                         "use" - it makes the key the MOST recently used.
    put(key, value)      insert or update key -> value. This also counts as
                         a use. If inserting a NEW key would exceed the
                         capacity, first evict the least recently used key.
                         Updating an EXISTING key never evicts anything.
    __len__()            number of entries currently stored

Both `get` and `put` must run in O(1) time on average.

Walk-through with capacity 2 (recency list: least recent on the LEFT):

    put(1, 1)    cache {1:1}          order: 1
    put(2, 2)    cache {1:1, 2:2}     order: 1 2
    get(1) -> 1                       order: 2 1     (1 is now most recent)
    put(3, 3)    full! evict 2        order: 1 3
    get(2) -> -1                      (2 was evicted)
    put(4, 4)    full! evict 1        order: 3 4
    get(1) -> -1
    get(3) -> 3                       order: 4 3
    get(4) -> 4                       order: 3 4

TWO WAYS TO GET O(1):

1. `collections.OrderedDict` - a dict that remembers insertion order and
   has two O(1) superpowers:
       od.move_to_end(key)       mark key as most recent (moves it right)
       od.popitem(last=False)    remove and return the OLDEST (leftmost)
   Together these are an LRU cache in a few lines.

2. Hash map + doubly linked list (how OrderedDict works inside). Keep
   nodes in a doubly linked list ordered by recency, with each node having
   `.prev` and `.next`. A dict maps key -> node so you can find any node
   in O(1), and because the list is DOUBLY linked you can unlink that node
   in O(1) without walking the list:

       dict: {1: node1, 3: node3}

       head <-> [key 1] <-> [key 3] <-> tail
       (LRU end)                   (MRU end)

   "head" and "tail" are dummy sentinel nodes so you never special-case an
   empty list. Use = unlink the node and re-insert it before tail. Evict
   = unlink head.next and delete its key from the dict.

Solve it with approach 1 first; approach 2 is the stretch goal.

========================================================================
EXAMPLES
========================================================================
    >>> cache = LRUCache(2)
    >>> cache.put(1, 1)
    >>> cache.put(2, 2)
    >>> cache.get(1)
    1
    >>> cache.put(3, 3)      # evicts key 2
    >>> cache.get(2)
    -1
    >>> len(cache)
    2

========================================================================
CONSTRAINTS
========================================================================
- `capacity` is an int >= 1. If capacity < 1, `__init__` raises
  `ValueError`.
- Keys and values are ints; values are >= 0 (so -1 unambiguously means
  "missing").
- `put` returns None.
- A `get` MISS does not change the recency order.
- Up to 200_000 calls in total.

========================================================================
COMPLEXITY TARGET
========================================================================
- Time:  O(1) average for get and put.
- Space: O(capacity).

========================================================================
EDGE CASES TO TEST
========================================================================
- get on an empty cache -> -1
- capacity = 1: every new key evicts the previous one
- put an existing key updates its value AND makes it most recent, and
  does not evict anything or change len()
- A get makes a key "fresh" so a different key is evicted next
- len() never exceeds capacity
- LRUCache(0) -> ValueError

========================================================================
HINTS (read only if you get stuck)
========================================================================
1. Store `self._capacity` and `self._data = OrderedDict()` in __init__.
2. get: if the key is missing return -1; otherwise move_to_end(key) and
   return the value.
3. put for an existing key: update the value and move_to_end.
4. put for a new key: add it (it goes to the end automatically); then, if
   len > capacity, popitem(last=False).
5. Stretch version: write a tiny `_Node` class with key, value, prev,
   next; helper methods `_remove(node)` and `_add_to_end(node)` keep the
   get/put code short.

========================================================================
PYTHON CONCEPTS TO LEARN
========================================================================
- `collections.OrderedDict`: move_to_end, popitem(last=False)
- Plain dicts also keep insertion order (3.7+) but lack move_to_end
- `functools.lru_cache` - the built-in decorator that uses this idea
- Doubly linked lists and sentinel nodes
- `__slots__` for lightweight node classes

========================================================================
STRETCH GOALS
========================================================================
- Implement it WITHOUT OrderedDict: a plain dict + your own doubly linked
  list (approach 2). Your existing tests should pass unchanged.
- Add `peek(key)` that returns the value without updating recency.
- Implement an LFU (least frequently used) cache (LeetCode #460).
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
