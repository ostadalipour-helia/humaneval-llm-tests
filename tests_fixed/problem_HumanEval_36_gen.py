import unittest
from sut_llm.problem_HumanEval_36 import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_docstring_example_50(self):
        # Test a typical input as per docstring example
        self.assertEqual(fizz_buzz(50), 0)

    def test_docstring_example_78(self):
        # Test a typical input as per docstring example, includes 77 (two 7s)
        self.assertEqual(fizz_buzz(78), 2)

    def test_docstring_example_79(self):
        # Test a typical input as per docstring example, includes 77 (two 7s) and 78 (one 7)
        self.assertEqual(fizz_buzz(79), 3)

    def test_empty_range_n_1(self):
        # Boundary test: n=1, the range (1 to n-1) is empty
        self.assertEqual(fizz_buzz(1), 0)

    def test_empty_range_n_0(self):
        # Edge case: n=0, the range (1 to n-1) is empty
        self.assertEqual(fizz_buzz(0), 0)

    def test_no_sevens_before_77(self):
        # Boundary test: n just before the first number containing 7 (77) that qualifies
        # Checks numbers up to 69. All qualifying numbers (11,13,22,26,33,39,44,52,55,65,66) have no 7s.
        self.assertEqual(fizz_buzz(70), 0)

    def test_first_divisible_no_seven(self):
        # Edge case: n includes 11 and 13, but neither contains a 7.
        # Tests the 'or' condition for divisibility and the absence of '7'.
        self.assertEqual(fizz_buzz(14), 0)

    def test_n_just_after_77_and_78(self):
        # Boundary and off-by-one test: n=80, includes 77 (two 7s) and 78 (one 7).
        # Verifies the count when crossing a critical number.
        self.assertEqual(fizz_buzz(80), 3)

    def test_large_range_with_multiple_sevens(self):
        # Extreme input: A larger range to test cumulative counting.
        # Includes 77 (2x7) and 78 (1x7).
        self.assertEqual(fizz_buzz(100), 3)

    def test_very_large_range_with_more_sevens(self):
        # Extreme input: An even larger range, including 176 (div by 11, one 7) and 187 (div by 11, one 7).
        # Expected: 77 (2) + 78 (1) + 117 (1) + 176 (1) + 187 (1) = 6
        self.assertEqual(fizz_buzz(200), 6)