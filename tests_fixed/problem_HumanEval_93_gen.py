import unittest
from sut_llm.problem_HumanEval_93 import encode

class TestEncodeFunction(unittest.TestCase):

    def test_example_one(self):
        """
        Test case from the docstring: 'test' -> 'TGST'.
        Covers: lowercase input, mix of vowel/consonant, case swap, vowel replacement.
        """
        self.assertEqual(encode('test'), 'TGST')

    def test_example_two(self):
        """
        Test case from the docstring: 'This is a message' -> 'tHKS KS C MGSSCGG'.
        Covers: mixed case input, spaces, multiple words, multiple vowels, multiple consonants.
        """
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

    def test_all_lowercase_vowels(self):
        """
        Boundary test: Input with all lowercase vowels.
        Covers: all lowercase vowels, boundary for vowel replacement (a, u).
        """
        self.assertEqual(encode('aeiou'), 'CGKQW')

    def test_all_uppercase_vowels(self):
        """
        Boundary test: Input with all uppercase vowels.
        Covers: all uppercase vowels, boundary for vowel replacement (A, U).
        """
        self.assertEqual(encode('AEIOU'), 'CGKQW')

    def test_all_lowercase_consonants(self):
        """
        Extreme input test: Input with only lowercase consonants.
        Covers: only consonants, case swap, checks non-vowel logic.
        """
        self.assertEqual(encode('bcdfghjklmnpqrstvwxyz'), 'BCDFGHJKLMNPQRSTVWXYZ')

    def test_all_uppercase_consonants(self):
        """
        Extreme input test: Input with only uppercase consonants.
        Covers: only consonants, case swap, checks non-vowel logic.
        """
        self.assertEqual(encode('BCDFGHJKLMNPQRSTVWXYZ'), 'bcdfghjklmnpqrstvwxyz')

    def test_empty_string(self):
        """
        Edge case: Empty input string.
        Covers: empty collection.
        """
        self.assertEqual(encode(''), '')

    def test_single_character_vowel(self):
        """
        Edge case: Single character input, a vowel.
        Covers: single element, vowel replacement.
        """
        self.assertEqual(encode('a'), 'C')

    def test_single_character_consonant(self):
        """
        Edge case: Single character input, a consonant.
        Covers: single element, consonant case swap.
        """
        self.assertEqual(encode('b'), 'B')

    def test_mixed_case_and_spaces(self):
        """
        Typical/Unusual input test: A more complex string with mixed case, spaces, and various vowels/consonants.
        Covers: mixed case, spaces, multiple words, different vowel/consonant positions.
        """
        self.assertEqual(encode('PyThOn Is FuN'), 'pYtHQN KS fWn')