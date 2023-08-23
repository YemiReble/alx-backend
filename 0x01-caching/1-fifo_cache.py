#!/usr/bin/env python3
"""
A First In First Out Caching System
that inherint from BaseCaching Parent Class
which is also a caching system
"""


BaseCaching = __import__("basecaching").BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache Class that """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Put function for adding new data """
        self.key = key
        self.item = item

        if self.key is None or self.item is None:
            return

        if self.key and self.item:
            add_data = {self.key: self.item}
            add_data[self.key] = self.item
            # return self.cache_data.update(add_data)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data.keys():
            cache = next(iter(self.cache_data.keys()))
            del self.cache_data[cache]
            print("DISCARD: {}".format(cache))

        return self.cache_data.update(add_data)

    def get(self, key):
        """ Get cache data for cache """
        self.key = key
        if self.key is None or self.key not in self.cache_data:
            return None

        for keys in self.cache_data:
            return self.cache_data[self.key]
