import unittest
from sut_llm.problem_HumanEval_162 import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_empty_string(self):
        """Test case for an empty input string, which should return None."""
        self.assertIsNone(string_to_md5(''))

    def test_docstring_example(self):
        """Test case from the function's docstring."""
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_simple_lowercase_string(self):
        """Test case with a simple, common lowercase string."""
        self.assertEqual(string_to_md5('test'), '098f6bcd4621d373cade4e832627b4f6')

    def test_string_with_numbers(self):
        """Test case with a string containing only digits."""
        self.assertEqual(string_to_md5('12345'), '827ccb0eea8a706c4c34a16891f84e7b')

    def test_string_with_special_characters(self):
        """Test case with a string containing various special characters."""
        self.assertEqual(string_to_md5('!@#$%^&*()'), '05b28d17a7b6e7024b6e5d8cc43a8bf7')

    def test_string_with_mixed_case(self):
        """Test case with a string containing both uppercase and lowercase letters."""
        self.assertEqual(string_to_md5('Python Developer'), 'bb0f2be452d373036ebe412970abb071')

    def test_long_string_pangram(self):
        """Test case with a longer, well-known string (pangram)."""
        self.assertEqual(string_to_md5('The quick brown fox jumps over the lazy dog.'), 'e4d909c290d0fb1ca068ffaddf22cbd0')

    def test_single_character_string(self):
        """Test case with a single character input string."""
        self.assertEqual(string_to_md5('a'), '0cc175b9c0f1b6a831c399e269772661')

    def test_string_with_leading_trailing_whitespace(self