import unittest
from sut.problem_HumanEval_30 import get_positive

class Test_get_positive(unittest.TestCase):

    def test_mixed_integers_normal_case(self):
        """
        Normal case: Mixed list of positive and negative integers.
        Input: l = [-1, 2, -4, 5, 6]
        Expected: [2, 5, 6]
        """
        l = [-1, 2, -4, 5, 6]
        expected_output = [2, 5, 6]
        self.assertEqual(get_positive(l), expected_output)

    def test_mixed_integers_with_zero_normal_case(self):
        """
        Normal case: Mixed list including positive, negative, and zero integers.
        Input: l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
        Expected: [5, 3, 2, 3, 9, 123, 1]
        """
        l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
        expected_output = [5, 3, 2, 3, 9, 123, 1]
        self.assertEqual(get_positive(l), expected_output)

    def test_empty_list_edge_case(self):
        """
        Edge case: An empty input list.
        Input: l = []
        Expected: []
        """
        l = []
        expected_output = []
        self.assertEqual(get_positive(l), expected_output)

    def test_only_positive_numbers_edge_case(self):
        """
        Edge case: A list containing only positive numbers.
        Input: l = [1, 2, 3, 4]
        Expected: [1, 2, 3, 4]
        """
        l = [1, 2, 3, 4]
        expected_output = [1, 2, 3, 4]
        self.assertEqual(get_positive(l), expected_output)

    def test_only_negative_numbers_edge_case(self):
        """
        Edge case: A list containing only negative numbers.
        Input: l = [-1, -2, -3, -4]
        Expected: []
        """
        l = [-1, -2, -3, -4]
        expected_output = []
        self.assertEqual(get_positive(l), expected_output)

    def test_only_zeros_edge_case(self):
        """
        Edge case: A list containing only zeros.
        Input: l = [0, 0, 0]
        Expected: []
        """
        l = [0, 0, 0]
        expected_output = []
        self.assertEqual(get_positive(l), expected_output)

    def test_mixed_zero_positive_negative_edge_case(self):
        """
        Edge case: A list with a mix of positive, negative, and zero numbers.
        Input: l = [0, 1, -1, 0, 2, -2]
        Expected: [1, 2]
        """
        l = [0, 1, -1, 0, 2, -2]
        expected_output = [1, 2]
        self.assertEqual(get_positive(l), expected_output)

    def test_floating_point_numbers_edge_case(self):
        """
        Edge case: A list containing floating-point numbers.
        Input: l = [1.5, -2.0, 3.14, 0.0, 0.5]
        Expected: [1.5, 3.14, 0.5]
        """
        l = [1.5, -2.0, 3.14, 0.0, 0.5]
        expected_output = [1.5, 3.14, 0.5]
        self.assertEqual(get_positive(l), expected_output)

    def test_input_none_error(self):
        """
        Error case: Input is None.
        Expected behavior: Raise TypeError or AttributeError.
        """
        with self.assertRaises(TypeError):
            get_positive(None)

    def test_input_string_error(self):
        """
        Error case: Input is a string, not a list.
        Expected behavior: Raise TypeError.
        """
        with self.assertRaises(TypeError):
            get_positive('not_a_list')

    def test_list_with_non_numeric_elements_error(self):
        """
        Error case: Input list contains non-numeric elements.
        Expected behavior: Raise TypeError when comparison with 0 is attempted.
        """
        with self.assertRaises(TypeError):
            get_positive([1, 'a', 2])

    def test_input_list_not_modified_invariant(self):
        """
        Invariant check: The input list `l` must not be modified by the function.
        """
        original_list = [-1, 2, -4, 5, 6]
        # Create a copy to ensure we can compare the original state
        list_before_call = list(original_list)
        get_positive(original_list)
        self.assertEqual(original_list, list_before_call, "The input list was modified by the function.")