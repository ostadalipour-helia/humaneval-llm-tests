import unittest
from sut.problem_HumanEval_102 import choose_num

class TestChooseNum(unittest.TestCase):

    def test_docstring_example_1(self):
        # Typical case: range contains even numbers, y is odd, result is y-1
        self.assertEqual(choose_num(12, 15), 14)

    def test_docstring_example_2_invalid_range(self):
        # Boundary case: x > y, should return -1
        self.assertEqual(choose_num(13, 12), -1)

    def test_x_equals_y_even(self):
        # Boundary case: x = y, and the number is even
        self.assertEqual(choose_num(10, 10), 10)

    def test_x_equals_y_odd(self):
        # Boundary case: x = y, and the number is odd, no even found
        self.assertEqual(choose_num(11, 11), -1)

    def test_smallest_positive_no_even(self):
        # Edge case: Smallest positive numbers, no even in range
        self.assertEqual(choose_num(1, 1), -1)

    def test_smallest_positive_with_even(self):
        # Edge case: Smallest positive numbers, range includes an even
        self.assertEqual(choose_num(1, 2), 2)

    def test_range_all_odd_no_even(self):
        # Logic mutation: Range contains only odd numbers, no even found
        self.assertEqual(choose_num(3, 5), -1)

    def test_range_starts_odd_ends_even(self):
        # Typical case: Range starts with odd, ends with even, y is the result
        self.assertEqual(choose_num(7, 10), 10)

    def test_large_numbers_y_minus_1_is_target(self):
        # Extreme input: Large numbers, y is odd, result is y-1
        self.assertEqual(choose_num(1000001, 1000005), 1000004)

    def test_large_numbers_y_is_target(self):
        # Extreme input: Large numbers, y is even, result is y
        self.assertEqual(choose_num(1000000, 1000004), 1000004)