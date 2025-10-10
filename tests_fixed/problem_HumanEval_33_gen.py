import unittest
from sut_llm.problem_HumanEval_33 import sort_third

class TestSortThird(unittest.TestCase):

    def test_01_empty_list(self):
        # Edge Case: Empty list
        # Boundary: Smallest possible input
        self.assertEqual(sort_third([]), [])

    def test_02_single_element_list(self):
        # Edge Case: Single element list
        # Boundary: List length 1 (index 0 is divisible by 3)
        self.assertEqual(sort_third([10]), [10])

    def test_03_list_length_three_unsorted(self):
        # Boundary: List length 3 (first full cycle of indices 0, 1, 2)
        # Index 0 is divisible by 3.
        self.assertEqual(sort_third([3, 2, 1]), [3, 2, 1])

    def test_04_list_length_four_unsorted(self):
        # Boundary: List length 4 (one element past a full cycle)
        # Indices 0 and 3 are divisible by 3.
        self.assertEqual(sort_third([4, 3, 2, 1]), [1, 3, 2, 4])

    def test_05_typical_case_multiple_indices_unsorted(self):
        # Typical Input: Multiple elements at %3 indices, requiring sorting.
        # Logic Mutation: Tests if sorting logic is applied correctly.
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

    def test_06_already_sorted_at_divisible_indices(self):
        # Logic Mutation: Tests if the function correctly handles already sorted sub-lists.
        # Return Value: Verifies no unnecessary changes.
        self.assertEqual(sort_third([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_07_all_elements_same(self):
        # Edge Case: List with all identical elements.
        # Logic Mutation: Ensures stability and correct handling of duplicates.
        self.assertEqual(sort_third([7, 7, 7, 7, 7, 7, 7]), [7, 7, 7, 7, 7, 7, 7])

    def test_08_negative_numbers_and_zero(self):
        # Extreme/Unusual Input: Tests with negative numbers and zero.
        # Sign and Zero Testing: Verifies correct sorting behavior with different signs.
        self.assertEqual(sort_third([-3, 0, -1, 5, -2, 10, -4]), [-4, 0, -1, -3, -2, 10, 5])

    def test_09_large_and_small_numbers_mixed(self):
        # Extreme/Unusual Input: Tests with a mix of very large and small numbers.
        # Return Value: Verifies exact output for diverse numeric range.
        self.assertEqual(sort_third([1000, 1, 2, 50, 3, 4, 200]), [50, 1, 2, 200, 3, 4, 1000])

    def test_10_list_not_multiple_of_three_length(self):
        # Typical Input: List length not a multiple of three, with unsorted elements.
        # Off-by-One: Ensures correct handling of list end when not aligned with %3 indices.
        self.assertEqual(sort_third([10, 1, 2, 7, 4, 5, 8, 7, 9, 11]), [7, 1, 2, 8, 4, 5, 10, 7, 9, 11])