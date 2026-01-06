import unittest
import sut.problem_HumanEval_0 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1(self):
            # Typical input, no close elements
            numbers = [1.0, 2.0, 3.0]
            threshold = 0.5
            self.assertEqual(mod.has_close_elements(numbers, threshold), False)

    def test_docstring_example_2(self):
            # Typical input, with close elements
            numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
            threshold = 0.3
            self.assertEqual(mod.has_close_elements(numbers, threshold), True)

    def test_boundary_exact_threshold_false(self):
            # Test when difference is exactly equal to threshold (should be False due to '<')
            numbers = [1.0, 2.0]
            threshold = 1.0
            self.assertEqual(mod.has_close_elements(numbers, threshold), False)

    def test_boundary_just_below_threshold_true(self):
            # Test when difference is just below threshold (should be True)
            numbers = [1.0, 1.999]
            threshold = 1.0
            self.assertEqual(mod.has_close_elements(numbers, threshold), True)

    def test_edge_empty_list(self):
            # Edge case: empty list of numbers
            numbers = []
            threshold = 0.1
            self.assertEqual(mod.has_close_elements(numbers, threshold), False)

    def test_edge_single_element_list(self):
            # Edge case: list with a single number
            numbers = [5.0]
            threshold = 0.1
            self.assertEqual(mod.has_close_elements(numbers, threshold), False)

    def test_edge_two_elements_not_close(self):
            # Edge case: list with two elements, but not close enough
            numbers = [1.0, 5.0]
            threshold = 1.0
            self.assertEqual(mod.has_close_elements(numbers, threshold), False)

    def test_extreme_large_numbers_close(self):
            # Extreme input: very large numbers that are close
            numbers = [1000000.0, 1000000.0001]
            threshold = 0.001
            self.assertEqual(mod.has_close_elements(numbers, threshold), True)

    def test_extreme_negative_numbers_close(self):
            # Extreme input: negative numbers that are close
            numbers = [-5.0, -4.95]
            threshold = 0.1
            self.assertEqual(mod.has_close_elements(numbers, threshold), True)

    def test_logic_multiple_close_pairs_mixed_signs(self):
            # Logic mutation: multiple pairs satisfy the condition, including zero and mixed signs
            numbers = [-1.0, 0.0, 0.05, 1.0, 1.02]
            threshold = 0.1
            # abs(0.0 - 0.05) = 0.05 < 0.1
            # abs(1.0 - 1.02) = 0.02 < 0.1
            self.assertEqual(mod.has_close_elements(numbers, threshold), True)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_no_close_elements(self):
            # No two numbers are closer than the threshold.
            numbers = [1.0, 2.0, 3.0]
            threshold = 0.5
            expected_output = False
            self.assertEqual(mod.has_close_elements(numbers, threshold), expected_output)

    def test_normal_two_close_elements(self):
            # Two numbers (2.8 and 3.0) are closer than the threshold (abs(2.8-3.0) = 0.2 < 0.3).
            numbers = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
            threshold = 0.3
            expected_output = True
            self.assertEqual(mod.has_close_elements(numbers, threshold), expected_output)

    def test_normal_small_difference(self):
            # Two numbers (10.0 and 10.05) are closer than the threshold (abs(10.0-10.05) = 0.05 < 0.06).
            numbers = [10.0, 10.05, 10.1, 10.2]
            threshold = 0.06
            expected_output = True
            self.assertEqual(mod.has_close_elements(numbers, threshold), expected_output)

    def test_edge_identical_elements(self):
            # List contains identical numbers at different indices, their difference is 0 which is less than a positive threshold.
            numbers = [1.0, 1.0, 2.0]
            threshold = 0.1
            expected_output = True
            self.assertEqual(mod.has_close_elements(numbers, threshold), expected_output)

    def test_edge_zero_threshold(self):
            # Threshold is zero, so no absolute difference can be strictly less than it.
            numbers = [1.0, 2.0, 3.0]
            threshold = 0.0
            expected_output = False
            self.assertEqual(mod.has_close_elements(numbers, threshold), expected_output)

    def test_edge_negative_numbers(self):
            # List contains negative numbers, abs(-1.0 - -1.2) = 0.2 < 0.3.
            numbers = [-1.0, -1.2, 0.0]
            threshold = 0.3
            expected_output = True
            self.assertEqual(mod.has_close_elements(numbers, threshold), expected_output)

    def test_error_numbers_not_list(self):
            # 'numbers' is not a list.
            numbers = "not a list"
            threshold = 0.5
            with self.assertRaises(TypeError):
                mod.has_close_elements(numbers, threshold)

    def test_error_threshold_not_float(self):
            # 'threshold' is not a float.
            numbers = [1.0, 2.0]
            threshold = "not a float"
            with self.assertRaises(TypeError):
                mod.has_close_elements(numbers, threshold)

