# a naive hash table. shouldn't go to dances or social events where there will
# be drinking, gambling, or disreputable people.

from linkedlist import Node, SingleLL


class NaiveHashTable(object):
    """A naive hash table that hashes a string to determine in which bucket to
    store it and its associated value."""

    def __init__(self, slots=10):  # length of 10 chosen b/c that's what we
                                   # used in class. it can be any value.
        self.slots = slots
        self.bucket_list = Bucket()  # this is what will catch the k:v pairs
        for i in range(self.slots):   # put in ten LL, from 0-9
            self.bucket_list.insert(Bucket)

    def set(self, key, val):
        """stores the given val using the given key"""
        bucket_number = self.hash_(key)
        if not self.bucket_list[bucket_number]:
           self.bucket_list[bucket_number].head = bucket_number
           self.bucket_list[bucket_number].head.next = SingleLL((key, val))
        else:
            for i in range(bucket_number):
                self.value.next
            self.bucket_list[bucket_number].next = Node(key, val)
            # look through the list until you find one that's empty.

    def get(self, key):
        """returns the value stored with the given key"""
        key_to_get = self.hash_(key)
        start = bucket_list[key_to_get].value
        while start:
            if start.value[0] == key:
                return start.value[1]
            start = start.next
        raise KeyError("That key cannot be found in the hash. Bummer.")



    def hash_(self, key):
        """hashes the key provided"""
        if type(key) is not str:    # my ht can only deal with strings. naive.
            raise TypeError("This is a naive hash table and can only handle \
                strings.")
        else:                           # so, if it is a string...
            adder = 0                   # we take each character in the string
            for char in key:            # and turn it into a value
                adder += ord(char)      # these values are put in a list
            return adder % self.slots   # and then added up and modulo'd.


class Bucket(SingleLL):
    """a bucket to hold values"""
    pass
