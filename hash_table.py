# a naive hash table. shouldn't go to dances or social events where there will
# be drinking or.

from linkedlist import Node, SingleLL

class NaiveHashTable(object):
    """A hash table."""

    def __init__(self, length=10):
        self.length = length
        self.bucket_list = SingleLL()
        for i in range(self.length):
            self.bucket_list.insert(i)

    def get(self, key):
        pass

    def set(self, key, val):
        pass

    def hash(self, key):
        if type(key) is not str:
            raise TypeError("This is a naive hash table and can only handle \
                strings.")
        else:
            adder = []
            for char in key:
                adder.append(ord(char))
            return sum(adder) % self.size
