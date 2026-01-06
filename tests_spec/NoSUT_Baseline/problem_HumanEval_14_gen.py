import unittest
import sut.problem_HumanEval_14 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            # Boundary: empty string, edge case
            self.assertListEqual(mod.all_prefixes(""), [])

    def test_single_character_string(self):
            # Boundary: single character string, edge case, off-by-one (loop for 1 iteration)
            self.assertListEqual(mod.all_prefixes("a"), ["a"])

    def test_two_character_string(self):
            # Off-by-one: loop for 2 iterations
            self.assertListEqual(mod.all_prefixes("ab"), ["a", "ab"])

    def test_docstring_example(self):
            # Typical input, verifies example from docstring
            self.assertListEqual(mod.all_prefixes("abc"), ["a", "ab", "abc"])

    def test_medium_length_string(self):
            # Typical input, general case
            self.assertListEqual(mod.all_prefixes("hello"), ["h", "he", "hel", "hell", "hello"])

    def test_string_with_spaces(self):
            # Extreme/unusual input: string containing spaces
            self.assertListEqual(mod.all_prefixes("hi there"), ["h", "hi", "hi ", "hi t", "hi th", "hi the", "hi ther", "hi there"])

    def test_string_with_digits_and_symbols(self):
            # Extreme/unusual input: string with numbers and special characters
            self.assertListEqual(mod.all_prefixes("123!"), ["1", "12", "123", "123!"])

    def test_string_with_all_same_characters(self):
            # Edge case: string with all identical characters, duplicate values
            self.assertListEqual(mod.all_prefixes("aaaa"), ["a", "aa", "aaa", "aaaa"])

    def test_string_with_mixed_case(self):
            # Typical input: string with mixed upper and lower case characters
            self.assertListEqual(mod.all_prefixes("PyThOn"), ["P", "Py", "PyT", "PyTh", "PyThO", "PyThOn"])

    def test_string_with_unicode_characters(self):
            # Extreme/unusual input: string with multi-byte unicode characters
            self.assertListEqual(mod.all_prefixes("你好世界"), ["你", "你好", "你好世", "你好世界"])

    def test_normal_multi_character_string_abc(self):
            # Standard case with a multi-character string.
            string = "abc"
            expected_output = ["a", "ab", "abc"]
            self.assertEqual(mod.all_prefixes(string), expected_output)

    def test_normal_longer_string_hello(self):
            # A longer multi-character string.
            string = "hello"
            expected_output = ["h", "he", "hel", "hell", "hello"]
            self.assertEqual(mod.all_prefixes(string), expected_output)

    def test_edge_empty_string(self):
            # Empty input string should return an empty list.
            string = ""
            expected_output = []
            self.assertEqual(mod.all_prefixes(string), expected_output)

    def test_edge_single_character_string(self):
            # Single character input string.
            string = "a"
            expected_output = ["a"]
            self.assertEqual(mod.all_prefixes(string), expected_output)

    def test_edge_string_with_numbers_and_special_chars(self):
            # String containing numbers and special characters.
            string = "123!"
            expected_output = ["1", "12", "123", "123!"]
            self.assertEqual(mod.all_prefixes(string), expected_output)

    def test_edge_whitespace_string(self):
            # String containing only whitespace characters.
            string = "  "
            expected_output = [" ", "  "]
            self.assertEqual(mod.all_prefixes(string), expected_output)

    def test_error_input_integer(self):
            # Input is not a string (e.g., an integer).
            string = 123
            with self.assertRaises(TypeError):
                mod.all_prefixes(string)

    def test_error_input_none(self):
            # Input is not a string (e.g., None).
            string = None
            with self.assertRaises(TypeError):
                mod.all_prefixes(string)

