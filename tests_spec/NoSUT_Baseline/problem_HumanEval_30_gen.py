import unittest
import sut.problem_HumanEval_30 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_1(self):
            # Verifies the first example from the docstring.
            self.assertListEqual(mod.get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_docstring_example_2(self):
            # Verifies the second example from the docstring.
            self.assertListEqual(mod.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_empty_input_list(self):
            # Edge case: an empty list should return an empty list.
            self.assertListEqual(mod.get_positive([]), [])

    def test_list_with_only_zeros(self):
            # Boundary case: a list containing only zeros.
            # Catches mutations like `x >= 0`.
            self.assertListEqual(mod.get_positive([0, 0, 0, 0]), [])

    def test_list_with_only_negative_numbers(self):
            # Edge case: a list containing only negative numbers.
            # Catches mutations like `x <= 0` or `x < 0`.
            self.assertListEqual(mod.get_positive([-10, -5, -1, -100]), [])

    def test_list_with_only_positive_numbers(self):
            # Edge case: a list containing only positive numbers.
            # Catches mutations like `x <= 0` or `x < 0`.
            self.assertListEqual(mod.get_positive([1, 5, 10, 100]), [1, 5, 10, 100])

    def test_boundary_values_around_zero(self):
            # Boundary testing: includes numbers exactly at, one below, and one above zero.
            # Crucial for `x > 0` vs `x >= 0` or `x != 0` mutations.
            self.assertListEqual(mod.get_positive([-2, -1, 0, 1, 2]), [1, 2])

    def test_large_and_small_integers(self):
            # Extreme/unusual inputs: very large and very small integers, mixed with boundary values.
            self.assertListEqual(mod.get_positive([10**9, -10**9, 0, 1, -1, 5]), [10**9, 1, 5])

    def test_float_numbers_and_zero_point_five(self):
            # Extreme/unusual inputs: includes float numbers, including those close to zero.
            # Tests boundary conditions for floats (e.g., 0.0, 0.5, -0.5).
            self.assertListEqual(mod.get_positive([0.5, -0.5, 0.0, 1.0, -1.0, 2.5, -0.001, 0.001]), [0.5, 1.0, 2.5, 0.001])

    def test_duplicates_and_order_preservation(self):
            # Logic mutation test: ensures duplicates are preserved and original order is maintained for positive numbers.
            self.assertListEqual(mod.get_positive([1, -1, 2, 0, 1, 3, -3, 2]), [1, 2, 1, 3, 2])

    def test_mixed_integers_normal_case(self):
            """
            Normal case: Mixed list of positive and negative integers.
            Input: l = [-1, 2, -4, 5, 6]
            Expected: [2, 5, 6]
            """
            l = [-1, 2, -4, 5, 6]
            expected_output = [2, 5, 6]
            self.assertEqual(mod.get_positive(l), expected_output)

    def test_mixed_integers_with_zero_normal_case(self):
            """
            Normal case: Mixed list including positive, negative, and zero integers.
            Input: l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
            Expected: [5, 3, 2, 3, 9, 123, 1]
            """
            l = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
            expected_output = [5, 3, 2, 3, 9, 123, 1]
            self.assertEqual(mod.get_positive(l), expected_output)

    def test_empty_list_edge_case(self):
            """
            Edge case: An empty input list.
            Input: l = []
            Expected: []
            """
            l = []
            expected_output = []
            self.assertEqual(mod.get_positive(l), expected_output)

    def test_only_positive_numbers_edge_case(self):
            """
            Edge case: A list containing only positive numbers.
            Input: l = [1, 2, 3, 4]
            Expected: [1, 2, 3, 4]
            """
            l = [1, 2, 3, 4]
            expected_output = [1, 2, 3, 4]
            self.assertEqual(mod.get_positive(l), expected_output)

    def test_only_negative_numbers_edge_case(self):
            """
            Edge case: A list containing only negative numbers.
            Input: l = [-1, -2, -3, -4]
            Expected: []
            """
            l = [-1, -2, -3, -4]
            expected_output = []
            self.assertEqual(mod.get_positive(l), expected_output)

    def test_only_zeros_edge_case(self):
            """
            Edge case: A list containing only zeros.
            Input: l = [0, 0, 0]
            Expected: []
            """
            l = [0, 0, 0]
            expected_output = []
            self.assertEqual(mod.get_positive(l), expected_output)

    def test_mixed_zero_positive_negative_edge_case(self):
            """
            Edge case: A list with a mix of positive, negative, and zero numbers.
            Input: l = [0, 1, -1, 0, 2, -2]
            Expected: [1, 2]
            """
            l = [0, 1, -1, 0, 2, -2]
            expected_output = [1, 2]
            self.assertEqual(mod.get_positive(l), expected_output)

    def test_floating_point_numbers_edge_case(self):
            """
            Edge case: A list containing floating-point numbers.
            Input: l = [1.5, -2.0, 3.14, 0.0, 0.5]
            Expected: [1.5, 3.14, 0.5]
            """
            l = [1.5, -2.0, 3.14, 0.0, 0.5]
            expected_output = [1.5, 3.14, 0.5]
            self.assertEqual(mod.get_positive(l), expected_output)

    def test_input_none_error(self):
            """
            Error case: Input is None.
            Expected behavior: Raise TypeError or AttributeError.
            """
            with self.assertRaises(TypeError):
                mod.get_positive(None)

    def test_input_string_error(self):
            """
            Error case: Input is a string, not a list.
            Expected behavior: Raise TypeError.
            """
            with self.assertRaises(TypeError):
                mod.get_positive('not_a_list')

    def test_list_with_non_numeric_elements_error(self):
            """
            Error case: Input list contains non-numeric elements.
            Expected behavior: Raise TypeError when comparison with 0 is attempted.
            """
            with self.assertRaises(TypeError):
                mod.get_positive([1, 'a', 2])

    def test_input_list_not_modified_invariant(self):
            """
            Invariant check: The input list `l` must not be modified by the function.
            """
            original_list = [-1, 2, -4, 5, 6]
            # Create a copy to ensure we can compare the original state
            list_before_call = list(original_list)
            mod.get_positive(original_list)
            self.assertEqual(original_list, list_before_call, "The input list was modified by the function.")

