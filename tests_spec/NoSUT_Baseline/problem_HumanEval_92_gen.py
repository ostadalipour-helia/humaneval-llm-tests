import unittest
import sut.problem_HumanEval_92 as mod

class TestHybrid(unittest.TestCase):
    def test_01_basic_true_case_x_is_sum_of_y_z(self):
            # Test case from docstring: x = y + z, all integers
            self.assertEqual(mod.any_int(5, 2, 7), True)

    def test_02_basic_false_case_one_float_number(self):
            # Test case from docstring: one number is a float
            self.assertEqual(mod.any_int(3.6, -2.2, 2), False)

    def test_03_sum_condition_fails_off_by_one_positive(self):
            # All integers, but no number is the sum of the other two (off-by-one)
            self.assertEqual(mod.any_int(5, 2, 6), False)

    def test_04_sum_condition_fails_off_by_one_negative(self):
            # All integers, but no number is the sum of the other two (off-by-one)
            self.assertEqual(mod.any_int(5, 3, 1), False)

    def test_05_true_case_y_is_sum_of_x_z(self):
            # Test where y = x + z, all integers
            self.assertEqual(mod.any_int(2, 7, 5), True)

    def test_06_true_case_z_is_sum_of_x_y(self):
            # Test where z = x + y, all integers
            self.assertEqual(mod.any_int(7, 5, 2), True)

    def test_07_false_case_duplicate_numbers_sum_fails(self):
            # Test case from docstring: duplicate numbers, sum condition fails
            self.assertEqual(mod.any_int(3, 2, 2), False)

    def test_08_true_case_with_negative_numbers(self):
            # Test case from docstring: negative numbers, sum condition holds
            self.assertEqual(mod.any_int(3, -2, 1), True)

    def test_09_true_case_with_all_zero_values(self):
            # Edge case: all numbers are zero, sum condition holds (0 = 0 + 0)
            self.assertEqual(mod.any_int(0, 0, 0), True)

    def test_10_extreme_values_large_numbers(self):
            # Test with very large numbers where sum condition holds
            self.assertEqual(mod.any_int(10**9, 1, 10**9 + 1), True)

    def test_normal_positive_sum(self):
            # Normal case: All integers, one is sum of others (7 == 5 + 2)
            self.assertTrue(mod.any_int(5, 2, 7))

    def test_normal_negative_sum(self):
            # Normal case: All integers, one is sum of others (1 == 3 + (-2))
            self.assertTrue(mod.any_int(3, -2, 1))

    def test_normal_no_sum(self):
            # Normal case: All integers, but no sum matches (3 != 2+2)
            self.assertFalse(mod.any_int(3, 2, 2))

    def test_edge_zero_sum(self):
            # Edge case: All zeros, sum matches (0 == 0 + 0)
            self.assertTrue(mod.any_int(0, 0, 0))

    def test_edge_mixed_zero_sum(self):
            # Edge case: Zero and positive integers, sum matches (5 == 0 + 5)
            self.assertTrue(mod.any_int(0, 5, 5))

    def test_edge_negative_all_sum(self):
            # Edge case: All negative integers, sum matches (-7 == -5 + (-2))
            self.assertTrue(mod.any_int(-5, -2, -7))

    def test_edge_float_one_arg(self):
            # Edge case: Not all integers (3.6 and -2.2 are floats)
            self.assertFalse(mod.any_int(3.6, -2.2, 2))

    def test_edge_float_integer_value(self):
            # Edge case: 3.0 is a float, not an integer type, even if its value is an integer.
            self.assertFalse(mod.any_int(3.0, 2, 5))

    def test_edge_all_floats_integer_value(self):
            # Edge case: All numbers are floats, not integers, even if values are integers.
            self.assertFalse(mod.any_int(1.0, 2.0, 3.0))

    def test_edge_all_floats_zero_value(self):
            # Edge case: All numbers are floats, not integers, even if values are zero.
            self.assertFalse(mod.any_int(0.0, 0.0, 0.0))

