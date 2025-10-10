import unittest
from sut_llm.problem_HumanEval_114 import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    # Test 1: Basic example from docstring (mixed positive, min is a single positive element)
    # Covers: Typical input, exact output, positive numbers, minimum is a single element.
    def test_example_mixed_positive_min_single(self):
        nums = [2, 3, 4, 1, 2, 4]
        self.assertEqual(minSubArraySum(nums), 1)

    # Test 2: Basic example from docstring (all negative, min is the entire array sum)
    # Covers: Typical input, exact output, all negative numbers, minimum is the sum of the entire array.
    def test_example_all_negative_min_entire_array(self):
        nums = [-1, -2, -3]
        self.assertEqual(minSubArraySum(nums), -6)

    # Test 3: Single element array (positive)
    # Covers: Edge case (single element), boundary condition (smallest possible array length).
    def test_single_positive_element(self):
        nums = [5]
        self.assertEqual(minSubArraySum(nums), 5)

    # Test 4: Single element array (negative)
    # Covers: Edge case (single element), boundary condition, negative numbers.
    def test_single_negative_element(self):
        nums = [-10]
        self.assertEqual(minSubArraySum(nums), -10)

    # Test 5: Array containing zero, where zero is the minimum sub-array sum
    # Covers: Sign and Zero testing, minimum sum is zero.
    def test_array_with_zero_min_is_zero(self):
        nums = [1, 0, 2]
        self.assertEqual(minSubArraySum(nums), 0)

    # Test 6: Mixed positive/negative, minimum is a single negative number in the middle
    # Covers: Boundary (minimum is a single element not at an end), mixed signs, off-by-one potential.
    def test_mixed_min_single_negative_middle(self):
        nums = [10, -5, 20]
        self.assertEqual(minSubArraySum(nums), -5)

    # Test 7: Mixed positive/negative, minimum is a sub-array of multiple negative numbers
    # Covers: Logic mutations (e.g., if a sum was incorrectly reset), multiple negative numbers forming the minimum.
    def test_mixed_min_multiple_negative_subarray(self):
        nums = [5, -1, -2, 3, -1, 4] # The minimum sub-array is [-1, -2] with sum -3
        self.assertEqual(minSubArraySum(nums), -3)

    # Test 8: Array with all same positive numbers
    # Covers: Edge case (all same values), boundary (minimum is a single element).
    def test_all_same_positive_numbers(self):
        nums = [7, 7, 7, 7]
        self.assertEqual(minSubArraySum(nums), 7)

    # Test 9: Array with all same negative numbers
    # Covers: Edge case (all same values), boundary (minimum is the entire array sum), extreme input (large negative sum).
    def test_all_same_negative_numbers(self):
        nums = [-3, -3, -3]
        self.assertEqual(minSubArraySum(nums), -9)

    # Test 10: Longer mixed array, minimum formed by a sequence of negative numbers, with positive numbers interrupting
    # Covers: Extreme/unusual input, off-by-one errors (loop boundaries), logic mutations (handling positive numbers breaking negative streaks).
    def test_longer_mixed_array_min_sequence(self):
        nums = [10, -1, -2, 5, -3, -4, 1] # The minimum sub-array is [-3, -4] with sum -7
        self.assertEqual(minSubArraySum(nums), -7)