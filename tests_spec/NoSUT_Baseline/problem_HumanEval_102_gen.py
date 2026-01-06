import unittest
import sut.problem_HumanEval_102 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1(self):
            # Typical case: range contains even numbers, y is odd, result is y-1
            self.assertEqual(mod.choose_num(12, 15), 14)

    def test_docstring_example_2_invalid_range(self):
            # Boundary case: x > y, should return -1
            self.assertEqual(mod.choose_num(13, 12), -1)

    def test_x_equals_y_even(self):
            # Boundary case: x = y, and the number is even
            self.assertEqual(mod.choose_num(10, 10), 10)

    def test_x_equals_y_odd(self):
            # Boundary case: x = y, and the number is odd, no even found
            self.assertEqual(mod.choose_num(11, 11), -1)

    def test_smallest_positive_no_even(self):
            # Edge case: Smallest positive numbers, no even in range
            self.assertEqual(mod.choose_num(1, 1), -1)

    def test_smallest_positive_with_even(self):
            # Edge case: Smallest positive numbers, range includes an even
            self.assertEqual(mod.choose_num(1, 2), 2)

    def test_range_starts_odd_ends_even(self):
            # Typical case: Range starts with odd, ends with even, y is the result
            self.assertEqual(mod.choose_num(7, 10), 10)

    def test_large_numbers_y_minus_1_is_target(self):
            # Extreme input: Large numbers, y is odd, result is y-1
            self.assertEqual(mod.choose_num(1000001, 1000005), 1000004)

    def test_large_numbers_y_is_target(self):
            # Extreme input: Large numbers, y is even, result is y
            self.assertEqual(mod.choose_num(1000000, 1000004), 1000004)

    def test_normal_multiple_evens_largest(self):
            # Range includes multiple even numbers, returns the largest.
            self.assertEqual(mod.choose_num(12, 15), 14)

    def test_normal_largest_is_y(self):
            # Range includes multiple even numbers, largest is y.
            self.assertEqual(mod.choose_num(10, 20), 20)

    def test_normal_x_y_same_even(self):
            # x and y are the same even number.
            self.assertEqual(mod.choose_num(10, 10), 10)

    def test_edge_x_greater_than_y(self):
            # x is greater than y, no numbers in range.
            self.assertEqual(mod.choose_num(13, 12), -1)

    def test_edge_x_y_same_odd(self):
            # x and y are the same odd number, no even number in range.
            self.assertEqual(mod.choose_num(13, 13), -1)

    def test_edge_smallest_no_even(self):
            # Smallest positive range with no even number.
            self.assertEqual(mod.choose_num(1, 1), -1)

    def test_edge_single_even_in_range(self):
            # Range includes only one even number.
            self.assertEqual(mod.choose_num(1, 3), 2)

    def test_edge_smallest_positive_even_x_y(self):
            # Smallest positive even number as both x and y.
            self.assertEqual(mod.choose_num(2, 2), 2)

    def test_error_x_not_integer(self):
            # x is not an integer.
            with self.assertRaises(TypeError):
                mod.choose_num('a', 5)

