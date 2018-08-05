#!/usr/bin/python3
"""
4-mru_cache.py - contains class definition for MRUCache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class definition for 'MRUCache'"""
    def __init__(self):
        super().__init__()
        self.last_used = None

    def put(self, key, item):
        """Updates cache with given key/value (kv) pair. If cache is at capacity,
        most recently accessed kv pair is deleted."""
        if key and item:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_used))
                del self.cache_data[self.last_used]
            self.cache_data[key] = item
            self.last_used = key

    def get(self, key):
        """Returns a key's value from parent dictionary, 'cache_data'"""
        val = self.cache_data.get(key)
        if val:
            self.last_used = key
        return val
