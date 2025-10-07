import unittest
from sut_llm.problem_HumanEval_124 import valid_date

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

    def test_february_valid_date(self):
        # Covers lines 53 (elif month == 2) and 54 (max_days = 29)
        result = valid_date('02-15-2000')
        self.assertTrue(result)

    def test_invalid_date_non_integer_part(self):
        # Covers line 46 (except ValueError) by providing a non-numeric day part.
        result = valid_date('03-XX-2000')
        self.assertFalse(result)

    def test_valid_date_covers_part_length_check(self):
        # Covers line 40 (if len(month_str) != 2 or len(day_str) != 2 or len(year_str) != 4).
        # This line is executed for any date string that passes previous format checks.
        # If line 40 is reported as uncovered, it implies no test has reached this point.
        result = valid_date('01-01-2000')
        self.assertTrue(result)

