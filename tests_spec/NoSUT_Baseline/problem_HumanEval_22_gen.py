import unittest
import sut.problem_HumanEval_22 as mod

class TestHybrid(unittest.TestCase):
    def test_1_basic_mixed_types_docstring_example_1(self):
            # Typical input with mixed types, including float and string
            # Verifies basic filtering functionality
            self.assertListEqual(mod.filter_integers(['a', 3.14, 5]), [5])

    def test_2_basic_mixed_types_docstring_example_2(self):
            # Typical input with various non-integer types
            # Verifies basic filtering functionality
            self.assertListEqual(mod.filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

    def test_3_edge_case_empty_list(self):
            # Edge case: an empty input list
            # Verifies correct handling of empty collections
            self.assertListEqual(mod.filter_integers([]), [])

    def test_4_edge_case_list_with_only_non_integers(self):
            # Edge case: a list containing only non-integer types
            # Verifies that no non-integers are mistakenly included
            self.assertListEqual(mod.filter_integers(['hello', 3.14, None, [], {}]), [])

    def test_5_all_integers_positive_negative_zero(self):
            # Input with only integers, covering positive, negative, and zero values
            # Verifies that all integers are retained and sign/zero handling
            self.assertListEqual(mod.filter_integers([1, -5, 0, 1000]), [1, -5, 0, 1000])

    def test_6_boundary_boolean_values_are_integers(self):
            # Boundary case: Python booleans (True/False) are subclasses of int
            # Verifies correct handling of this specific type hierarchy
            self.assertListEqual(mod.filter_integers([True, False, 1, 'text', 2.0]), [True, False, 1])

    def test_7_boundary_float_values_that_look_like_integers(self):
            # Boundary case: float values with zero decimal part (e.g., 5.0)
            # Verifies that floats are correctly excluded, even if they represent whole numbers
            self.assertListEqual(mod.filter_integers([5.0, 7, 3.14, -2.0, -10]), [7, -10])

    def test_8_off_by_one_single_and_two_elements_mixed(self):
            # Off-by-one/Edge case: list with a single integer and a list with two elements (one int, one non-int)
            # Verifies correct handling of small list sizes and element positions
            self.assertListEqual(mod.filter_integers([42, 'not_int']), [42])
            self.assertListEqual(mod.filter_integers(['not_int', 42]), [42]) # Test first/last position

    def test_9_extreme_values_large_numbers_and_duplicates(self):
            # Extreme input: very large/small integers, duplicates, and mixed with non-integers
            # Verifies handling of large numeric values and duplicate entries
            self.assertListEqual(
                mod.filter_integers([999999999999999999, -1234567890, 'large_str', 0, 999999999999999999]),
                [999999999999999999, -1234567890, 0, 999999999999999999]
            )

    def test_10_logic_mutation_none_and_other_complex_types(self):
            # Logic mutation: tests various non-numeric and complex types including None
            # Ensures that None, lists, dictionaries, etc., are correctly filtered out
            self.assertListEqual(mod.filter_integers([None, 1, 'a', 2.5, 3, [], {'key': 'value'}]), [1, 3])

    def test_normal_mixed_string_float_int(self):
            # Description: Mixed list with strings, floats, and integers.
            values = ['a', 3.14, 5]
            expected_output = [5]
            self.assertEqual(mod.filter_integers(values), expected_output)

    def test_normal_mixed_types(self):
            # Description: Mixed list with integers, strings, dictionaries, and lists.
            values = [1, 2, 3, 'abc', {}, []]
            expected_output = [1, 2, 3]
            self.assertEqual(mod.filter_integers(values), expected_output)

    def test_normal_mixed_string_float_int_2(self):
            # Description: Mixed list with integers, strings, and floats.
            values = [10, 'hello', 20, 30.5, 40]
            expected_output = [10, 20, 40]
            self.assertEqual(mod.filter_integers(values), expected_output)

    def test_edge_empty_list(self):
            # Description: An empty input list.
            values = []
            expected_output = []
            self.assertEqual(mod.filter_integers(values), expected_output)

    def test_edge_no_integers(self):
            # Description: A list containing no integers.
            values = ['a', 3.14, 'b', None]
            expected_output = []
            self.assertEqual(mod.filter_integers(values), expected_output)

    def test_edge_only_integers(self):
            # Description: A list containing only integers.
            values = [1, 2, 3, 4]
            expected_output = [1, 2, 3, 4]
            self.assertEqual(mod.filter_integers(values), expected_output)

    def test_edge_booleans_and_integers(self):
            # Description: A list containing booleans (which are subclasses of int) and an integer.
            values = [True, False, 10]
            expected_output = [True, False, 10] # Booleans are instances of int
            self.assertEqual(mod.filter_integers(values), expected_output)

    def test_edge_zero_negative_integers(self):
            # Description: A list containing zero and negative integers.
            values = [0, -5, 100]
            expected_output = [0, -5, 100]
            self.assertEqual(mod.filter_integers(values), expected_output)

    def test_error_none_input(self):
            # Description: Input 'values' is not a list (e.g., None).
            with self.assertRaises(TypeError):
                mod.filter_integers(None)

    def test_error_int_input(self):
            # Description: Input 'values' is not a list (e.g., an integer).
            with self.assertRaises(TypeError):
                mod.filter_integers(123)

