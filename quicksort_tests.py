import unittest
from quicksort import quicksort
import random


class TestingQuicksortConstituents(unittest.TestCase):
    """Tests for the constituent parts of my quicksort function"""
    def setUp(self):
        self.li = [7580, 4074, 7510, 8383, 1783, 1251, 724, 6247, 3174, 9311]
        self.pivot = 1783

    def test_my_random_pivot_works(self):
        pivot = self.li[random.randint(0, (len(self.li) - 1))]
        self.assertIn(pivot, self.li)

    def test_if_my_less_function_works(self):
        less = [x for x in self.li if x < self.pivot]
        self.assertEqual(less, [1251, 724])

    def test_if_my_equal_function_works(self):
        equal = [x for x in self.li if x == self.pivot]
        self.assertEqual(equal, [self.pivot])

    def test_if_my_greater_listcomp_works(self):
        greater = [x for x in self.li if x > self.pivot]
        self.assertEqual(greater, [7580, 4074, 7510, 8383, 6247, 3174, 9311])


class TestingQuickstartFunction(unittest.TestCase):
    """Seeing how the Quicksort function performs in different cases."""
    def setUp(self):
        self.empty_li = []
        self.single_li = [1337]
        self.full_li = [7580, 4074, 7510, 8383, 1783, 1251, 724, 6247, 3174,
                        9311]
        self.stuttering_li = [1, 1, 1, 1, 1, 1, 1, 1, 1]

    def test_how_it_handles_empty_li(self):
        self.assertEqual(quicksort(self.empty_li), [])

    def test_how_it_handles_list_of_one(self):
        self.assertEqual(quicksort(self.single_li), [1337])

    def test_how_it_handles_a_full_list(self):
        sorted = [724, 1251, 1783, 3174, 4074, 6247, 7510, 7580, 8383, 9311]
        self.assertEqual(quicksort(self.full_li), sorted)

    def test_its_patience(self):
        self.assertEqual(quicksort(self.stuttering_li), [1, 1, 1, 1, 1, 1, 1,
                                                         1, 1])


if __name__ == '__main__':
    unittest.main()
