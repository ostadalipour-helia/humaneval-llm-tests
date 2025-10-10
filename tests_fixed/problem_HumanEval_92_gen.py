import unittest
from sut_llm.problem_HumanEval_92 import any_int

class TestAnyInt(unittest.TestCase):

    def test_01_basic_true_case_x_is_sum_of_y_z(self):
        # Test case from docstring: x = y + z, all integers
        self.assertEqual(any_int(5, 2, 7), True)

    def test_02_basic_false_case_one_float_number(self):
        # Test case from docstring: one number is a float
        self.assertEqual(any_int(3.6, -2.2, 2), False)

    def test_03_sum_condition_fails_off_by_one_positive(self):
        # All integers, but no number is the sum of the other two (off-by-one)
        self.assertEqual(any_int(5, 2, 6), False)

    def test_04_sum_condition_fails_off_by_one_negative(self):
        # All integers, but no number is the sum of the other two (off-by-one)
        self.assertEqual(any_int(5, 3, 1), False)

    def test_05_true_case_y_is_sum_of_x_z(self):
        # Test where y = x + z, all integers
        self.assertEqual(any_int(2, 7, 5), True)

    def test_06_true_case_z_is_sum_of_x_y(self):
        # Test where z = x + y, all integers
        self.assertEqual(any_int(7, 5, 2), True)

    def test_07_false_case_duplicate_numbers_sum_fails(self):
        # Test case from docstring: duplicate numbers, sum condition fails
        self.assertEqual(any_int(3, 2, 2), False)

    def test_08_true_case_with_negative_numbers(self):
        # Test case from docstring: negative numbers, sum condition holds
        self.assertEqual(any_int(3, -2, 1), True)

    def test_09_true_case_with_all_zero_values(self):
        # Edge case: all numbers are zero, sum condition holds (0 = 0 + 0)
        self.assertEqual(any_int(0, 0, 0), True)

    def test_10_extreme_values_large_numbers(self):
        # Test with very large numbers where sum condition holds
        self.assertEqual(any_int(10**9, 1, 10**9 + 1), True)