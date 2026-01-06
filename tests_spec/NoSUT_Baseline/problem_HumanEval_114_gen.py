import unittest
import sut.problem_HumanEval_114 as mod

class TestHybrid(unittest.TestCase):
    def test_example_mixed_positive_min_single(self):
            nums = [2, 3, 4, 1, 2, 4]
            self.assertEqual(mod.minSubArraySum(nums), 1)
    
        # Test 2: Basic example from docstring (all negative, min is the entire array sum)
        # Covers: Typical input, exact output, all negative numbers, minimum is the sum of the entire array.

    def test_example_all_negative_min_entire_array(self):
            nums = [-1, -2, -3]
            self.assertEqual(mod.minSubArraySum(nums), -6)
    
        # Test 3: Single element array (positive)
        # Covers: Edge case (single element), boundary condition (smallest possible array length).

    def test_single_positive_element(self):
            nums = [5]
            self.assertEqual(mod.minSubArraySum(nums), 5)
    
        # Test 4: Single element array (negative)
        # Covers: Edge case (single element), boundary condition, negative numbers.

    def test_single_negative_element(self):
            nums = [-10]
            self.assertEqual(mod.minSubArraySum(nums), -10)
    
        # Test 5: Array containing zero, where zero is the minimum sub-array sum
        # Covers: Sign and Zero testing, minimum sum is zero.

    def test_array_with_zero_min_is_zero(self):
            nums = [1, 0, 2]
            self.assertEqual(mod.minSubArraySum(nums), 0)
    
        # Test 6: Mixed positive/negative, minimum is a single negative number in the middle
        # Covers: Boundary (minimum is a single element not at an end), mixed signs, off-by-one potential.

    def test_mixed_min_single_negative_middle(self):
            nums = [10, -5, 20]
            self.assertEqual(mod.minSubArraySum(nums), -5)
    
        # Test 7: Mixed positive/negative, minimum is a sub-array of multiple negative numbers
        # Covers: Logic mutations (e.g., if a sum was incorrectly reset), multiple negative numbers forming the minimum.

    def test_mixed_min_multiple_negative_subarray(self):
            nums = [5, -1, -2, 3, -1, 4] # The minimum sub-array is [-1, -2] with sum -3
            self.assertEqual(mod.minSubArraySum(nums), -3)
    
        # Test 8: Array with all same positive numbers
        # Covers: Edge case (all same values), boundary (minimum is a single element).

    def test_all_same_positive_numbers(self):
            nums = [7, 7, 7, 7]
            self.assertEqual(mod.minSubArraySum(nums), 7)
    
        # Test 9: Array with all same negative numbers
        # Covers: Edge case (all same values), boundary (minimum is the entire array sum), extreme input (large negative sum).

    def test_all_same_negative_numbers(self):
            nums = [-3, -3, -3]
            self.assertEqual(mod.minSubArraySum(nums), -9)
    
        # Test 10: Longer mixed array, minimum formed by a sequence of negative numbers, with positive numbers interrupting
        # Covers: Extreme/unusual input, off-by-one errors (loop boundaries), logic mutations (handling positive numbers breaking negative streaks).

    def test_longer_mixed_array_min_sequence(self):
            nums = [10, -1, -2, 5, -3, -4, 1] # The minimum sub-array is [-3, -4] with sum -7
            self.assertEqual(mod.minSubArraySum(nums), -7)

    def test_normal_positive_elements(self):
            # Example from docstring: minimum sum is a single positive element.
            nums = [2, 3, 4, 1, 2, 4]
            expected_output = 1
            self.assertEqual(mod.minSubArraySum(nums), expected_output)

    def test_normal_all_negative_elements(self):
            # Example from docstring: minimum sum is the sum of all negative elements.
            nums = [-1, -2, -3]
            expected_output = -6
            self.assertEqual(mod.minSubArraySum(nums), expected_output)

    def test_normal_mixed_single_negative(self):
            # Mixed positive and negative numbers, minimum is a single negative element.
            nums = [1, -2, 3, -4, 5]
            expected_output = -4
            self.assertEqual(mod.minSubArraySum(nums), expected_output)

    def test_edge_single_positive_element(self):
            # Single element array.
            nums = [7]
            expected_output = 7
            self.assertEqual(mod.minSubArraySum(nums), expected_output)

    def test_edge_all_zeros(self):
            # Array with all zeros.
            nums = [0, 0, 0]
            expected_output = 0
            self.assertEqual(mod.minSubArraySum(nums), expected_output)

    def test_edge_negative_block_surrounded(self):
            # Minimum sum is a contiguous block of negative numbers surrounded by large positive numbers.
            nums = [100, -1, -2, -3, 200]
            expected_output = -6
            self.assertEqual(mod.minSubArraySum(nums), expected_output)

    def test_error_empty_list(self):
            # Input list is empty, no non-empty sub-array can be formed.
            nums = []
            with self.assertRaises(ValueError):
                mod.minSubArraySum(nums)

    def test_error_non_integer_elements(self):
            # Input list contains non-integer elements.
            nums = [1, 'a', 3]
            with self.assertRaises(TypeError):
                mod.minSubArraySum(nums)

    def test_error_input_is_none(self):
            # Input is not a list (e.g., None).
            nums = None
            with self.assertRaises(TypeError):
                mod.minSubArraySum(nums)

    def test_error_input_is_integer(self):
            # Input is not a list (e.g., an integer).
            nums = 123
            with self.assertRaises(TypeError):
                mod.minSubArraySum(nums)

