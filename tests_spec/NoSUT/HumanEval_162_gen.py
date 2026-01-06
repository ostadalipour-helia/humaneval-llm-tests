import unittest
from sut.problem_HumanEval_162 import string_to_md5

class Test_string_to_md5(unittest.TestCase):

    def test_normal_hello_world(self):
        """Test with a common string 'Hello world'."""
        text = "Hello world"
        expected_output = "3e25960a79dbc69b674cd4ec67a72c62"
        self.assertEqual(string_to_md5(text), expected_output)

    def test_normal_python(self):
        """Test with another common string 'Python'."""
        text = "Python"
        expected_output = "86f7e437fa5a7745ff8d07478f726a5a"
        self.assertEqual(string_to_md5(text), expected_output)

    def test_normal_quick_brown_fox(self):
        """Test with a longer common string."""
        text = "The quick brown fox jumps over the lazy dog"
        expected_output = "9e107d9d372bb6826bd81d3542a419d6"
        self.assertEqual(string_to_md5(text), expected_output)

    def test_edge_empty_string(self):
        """Test with an empty string, which should return None."""
        text = ""
        self.assertIsNone(string_to_md5(text))

    def test_edge_single_character(self):
        """Test with a single character string."""
        text = "a"
        expected_output = "0cc175b9c0f1b6a831c399e269772661"
        self.assertEqual(string_to_md5(text), expected_output)

    def test_edge_space_character(self):
        """Test with a string containing only a space."""
        text = " "
        expected_output = "7215ee9c7d9dc229d2921a40e899ec5f"
        self.assertEqual(string_to_md5(text), expected_output)

    def test_edge_digits_string(self):
        """Test with a string of digits."""
        text = "1234567890"
        expected_output = "827ccb0eea8a706c4c34a16891f84e7b"
        self.assertEqual(string_to_md5(text), expected_output)

    def test_edge_special_characters(self):
        """Test with a string of special characters."""
        text = "!@#$%^&*()"
        expected_output = "f1822412212222222222222222222222"
        self.assertEqual(string_to_md5(text), expected_output)

    def test_error_integer_input(self):
        """Test with an integer input, expecting a TypeError."""
        with self.assertRaises(TypeError):
            string_to_md5(123)

    def test_error_none_input(self):
        """Test with None as input, expecting a TypeError."""
        with self.assertRaises(TypeError):
            string_to_md5(None)

    def test_error_list_input(self):
        """Test with a list as input, expecting a TypeError."""
        with self.assertRaises(TypeError):
            string_to_md5(["list"])

    def test_postcondition_return_format(self):
        """
        Test that for non-empty strings, the return value is a 32-character
        hexadecimal string.
        """
        test_strings = ["test", "another test string", "123abcDEF"]
        for text in test_strings:
            result = string_to_md5(text)
            self.assertIsInstance(result, str)
            self.assertEqual(len(result), 32)
            # Check if it's a hexadecimal string
            self.assertTrue(all(c in "0123456789abcdef" for c in result))