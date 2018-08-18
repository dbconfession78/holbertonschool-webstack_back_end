#!/usr/bin/python3
"""
3-lru_cache.py - contains class definition for LRUCache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    : Class definition for 'LRUCache'
    : @dct1: key to access-index dictionary
    : @dct2: access-index to key dictionary
    """
    def __init__(self):
        super().__init__()
        self.dct1 = {}
        self.dct2 = {}
        self.idx = 0

    def put(self, key, item):
        """Updates cache with given key/value (kv) pair. If cache is at capacity,
        least recently accessed kv pair is deleted."""
        input("hi")
        if key and item:
            self.cache_data[key] = item
            self.access(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key = min(list(self.dct2.keys()))
                to_remove = self.dct2.get(key)
                print("DISCARD: {}".format(to_remove))
                del self.cache_data[to_remove]
                del self.dct1[to_remove]
                del self.dct2[key]

    def get(self, key):
        """Returns a key's value from parent dictionary, 'cache_data'"""
        val = self.cache_data.get(key)
        if val:
            self.access(key)
        return val

    def access(self, key):
        """ Updates key's access order in two dictionaries """
        curr_idx = self.dct1.pop(key) if self.dct1.get(key) else None
        if curr_idx:
            del self.dct2[curr_idx]
        self.dct1[key] = self.idx
        self.dct2[self.idx] = key
        self.idx += 1
