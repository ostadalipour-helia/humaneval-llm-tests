import unittest
from sut.problem_HumanEval_126 import is_sorted

class Test_is_sorted(unittest.TestCase):

    # Normal Cases
    def test_normal_sorted_no_duplicates(self):
        # Reason: List is sorted in ascending order, and no number appears more than twice.
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))

    def test_normal_unsorted(self):
        # Reason: List is not sorted in ascending order (3 > 2).
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))

    def test_normal_sorted_with_two_duplicates(self):
        # Reason: List is sorted in ascending order, and numbers 2 and 3 each appear exactly twice, which is allowed.
        self.assertTrue(is_sorted([1, 2, 2, 3, 3, 4]))

    def test_normal_sorted_with_three_duplicates(self):
        # Reason: List is sorted, but the number 2 appears three times, violating the 'no more than 1 duplicate' rule.
        self.assertFalse(is_sorted([1, 2, 2, 2, 3, 4]))

    # Edge Cases
    def test_edge_empty_list(self):
        # Reason: An empty list is considered sorted and has no duplicates.
        self.assertTrue(is_sorted([]))

    def test_edge_single_element_list(self):
        # Reason: A list with a single element is considered sorted and has no duplicates.
        self.assertTrue(is_sorted([5]))

    def test_edge_two_elements_one_duplicate(self):
        # Reason: List is sorted, and the number 1 appears twice, which is allowed.
        self.assertTrue(is_sorted([1, 1]))

    def test_edge_three_elements_three_duplicates(self):
        # Reason: List is sorted, but the number 0 appears three times, violating the duplicate rule.
        self.assertFalse(is_sorted([0, 0, 0]))

    # Error Conditions
    def test_error_non_integer_element(self):
        # Reason: Input list contains a non-integer element (2.5), violating the precondition.
        with self.assertRaises(TypeError):
            is_sorted([1, 2.5, 3])

    def test_error_negative_element(self):
        # Reason: Input list contains a negative number (-2), violating the precondition.
        with self.assertRaises(ValueError):
            is_sorted([1, -2, 3])

    def test_error_input_not_list(self):
        # Reason: Input is not a list (None or string), violating the precondition.
        with self.assertRaises(TypeError):
            is_sorted(None)
        with self.assertRaises(TypeError):
            is_sorted("hello")

    # Invariant Check
    def test_invariant_list_not_modified(self):
        # Reason: The input list `lst` must not be modified by the function.
        original_list = [1, 2, 2, 3, 4]
        list_copy = list(original_list) # Create a copy to ensure no modification
        is_sorted(original_list) # Call the function
        self.assertEqual(original_list, list_copy, "The input list was modified by the function.")