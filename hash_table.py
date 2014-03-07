# a naive hash table. shouldn't go to dances or social events where there will
# be drinking, gambling, or disreputable people.

from linkedlist import Node, SingleLL


class NaiveHashTable(object):
    """A naive hash table that hashes a string to determine in which bucket to
    store it and its associated value."""

    def __init__(self, slots=10):  # length of 10 chosen b/c that's what we
                                   # used in class. it can be any value.
        self.slots = slots
        self.bucket_list =[]  # this is what will catch the k:v pairs
        for i in range(self.slots):   # from 0-9
            self.bucket_list.append({})  # insert a dictionary

    def hash(self, key):
        """hashes the key provided"""
        if type(key) is not str:    # my ht can only deal with strings. naive.
            raise TypeError("This is a naive hash table and can only handle "
                "strings.")
        else:                           # so, if it is a string...
            adder = 0                   # we take each character in the string
            for char in key:            # and turn it into a value
                adder += ord(char)      # these values are put in a list
            return adder % self.slots   # and then added up and modulo'd.

    def set(self, key, val):
        """stores the given val using the given key"""
        hashed = self.hash(key)
        self.bucket_list[hashed].update({(key, val)})

    def get(self, key):
        """returns the value stored with the given key"""
        key_to_get = self.hash(key)
        sorted = self.bucket_list[key_to_get].items()
        try:
            for k, v in sorted:
                if k == key:
                    return v
        except:
            TypeError("That key cannot be found in the hash. Bummer.")
        # except KeyError("That key cannot be found in the hash. Bummer.")
