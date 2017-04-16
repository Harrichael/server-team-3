"""
Sorted Collection, custome binary list with key support
"""

from bisect import bisect_left, bisect_right

class SortedCollection(object):
    def __init__(self, key=id):
        self._key = key
        self._keys = []
        self._items = []

    def clear(self):
        self.__init__(self._key)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __iter__(self):
        return iter(self._items)

    def __reversed__(self):
        return reversed(self._items)

    def __contains__(self, item):
        k = self._key(item)
        i = bisect_left(self._keys, k)
        j = bisect_right(self._keys, k)
        return item in self._items[i:j]

    def index(self, item):
        k = self._key(item)
        index = bisect_left(self._keys, k)
        if self._items[index] == item:
            return index
        raise ValueError

    def index_by_key(self, key):
        index = bisect_left(self._keys, key)
        if index != len(self) and self._keys[index] == key:
            return index
        raise ValueError('No item found with key equal to: ' + str(key))

    def insert(self, item):
        k = self._key(item)
        index = bisect_right(self._keys, k)
        self._keys.insert(index, k)
        self._items.insert(index, item)

    def insert_last(self, item):
        k = self._key(item)
        if not self._keys or k >= self._keys[-1]:
            self._keys.append(k)
            self._items.append(item)
        else:
            raise Exception('You promised you would insert last')

    def remove(self, item):
        index = self.index(item)
        del self._keys[index]
        del self._items[index]

    def remove_by_key(self, key):
        index = self.index_by_key(key)
        del self._keys[index]
        del self._items[index]

    def find(self, key):
        index = bisect_left(self._keys, key)
        if index != len(self) and self._keys[index] == key:
            return self._items[index]
        raise ValueError('No item found with key equal to: ' + str(key))

