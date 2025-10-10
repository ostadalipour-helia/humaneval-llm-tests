import unittest
from sut.problem_HumanEval_151 import double_the_difference

class TestDoubleTheDifference(unittest.TestCase):

    def test_empty_list(self):
        # Edge case: Empty list should return 0.
        self.assertEqual(double_the_difference([]), 0)

    def test_docstring_example_1(self):
        # Typical input from docstring, verifies sum of squares of odd positive integers.
        self.assertEqual(double_the_difference([1, 3, 2, 0]), 10)

    def test_docstring_example_2(self):
        # Typical input from docstring, verifies negative numbers are ignored.
        self.assertEqual(double_the_difference([-1, -2, 0]), 0)

    def test_single_positive_odd(self):
        # Edge case: Single element list, positive and odd.
        self.assertEqual(double_the_difference([5]), 25)

    def test_all_even_numbers(self):
        # Boundary case: All numbers are even, so none should be included.
        self.assertEqual(double_the_difference([2, 4, 6, 0]), 0)

    def test_all_negative_odd_numbers(self):
        # Boundary case: All numbers are odd but negative, so none should be included.
        self.assertEqual(double_the_difference([-1, -3, -5]), 0)

    def test_mixed_valid_and_invalid(self):
        # Logic mutation test: Mix of positive odd, negative, even, and zero.
        # Valid: 3, 5, 1. Invalid: -3 (negative), 2 (even), 0 (even).
        self.assertEqual(double_the_difference([3, -3, 5, 2, 1, 0]), 35) # 3^2 + 5^2 + 1^2 = 9 + 25 + 1 = 35

    def test_float_numbers_ignored(self):
        # Extreme/unusual input: Contains floats which should be ignored as "not integers".
        # Only 5 is an integer. 1.0, 3.0, 2.5, 7.0 are floats.
        self.assertEqual(double_the_difference([1.0, 3.0, 2.5, 5, 7.0]), 25)

    def test_large_odd_number(self):
        # Extreme/unusual input: A very large positive odd integer.
        large_num = 1000000000000000001
        self.assertEqual(double_the_difference([large_num]), large_num**2)

    def test_zero_and_boundary_values(self):
        # Boundary test: Includes 0, 1, -1, 2, 3, -2 to test conditions around zero and small numbers.
        # Valid: 1, 3. Invalid: 0 (even), -1 (negative), 2 (even), -2 (negative).
        self.assertEqual(double_the_difference([0, 1, -1, 2, 3, -2]), 10) # 1^2 + 3^2 = 1 + 9 = 10