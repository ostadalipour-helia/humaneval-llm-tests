import unittest
from sut.problem_HumanEval_124 import valid_date

class TestValidDate(unittest.TestCase):

    def test_valid_typical_date(self):
        # CRITICAL: Typical/Expected Input, Return Value Testing (True path)
        # Verifies a standard valid date.
        self.assertEqual(valid_date('03-11-2000'), True)

    def test_invalid_empty_string(self):
        # CRITICAL: Edge Case (empty collection), Rule 1 violation
        # Verifies the function handles an empty input string.
        self.assertEqual(valid_date(''), False)

    def test_invalid_format_slash_separator(self):
        # CRITICAL: Edge Case (incorrect format), Rule 4 violation
        # Verifies the function rejects dates with incorrect separators.
        self.assertEqual(valid_date('06/04/2020'), False)

    def test_invalid_format_day_not_two_digits(self):
        # CRITICAL: Logic Mutation (parsing), Rule 4 violation
        # Verifies the function rejects dates where day is not 'dd' format.
        self.assertEqual(valid_date('04-0-2040'), False)

    def test_boundary_valid_min_month_min_day(self):
        # CRITICAL: Boundary Testing (min month, min day), Return Value Testing (True path)
        # Verifies the earliest valid date components.
        self.assertEqual(valid_date('01-01-2023'), True)

    def test_boundary_valid_max_month_max_day_31_month(self):
        # CRITICAL: Boundary Testing (max month, max day for 31-day month), Return Value Testing (True path)
        # Verifies the latest valid date components for a 31-day month.
        self.assertEqual(valid_date('12-31-2023'), True)

    def test_invalid_day_too_high_31_day_month(self):
        # CRITICAL: Boundary Testing (day > 31), Off-by-One Error (31+1), Rule 2 violation
        # Verifies that a day exceeding 31 for a 31-day month is invalid.
        self.assertEqual(valid_date('01-32-2023'), False)

    def test_invalid_day_too_high_february(self):
        # CRITICAL: Boundary Testing (day > 29 for Feb), Off-by-One Error (29+1), Rule 2 violation
        # Verifies that a day exceeding 29 for February is invalid.
        self.assertEqual(valid_date('02-30-2023'), False)

    def test_invalid_month_too_low(self):
        # CRITICAL: Boundary Testing (month < 1), Off-by-One Error (1-1), Rule 3 violation
        # Verifies that a month less than 1 is invalid.
        self.assertEqual(valid_date('00-15-2023'), False)

    def test_invalid_month_too_high(self):
        # CRITICAL: Boundary Testing (month > 12), Off-by-One Error (12+1), Rule 3 violation
        # Verifies that a month greater than 12 is invalid.
        self.assertEqual(valid_date('13-15-2023'), False)