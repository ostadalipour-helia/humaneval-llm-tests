import unittest
from sut.problem_HumanEval_0 import has_close_elements

class Test_has_close_elements(unittest.TestCase):
    def test_normal_no_close_elements(self):
        # No two numbers are closer than the threshold.
        numbers = [1.0, 2.0, 3.0]
        threshold = 0.5
        expected_output = False
        self.assertEqual(has_close_elements(numbers, threshold), expected_output)

    def test_normal_two_close_elements(self):
        # Two numbers (2.8 and 3.0) are closer than the threshold (abs(2.8-3.0) = 0.2 < 0.3).
        numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
        threshold = 0.3
        expected_output = True
        self.assertEqual(has_close_elements(numbers, threshold), expected_output)

    def test_normal_small_difference(self):
        # Two numbers (10.0 and 10.05) are closer than the threshold (abs(10.0-10.05) = 0.05 < 0.06).
        numbers = [10.0, 10.05, 10.1, 10.2]
        threshold = 0.06
        expected_output = True
        self.assertEqual(has_close_elements(numbers, threshold), expected_output)

    def test_edge_empty_list(self):
        # Empty list of numbers, no pairs to compare.
        numbers = []
        threshold = 0.5
        expected_output = False
        self.assertEqual(has_close_elements(numbers, threshold), expected_output)

    def test_edge_identical_elements(self):
        # List contains identical numbers at different indices, their difference is 0 which is less than a positive threshold.
        numbers = [1.0, 1.0, 2.0]
        threshold = 0.1
        expected_output = True
        self.assertEqual(has_close_elements(numbers, threshold), expected_output)

    def test_edge_zero_threshold(self):
        # Threshold is zero, so no absolute difference can be strictly less than it.
        numbers = [1.0, 2.0, 3.0]
        threshold = 0.0
        expected_output = False
        self.assertEqual(has_close_elements(numbers, threshold), expected_output)

    def test_edge_negative_numbers(self):
        # List contains negative numbers, abs(-1.0 - -1.2) = 0.2 < 0.3.
        numbers = [-1.0, -1.2, 0.0]
        threshold = 0.3
        expected_output = True
        self.assertEqual(has_close_elements(numbers, threshold), expected_output)

    def test_error_numbers_not_list(self):
        # 'numbers' is not a list.
        numbers = "not a list"
        threshold = 0.5
        with self.assertRaises(TypeError):
            has_close_elements(numbers, threshold)

    def test_error_numbers_contains_non_float(self):
        # 'numbers' contains non-float elements (integers).
        numbers = [1, 2, 3]
        threshold = 0.5
        with self.assertRaises(TypeError):
            has_close_elements(numbers, threshold)

    def test_error_threshold_not_float(self):
        # 'threshold' is not a float.
        numbers = [1.0, 2.0]
        threshold = "not a float"
        with self.assertRaises(TypeError):
            has_close_elements(numbers, threshold)