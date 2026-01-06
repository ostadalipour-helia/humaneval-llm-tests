import unittest
from sut.problem_HumanEval_114 import minSubArraySum

class Test_minSubArraySum(unittest.TestCase):

    def test_normal_positive_elements(self):
        # Example from docstring: minimum sum is a single positive element.
        nums = [2, 3, 4, 1, 2, 4]
        expected_output = 1
        self.assertEqual(minSubArraySum(nums), expected_output)

    def test_normal_all_negative_elements(self):
        # Example from docstring: minimum sum is the sum of all negative elements.
        nums = [-1, -2, -3]
        expected_output = -6
        self.assertEqual(minSubArraySum(nums), expected_output)

    def test_normal_mixed_single_negative(self):
        # Mixed positive and negative numbers, minimum is a single negative element.
        nums = [1, -2, 3, -4, 5]
        expected_output = -4
        self.assertEqual(minSubArraySum(nums), expected_output)

    def test_edge_single_positive_element(self):
        # Single element array.
        nums = [7]
        expected_output = 7
        self.assertEqual(minSubArraySum(nums), expected_output)

    def test_edge_all_zeros(self):
        # Array with all zeros.
        nums = [0, 0, 0]
        expected_output = 0
        self.assertEqual(minSubArraySum(nums), expected_output)

    def test_edge_negative_block_surrounded(self):
        # Minimum sum is a contiguous block of negative numbers surrounded by large positive numbers.
        nums = [100, -1, -2, -3, 200]
        expected_output = -6
        self.assertEqual(minSubArraySum(nums), expected_output)

    def test_error_empty_list(self):
        # Input list is empty, no non-empty sub-array can be formed.
        nums = []
        with self.assertRaises(ValueError):
            minSubArraySum(nums)

    def test_error_non_integer_elements(self):
        # Input list contains non-integer elements.
        nums = [1, 'a', 3]
        with self.assertRaises(TypeError):
            minSubArraySum(nums)

    def test_error_input_is_none(self):
        # Input is not a list (e.g., None).
        nums = None
        with self.assertRaises(TypeError):
            minSubArraySum(nums)

    def test_error_input_is_integer(self):
        # Input is not a list (e.g., an integer).
        nums = 123
        with self.assertRaises(TypeError):
            minSubArraySum(nums)