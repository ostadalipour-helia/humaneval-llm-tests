import unittest
from sut.problem_HumanEval_23 import strlen

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        """
        Test with an empty string.
        Covers: Boundary (minimum length), Edge Case (empty collection), Sign/Zero (return 0).
        Catches: Off-by-one errors (e.g., returning 1 for empty), mutations changing 0 to 1.
        """
        self.assertEqual(strlen(''), 0)

    def test_single_character_string(self):
        """
        Test with a string containing a single character.
        Covers: Boundary (length 1), Edge Case (single element collection), Off-by-one.
        Catches: Off-by-one errors (e.g., returning 0 or 2).
        """
        self.assertEqual(strlen('a'), 1)

    def test_two_character_string(self):
        """
        Test with a string containing two characters.
        Covers: Boundary (length 2), Off-by-one.
        Catches: Off-by-one errors (e.g., returning 1 or 3).
        """
        self.assertEqual(strlen('ab'), 2)

    def test_docstring_example_abc(self):
        """
        Test with a typical string from the docstring example.
        Covers: Typical input, verifies expected behavior.
        """
        self.assertEqual(strlen('abc'), 3)

    def test_typical_five_char_string(self):
        """
        Test with another typical string of moderate length.
        Covers: Typical input.
        """
        self.assertEqual(strlen('hello'), 5)

    def test_string_with_spaces(self):
        """
        Test with a string containing spaces.
        Covers: Unusual input (spaces are characters), verifies correct counting.
        """
        self.assertEqual(strlen('hello world'), 11)

    def test_string_with_special_characters(self):
        """
        Test with a string composed entirely of special characters.
        Covers: Extreme/Unusual input, verifies character counting for non-alphanumeric.
        """
        self.assertEqual(strlen('!@#$%^&*()'), 10)

    def test_string_with_unicode_characters(self):
        """
        Test with a string containing multi-byte Unicode characters.
        Covers: Extreme/Unusual input, verifies character counting (not byte counting).
        """
        self.assertEqual(strlen('你好世界'), 4)

    def test_long_string(self):
        """
        Test with a very long string.
        Covers: Extreme input, performance for large inputs, verifies scalability.
        Catches: Potential issues with loop boundaries or integer overflow (though unlikely for Python int).
        """
        long_str = 'x' * 1000
        self.assertEqual(strlen(long_str), 1000)

    def test_string_with_digits(self):
        """
        Test with a string composed of digits.
        Covers: Typical input (digits are characters), verifies correct counting.
        """
        self.assertEqual(strlen('1234567890'), 10)