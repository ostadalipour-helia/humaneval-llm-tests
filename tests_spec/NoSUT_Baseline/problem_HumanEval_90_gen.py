import unittest
import sut.problem_HumanEval_90 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_basic_sorted(self):
            # Test a typical case with a sorted list
            self.assertEqual(mod.next_smallest([1, 2, 3, 4, 5]), 2)

    def test_docstring_example_basic_unsorted(self):
            # Test a typical case with an unsorted list
            self.assertEqual(mod.next_smallest([5, 1, 4, 3, 2]), 2)

    def test_edge_empty_list(self):
            # Boundary test: empty list
            self.assertIsNone(mod.next_smallest([]))

    def test_edge_single_element_list(self):
            # Boundary test: list with a single element
            self.assertIsNone(mod.next_smallest([7]))

    def test_edge_all_same_elements(self):
            # Boundary test: list where all elements are identical
            self.assertIsNone(mod.next_smallest([5, 5, 5, 5]))

    def test_boundary_two_distinct_elements(self):
            # Boundary test: the smallest possible list that should return a value
            self.assertEqual(mod.next_smallest([10, 20]), 20)

    def test_negative_numbers(self):
            # Test with negative numbers, including unsorted order
            self.assertEqual(mod.next_smallest([-5, -1, -4, -3, -2]), -4)

    def test_mixed_numbers_with_zero(self):
            # Test with a mix of positive, negative, and zero values
            self.assertEqual(mod.next_smallest([-10, 0, 5, -2, 1]), -2)

    def test_duplicates_but_still_has_second_smallest(self):
            # Test with duplicates where the second smallest distinct element exists
            # This catches mutations that don't correctly handle distinctness.
            self.assertEqual(mod.next_smallest([1, 1, 2, 3, 4]), 2)

    def test_large_numbers_and_unsorted(self):
            # Test with larger numbers and an unsorted list to ensure robustness
            self.assertEqual(mod.next_smallest([1000, 50, 200, 10, 500]), 50)

    def test_normal_ascending_distinct(self):
            # A list with distinct elements in ascending order.
            lst = [1, 2, 3, 4, 5]
            expected_output = 2
            self.assertEqual(mod.next_smallest(lst), expected_output)

    def test_normal_mixed_distinct(self):
            # A list with distinct elements in mixed order.
            lst = [5, 1, 4, 3, 2]
            expected_output = 2
            self.assertEqual(mod.next_smallest(lst), expected_output)

    def test_normal_duplicates_present(self):
            # A list with duplicate elements, but a clear second smallest distinct element.
            lst = [100, 10, 20, 30, 100]
            expected_output = 20
            self.assertEqual(mod.next_smallest(lst), expected_output)

    def test_edge_single_element(self):
            # A list with a single element.
            lst = [1]
            expected_output = None
            self.assertEqual(mod.next_smallest(lst), expected_output)

    def test_edge_one_distinct_element_multiple_occurrences(self):
            # A list with multiple identical elements (only one distinct element).
            lst = [1, 1, 1, 1]
            expected_output = None
            self.assertEqual(mod.next_smallest(lst), expected_output)

    def test_edge_exactly_two_distinct_elements(self):
            # A list with exactly two distinct elements.
            lst = [1, 2]
            expected_output = 2
            self.assertEqual(mod.next_smallest(lst), expected_output)

    def test_edge_second_smallest_duplicated(self):
            # A list with two distinct elements, where the second smallest is duplicated.
            lst = [1, 2, 2, 2]
            expected_output = 2
            self.assertEqual(mod.next_smallest(lst), expected_output)

    def test_error_input_not_list_int(self):
            # Input is an integer, not a list.
            with self.assertRaises(TypeError):
                mod.next_smallest(123)

    def test_error_list_contains_string(self):
            # List contains non-integer elements (string).
            with self.assertRaises(TypeError):
                mod.next_smallest([1, 2, 'a', 4])

    def test_invariance_list_not_modified(self):
            # The input list `lst` must not be modified by the function.
            original_lst = [5, 1, 4, 3, 2]
            lst_copy = list(original_lst) # Create a copy to pass to the function
            mod.next_smallest(lst_copy)
            self.assertEqual(original_lst, lst_copy, "The input list should not be modified.")

