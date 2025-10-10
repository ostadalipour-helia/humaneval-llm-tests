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


    def test_string_with_numbers(self):
        """Test with a string containing only numbers."""
        text = '12345'
        expected_md5 = '827ccb0eea8a706c4c34a16891f84e7b'
        self.assertEqual(string_to_md5(text), expected_md5)






if __name__ == '__main__':
    unittest.main()