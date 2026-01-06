import unittest
import sut.problem_HumanEval_70 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_list(self):
            """
            Test case for an empty input list.
            This covers an edge case and a specific return path.
            """
            self.assertListEqual(mod.strange_sort_list([]), [])

    def test_single_element_list(self):
            """
            Test case for a list with a single element.
            This covers an edge case and a boundary condition.
            """
            self.assertListEqual(mod.strange_sort_list([7]), [7])

    def test_two_elements_sorted(self):
            """
            Test case for a two-element list that is already sorted.
            This covers a boundary condition and off-by-one logic for small lists.
            """
            self.assertListEqual(mod.strange_sort_list([1, 2]), [1, 2])

    def test_two_elements_unsorted(self):
            """
            Test case for a two-element list that is unsorted.
            This covers a boundary condition and ensures min/max logic works correctly.
            """
            self.assertListEqual(mod.strange_sort_list([2, 1]), [1, 2])

    def test_four_elements_example(self):
            """
            Test case using the example from the docstring with an even number of elements.
            This covers a typical input and verifies the core strange sorting logic.
            """
            self.assertListEqual(mod.strange_sort_list([1, 2, 3, 4]), [1, 4, 2, 3])

    def test_five_elements_odd_length(self):
            """
            Test case for a list with an odd number of elements.
            This covers off-by-one errors related to loop termination and handling the middle element.
            """
            self.assertListEqual(mod.strange_sort_list([1, 2, 3, 4, 5]), [1, 5, 2, 4, 3])

    def test_all_same_elements(self):
            """
            Test case for a list where all elements are identical.
            This covers an edge case and tests logic mutations related to min/max on duplicates.
            """
            self.assertListEqual(mod.strange_sort_list([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_negative_numbers(self):
            """
            Test case with only negative numbers.
            This covers sign testing and ensures min/max logic works correctly with negative values.
            """
            self.assertListEqual(mod.strange_sort_list([-3, -1, -2]), [-3, -1, -2])

    def test_mixed_signs_and_zero(self):
            """
            Test case with a mix of positive, negative, and zero values.
            This covers extreme inputs and comprehensive sign testing.
            """
            self.assertListEqual(mod.strange_sort_list([-5, 0, 5, -10, 10]), [-10, 10, -5, 5, 0])

    def test_duplicates_and_unsorted_longer_list(self):
            """
            Test case with duplicates, unsorted elements, and a longer list.
            This covers extreme inputs, logic mutations (e.g., `remove` behavior), and off-by-one errors.
            """
            self.assertListEqual(mod.strange_sort_list([3, 1, 4, 1, 5, 9, 2, 6]), [1, 9, 1, 6, 2, 5, 3, 4])
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_sorted_list(self):
            # Description: Alternating min/max for a sorted list.
            lst = [1, 2, 3, 4]
            expected_output = [1, 4, 2, 3]
            self.assertEqual(mod.strange_sort_list(lst), expected_output)

    def test_normal_identical_elements(self):
            # Description: List with all identical elements.
            lst = [5, 5, 5, 5]
            expected_output = [5, 5, 5, 5]
            self.assertEqual(mod.strange_sort_list(lst), expected_output)

    def test_normal_unsorted_odd_length(self):
            # Description: Unsorted list with odd number of elements.
            lst = [10, 1, 8, 3, 6]
            expected_output = [1, 10, 3, 8, 6]
            self.assertEqual(mod.strange_sort_list(lst), expected_output)

    def test_normal_mixed_signs(self):
            # Description: List with negative, zero, and positive integers.
            lst = [-5, 0, 5, -10]
            expected_output = [-10, 5, -5, 0]
            self.assertEqual(mod.strange_sort_list(lst), expected_output)

    def test_edge_empty_list(self):
            # Description: Empty list.
            lst = []
            expected_output = []
            self.assertEqual(mod.strange_sort_list(lst), expected_output)

    def test_edge_single_element(self):
            # Description: Single element list.
            lst = [7]
            expected_output = [7]
            self.assertEqual(mod.strange_sort_list(lst), expected_output)

    def test_edge_two_elements_sorted(self):
            # Description: Two element list.
            lst = [10, 20]
            expected_output = [10, 20]
            self.assertEqual(mod.strange_sort_list(lst), expected_output)

    def test_edge_two_elements_reverse_sorted(self):
            # Description: Two element list, reverse sorted.
            lst = [20, 10]
            expected_output = [10, 20]
            self.assertEqual(mod.strange_sort_list(lst), expected_output)

    def test_error_list_with_string(self):
            # Description: List contains non-integer elements (string).
            lst = [1, 2, "three", 4]
            with self.assertRaises(TypeError): # Expecting TypeError due to comparison of int and str
                mod.strange_sort_list(lst)

