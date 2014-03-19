import unittest
from merge_sort import merge_sort


class MergeSortTests(unittest.TestCase):
    """Testing my merge sort function"""

    def setUp(self):
        self.l_odd = [289, 441, 445, 57, 182]
        self.l_even = [289, 441, 445, 57]
        self.l_empty = []

    def test_basic_function(self):
        self.assertEqual(merge_sort(self.l_odd), [57, 182, 289, 441, 445])
        self.assertEqual(merge_sort(self.l_even), [57, 289, 441, 445])
        self.assertEqual(merge_sort(self.l_empty), [])

if __name__ == '__main__':
    unittest.main()
