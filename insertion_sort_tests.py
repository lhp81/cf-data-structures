import unittest
from insertion_sort import insertion_sort

class TestTheFunction(unittest.TestCase):
    def setUp(self):
        self.empty_list = []
        self.sorted_list = [1, 2, 3, 4, 5]
        self.random_list = [251, 198, 691, 268, 554]

    def test_an_empty_list(self):
        self.assertEqual(insertion_sort(self.empty_list), [])

    def test_an_ordered_list(self):
        self.assertEqual(insertion_sort(self.sorted_list), [1, 2, 3, 4, 5])

    def test_a_random_list(self):
        self.assertEqual(insertion_sort(self.random_list), [198, 251, 268, 554,
                                                            691])


if __name__ == '__main__':
    unittest.main()
