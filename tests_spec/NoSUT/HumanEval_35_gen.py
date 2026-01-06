import unittest
from sut.problem_HumanEval_35 import max_element

class Test_max_element(unittest.TestCase):

    # Normal Cases
    def test_positive_ascending_integers(self):
        # Description: List with positive integers in ascending order.
        l = [1, 2, 3]
        self.assertEqual(max_element(l), 3)

    def test_mixed_integers(self):
        # Description: List with mixed positive, negative, and zero integers.
        l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
        self.assertEqual(max_element(l), 123)

    def test_negative_integers(self):
        # Description: List with only negative integers.
        l = [-10, -5, -1, -20]
        self.assertEqual(max_element(l), -1)

    def test_duplicate_maximums(self):
        # Description: List with duplicate maximums and other elements.
        l = [7, 7, 7, 1, 7]
        self.assertEqual(max_element(l), 7)

    # Edge Cases
    def test_single_element_list(self):
        # Description: List with a single element.
        l = [42]
        self.assertEqual(max_element(l), 42)

    def test_all_identical_elements(self):
        # Description: List where all elements are identical.
        l = [5, 5, 5, 5]
        self.assertEqual(max_element(l), 5)

    def test_all_zero_elements(self):
        # Description: List with only zero elements.
        l = [0, 0, 0]
        self.assertEqual(max_element(l), 0)

    # Error Conditions
    def test_empty_list_raises_value_error(self):
        # Description: Input list is empty. A maximum cannot be determined.
        l = []
        with self.assertRaises(ValueError):
            max_element(l)

    def test_none_input_raises_type_error(self):
        # Description: Input is not a list (e.g., None).
        l = None
        with self.assertRaises(TypeError):
            max_element(l)

    def test_string_input_raises_type_error(self):
        # Description: Input is a string, not a list.
        l = "not_a_list"
        with self.assertRaises(TypeError):
            max_element(l)

    def test_mixed_types_raises_type_error(self):
        # Description: Input list contains non-comparable elements (e.g., int and str).
        l = [1, "a", 3]
        with self.assertRaises(TypeError):
            max_element(l)