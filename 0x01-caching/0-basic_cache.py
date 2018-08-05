#!/usr/bin/python3
"""
0-basic_cache - contains class definition for BasicCache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class definition for 'BasicCache'"""
    def put(self, key, item):
        """Stores a key/value pair to the parent 'cache_data' dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns a key's value from parent dictionary, 'cache_data'"""
        return self.cache_data.get(key)
