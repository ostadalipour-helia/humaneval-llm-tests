import unittest
import sut.problem_HumanEval_126 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_list(self):
            # Edge case: An empty list is considered sorted and has no duplicates.
            self.assertEqual(mod.is_sorted([]), True)

    def test_single_element_list(self):
            # Edge case: A single-element list is considered sorted and has no duplicates.
            self.assertEqual(mod.is_sorted([5]), True)

    def test_perfectly_sorted_no_duplicates(self):
            # Typical input: A list sorted in ascending order with no duplicates.
            self.assertEqual(mod.is_sorted([1, 2, 3, 4, 5]), True)

    def test_unsorted_middle_element(self):
            # Typical input: A list that violates ascending order in the middle.
            # Tests the '<' vs '<=' boundary for sorting.
            self.assertEqual(mod.is_sorted([1, 3, 2, 4, 5]), False)

    def test_sorted_with_one_duplicate_pair(self):
            # Boundary condition: A list sorted with exactly one pair of duplicates.
            # This should return True as per the "more than 1 duplicate" rule.
            self.assertEqual(mod.is_sorted([1, 2, 2, 3, 4]), True)

    def test_sorted_with_two_duplicate_pairs(self):
            # Boundary condition: A list sorted with multiple pairs of duplicates.
            # This should return True.
            self.assertEqual(mod.is_sorted([1, 1, 2, 2, 3]), True)

    def test_sorted_with_three_duplicates_of_one_number(self):
            # Boundary condition: A list sorted but with three occurrences of the same number.
            # This violates the "more than 1 duplicate" rule, so should be False.
            self.assertEqual(mod.is_sorted([1, 2, 2, 2, 3]), False)

    def test_unsorted_with_three_duplicates(self):
            # Logic mutation test: A list that is both unsorted AND has too many duplicates.
            # Verifies that either condition failing leads to False.
            self.assertEqual(mod.is_sorted([1, 3, 2, 2, 2, 4]), False)

    def test_boundary_zero_and_one_duplicate(self):
            # Sign and Zero Testing: Tests with zero and a duplicate pair of zeros.
            # This should be True.
            self.assertEqual(mod.is_sorted([0, 0, 1, 2]), True)

    def test_large_numbers_sorted_with_duplicate(self):
            # Extreme input: Tests with large numbers and a duplicate pair.
            # Verifies handling of larger integer values.
            self.assertEqual(mod.is_sorted([100, 100, 200, 300, 1000000]), True)

    def test_normal_sorted_no_duplicates(self):
            # Reason: List is sorted in ascending order, and no number appears more than twice.
            self.assertTrue(mod.is_sorted([1, 2, 3, 4, 5]))

    def test_normal_unsorted(self):
            # Reason: List is not sorted in ascending order (3 > 2).
            self.assertFalse(mod.is_sorted([1, 3, 2, 4, 5]))

    def test_normal_sorted_with_two_duplicates(self):
            # Reason: List is sorted in ascending order, and numbers 2 and 3 each appear exactly twice, which is allowed.
            self.assertTrue(mod.is_sorted([1, 2, 2, 3, 3, 4]))

    def test_normal_sorted_with_three_duplicates(self):
            # Reason: List is sorted, but the number 2 appears three times, violating the 'no more than 1 duplicate' rule.
            self.assertFalse(mod.is_sorted([1, 2, 2, 2, 3, 4]))
    
        # Edge Cases

    def test_edge_empty_list(self):
            # Reason: An empty list is considered sorted and has no duplicates.
            self.assertTrue(mod.is_sorted([]))

    def test_edge_single_element_list(self):
            # Reason: A list with a single element is considered sorted and has no duplicates.
            self.assertTrue(mod.is_sorted([5]))

    def test_edge_two_elements_one_duplicate(self):
            # Reason: List is sorted, and the number 1 appears twice, which is allowed.
            self.assertTrue(mod.is_sorted([1, 1]))

    def test_edge_three_elements_three_duplicates(self):
            # Reason: List is sorted, but the number 0 appears three times, violating the duplicate rule.
            self.assertFalse(mod.is_sorted([0, 0, 0]))
    
        # Error Conditions

    def test_invariant_list_not_modified(self):
            # Reason: The input list `lst` must not be modified by the function.
            original_list = [1, 2, 2, 3, 4]
            list_copy = list(original_list) # Create a copy to ensure no modification
            mod.is_sorted(original_list) # Call the function
            self.assertEqual(original_list, list_copy, "The input list was modified by the function.")

