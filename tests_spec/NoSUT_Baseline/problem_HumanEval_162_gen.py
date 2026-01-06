import unittest
import sut.problem_HumanEval_162 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            """Test case for an empty input string, which should return None."""
            self.assertIsNone(mod.string_to_md5(''))

    def test_docstring_example(self):
            """Test case from the function's docstring."""
            self.assertEqual(mod.string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_simple_lowercase_string(self):
            """Test case with a simple, common lowercase string."""
            self.assertEqual(mod.string_to_md5('test'), '098f6bcd4621d373cade4e832627b4f6')

    def test_string_with_numbers(self):
            """Test case with a string containing only digits."""
            self.assertEqual(mod.string_to_md5('12345'), '827ccb0eea8a706c4c34a16891f84e7b')

    def test_single_character_string(self):
            """Test case with a single character input string."""
            self.assertEqual(mod.string_to_md5('a'), '0cc175b9c0f1b6a831c399e269772661')

    def test_normal_hello_world(self):
            """Test with a common string 'Hello world'."""
            text = "Hello world"
            expected_output = "3e25960a79dbc69b674cd4ec67a72c62"
            self.assertEqual(mod.string_to_md5(text), expected_output)

    def test_normal_quick_brown_fox(self):
            """Test with a longer common string."""
            text = "The quick brown fox jumps over the lazy dog"
            expected_output = "9e107d9d372bb6826bd81d3542a419d6"
            self.assertEqual(mod.string_to_md5(text), expected_output)

    def test_edge_empty_string(self):
            """Test with an empty string, which should return None."""
            text = ""
            self.assertIsNone(mod.string_to_md5(text))

    def test_edge_single_character(self):
            """Test with a single character string."""
            text = "a"
            expected_output = "0cc175b9c0f1b6a831c399e269772661"
            self.assertEqual(mod.string_to_md5(text), expected_output)

    def test_edge_space_character(self):
            """Test with a string containing only a space."""
            text = " "
            expected_output = "7215ee9c7d9dc229d2921a40e899ec5f"
            self.assertEqual(mod.string_to_md5(text), expected_output)

    def test_postcondition_return_format(self):
            """
            Test that for non-empty strings, the return value is a 32-character
            hexadecimal string.
            """
            test_strings = ["test", "another test string", "123abcDEF"]
            for text in test_strings:
                result = mod.string_to_md5(text)
                self.assertIsInstance(result, str)
                self.assertEqual(len(result), 32)
                # Check if it's a hexadecimal string
                self.assertTrue(all(c in "0123456789abcdef" for c in result))

