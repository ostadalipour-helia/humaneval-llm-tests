import unittest
import sut.problem_HumanEval_36 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_50(self):
            # Test a typical input as per docstring example
            self.assertEqual(mod.fizz_buzz(50), 0)

    def test_docstring_example_78(self):
            # Test a typical input as per docstring example, includes 77 (two 7s)
            self.assertEqual(mod.fizz_buzz(78), 2)

    def test_docstring_example_79(self):
            # Test a typical input as per docstring example, includes 77 (two 7s) and 78 (one 7)
            self.assertEqual(mod.fizz_buzz(79), 3)

    def test_empty_range_n_1(self):
            # Boundary test: n=1, the range (1 to n-1) is empty
            self.assertEqual(mod.fizz_buzz(1), 0)

    def test_empty_range_n_0(self):
            # Edge case: n=0, the range (1 to n-1) is empty
            self.assertEqual(mod.fizz_buzz(0), 0)

    def test_no_sevens_before_77(self):
            # Boundary test: n just before the first number containing 7 (77) that qualifies
            # Checks numbers up to 69. All qualifying numbers (11,13,22,26,33,39,44,52,55,65,66) have no 7s.
            self.assertEqual(mod.fizz_buzz(70), 0)

    def test_first_divisible_no_seven(self):
            # Edge case: n includes 11 and 13, but neither contains a 7.
            # Tests the 'or' condition for divisibility and the absence of '7'.
            self.assertEqual(mod.fizz_buzz(14), 0)

    def test_n_just_after_77_and_78(self):
            # Boundary and off-by-one test: n=80, includes 77 (two 7s) and 78 (one 7).
            # Verifies the count when crossing a critical number.
            self.assertEqual(mod.fizz_buzz(80), 3)

    def test_large_range_with_multiple_sevens(self):
            # Extreme input: A larger range to test cumulative counting.
            # Includes 77 (2x7) and 78 (1x7).
            self.assertEqual(mod.fizz_buzz(100), 3)

    def test_normal_case_n50(self):
            """
            Numbers less than 50 divisible by 11 or 13 are: 11, 13, 22, 26, 33, 39, 44.
            None of these contain the digit '7'.
            """
            self.assertEqual(mod.fizz_buzz(50), 0)

    def test_normal_case_n78(self):
            """
            Numbers less than 78 divisible by 11 or 13 include 77 (11 * 7).
            The number 77 contains two '7's. No other qualifying numbers in this range contain '7'.
            """
            self.assertEqual(mod.fizz_buzz(78), 2)

    def test_normal_case_n100(self):
            """
            Numbers less than 100 divisible by 11 or 13 that contain the digit '7' are:
            77 (two '7's) and 91 (13 * 7, one '7'). The total count is 2 + 1 = 3.
            """
            self.assertEqual(mod.fizz_buzz(100), 3)

    def test_edge_case_n0(self):
            """
            When n is 0, the range of integers (1 to n-1) is empty,
            so no numbers are checked and the count is 0.
            """
            self.assertEqual(mod.fizz_buzz(0), 0)

    def test_edge_case_n1(self):
            """
            When n is 1, the range of integers (1 to n-1) is empty,
            so no numbers are checked and the count is 0.
            """
            self.assertEqual(mod.fizz_buzz(1), 0)

    def test_edge_case_n10(self):
            """
            No numbers less than 10 are divisible by 11 or 13, so the count is 0.
            """
            self.assertEqual(mod.fizz_buzz(10), 0)

    def test_edge_case_n77(self):
            """
            Numbers less than 77 divisible by 11 or 13 (e.g., 11, 13, ..., 66)
            do not contain the digit '7'. The number 77 itself is not included
            as it is not 'less than n'.
            """
            self.assertEqual(mod.fizz_buzz(77), 0)

    def test_error_case_n_string(self):
            """
            Input 'n' must be an integer.
            """
            with self.assertRaises(TypeError):
                mod.fizz_buzz("invalid")

    def test_error_case_n_float(self):
            """
            Input 'n' must be an integer.
            """
            with self.assertRaises(TypeError):
                mod.fizz_buzz(7.5)

    def test_error_case_n_none(self):
            """
            Input 'n' must be an integer.
            """
            with self.assertRaises(TypeError):
                mod.fizz_buzz(None)

