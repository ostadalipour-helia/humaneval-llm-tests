import unittest
from sut.problem_HumanEval_64 import vowels_count

class Test_vowels_count(unittest.TestCase):
    def test_normal_abcde(self):
        # Standard word with multiple vowels, no 'y' at end.
        self.assertEqual(vowels_count("abcde"), 2)

    def test_normal_acedy(self):
        # Mixed case word with 'y' at the end counting as a vowel.
        self.assertEqual(vowels_count("ACEDY"), 3)

    def test_normal_education(self):
        # Word with many vowels, mixed case.
        self.assertEqual(vowels_count("Education"), 5)

    def test_edge_empty_string(self):
        # Empty string should return 0 vowels.
        self.assertEqual(vowels_count(""), 0)

    def test_edge_single_y(self):
        # Single character string, 'y' at the end.
        self.assertEqual(vowels_count("y"), 1)

    def test_edge_rhythm(self):
        # Word with 'y' at the end as the only vowel.
        self.assertEqual(vowels_count("rhythm"), 1)

    def test_edge_rhythms(self):
        # Word with 'y' not at the end, no other vowels.
        self.assertEqual(vowels_count("rhythms"), 0)

    def test_edge_syzygy(self):
        # Word with multiple 'y's, only the last one counts.
        self.assertEqual(vowels_count("syzygy"), 1)

    def test_edge_with_numbers(self):
        # String with numbers, only alphabetic vowels are counted.
        self.assertEqual(vowels_count("h3ll0"), 2)

    def test_edge_crypt(self):
        # Word with no vowels according to the rules.
        self.assertEqual(vowels_count("crypt"), 0)

    def test_error_none_input(self):
        # Input is `None` instead of a string.
        with self.assertRaises(TypeError):
            vowels_count(None)

    def test_error_int_input(self):
        # Input is an integer instead of a string.
        with self.assertRaises(TypeError):
            vowels_count(123)