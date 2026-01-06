import unittest
from sut.problem_HumanEval_40 import triples_sum_to_zero

class Test_triples_sum_to_zero(unittest.TestCase):

    # Helper method to test the function and ensure the input list is not modified
    def _test_and_check_invariant(self, input_list, expected_output):
        # Create a copy of the input list to check for modifications
        original_list_copy = list(input_list)
        
        # Call the function under test
        result = triples_sum_to_zero(input_list)
        
        # Assert the function's return value
        self.assertEqual(result, expected_output)
        
        # Assert that the input list was not modified
        self.assertEqual(input_list, original_list_copy, "The input list was modified by the function.")

    # Normal Cases
    def test_normal_no_sum_to_zero_case1(self):
        # Description: No three distinct elements sum to zero.
        self._test_and_check_invariant([1, 3, 5, 0], False)

    def test_normal_sum_to_zero_with_duplicates(self):
        # Description: Elements at distinct indices (e.g., l[0]=1, l[2]=-2, l[3]=1) sum to zero.
        self._test_and_check_invariant([1, 3, -2, 1], True)

    def test_normal_sum_to_zero_mixed_values(self):
        # Description: Elements at distinct indices (e.g., l[0]=2, l[2]=-5, l[3]=3) sum to zero.
        self._test_and_check_invariant([2, 4, -5, 3, 9, 7], True)

    # Edge Cases
    def test_edge_empty_list(self):
        # Description: An empty list, fewer than three elements.
        self._test_and_check_invariant([], False)

    def test_edge_two_elements(self):
        # Description: A list with two elements, fewer than three elements.
        self._test_and_check_invariant([1, 2], False)

    def test_edge_three_zeros(self):
        # Description: Exactly three elements, all zeros, sum to zero.
        self._test_and_check_invariant([0, 0, 0], True)

    def test_edge_three_elements_sum_to_zero(self):
        # Description: Exactly three elements that sum to zero.
        self._test_and_check_invariant([-1, 0, 1], True)

    def test_edge_duplicates_form_sum_to_zero(self):
        # Description: List with duplicate values, but three elements at distinct indices (e.g., l[0]=1, l[1]=1, l[3]=-2) sum to zero.
        self._test_and_check_invariant([1, 1, 1, -2], True)

    # Error Cases
    def test_error_input_is_none(self):
        # Description: Input is not a list.
        with self.assertRaises(TypeError):
            triples_sum_to_zero(None)

    def test_error_input_is_integer(self):
        # Description: Input is an integer, not a list.
        with self.assertRaises(TypeError):
            triples_sum_to_zero(123)

    def test_error_list_contains_string(self):
        # Description: List contains non-integer elements (string).
        with self.assertRaises(TypeError):
            triples_sum_to_zero([1, 2, "a"])

    def test_error_list_contains_float(self):
        # Description: List contains non-integer elements (float).
        with self.assertRaises(TypeError):
            triples_sum_to_zero([1, 2, 3.0])