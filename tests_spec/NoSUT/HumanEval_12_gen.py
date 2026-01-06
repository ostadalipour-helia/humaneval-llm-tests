import unittest
from sut.problem_HumanEval_12 import longest

class Test_longest(unittest.TestCase):
    def test_normal_clear_longest(self):
        # Returns the clearly longest string.
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_normal_varying_lengths(self):
        # Returns the longest string when lengths vary.
        self.assertEqual(longest(['apple', 'banana', 'cherry']), 'banana')

    def test_normal_first_of_max_length(self):
        # Returns the first string when multiple strings have the same maximum length.
        self.assertEqual(longest(['hello', 'world']), 'hello')

    def test_normal_longest_from_mixed_lengths(self):
        # Returns the longest string from a list with varying lengths.
        self.assertEqual(longest(['short', 'medium', 'longest_string']), 'longest_string')

    def test_edge_empty_list(self):
        # Returns None for an empty input list.
        self.assertIsNone(longest([]))

    def test_edge_all_same_length(self):
        # Returns the first string when all strings have the same length.
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_edge_single_empty_string(self):
        # Returns an empty string if it's the only element.
        self.assertEqual(longest(['']), '')

    def test_edge_empty_string_among_others(self):
        # Handles empty strings correctly when other strings are present.
        self.assertEqual(longest(['', 'a', 'bb']), 'bb')

    def test_edge_single_element_list(self):
        # Returns the single string in a list with one element.
        self.assertEqual(longest(['a']), 'a')

    def test_error_input_none(self):
        # Input is not a list (None).
        with self.assertRaises(TypeError):
            longest(None)

    def test_error_input_not_list_int(self):
        # Input is an integer, not a list.
        with self.assertRaises(TypeError):
            longest(123)

    def test_error_list_contains_ints(self):
        # List contains non-string elements (integers).
        with self.assertRaises(TypeError):
            longest([1, 2, 3])

    def test_error_list_contains_mixed_types(self):
        # List contains mixed types, including non-string elements.
        with self.assertRaises(TypeError):
            longest(['a', 1, 'b'])

    def test_error_list_contains_nested_lists(self):
        # List contains nested lists instead of strings.
        with self.assertRaises(TypeError):
            longest([['a'], ['b']])