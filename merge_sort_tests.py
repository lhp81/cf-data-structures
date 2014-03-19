import unittest
from merge_sort import merge_sort


class MergeSortTests(unittest.TestCase):
    """Testing my merge sort function"""

    def setUp(self):
        l = [289, 441, 445, 57, 182, 1, 493, 41, 67, 113, 126, 212, 379, 77,
             250, 425, 352, 130, 329, 447]
        msl = merge_sort(l)

    def test_basic_setup(self):
        self.assertEqual(len(self.msl.set_one), 10)

if __name__ == '__main__':
    unittest.main()
