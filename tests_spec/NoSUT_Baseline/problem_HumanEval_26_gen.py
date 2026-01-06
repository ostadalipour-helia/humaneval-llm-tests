import unittest
import sut.problem_HumanEval_26 as mod

class TestHybrid(unittest.TestCase):
    def test_1_basic_example(self):
            # Test from docstring, typical input with mixed unique and duplicate elements.
            # Verifies order preservation and correct removal.
            self.assertListEqual(mod.remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_2_all_unique_elements(self):
            # Boundary test: all elements occur exactly once.
            # Should return the list unchanged. Catches mutations like removing all elements.
            self.assertListEqual(mod.remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_3_all_duplicate_elements(self):
            # Boundary test: all elements occur more than once.
            # Should return an empty list. Catches mutations like keeping all elements.
            self.assertListEqual(mod.remove_duplicates([1, 1, 2, 2, 3, 3]), [])

    def test_4_empty_list_edge_case(self):
            # Edge case: empty input list.
            # Should return an empty list.
            self.assertListEqual(mod.remove_duplicates([]), [])

    def test_5_single_element_list_edge_case(self):
            # Edge case: list with a single element.
            # Should return the list unchanged as the element occurs only once.
            self.assertListEqual(mod.remove_duplicates([7]), [7])

    def test_6_duplicates_with_zero_and_negative_numbers(self):
            # Sign and zero testing: includes zero and negative numbers with duplicates.
            # Verifies correct handling of different number types and order.
            self.assertListEqual(mod.remove_duplicates([0, -1, 0, 5, -1, 10]), [5, 10])

    def test_7_all_same_value_multiple_occurrences(self):
            # Edge case: all elements are the same and occur multiple times.
            # Should result in an empty list. Catches off-by-one errors in counting.
            self.assertListEqual(mod.remove_duplicates([5, 5, 5, 5]), [])

    def test_8_duplicates_at_boundaries_and_middle(self):
            # Boundary test: duplicates appear at the beginning, end, and middle of the list.
            # Verifies robust handling of element positions.
            self.assertListEqual(mod.remove_duplicates([1, 2, 3, 4, 1, 5, 4]), [2, 3, 5])

    def test_9_large_numbers_and_mixed_duplicates(self):
            # Extreme input: large numbers with mixed unique and duplicate values.
            # Ensures the logic works for values beyond small integers.
            self.assertListEqual(mod.remove_duplicates([1000, 2000, 1000, 3000, 2000, 4000, 5000, 5000]), [3000, 4000])

    def test_10_two_elements_one_unique_one_duplicate(self):
            # Off-by-one error test: a small list where one element is unique and another is duplicated.
            # Catches issues with list length processing or incorrect count comparisons (e.g., `count == 1` vs `count > 1`).
            self.assertListEqual(mod.remove_duplicates([1, 2, 1]), [2])

    def test_normal_mixed_unique_and_duplicate(self):
            # Example from docstring: mixed unique and duplicate elements.
            numbers = [1, 2, 3, 2, 4]
            expected_output = [1, 3, 4]
            self.assertEqual(mod.remove_duplicates(numbers), expected_output)

    def test_normal_all_unique(self):
            # All elements are unique, so all should be kept.
            numbers = [5, 6, 7, 8]
            expected_output = [5, 6, 7, 8]
            self.assertEqual(mod.remove_duplicates(numbers), expected_output)

    def test_normal_multiple_duplicates(self):
            # Multiple elements appear more than once, some appear once.
            numbers = [10, 20, 10, 30, 20, 40]
            expected_output = [30, 40]
            self.assertEqual(mod.remove_duplicates(numbers), expected_output)

    def test_edge_empty_list(self):
            # Empty input list.
            numbers = []
            expected_output = []
            self.assertEqual(mod.remove_duplicates(numbers), expected_output)

    def test_edge_all_duplicates(self):
            # All elements are duplicates, so the output should be an empty list.
            numbers = [1, 1, 1, 1]
            expected_output = []
            self.assertEqual(mod.remove_duplicates(numbers), expected_output)

    def test_edge_single_unique_element(self):
            # List with a single unique element.
            numbers = [7]
            expected_output = [7]
            self.assertEqual(mod.remove_duplicates(numbers), expected_output)

    def test_edge_negative_numbers_and_zero(self):
            # List containing negative numbers and zero.
            numbers = [-1, 0, -1, 2]
            expected_output = [0, 2]
            self.assertEqual(mod.remove_duplicates(numbers), expected_output)

