import unittest
import sut.problem_HumanEval_93 as mod

class TestHybrid(unittest.TestCase):
    def test_example_one(self):
            """
            Test case from the docstring: 'test' -> 'TGST'.
            Covers: lowercase input, mix of vowel/consonant, case swap, vowel replacement.
            """
            self.assertEqual(mod.encode('test'), 'TGST')

    def test_example_two(self):
            """
            Test case from the docstring: 'This is a message' -> 'tHKS KS C MGSSCGG'.
            Covers: mixed case input, spaces, multiple words, multiple vowels, multiple consonants.
            """
            self.assertEqual(mod.encode('This is a message'), 'tHKS KS C MGSSCGG')

    def test_all_lowercase_consonants(self):
            """
            Extreme input test: Input with only lowercase consonants.
            Covers: only consonants, case swap, checks non-vowel logic.
            """
            self.assertEqual(mod.encode('bcdfghjklmnpqrstvwxyz'), 'BCDFGHJKLMNPQRSTVWXYZ')

    def test_all_uppercase_consonants(self):
            """
            Extreme input test: Input with only uppercase consonants.
            Covers: only consonants, case swap, checks non-vowel logic.
            """
            self.assertEqual(mod.encode('BCDFGHJKLMNPQRSTVWXYZ'), 'bcdfghjklmnpqrstvwxyz')

    def test_empty_string(self):
            """
            Edge case: Empty input string.
            Covers: empty collection.
            """
            self.assertEqual(mod.encode(''), '')

    def test_single_character_vowel(self):
            """
            Edge case: Single character input, a vowel.
            Covers: single element, vowel replacement.
            """
            self.assertEqual(mod.encode('a'), 'C')

    def test_single_character_consonant(self):
            """
            Edge case: Single character input, a consonant.
            Covers: single element, consonant case swap.
            """
            self.assertEqual(mod.encode('b'), 'B')

    def test_normal_docstring_example_1(self):
            # Example from docstring: a word with mixed case, vowels and consonants.
            self.assertEqual(mod.encode("test"), "TGST")

    def test_edge_empty_string(self):
            # Empty string input should result in an empty string output.
            self.assertEqual(mod.encode(""), "")

    def test_edge_all_consonants_mixed_case(self):
            # String containing only consonants (mixed case), demonstrating only case swaps.
            self.assertEqual(mod.encode("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz")

    def test_edge_non_alphabetic_characters(self):
            # String containing only non-alphabetic characters, which should remain unchanged.
            self.assertEqual(mod.encode("123!@#"), "123!@#")

    def test_edge_mixed_alphabetic_and_non_alphabetic(self):
            # A sentence with numbers and symbols, demonstrating preservation of non-alphabetic characters.
            self.assertEqual(mod.encode("Python 3.9 is great!"), "pYTHQN 3.9 KS GRGCT!")

