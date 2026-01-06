import unittest
import sut.problem_HumanEval_124 as mod

class TestHybrid(unittest.TestCase):
    def test_valid_typical_date(self):
            # CRITICAL: Typical/Expected Input, Return Value Testing (True path)
            # Verifies a standard valid date.
            self.assertEqual(mod.valid_date('03-11-2000'), True)

    def test_invalid_empty_string(self):
            # CRITICAL: Edge Case (empty collection), Rule 1 violation
            # Verifies the function handles an empty input string.
            self.assertEqual(mod.valid_date(''), False)

    def test_invalid_format_slash_separator(self):
            # CRITICAL: Edge Case (incorrect format), Rule 4 violation
            # Verifies the function rejects dates with incorrect separators.
            self.assertEqual(mod.valid_date('06/04/2020'), False)

    def test_invalid_format_day_not_two_digits(self):
            # CRITICAL: Logic Mutation (parsing), Rule 4 violation
            # Verifies the function rejects dates where day is not 'dd' format.
            self.assertEqual(mod.valid_date('04-0-2040'), False)

    def test_boundary_valid_min_month_min_day(self):
            # CRITICAL: Boundary Testing (min month, min day), Return Value Testing (True path)
            # Verifies the earliest valid date components.
            self.assertEqual(mod.valid_date('01-01-2023'), True)

    def test_invalid_day_too_high_31_day_month(self):
            # CRITICAL: Boundary Testing (day > 31), Off-by-One Error (31+1), Rule 2 violation
            # Verifies that a day exceeding 31 for a 31-day month is invalid.
            self.assertEqual(mod.valid_date('01-32-2023'), False)

    def test_invalid_day_too_high_february(self):
            # CRITICAL: Boundary Testing (day > 29 for Feb), Off-by-One Error (29+1), Rule 2 violation
            # Verifies that a day exceeding 29 for February is invalid.
            self.assertEqual(mod.valid_date('02-30-2023'), False)

    def test_invalid_month_too_low(self):
            # CRITICAL: Boundary Testing (month < 1), Off-by-One Error (1-1), Rule 3 violation
            # Verifies that a month less than 1 is invalid.
            self.assertEqual(mod.valid_date('00-15-2023'), False)

    def test_invalid_month_too_high(self):
            # CRITICAL: Boundary Testing (month > 12), Off-by-One Error (12+1), Rule 3 violation
            # Verifies that a month greater than 12 is invalid.
            self.assertEqual(mod.valid_date('13-15-2023'), False)

    def test_valid_date_normal_case_leap_year(self):
            # Normal case: Valid date in a leap year February
            self.assertTrue(mod.valid_date('02-15-2020'))

    def test_valid_date_normal_case_31_day_month(self):
            # Normal case: Valid date in a 31-day month
            self.assertTrue(mod.valid_date('03-11-2000'))

    def test_valid_date_edge_min_date(self):
            # Edge case: Minimum valid day and month
            self.assertTrue(mod.valid_date('01-01-1900'))

    def test_valid_date_edge_max_date_february_leap_year(self):
            # Edge case: Maximum valid day for February in a leap year
            self.assertTrue(mod.valid_date('02-29-2024'))

    def test_invalid_date_empty_string(self):
            # Edge case: Empty string input
            self.assertFalse(mod.valid_date(''))

    def test_invalid_date_month_too_high(self):
            # Edge case: Month greater than 12
            self.assertFalse(mod.valid_date('15-01-2012'))

    def test_invalid_date_day_too_high_for_month(self):
            # Edge case: Day greater than max for a 30-day month
            self.assertFalse(mod.valid_date('04-31-2023'))

    def test_invalid_date_day_too_high_february_non_leap(self):
            # Edge case: Day greater than 29 for February (even if it were a leap year, 30 is too high)
            self.assertFalse(mod.valid_date('02-30-2023'))

    def test_invalid_date_incorrect_separator(self):
            # Edge case: Incorrect date format (uses '/' instead of '-')
            self.assertFalse(mod.valid_date('06/04/2020'))

    def test_invalid_date_non_string_input_none(self):
            # Error case: Input is None (not a string)
            self.assertFalse(mod.valid_date(None))

    def test_invalid_date_non_string_input_int(self):
            # Error case: Input is an integer (not a string)
            self.assertFalse(mod.valid_date(12345))

