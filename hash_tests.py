# tests for my hash table.

import unittest
from data_structures.hash_table import NaiveHashTable
from linkedlist import Node, SingleLL  # do I need this?


class HashTests(unittest.TestCase):
    """To see if the parts of my hash table work."""

    def test_to_see_if_i_hash_keys_correctly(self):
        mh = NaiveHashTable()
        self.assertEqual(mh.hash('hello'), 2)
        # remember, it's a 2 here because we're taking 532 % 10
        # 532 = sum of ord() values of char in 'hello'; 10 = length.

    def test_to_see_if_hash_handles_nonstring_keys_correctly(self):
        mh = NaiveHashTable()
        self.assertRaises(TypeError, lambda: mh.hash(123))

    def test_assigning_hash_to_a_bucket(self):
        mh = NaiveHashTable()
        mh.set('hello', 'world')
        self.assertIsNotNone(mh.get('hello'))

    def test_getting_key_from_bucket(self):
        pass

if __name__ == '__main__':
    unittest.main()
