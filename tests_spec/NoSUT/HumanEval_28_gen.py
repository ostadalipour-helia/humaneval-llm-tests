import unittest
from sut.problem_HumanEval_28 import concatenate

class Test_concatenate(unittest.TestCase):
    def test_normal_multiple_non_empty_strings(self):
        # Concatenating a list of multiple non-empty strings.
        strings = ["a", "b", "c"]
        expected_output = "abc"
        self.assertEqual(concatenate(strings), expected_output)

    def test_normal_strings_with_spaces_punctuation(self):
        # Concatenating strings including spaces and punctuation.
        strings = ["hello", " ", "world", "!"]
        expected_output = "hello world!"
        self.assertEqual(concatenate(strings), expected_output)

    def test_edge_empty_list(self):
        # Concatenating an empty list of strings.
        strings = []
        expected_output = ""
        self.assertEqual(concatenate(strings), expected_output)

    def test_edge_single_string(self):
        # Concatenating a list containing only one string.
        strings = ["single_string"]
        expected_output = "single_string"
        self.assertEqual(concatenate(strings), expected_output)

    def test_edge_list_with_empty_strings(self):
        # Concatenating a list that includes empty strings.
        strings = ["", "test", ""]
        expected_output = "test"
        self.assertEqual(concatenate(strings), expected_output)

    def test_error_input_none(self):
        # Input `strings` is not a list (e.g., None).
        with self.assertRaises(TypeError):
            concatenate(None)

    def test_error_input_not_list_string(self):
        # Input `strings` is a string, not a list of strings.
        with self.assertRaises(TypeError):
            concatenate("not_a_list")

    def test_error_list_contains_integer(self):
        # Input list contains non-string elements (e.g., an integer).
        with self.assertRaises(TypeError):
            concatenate(["a", 123, "b"])

    def test_error_list_contains_list(self):
        # Input list contains non-string elements (e.g., another list).
        with self.assertRaises(TypeError):
            concatenate(["a", ["list"], "b"])