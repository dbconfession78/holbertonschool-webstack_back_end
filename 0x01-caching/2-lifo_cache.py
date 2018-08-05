#!/usr/bin/python3
"""
2-lifo_cache.py - contains class definition for LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Class definition for 'LIFOCache'"""
    def __init__(self):
        super().__init__()
        self.stk = []

    def put(self, key, item):
        """Stores a key/value pair to the parent 'cache_data' dictionary"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.stk.pop()
                print("DISCARD: {}".format(last_key))
                del self.cache_data[last_key]
            self.stk.append(key)

    def get(self, key):
        """Returns a key's value from parent dictionary, 'cache_data'"""

        return self.cache_data.get(key)
