import unittest
import sut.problem_HumanEval_33 as mod

class TestHybrid(unittest.TestCase):
    def test_01_empty_list(self):
            # Edge Case: Empty list
            # Boundary: Smallest possible input
            self.assertEqual(mod.sort_third([]), [])

    def test_02_single_element_list(self):
            # Edge Case: Single element list
            # Boundary: List length 1 (index 0 is divisible by 3)
            self.assertEqual(mod.sort_third([10]), [10])

    def test_03_list_length_three_unsorted(self):
            # Boundary: List length 3 (first full cycle of indices 0, 1, 2)
            # Index 0 is divisible by 3.
            self.assertEqual(mod.sort_third([3, 2, 1]), [3, 2, 1])

    def test_04_list_length_four_unsorted(self):
            # Boundary: List length 4 (one element past a full cycle)
            # Indices 0 and 3 are divisible by 3.
            self.assertEqual(mod.sort_third([4, 3, 2, 1]), [1, 3, 2, 4])

    def test_05_typical_case_multiple_indices_unsorted(self):
            # Typical Input: Multiple elements at %3 indices, requiring sorting.
            # Logic Mutation: Tests if sorting logic is applied correctly.
            self.assertEqual(mod.sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

    def test_06_already_sorted_at_divisible_indices(self):
            # Logic Mutation: Tests if the function correctly handles already sorted sub-lists.
            # Return Value: Verifies no unnecessary changes.
            self.assertEqual(mod.sort_third([1, 2, 3, 4, 5, 6, 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_07_all_elements_same(self):
            # Edge Case: List with all identical elements.
            # Logic Mutation: Ensures stability and correct handling of duplicates.
            self.assertEqual(mod.sort_third([7, 7, 7, 7, 7, 7, 7]), [7, 7, 7, 7, 7, 7, 7])

    def test_08_negative_numbers_and_zero(self):
            # Extreme/Unusual Input: Tests with negative numbers and zero.
            # Sign and Zero Testing: Verifies correct sorting behavior with different signs.
            self.assertEqual(mod.sort_third([-3, 0, -1, 5, -2, 10, -4]), [-4, 0, -1, -3, -2, 10, 5])

    def test_09_large_and_small_numbers_mixed(self):
            # Extreme/Unusual Input: Tests with a mix of very large and small numbers.
            # Return Value: Verifies exact output for diverse numeric range.
            self.assertEqual(mod.sort_third([1000, 1, 2, 50, 3, 4, 200]), [50, 1, 2, 200, 3, 4, 1000])

    def test_10_list_not_multiple_of_three_length(self):
            # Typical Input: List length not a multiple of three, with unsorted elements.
            # Off-by-One: Ensures correct handling of list end when not aligned with %3 indices.
            self.assertEqual(mod.sort_third([10, 1, 2, 7, 4, 5, 8, 7, 9, 11]), [7, 1, 2, 8, 4, 5, 10, 7, 9, 11])

    def test_normal_case_basic_sort(self):
            # General case with multiple elements at indices divisible by three that need sorting.
            l = [5, 6, 3, 4, 8, 9, 2]
            expected = [2, 6, 3, 4, 8, 9, 5]
            self.assertEqual(mod.sort_third(l), expected)

    def test_normal_case_longer_list(self):
            # Longer list with several elements at indices divisible by three, demonstrating sorting.
            l = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
            expected = [0, 8, 7, 3, 5, 4, 6, 2, 1, 9]
            self.assertEqual(mod.sort_third(l), expected)

    def test_normal_case_already_sorted(self):
            # List where elements at divisible-by-three indices are already sorted.
            l = [10, 20, 30, 40, 50, 60]
            expected = [10, 20, 30, 40, 50, 60]
            self.assertEqual(mod.sort_third(l), expected)

    def test_edge_case_empty_list(self):
            # Empty list.
            l = []
            expected = []
            self.assertEqual(mod.sort_third(l), expected)

    def test_edge_case_single_element(self):
            # List with a single element (at index 0, which is divisible by three).
            l = [10]
            expected = [10]
            self.assertEqual(mod.sort_third(l), expected)

    def test_edge_case_reverse_sorted(self):
            # Elements at divisible-by-three indices are reverse sorted.
            l = [9, 2, 1, 3, 5, 4]
            expected = [3, 2, 1, 9, 5, 4]
            self.assertEqual(mod.sort_third(l), expected)

    def test_edge_case_duplicates(self):
            # List with duplicate elements at indices divisible by three.
            l = [1, 2, 3, 1, 5, 6, 1]
            expected = [1, 2, 3, 1, 5, 6, 1]
            self.assertEqual(mod.sort_third(l), expected)

    def test_edge_case_negative_numbers(self):
            # List containing negative numbers.
            l = [-1, 0, -3, -2, -5, -6]
            expected = [-2, 0, -3, -1, -5, -6]
            self.assertEqual(mod.sort_third(l), expected)

    def test_error_case_none_input(self):
            # Input is not a list (None).
            with self.assertRaises(TypeError):
                mod.sort_third(None)

    def test_error_case_non_list_int(self):
            # Input is an integer, not a list.
            with self.assertRaises(TypeError):
                mod.sort_third(123)

    def test_error_case_uncomparable_types_at_divisible_indices_2(self):
            # List contains uncomparable types at indices divisible by three (e.g., int and str), leading to a sorting error.
            with self.assertRaises(TypeError):
                mod.sort_third([1, 2, 3, 'b', 5, 6])

