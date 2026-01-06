import unittest
from sut.problem_HumanEval_102 import choose_num

class Test_choose_num(unittest.TestCase):
    def test_normal_multiple_evens_largest(self):
        # Range includes multiple even numbers, returns the largest.
        self.assertEqual(choose_num(12, 15), 14)

    def test_normal_largest_is_y(self):
        # Range includes multiple even numbers, largest is y.
        self.assertEqual(choose_num(10, 20), 20)

    def test_normal_x_y_same_even(self):
        # x and y are the same even number.
        self.assertEqual(choose_num(10, 10), 10)

    def test_edge_x_greater_than_y(self):
        # x is greater than y, no numbers in range.
        self.assertEqual(choose_num(13, 12), -1)

    def test_edge_x_y_same_odd(self):
        # x and y are the same odd number, no even number in range.
        self.assertEqual(choose_num(13, 13), -1)

    def test_edge_smallest_no_even(self):
        # Smallest positive range with no even number.
        self.assertEqual(choose_num(1, 1), -1)

    def test_edge_single_even_in_range(self):
        # Range includes only one even number.
        self.assertEqual(choose_num(1, 3), 2)

    def test_edge_smallest_positive_even_x_y(self):
        # Smallest positive even number as both x and y.
        self.assertEqual(choose_num(2, 2), 2)

    def test_error_x_not_positive(self):
        # x is not a positive number (x <= 0).
        with self.assertRaises(ValueError):
            choose_num(0, 5)

    def test_error_y_not_positive(self):
        # y is not a positive number (y <= 0).
        with self.assertRaises(ValueError):
            choose_num(5, 0)

    def test_error_x_not_integer(self):
        # x is not an integer.
        with self.assertRaises(TypeError):
            choose_num('a', 5)

    def test_error_y_not_integer(self):
        # y is not an integer (float provided).
        with self.assertRaises(TypeError):
            choose_num(5, 5.5)