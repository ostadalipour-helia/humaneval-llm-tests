import unittest
import sut.problem_HumanEval_43 as mod

class TestHybrid(unittest.TestCase):
    def test_edge_empty_list(self):
            # Test case for an empty list.
            # Should return False as no two distinct elements exist.
            self.assertEqual(mod.pairs_sum_to_zero([]), False)

    def test_edge_single_zero(self):
            # Test case for a list with a single zero.
            # Should return False as distinct elements are required.
            self.assertEqual(mod.pairs_sum_to_zero([0]), False)

    def test_boundary_exact_pair(self):
            # Test case with the smallest possible list containing a pair that sums to zero.
            # Covers boundary condition for list length and exact sum.
            self.assertEqual(mod.pairs_sum_to_zero([5, -5]), True)

    def test_boundary_two_zeros(self):
            # Test case with two zeros, which should sum to zero and are distinct elements.
            # Covers distinctness requirement for zero and boundary for zero values.
            self.assertEqual(mod.pairs_sum_to_zero([0, 0]), True)

    def test_typical_pair_exists_middle(self):
            # Typical case where a pair exists, not at the beginning or end of the list.
            # Tests off-by-one for array indices and general logic.
            self.assertEqual(mod.pairs_sum_to_zero([1, 3, -2, 5, -5, 0]), True)

    def test_typical_no_pair_mixed_values(self):
            # Typical case where no pair sums to zero, with mixed positive, negative, and zero values.
            # Tests the 'False' return path and general logic.
            self.assertEqual(mod.pairs_sum_to_zero([1, 3, -2, 5, 0]), False)

    def test_extreme_large_numbers_pair(self):
            # Test with large positive and negative numbers that sum to zero.
            # Covers sign testing and extreme values.
            self.assertEqual(mod.pairs_sum_to_zero([1000000, -1000000, 5]), True)

    def test_extreme_no_pair_off_by_one(self):
            # Test with large numbers that are very close to summing to zero but don't.
            # Covers boundary conditions for sum and extreme values.
            self.assertEqual(mod.pairs_sum_to_zero([1000000, -999999, 5]), False)

    def test_logic_mutation_duplicate_non_zero_no_pair(self):
            # Test with duplicate non-zero values where no pair sums to zero.
            # Catches potential logic errors with handling duplicates or incorrect sum checks.
            self.assertEqual(mod.pairs_sum_to_zero([7, 7, 7, -6]), False)

    def test_logic_mutation_only_one_half_of_pair(self):
            # Test case where only one element of a potential pair (e.g., 'x' but not '-x') exists.
            # Ensures the function correctly identifies the absence of the complementary element.
            self.assertEqual(mod.pairs_sum_to_zero([1, 2, 3, -10, 5]), False)

    def test_normal_positive_pair(self):
            # Description: List contains a pair (5, -5) that sums to zero.
            l = [2, 4, -5, 3, 5, 7]
            original_l = list(l) # For invariant check
            expected_output = True
            self.assertEqual(mod.pairs_sum_to_zero(l), expected_output)
            self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_normal_no_pair(self):
            # Description: List contains no pair that sums to zero.
            l = [1, 3, 5, 0]
            original_l = list(l) # For invariant check
            expected_output = False
            self.assertEqual(mod.pairs_sum_to_zero(l), expected_output)
            self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_normal_multiple_pairs(self):
            # Description: List with multiple pairs summing to zero.
            l = [1, -1, 2, -2]
            original_l = list(l) # For invariant check
            expected_output = True
            self.assertEqual(mod.pairs_sum_to_zero(l), expected_output)
            self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_single_element(self):
            # Description: List with a single element, no pairs possible.
            l = [1]
            original_l = list(l) # For invariant check
            expected_output = False
            self.assertEqual(mod.pairs_sum_to_zero(l), expected_output)
            self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_two_zeros(self):
            # Description: List with two zeros, which are distinct elements by index and sum to zero.
            l = [0, 0]
            original_l = list(l) # For invariant check
            expected_output = True
            self.assertEqual(mod.pairs_sum_to_zero(l), expected_output)
            self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_two_elements_sum_to_zero(self):
            # Description: List with exactly two elements that sum to zero.
            l = [1, -1]
            original_l = list(l) # For invariant check
            expected_output = True
            self.assertEqual(mod.pairs_sum_to_zero(l), expected_output)
            self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_edge_large_numbers(self):
            # Description: List with large numbers summing to zero.
            l = [-1000000, 1000000]
            original_l = list(l) # For invariant check
            expected_output = True
            self.assertEqual(mod.pairs_sum_to_zero(l), expected_output)
            self.assertEqual(l, original_l, "Input list should not be modified.")

    def test_error_list_with_string(self):
            # Description: List contains non-integer elements (string).
            l = [1, 2, "three"]
            with self.assertRaises(TypeError):
                mod.pairs_sum_to_zero(l)

