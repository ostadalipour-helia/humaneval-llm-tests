import unittest
import sut.problem_HumanEval_40 as mod

class TestHybrid(unittest.TestCase):
    def test_01_empty_list(self):
            # Edge case: Empty list, cannot form any triple.
            self.assertEqual(mod.triples_sum_to_zero([]), False)

    def test_02_single_element_list(self):
            # Edge case: List with only one element, cannot form any triple.
            self.assertEqual(mod.triples_sum_to_zero([1]), False)

    def test_03_two_element_list(self):
            # Edge case: List with two elements, cannot form any triple.
            self.assertEqual(mod.triples_sum_to_zero([1, -1]), False)

    def test_04_basic_true_case(self):
            # Typical input: Smallest list with a triple summing to zero.
            # Covers: Positive, negative, and zero elements.
            self.assertEqual(mod.triples_sum_to_zero([1, -1, 0]), True)

    def test_05_basic_false_case(self):
            # Typical input: Smallest list where no triple sums to zero.
            # Covers: All positive numbers.
            self.assertEqual(mod.triples_sum_to_zero([1, 2, 3]), False)

    def test_07_distinctness_with_duplicates_with_solution(self):
            # Logic mutation: Test distinctness requirement with duplicates, but a valid distinct triple exists.
            # (1, 2, -3) sums to zero, despite duplicate '1'.
            self.assertEqual(mod.triples_sum_to_zero([1, 2, -3, 1, 5]), True)

    def test_08_boundary_mixed_values_with_solution(self):
            # Boundary testing: List with mixed positive and negative numbers, where a solution exists.
            # (2, 3, -5) sums to zero.
            self.assertEqual(mod.triples_sum_to_zero([1, 2, 3, -4, -5]), True)

    def test_09_extreme_large_numbers_no_solution(self):
            # Extreme input: Large numbers, no triple sums to zero.
            self.assertEqual(mod.triples_sum_to_zero([1000, 2000, 3000, -1, -2]), False)

    def test_10_extreme_large_numbers_with_solution(self):
            # Extreme input: Large numbers, where a triple sums to zero.
            # (1000, 2000, -3000) sums to zero.
            self.assertEqual(mod.triples_sum_to_zero([1000, 2000, -3000, 5, 6]), True)

    def test_error_input_is_none(self):
            # Description: Input is not a list.
            with self.assertRaises(TypeError):
                mod.triples_sum_to_zero(None)

    def test_error_input_is_integer(self):
            # Description: Input is an integer, not a list.
            with self.assertRaises(TypeError):
                mod.triples_sum_to_zero(123)

    def test_error_list_contains_string(self):
            # Description: List contains non-integer elements (string).
            with self.assertRaises(TypeError):
                mod.triples_sum_to_zero([1, 2, "a"])

