import unittest
import sut.problem_HumanEval_35 as mod

class TestHybrid(unittest.TestCase):
    def test_basic_positive_list(self):
            """
            Test with a simple list of positive integers, max at the end.
            Covers typical input and verifies exact output.
            """
            self.assertEqual(mod.max_element([1, 2, 3]), 3)

    def test_mixed_numbers_list(self):
            """
            Test with a list containing positive, negative, and zero values,
            including a large positive number. Covers typical/extreme input.
            """
            self.assertEqual(mod.max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

    def test_single_element_list(self):
            """
            Test with a list containing only one element.
            Covers an edge case and potential off-by-one errors in loop initialization.
            """
            self.assertEqual(mod.max_element([7]), 7)

    def test_all_negative_numbers(self):
            """
            Test with a list containing only negative numbers.
            Covers sign testing and ensures correct comparison with negative values.
            """
            self.assertEqual(mod.max_element([-1, -5, -10, -2]), -1)

    def test_max_at_start(self):
            """
            Test with the maximum element located at the beginning of the list.
            Covers a boundary condition and potential off-by-one errors in loop logic.
            """
            self.assertEqual(mod.max_element([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
            """
            Test with the maximum element located at the end of the list.
            Covers a boundary condition and potential off-by-one errors in loop termination.
            """
            self.assertEqual(mod.max_element([1, 2, 3, 10]), 10)

    def test_max_in_middle(self):
            """
            Test with the maximum element located in the middle of the list.
            Covers a typical scenario and ensures correct iteration.
            """
            self.assertEqual(mod.max_element([1, 5, 10, 2, 3]), 10)

    def test_list_with_duplicates_and_max(self):
            """
            Test with a list containing duplicate values, including the maximum element.
            Covers an edge case with duplicates and ensures the correct max is returned.
            """
            self.assertEqual(mod.max_element([1, 5, 2, 5, 10, 10]), 10)

    def test_list_with_zero_and_mixed_signs(self):
            """
            Test with a list containing zero, positive, and negative numbers.
            Covers sign testing and ensures zero is handled correctly in comparisons.
            """
            self.assertEqual(mod.max_element([-5, 0, 5, -1]), 5)

    def test_positive_ascending_integers(self):
            # Description: List with positive integers in ascending order.
            l = [1, 2, 3]
            self.assertEqual(mod.max_element(l), 3)

    def test_mixed_integers(self):
            # Description: List with mixed positive, negative, and zero integers.
            l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
            self.assertEqual(mod.max_element(l), 123)

    def test_negative_integers(self):
            # Description: List with only negative integers.
            l = [-10, -5, -1, -20]
            self.assertEqual(mod.max_element(l), -1)

    def test_duplicate_maximums(self):
            # Description: List with duplicate maximums and other elements.
            l = [7, 7, 7, 1, 7]
            self.assertEqual(mod.max_element(l), 7)
    
        # Edge Cases

    def test_all_identical_elements(self):
            # Description: List where all elements are identical.
            l = [5, 5, 5, 5]
            self.assertEqual(mod.max_element(l), 5)

    def test_all_zero_elements(self):
            # Description: List with only zero elements.
            l = [0, 0, 0]
            self.assertEqual(mod.max_element(l), 0)
    
        # Error Conditions

    def test_none_input_raises_type_error(self):
            # Description: Input is not a list (e.g., None).
            l = None
            with self.assertRaises(TypeError):
                mod.max_element(l)

    def test_mixed_types_raises_type_error(self):
            # Description: Input list contains non-comparable elements (e.g., int and str).
            l = [1, "a", 3]
            with self.assertRaises(TypeError):
                mod.max_element(l)

