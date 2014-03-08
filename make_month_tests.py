# make_month_tests.py

import unittest
from make_month import MakeMonth
from calendar import monthrange


class TestingTheBasics(unittest.TestCase):
    def test_that_it_has_right_length(self):
        mc = MakeMonth(2014, 03)
        self.assertEqual(mc.end_of_mnth, 31)

    def test_that_it_has_right_day(self):
        mc = MakeMonth(2014, 02)
        self.assertEqual(mc.start_of_mnth, 5)


class TestingFunctionality(unittest.TestCase):
    def test_that_it_wont_accept_invalid_dates(self):
        mc = MakeMonth(2014, 02)
        self.assertRaises(ValueError, lambda: mc.day(30))

    def test_that_it_wont_accept_nonnumeric_date(self):
        mc = MakeMonth(2014, 02)
        self.assertRaises(ValueError, lambda: mc.day('cat'))

    def test_it_wont_accept_a_negative(self):
        mc = MakeMonth(2014, 02)
        self.assertRaises(ValueError, lambda: mc.day(-5))

    def test_that_it_returns_correct_day(self):
        mc = MakeMonth(2014, 02)
        self.assertEqual(mc.day(1), "Saturday")


if __name__ == '__main__':
    unittest.main()
