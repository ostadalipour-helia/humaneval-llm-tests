import unittest
from sut.problem_HumanEval_124 import valid_date

class Test_valid_date(unittest.TestCase):
    def test_valid_date_normal_case_leap_year(self):
        # Normal case: Valid date in a leap year February
        self.assertTrue(valid_date('02-15-2020'))

    def test_valid_date_normal_case_31_day_month(self):
        # Normal case: Valid date in a 31-day month
        self.assertTrue(valid_date('03-11-2000'))

    def test_valid_date_edge_min_date(self):
        # Edge case: Minimum valid day and month
        self.assertTrue(valid_date('01-01-1900'))

    def test_valid_date_edge_max_date_31_day_month(self):
        # Edge case: Maximum valid day for a 31-day month
        self.assertTrue(valid_date('12-31-2099'))

    def test_valid_date_edge_max_date_february_leap_year(self):
        # Edge case: Maximum valid day for February in a leap year
        self.assertTrue(valid_date('02-29-2024'))

    def test_invalid_date_empty_string(self):
        # Edge case: Empty string input
        self.assertFalse(valid_date(''))

    def test_invalid_date_month_too_high(self):
        # Edge case: Month greater than 12
        self.assertFalse(valid_date('15-01-2012'))

    def test_invalid_date_day_too_high_for_month(self):
        # Edge case: Day greater than max for a 30-day month
        self.assertFalse(valid_date('04-31-2023'))

    def test_invalid_date_day_too_high_february_non_leap(self):
        # Edge case: Day greater than 29 for February (even if it were a leap year, 30 is too high)
        self.assertFalse(valid_date('02-30-2023'))

    def test_invalid_date_incorrect_separator(self):
        # Edge case: Incorrect date format (uses '/' instead of '-')
        self.assertFalse(valid_date('06/04/2020'))

    def test_invalid_date_year_too_short(self):
        # Edge case: Incorrect year format (not 'yyyy')
        self.assertFalse(valid_date('01-01-23'))

    def test_invalid_date_non_string_input_none(self):
        # Error case: Input is None (not a string)
        self.assertFalse(valid_date(None))

    def test_invalid_date_non_string_input_int(self):
        # Error case: Input is an integer (not a string)
        self.assertFalse(valid_date(12345))