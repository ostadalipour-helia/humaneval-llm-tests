import unittest
from sut.problem_HumanEval_43 import pairs_sum_to_zero

class Test_pairs_sum_to_zero(unittest.TestCase):

    def test_normal_positive_pair(self):
        # Description: List contains a pair (5, -5) that sums to zero.
        l = [2, 4, -5, 3, 5, 7]
        original_l = list(l) # For invariant check
        expected_output = True
        self.assertEqual(pairs_sum_to_zero(l), expected_output)
        self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_normal_no_pair(self):
        # Description: List contains no pair that sums to zero.
        l = [1, 3, 5, 0]
        original_l = list(l) # For invariant check
        expected_output = False
        self.assertEqual(pairs_sum_to_zero(l), expected_output)
        self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_normal_multiple_pairs(self):
        # Description: List with multiple pairs summing to zero.
        l = [1, -1, 2, -2]
        original_l = list(l) # For invariant check
        expected_output = True
        self.assertEqual(pairs_sum_to_zero(l), expected_output)
        self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_empty_list(self):
        # Description: Empty list, no pairs possible.
        l = []
        original_l = list(l) # For invariant check
        expected_output = False
        self.assertEqual(pairs_sum_to_zero(l), expected_output)
        self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_single_element(self):
        # Description: List with a single element, no pairs possible.
        l = [1]
        original_l = list(l) # For invariant check
        expected_output = False
        self.assertEqual(pairs_sum_to_zero(l), expected_output)
        self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_two_zeros(self):
        # Description: List with two zeros, which are distinct elements by index and sum to zero.
        l = [0, 0]
        original_l = list(l) # For invariant check
        expected_output = True
        self.assertEqual(pairs_sum_to_zero(l), expected_output)
        self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_two_elements_sum_to_zero(self):
        # Description: List with exactly two elements that sum to zero.
        l = [1, -1]
        original_l = list(l) # For invariant check
        expected_output = True
        self.assertEqual(pairs_sum_to_zero(l), expected_output)
        self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_large_numbers(self):
        # Description: List with large numbers summing to zero.
        l = [-1000000, 1000000]
        original_l = list(l) # For invariant check
        expected_output = True
        self.assertEqual(pairs_sum_to_zero(l), expected_output)
        self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_error_non_list_input(self):
        # Description: Input `l` is not a list.
        l = "not a list"
        with self.assertRaises(TypeError):
            pairs_sum_to_zero(l)

    def test_error_list_with_string(self):
        # Description: List contains non-integer elements (string).
        l = [1, 2, "three"]
        with self.assertRaises(TypeError):
            pairs_sum_to_zero(l)

    def test_error_list_with_float(self):
        # Description: List contains non-integer elements (float).
        l = [1, 2.5]
        with self.assertRaises(TypeError):
            pairs_sum_to_zero(l)