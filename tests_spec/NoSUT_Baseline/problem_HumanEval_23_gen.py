import unittest
import sut.problem_HumanEval_23 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            """
            Test with an empty string.
            Covers: Boundary (minimum length), Edge Case (empty collection), Sign/Zero (return 0).
            Catches: Off-by-one errors (e.g., returning 1 for empty), mutations changing 0 to 1.
            """
            self.assertEqual(mod.strlen(''), 0)

    def test_single_character_string(self):
            """
            Test with a string containing a single character.
            Covers: Boundary (length 1), Edge Case (single element collection), Off-by-one.
            Catches: Off-by-one errors (e.g., returning 0 or 2).
            """
            self.assertEqual(mod.strlen('a'), 1)

    def test_two_character_string(self):
            """
            Test with a string containing two characters.
            Covers: Boundary (length 2), Off-by-one.
            Catches: Off-by-one errors (e.g., returning 1 or 3).
            """
            self.assertEqual(mod.strlen('ab'), 2)

    def test_docstring_example_abc(self):
            """
            Test with a typical string from the docstring example.
            Covers: Typical input, verifies expected behavior.
            """
            self.assertEqual(mod.strlen('abc'), 3)

    def test_typical_five_char_string(self):
            """
            Test with another typical string of moderate length.
            Covers: Typical input.
            """
            self.assertEqual(mod.strlen('hello'), 5)

    def test_string_with_spaces(self):
            """
            Test with a string containing spaces.
            Covers: Unusual input (spaces are characters), verifies correct counting.
            """
            self.assertEqual(mod.strlen('hello world'), 11)

    def test_string_with_special_characters(self):
            """
            Test with a string composed entirely of special characters.
            Covers: Extreme/Unusual input, verifies character counting for non-alphanumeric.
            """
            self.assertEqual(mod.strlen('!@#$%^&*()'), 10)

    def test_string_with_unicode_characters(self):
            """
            Test with a string containing multi-byte Unicode characters.
            Covers: Extreme/Unusual input, verifies character counting (not byte counting).
            """
            self.assertEqual(mod.strlen('你好世界'), 4)

    def test_long_string(self):
            """
            Test with a very long string.
            Covers: Extreme input, performance for large inputs, verifies scalability.
            Catches: Potential issues with loop boundaries or integer overflow (though unlikely for Python int).
            """
            long_str = 'x' * 1000
            self.assertEqual(mod.strlen(long_str), 1000)

    def test_string_with_digits(self):
            """
            Test with a string composed of digits.
            Covers: Typical input (digits are characters), verifies correct counting.
            """
            self.assertEqual(mod.strlen('1234567890'), 10)

    def test_normal_alphanumeric_string(self):
            """
            A typical non-empty string with alphanumeric characters.
            Input: "abc", Expected Output: 3
            """
            self.assertEqual(mod.strlen("abc"), 3)

    def test_normal_string_with_spaces(self):
            """
            A string containing spaces.
            Input: "hello world", Expected Output: 11
            """
            self.assertEqual(mod.strlen("hello world"), 11)

    def test_normal_unicode_string(self):
            """
            A string containing Unicode characters.
            Input: "你好", Expected Output: 2
            """
            self.assertEqual(mod.strlen("你好"), 2)

    def test_edge_empty_string(self):
            """
            An empty string.
            Input: "", Expected Output: 0
            """
            self.assertEqual(mod.strlen(""), 0)

    def test_edge_single_character_string(self):
            """
            A string with a single character.
            Input: "a", Expected Output: 1
            """
            self.assertEqual(mod.strlen("a"), 1)

    def test_edge_special_characters_string(self):
            """
            A string with special characters.
            Input: "!@#$", Expected Output: 4
            """
            self.assertEqual(mod.strlen("!@#$"), 4)

    def test_error_input_integer(self):
            """
            Input is an integer instead of a string.
            Input: 123, Expected Exception: TypeError
            """
            with self.assertRaises(TypeError):
                mod.strlen(123)

    def test_error_input_none(self):
            """
            Input is None instead of a string.
            Input: None, Expected Exception: TypeError
            """
            with self.assertRaises(TypeError):
                mod.strlen(None)

