# tests for my hash table.

import unittest
from hash_table import NaiveHashTable
from linkedlist import Node, SingleLL  # do I need this?


class TestingHashAbility(unittest.TestCase):
    """To see if the hasher works as expected."""

    def test_to_see_if_i_hash_keys_correctly(self):  # passes
        mh = NaiveHashTable()
        self.assertEqual(mh.hash_('hello'), 2)
        # it's a 2 here because we're taking 532 % 10
        # 532 = sum of all ord() values of char in 'hello'; 10 = length.

    def test_that_i_can_hash_a_string_with_spaces(self):
        mh = NaiveHashTable()
        self.assertIsNotNone(mh.hash_('hello dave'))

    def test_that_i_can_hash_a_string_with_punctuation(self):
        mh = NaiveHashTable()
        self.assertIsNotNone(mh.hash_("it's"))

    def test_hashing_a_string_with_spaces_and_punctuation(self):
        mh = NaiveHashTable()
        self.assertIsNotNone(mh.hash_("it's a beautiful day in the \
                                       neighborhood"))

    def test_that_i_cant_sneak_in_a_float(self):
        mh = NaiveHashTable
        self.assertRaises(TypeError, lambda: mh.hash_(1.0))

    def test_that_i_cant_hash_an_int(self):
        mh = NaiveHashTable
        self.assertRaises(TypeError, lambda: mh.hash_(7))


class TestingSetAndGetMethods(unittest.TestCase):
    """To see if I can successfully get things in buckets"""

    def test_storing_string_in_a_bucket(self):
        mh = NaiveHashTable()
        mh.set('hello', 'world')
        # self.assertIsNotNone(mh.get('hello'))

    def test_storing_an_int(self):
        mh = NaiveHashTable()
        mh.set('an integer', 1)
        self.assertIsNotNone(mh.get('an integer'))

    def test_storing_a_float(self):
        mh = NaiveHashTable()
        mh.set('a float', 1.0)
        self.assertIsNotNone(mh.get('a float'))

    def test_assigning_multiple_hashes_to_buckets(self):
        mh = NaiveHashTable()
        mh.set('i am not that', 1337)
        mh.set("who's hungry for", 3.14)
        mh.set('by', 'ee cummings')
        mh.set('since feeling is first', 'who pays any attention to the')
        mh.set('syntax of things', 'will never wholly kiss you')
        mh.set('wholly to be a fool', 'while spring is in the world')
        mh.set('my blood approves', 'and kisses are a better fate')
        mh.set('than wisdom', 'lady i swear by all the flowers')
        mh.set('don\'t cry', 'the best gesture of my brain is less than')
        mh.set('your eyelid\'s flutter', 'which says')
        mh.set('we are for each other then', 'laugh, leaning back in my arms')
        mh.set('for life\'s not a paragraph', 'and death i think is no \
                parenthesis')

    def test_to_see_if_hash_handles_nonstring_keys_correctly(self):  # passes
        mh = NaiveHashTable()
        self.assertRaises(TypeError, lambda: mh.set(123, 'wun to tree'))

    def test_to_see_if_hash_handles_float_keys_correctly(self):
        mh = NaiveHashTable()
        self.assertRaises(TypeError, lambda: mh.set(1.0, 'wun poin toe'))




class TestingTheGetMethod(unittest.TestCase):
    """To see if I can successfully get things out of buckets."""

    def test_getting_from_empty_list(self):
        mh = NaiveHashTable()
        self.assertRaises(ValueError, lambda: mh.get())

    def test_getting_nonexistant_key(self):
        mh = NaiveHashTable()
        mh.set('dog', 'food')
        self.assertRaises(ValueError, lambda:mh.get('cat'))

    def test_getting_value_from_bucket(self):
        mh = NaiveHashTable()
        mh.set('hello', 'world')
        self.assertEqual(mh.get('hello'), 'world')

    def test_getting_string_from_full_list(self):
        mh = NaiveHashTable()
        mh.set('i am not that', 1337)
        mh.set("who's hungry for", 3.14)
        mh.set('since feeling is first', 'who pays any attention to the')
        mh.set('syntax of things', 'will never wholly kiss you')
        mh.set('wholly to be a fool', 'while spring is in the world')
        mh.set('my blood approves', 'and kisses are a better fate')
        mh.set('than wisdom', 'lady i swear by all the flowers')
        mh.set('don\'t cry', 'the best gesture of my brain is less than')
        mh.set('your eyelid\'s flutter', 'which says')
        mh.set('we are for each other then', 'laugh, leaning back in my arms')
        mh.set('for life\'s not a paragraph', 'and death i think is no \
                parenthesis')
        mh.set('by', 'ee cummings')
        self.assertEqual(mh.get('than wisdom'), 'lady i swear by all the \
                                flowers')

    def test_getting_int_from_full_list(self):
        mh = NaiveHashTable()
        mh.set('i am not that', 1337)
        mh.set("who's hungry for", 3.14)
        mh.set('since feeling is first', 'who pays any attention to the')
        mh.set('syntax of things', 'will never wholly kiss you')
        mh.set('wholly to be a fool', 'while spring is in the world')
        mh.set('my blood approves', 'and kisses are a better fate')
        mh.set('than wisdom', 'lady i swear by all the flowers')
        mh.set('don\'t cry', 'the best gesture of my brain is less than')
        mh.set('your eyelid\'s flutter', 'which says')
        mh.set('we are for each other then', 'laugh, leaning back in my arms')
        mh.set('for life\'s not a paragraph', 'and death i think is no \
                parenthesis')
        mh.set('by', 'ee cummings')
        self.assertEqual(mh.get('i am not that'), 1337)

    def test_getting_float_from_full_list(self):
        mh = NaiveHashTable()
        mh.set('i am not that', 1337)
        mh.set("who's hungry for", 3.14)
        mh.set('since feeling is first', 'who pays any attention to the')
        mh.set('syntax of things', 'will never wholly kiss you')
        mh.set('wholly to be a fool', 'while spring is in the world')
        mh.set('my blood approves', 'and kisses are a better fate')
        mh.set('than wisdom', 'lady i swear by all the flowers')
        mh.set('don\'t cry', 'the best gesture of my brain is less than')
        mh.set('your eyelid\'s flutter', 'which says')
        mh.set('we are for each other then', 'laugh, leaning back in my arms')
        mh.set('for life\'s not a paragraph', 'and death i think is no \
                parenthesis')
        mh.set('by', 'ee cummings')
        self.assertEqual(mh.get('who\'s hungry for'), 3.14)


if __name__ == '__main__':
    unittest.main()
