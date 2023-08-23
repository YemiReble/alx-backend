#!/usr/bin/env python3
""" BaseCaching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")


class BasicCache(BaseCaching):
    """ BasicCache is a class that inherit
        from BaseChasing as seen
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        self.key = key
        self.item = item
        try:
            if self.key is None:
                return

            new_data = {self.key: self.item}
            new_data[self.key] = self.item
            return self.cache_data.update(new_data)
            # self.cache_data.append(new_data)
        except Exception:
            raise NotImplementedError(
                "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        self.key = key
        try:
            if self.key is None or self.key not in self.cache_data:
                return None

            for keys in self.cache_data:
                return self.cache_data[key]
        except Exception:
            raise NotImplementedError(
                "get must be implemented in your cache class")
