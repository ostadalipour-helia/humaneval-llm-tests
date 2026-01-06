import unittest
from sut.problem_HumanEval_14 import all_prefixes

class Test_all_prefixes(unittest.TestCase):
    def test_normal_multi_character_string_abc(self):
        # Standard case with a multi-character string.
        string = "abc"
        expected_output = ["a", "ab", "abc"]
        self.assertEqual(all_prefixes(string), expected_output)

    def test_normal_longer_string_hello(self):
        # A longer multi-character string.
        string = "hello"
        expected_output = ["h", "he", "hel", "hell", "hello"]
        self.assertEqual(all_prefixes(string), expected_output)

    def test_edge_empty_string(self):
        # Empty input string should return an empty list.
        string = ""
        expected_output = []
        self.assertEqual(all_prefixes(string), expected_output)

    def test_edge_single_character_string(self):
        # Single character input string.
        string = "a"
        expected_output = ["a"]
        self.assertEqual(all_prefixes(string), expected_output)

    def test_edge_string_with_numbers_and_special_chars(self):
        # String containing numbers and special characters.
        string = "123!"
        expected_output = ["1", "12", "123", "123!"]
        self.assertEqual(all_prefixes(string), expected_output)

    def test_edge_whitespace_string(self):
        # String containing only whitespace characters.
        string = "  "
        expected_output = [" ", "  "]
        self.assertEqual(all_prefixes(string), expected_output)

    def test_error_input_integer(self):
        # Input is not a string (e.g., an integer).
        string = 123
        with self.assertRaises(TypeError):
            all_prefixes(string)

    def test_error_input_none(self):
        # Input is not a string (e.g., None).
        string = None
        with self.assertRaises(TypeError):
            all_prefixes(string)

    def test_error_input_list(self):
        # Input is not a string (e.g., a list).
        string = ["a", "b"]
        with self.assertRaises(TypeError):
            all_prefixes(string)