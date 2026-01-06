import unittest
from sut.problem_HumanEval_51 import remove_vowels

class Test_remove_vowels(unittest.TestCase):
    def test_normal_mixed_case_newline(self):
        # String with mixed case, vowels, consonants, and a newline character.
        self.assertEqual(remove_vowels("abcdef\nghijklm"), "bcdf\nghjklm")

    def test_normal_standard_string(self):
        # Standard string with both vowels and consonants.
        self.assertEqual(remove_vowels("abcdef"), "bcdf")

    def test_normal_hello_world(self):
        # String with mixed case, spaces, and punctuation.
        self.assertEqual(remove_vowels("Hello World!"), "Hll Wrld!")

    def test_edge_empty_string(self):
        # Empty string input.
        self.assertEqual(remove_vowels(""), "")

    def test_edge_only_vowels(self):
        # String containing only vowels.
        self.assertEqual(remove_vowels("aaaaa"), "")

    def test_edge_mixed_case_vowels_consonant(self):
        # String with mixed case vowels and a single consonant.
        self.assertEqual(remove_vowels("aaBAA"), "B")

    def test_edge_all_vowels_mixed_case(self):
        # String containing all vowels, mixed case.
        self.assertEqual(remove_vowels("AEIOUaeiou"), "")

    def test_edge_only_non_alphabetic(self):
        # String containing only non-alphabetic characters.
        self.assertEqual(remove_vowels("12345!@#$"), "12345!@#$")

    def test_error_integer_input(self):
        # Input is an integer, not a string.
        with self.assertRaises(TypeError):
            remove_vowels(123)

    def test_error_none_input(self):
        # Input is None, not a string.
        with self.assertRaises(TypeError):
            remove_vowels(None)

    def test_error_list_input(self):
        # Input is a list, not a string.
        with self.assertRaises(TypeError):
            remove_vowels(["a", "b", "c"])