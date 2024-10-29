#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a caching system with no limit """

    def put(self, key, item):
        """ Assigns the item to the cache_data dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Returns the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
