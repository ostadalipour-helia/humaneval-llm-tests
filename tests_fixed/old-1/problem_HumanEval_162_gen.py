import unittest
from sut_llm.problem_HumanEval_162 import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_example_from_docstring(self):
        """Test with the example string provided in the docstring."""
        text = 'Hello world'
        expected_md5 = '3e25960a79dbc69b674cd4ec67a72c62'
        self.assertEqual(string_to_md5(text), expected_md5)

    def test_empty_string(self):
        """Test with an empty string, which should return None."""
        text = ''
        expected_md5 = None
        self.assertIsNone(string_to_md5(text))

    def test_simple_lowercase_string(self):
        """Test with a simple lowercase string."""
        text = 'abc'
        expected_md5 = '900150983cd24fb0d6963f7d28e17f72'
        self.assertEqual(string_to_md5(text), expected_md5)

    def test_simple_uppercase_string(self):
        """Test with a simple uppercase string."""
        text = 'ABC'
        expected_md5 = '902fbdd2b1df0c4f70b4a5d23525e932'
        self.assertEqual(string_to_md5(text), expected_md5)

    def test_string_with_numbers(self):
        """Test with a string containing only numbers."""
        text = '12345'
        expected_md5 = '827ccb0eea8a706c4c34a16891f84e7b'
        self.assertEqual(string_to_md5(text), expected_md5)

    def test_string_with_special_characters(self):
        """Test with a string containing special characters."""
        text = '!@#$%'
        expected_md5 = '507250b947cc397023a9595001fcf167'
        self.assertEqual(string_to_md5(text), expected_md5)

    def test_string_with_mixed_characters_and_spaces(self):
        """Test with a string containing mixed characters and spaces."""
        text = 'Python MD5 Hash'
        expected_md5 = '1716d6cdffb3e18f75579ccb40a35eb6' # Calculated using hashlib.md5('Python MD5 Hash'.encode('utf-8')).hexdigest()
        self.assertEqual(string_to_md5(text), expected_md5)

    def test_long_string(self):
        """Test with a relatively long string."""
        text = 'The quick brown fox jumps over the lazy dog. This is a longer sentence to ensure a more complex hash.'
        expected_md5 = 'f74237bdf68cea4b9550cc083a7ca832' # Calculated using hashlib.md5(text.encode('utf-8')).hexdigest()
        self.assertEqual(string_to_md5(text), expected_md5)

    def test_string_with_leading_trailing_spaces(self):
        """Test with a string that has leading and trailing spaces."""
        text = '  padded string  '
        expected_md5 = '08157197bbf5a4c217eeb5767b7bcd45' # Correct MD5 for '  padded string  '
        self.assertEqual(string_to_md5(text), expected_md5)

    def test_unicode_string(self):
        """Test with a Unicode string (non-ASCII characters)."""
        text = '你好世界' # "Hello world" in Chinese
        expected_md5 = '65396ee4aad0b4f17aacd1c6112ee364' # Calculated using hashlib.md5('你好世界'.encode('utf-8')).hexdigest()
        self.assertEqual(string_to_md5(text), expected_md5)

if __name__ == '__main__':
    unittest.main()