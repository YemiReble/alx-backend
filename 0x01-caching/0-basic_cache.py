#!/usr/bin/env python3
""" BasicCaching Class is a caching system class
    subclass that inherits from BaseCaching Parent
    Class
"""


# BaseCaching = __import__("basecaching").BaseCaching
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a class that inherit
        from BaseChasing as seen
    """

    def __init__(self):
        """ Initialization """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        self.key = key
        self.item = item
        if self.key is None or self.item is None:
            return

        new_data = {self.key: self.item}
        new_data[self.key] = self.item
        return self.cache_data.update(new_data)
        # self.cache_data.append(new_data)

    def get(self, key):
        """ Get an item by key
        """
        self.key = key
        if self.key is None or self.key not in self.cache_data:
            return None

        for keys in self.cache_data:
            return self.cache_data[self.key]
