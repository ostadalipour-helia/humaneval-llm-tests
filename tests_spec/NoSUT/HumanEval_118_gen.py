import unittest
from sut.problem_HumanEval_118 import get_closest_vowel

class Test_get_closest_vowel(unittest.TestCase):
    def test_normal_yogurt(self):
        # Typical case with a vowel between two consonants.
        self.assertEqual(get_closest_vowel("yogurt"), "u")

    def test_normal_full_uppercase(self):
        # Typical case with an uppercase vowel between two consonants.
        self.assertEqual(get_closest_vowel("FULL"), "U")

    def test_normal_rightmost_vowel(self):
        # Multiple valid vowels, returns the rightmost one.
        self.assertEqual(get_closest_vowel("zzzaUzzzzAzzzz"), "A")

    def test_edge_no_vowel_between_consonants(self):
        # Vowels are present but not between two consonants.
        self.assertEqual(get_closest_vowel("quick"), "")

    def test_edge_vowel_at_beginning(self):
        # Vowel at the beginning, not counted.
        self.assertEqual(get_closest_vowel("ab"), "")

    def test_edge_vowel_at_end(self):
        # Vowel at the end, not counted.
        self.assertEqual(get_closest_vowel("apple"), "")

    def test_edge_empty_string(self):
        # Empty string input.
        self.assertEqual(get_closest_vowel(""), "")

    def test_edge_all_vowels(self):
        # String composed entirely of vowels.
        self.assertEqual(get_closest_vowel("aeiou"), "")

    def test_edge_no_vowels_at_all(self):
        # String with no vowels.
        self.assertEqual(get_closest_vowel("rhythm"), "")

    def test_edge_valid_vowel_single_instance(self):
        # Vowel 'U' is between two 'z' consonants.
        self.assertEqual(get_closest_vowel("zzzaUzzzz"), "U")

    def test_error_non_string_int(self):
        # Input 'word' is not a string (integer).
        with self.assertRaises(TypeError):
            get_closest_vowel(123)

    def test_error_non_string_list(self):
        # Input 'word' is not a string (list).
        with self.assertRaises(TypeError):
            get_closest_vowel(["hello"])