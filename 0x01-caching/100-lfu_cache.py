#!/usr/bin/env python3
""" LFUCache module
"""

from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a caching system using LFU algorithm """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_freq = defaultdict(int)  # Dictionary to count frequency of use
        self.least_freq = None  # Track the least frequency

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            # If key already exists, update the value and frequency
            if key in self.cache_data:
                self.cache_data[key] = item
                self.cache_freq[key] += 1
            else:
                # If cache exceeds limit, remove the least frequently used item
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_used_key = min(self.cache_freq, key=self.cache_freq.get)
                    del self.cache_data[least_used_key]
                    del self.cache_freq[least_used_key]
                    print(f"DISCARD: {least_used_key}")
                
                # Add the new key-value pair and set its frequency to 1
                self.cache_data[key] = item
                self.cache_freq[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            # Increase the frequency count since it's being accessed
            self.cache_freq[key] += 1
            return self.cache_data[key]
        return None
