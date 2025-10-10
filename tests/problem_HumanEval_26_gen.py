import unittest
from sut.problem_HumanEval_26 import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_1_basic_example(self):
        # Test from docstring, typical input with mixed unique and duplicate elements.
        # Verifies order preservation and correct removal.
        self.assertListEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_2_all_unique_elements(self):
        # Boundary test: all elements occur exactly once.
        # Should return the list unchanged. Catches mutations like removing all elements.
        self.assertListEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_3_all_duplicate_elements(self):
        # Boundary test: all elements occur more than once.
        # Should return an empty list. Catches mutations like keeping all elements.
        self.assertListEqual(remove_duplicates([1, 1, 2, 2, 3, 3]), [])

    def test_4_empty_list_edge_case(self):
        # Edge case: empty input list.
        # Should return an empty list.
        self.assertListEqual(remove_duplicates([]), [])

    def test_5_single_element_list_edge_case(self):
        # Edge case: list with a single element.
        # Should return the list unchanged as the element occurs only once.
        self.assertListEqual(remove_duplicates([7]), [7])

    def test_6_duplicates_with_zero_and_negative_numbers(self):
        # Sign and zero testing: includes zero and negative numbers with duplicates.
        # Verifies correct handling of different number types and order.
        self.assertListEqual(remove_duplicates([0, -1, 0, 5, -1, 10]), [5, 10])

    def test_7_all_same_value_multiple_occurrences(self):
        # Edge case: all elements are the same and occur multiple times.
        # Should result in an empty list. Catches off-by-one errors in counting.
        self.assertListEqual(remove_duplicates([5, 5, 5, 5]), [])

    def test_8_duplicates_at_boundaries_and_middle(self):
        # Boundary test: duplicates appear at the beginning, end, and middle of the list.
        # Verifies robust handling of element positions.
        self.assertListEqual(remove_duplicates([1, 2, 3, 4, 1, 5, 4]), [2, 3, 5])

    def test_9_large_numbers_and_mixed_duplicates(self):
        # Extreme input: large numbers with mixed unique and duplicate values.
        # Ensures the logic works for values beyond small integers.
        self.assertListEqual(remove_duplicates([1000, 2000, 1000, 3000, 2000, 4000, 5000, 5000]), [3000, 4000])

    def test_10_two_elements_one_unique_one_duplicate(self):
        # Off-by-one error test: a small list where one element is unique and another is duplicated.
        # Catches issues with list length processing or incorrect count comparisons (e.g., `count == 1` vs `count > 1`).
        self.assertListEqual(remove_duplicates([1, 2, 1]), [2])