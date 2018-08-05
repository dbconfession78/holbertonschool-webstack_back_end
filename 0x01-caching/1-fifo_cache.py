#!/usr/bin/python3
"""
1-fifo_cache - contains class definition for FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class definition for 'FIFOCache'"""
    def __init__(self):
        super().__init__()
        self.stk = []

    def put(self, key, item):
        """Stores a key/value pair to the parent 'cache_data' dictionary"""
        if key and item:
            self.cache_data[key] = item
            self.stk.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.stk.pop(0)
                print("DISCARD: {}".format(first_key))
                del self.cache_data[first_key]

    def get(self, key):
        """Returns a key's value from parent dictionary, 'cache_data'"""

        return self.cache_data.get(key)
