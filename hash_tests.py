# tests for my hash table.

import unittest
from hash_table import NaiveHashTable
from linkedlist import Node, SingleLL


class HashTests(unittest.TestCase):
    """To see if the parts of my hash table work."""

    def test_to_see_if_i_hash_keys_correctly(self):
        mh = NaiveHashTable()
        self.assertEqual(mh.hash('hello'), 2)

    def test_to_see_if_hash_handles_nonstring_keys_correctly(self):
        mh = NaiveHashTable()
        self.assertRaises(TypeError, lambda: mh.hash(123))

if __name__ == '__main__':
    unittest.main()
