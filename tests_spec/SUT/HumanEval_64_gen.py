import unittest
from sut.problem_HumanEval_64 import vowels_count

class Test_vowels_count(unittest.TestCase):

    def test_normal_cases(self):
        self.assertEqual(vowels_count("abcde"), 2)
        self.assertEqual(vowels_count("hello"), 2)
        self.assertEqual(vowels_count("Education"), 5)

    def test_y_at_end_as_vowel(self):
        self.assertEqual(vowels_count("ACEDY"), 3)
        self.assertEqual(vowels_count("mystery"), 2)
        self.assertEqual(vowels_count("fly"), 1)
        self.assertEqual(vowels_count("syzygy"), 1)
        self.assertEqual(vowels_count("rhythmY"), 1)

    def test_y_not_at_end(self):
        self.assertEqual(vowels_count("rhythms"), 0)
        self.assertEqual(vowels_count("Python"), 1)

    def test_empty_string(self):
        with self.assertRaises(IndexError):
            vowels_count("")

    def test_single_character_strings(self):
        self.assertEqual(vowels_count("a"), 1)
        self.assertEqual(vowels_count("b"), 0)
        self.assertEqual(vowels_count("y"), 1)
        self.assertEqual(vowels_count("Y"), 1)

    def test_all_vowels(self):
        self.assertEqual(vowels_count("aeiouAEIOU"), 10)

    def test_no_vowels(self):
        self.assertEqual(vowels_count("rhythm"), 0)
        self.assertEqual(vowels_count("crypt"), 0)

    def test_with_numbers(self):
        self.assertEqual(vowels_count("h3ll0"), 0)

    def test_case_insensitivity(self):
        self.assertEqual(vowels_count("ACEDY"), 3)
        self.assertEqual(vowels_count("Education"), 5)
        self.assertEqual(vowels_count("Y"), 1)
        self.assertEqual(vowels_count("rhythmY"), 1)

    def test_combined_edge_cases(self):
        self.assertEqual(vowels_count("syzygy"), 1)
        self.assertEqual(vowels_count("Python"), 1)
        self.assertEqual(vowels_count("fly"), 1)