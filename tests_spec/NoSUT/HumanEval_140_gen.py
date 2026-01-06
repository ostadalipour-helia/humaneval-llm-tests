import unittest
from sut.problem_HumanEval_140 import fix_spaces

class Test_fix_spaces(unittest.TestCase):
    def test_no_spaces(self):
        # Normal case: No spaces in the input string.
        self.assertEqual(fix_spaces("Example"), "Example")

    def test_single_space(self):
        # Normal case: Single space replaced by underscore.
        self.assertEqual(fix_spaces("Example 1"), "Example_1")

    def test_two_consecutive_spaces(self):
        # Normal case: Two consecutive spaces replaced by two underscores.
        self.assertEqual(fix_spaces("Hello  World"), "Hello__World")

    def test_three_consecutive_spaces(self):
        # Normal case: Three consecutive spaces replaced by a hyphen.
        self.assertEqual(fix_spaces("Example   3"), "Example-3")

    def test_mixed_leading_internal_trailing_spaces(self):
        # Normal case: Mixed leading, internal, and trailing spaces with different lengths.
        self.assertEqual(fix_spaces("  Test   String "), "__Test-String_")

    def test_empty_string(self):
        # Edge case: Empty string input.
        self.assertEqual(fix_spaces(""), "")

    def test_string_with_only_single_space(self):
        # Edge case: String with only a single space.
        self.assertEqual(fix_spaces(" "), "_")

    def test_string_with_only_two_spaces(self):
        # Edge case: String with only two consecutive spaces.
        self.assertEqual(fix_spaces("  "), "__")

    def test_string_with_only_three_spaces(self):
        # Edge case: String with only three consecutive spaces.
        self.assertEqual(fix_spaces("   "), "-")

    def test_string_with_various_lengths_of_consecutive_spaces(self):
        # Edge case: String with various lengths of consecutive spaces.
        self.assertEqual(fix_spaces("A  B   C    D     E"), "A__B-C-D-E")

    def test_error_input_is_integer(self):
        # Error case: Input is not a string (e.g., an integer).
        with self.assertRaises(TypeError):
            fix_spaces(123)

    def test_error_input_is_none(self):
        # Error case: Input is not a string (e.g., None).
        with self.assertRaises(TypeError):
            fix_spaces(None)