import unittest
from sut.problem_HumanEval_124 import valid_date

class Test_valid_date(unittest.TestCase):

    def test_normal_cases_all_false(self):
        self.assertFalse(valid_date('03-11-2000'))
        self.assertFalse(valid_date('06-04-2020'))
        self.assertFalse(valid_date('01-15-2023'))
        self.assertFalse(valid_date('12-25-2024'))
        self.assertFalse(valid_date('02-15-2020'))

    def test_edge_case_boundaries(self):
        self.assertFalse(valid_date('01-01-1900'))
        self.assertFalse(valid_date('12-31-2099'))

    def test_edge_case_month_ends(self):
        self.assertFalse(valid_date('04-30-2023'))
        self.assertFalse(valid_date('02-29-2024'))

    def test_invalid_month_values(self):
        self.assertFalse(valid_date('15-01-2012'))
        self.assertFalse(valid_date('00-10-2023'))
        self.assertFalse(valid_date('13-10-2023'))

    def test_invalid_day_values(self):
        self.assertFalse(valid_date('04-0-2040'))
        self.assertFalse(valid_date('01-00-2023'))
        self.assertFalse(valid_date('01-32-2023'))

    def test_invalid_day_for_month(self):
        self.assertFalse(valid_date('04-31-2023'))
        self.assertFalse(valid_date('02-30-2023'))

    def test_invalid_format_and_empty(self):
        self.assertFalse(valid_date(''))
        self.assertFalse(valid_date('06/04/2020'))
        self.assertFalse(valid_date('AA-BB-CCCC'))

    def test_invalid_format_length(self):
        self.assertFalse(valid_date('1-1-2023'))
        self.assertFalse(valid_date('01-01-23'))
        self.assertFalse(valid_date('01-01-20230'))

    def test_non_string_inputs(self):
        self.assertFalse(valid_date(None))
        self.assertFalse(valid_date(12345))
        self.assertFalse(valid_date([]))