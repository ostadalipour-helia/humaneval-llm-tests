import unittest
from sut.problem_HumanEval_161 import solve

class Test_solve(unittest.TestCase):
    def test_normal_all_lowercase(self):
        # Description: String with all lowercase letters, all cases reversed.
        s = "ab"
        expected_output = "AB"
        self.assertEqual(solve(s), expected_output)

    def test_normal_mixed_letters_non_letters(self):
        # Description: String with mixed letters and non-letters, cases reversed for letters.
        s = "#a@C"
        expected_output = "#A@c"
        self.assertEqual(solve(s), expected_output)

    def test_normal_hello_world(self):
        # Description: String with mixed case letters, spaces, and punctuation.
        s = "Hello World!"
        expected_output = "hELLO wORLD!"
        self.assertEqual(solve(s), expected_output)

    def test_edge_no_letters_reversed(self):
        # Description: String containing no letters, should be entirely reversed.
        s = "1234"
        expected_output = "4321"
        self.assertEqual(solve(s), expected_output)

    def test_edge_empty_string(self):
        # Description: Empty string, contains no letters, reversed is itself.
        s = ""
        expected_output = ""
        self.assertEqual(solve(s), expected_output)

    def test_edge_single_uppercase_letter(self):
        # Description: Single uppercase letter.
        s = "A"
        expected_output = "a"
        self.assertEqual(solve(s), expected_output)

    def test_edge_single_lowercase_letter(self):
        # Description: Single lowercase letter.
        s = "z"
        expected_output = "Z"
        self.assertEqual(solve(s), expected_output)

    def test_edge_single_non_letter(self):
        # Description: Single non-letter character, contains no letters, reversed is itself.
        s = "!"
        expected_output = "!"
        self.assertEqual(solve(s), expected_output)

    def test_edge_mixed_case_and_spaces(self):
        # Description: String with mixed case letters and spaces.
        s = "aB cD"
        expected_output = "Ab Cd"
        self.assertEqual(solve(s), expected_output)

    def test_error_input_none(self):
        # Description: Input `s` is not a string (e.g., None).
        with self.assertRaises((TypeError, AttributeError)):
            solve(None)

    def test_error_input_integer(self):
        # Description: Input `s` is not a string (e.g., integer).
        with self.assertRaises((TypeError, AttributeError)):
            solve(123)

    def test_error_input_list(self):
        # Description: Input `s` is not a string (e.g., list).
        with self.assertRaises((TypeError, AttributeError)):
            solve(["a", "b"])