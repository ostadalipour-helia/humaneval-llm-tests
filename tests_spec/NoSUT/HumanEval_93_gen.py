import unittest
from sut.problem_HumanEval_93 import encode

class Test_encode(unittest.TestCase):
    def test_normal_docstring_example_1(self):
        # Example from docstring: a word with mixed case, vowels and consonants.
        self.assertEqual(encode("test"), "TGST")

    def test_normal_hello_world(self):
        # A common phrase with mixed letters and spaces, demonstrating vowel and consonant transformations.
        self.assertEqual(encode("Hello World"), "hGLLQ WQRLL")

    def test_edge_empty_string(self):
        # Empty string input should result in an empty string output.
        self.assertEqual(encode(""), "")

    def test_edge_all_vowels_mixed_case(self):
        # String containing only vowels (mixed case), demonstrating all vowel transformations.
        self.assertEqual(encode("aeiouAEIOU"), "CGKPWcgkpw")

    def test_edge_all_consonants_mixed_case(self):
        # String containing only consonants (mixed case), demonstrating only case swaps.
        self.assertEqual(encode("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz")

    def test_edge_non_alphabetic_characters(self):
        # String containing only non-alphabetic characters, which should remain unchanged.
        self.assertEqual(encode("123!@#"), "123!@#")

    def test_edge_mixed_alphabetic_and_non_alphabetic(self):
        # A sentence with numbers and symbols, demonstrating preservation of non-alphabetic characters.
        self.assertEqual(encode("Python 3.9 is great!"), "pYTHQN 3.9 KS GRGCT!")

    def test_error_integer_input(self):
        # Input is an integer instead of a string.
        with self.assertRaises(TypeError):
            encode(123)

    def test_error_list_input(self):
        # Input is a list instead of a string.
        with self.assertRaises(TypeError):
            encode(["hello"])

    def test_error_none_input(self):
        # Input is None instead of a string.
        with self.assertRaises(TypeError):
            encode(None)