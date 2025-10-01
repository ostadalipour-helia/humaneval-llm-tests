import unittest
from sut.problem_HumanEval_124 import valid_date

class TestValidDate(unittest.TestCase):

    def test_01_valid_date_example_1(self):
        self.assertTrue(valid_date('03-11-2000'))

    def test_02_valid_date_example_2(self):
        self.assertTrue(valid_date('06-04-2020'))

    def test_03_invalid_format_wrong_separator(self):
        self.assertFalse(valid_date('06/04/2020'))

    def test_04_invalid_format_day_zero(self):
        self.assertFalse(valid_date('04-0-2040'))

    def test_05_invalid_month_too_low(self):
        self.assertFalse(valid_date('00-15-2023'))

    def test_06_invalid_month_too_high(self):
        self.assertFalse(valid_date('13-15-2023'))

    def test_07_invalid_day_for_31_day_month(self):
        self.assertFalse(valid_date('01-32-2023')) # January has 31 days

    def test_08_invalid_day_for_30_day_month(self):
        self.assertFalse(valid_date('04-31-2023')) # April has 30 days

    def test_09_invalid_day_for_february_too_high(self):
        self.assertFalse(valid_date('02-30-2023')) # February has max 29 days per rule

    def test_10_empty_date_string(self):
        self.assertFalse(valid_date(''))