import unittest
from linkedlist import SingleLL, Node


class SingleLinkedListTest(unittest.TestCase):
    """To try making a Single Linked List"""

    def test_insert_and_size(self):
        myll = SingleLL()
        myll.insert(1)
        myll.insert('(^_^)')
        self.assertEqual(myll.size(), 2)

    def test_pop(self):
        myll = SingleLL()
        myll.insert(1)
        self.assertEqual(myll.pop(), '1')

    def test_search(self):
        myll = SingleLL()
        myll.insert(1)
        myll.insert('(^_^)')
        self.assertEqual(myll.search(1), (1, None))

    def test_failed_search(self):
        myll = SingleLL()
        myll.insert(1)
        myll.insert('(^_^)')
        self.assertRaises(myll.search('cat'), None)

    def test_print_single_linked_list(self):
        myll = SingleLL()
        myll.insert(1)
        myll.insert('(^_^)')
        self.assertEqual(myll.__str__(), '((^_^),1) (1,None) ')

    def test_count(self):
        myll = SingleLL()
        myll.insert(1)
        myll.insert('(^_^)')
        self.assertEqual(myll.count, 2)

    def test_other_count(self):
        myll = SingleLL(2)
        self.assertEqual(myll.count, 1)

    # def test_remove(self):
    #     myll = SingleLL()
    #     myll.insert(1)
    #     myll.insert('(^_^)')
    #     self.assertEqual(myll.remove(1), 1)

    # def test_failed_remove(self):
    #     myll = SingleLL()
    #     myll.insert(1)
    #     self.assertEqual(myll.remove('cat'), 'Not Found.')

if __name__ == '__main__':
    unittest.main()
