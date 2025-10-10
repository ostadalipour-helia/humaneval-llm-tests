import unittest
from sut.problem_HumanEval_114 import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_example_one(self):
        # Test case from the docstring: all positive, minimum is a single element.
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_example_two(self):
        # Test case from the docstring: all negative, minimum is the sum of all elements.
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_all_positive_different_min(self):
        # All positive numbers, minimum is a single element not at the ends.
        self.assertEqual(minSubArraySum([10, 5, 20, 3, 15]), 3)

    def test_all_negative_mixed_length(self):
        # All negative numbers, minimum is the sum of all elements.
        self.assertEqual(minSubArraySum([-5, -1, -10, -2]), -18)

    def test_mixed_numbers_negative_sum_middle(self):
        # Mixed positive and negative, minimum is a sum of consecutive negative numbers in the middle.
        self.assertEqual(minSubArraySum([1, -2, -3, 4, -1]), -5)

    def test_mixed_numbers_single_negative_min(self):
        # Mixed positive and negative, minimum is a single very negative element.
        self.assertEqual(minSubArraySum([10, -100, 5, -1, 20]), -100)

    def test_array_with_zeros(self):
        # Array containing zeros, minimum is a negative element.
        self.assertEqual(minSubArraySum([5, 0, -7, 0, 3]), -7)

    def test_single_element_positive(self):
        # Edge case: array with a single positive element.
        self.assertEqual(minSubArraySum([42]), 42)

    def test_single_element_negative(self):
        # Edge case: array with a single negative element.
        self.assertEqual(minSubArraySum([-99]), -99)

    def test_mixed_numbers_min_at_start(self):
        # Mixed positive and negative, minimum is a sum of elements at the beginning.
        self.assertEqual(minSubArraySum([-10, -5, 1, 20, 30]), -15)

if __name__ == '__main__':
    unittest.main()