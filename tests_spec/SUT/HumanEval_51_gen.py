import unittest
from sut.problem_HumanEval_51 import remove_vowels

class Test_remove_vowels(unittest.TestCase):

    def test_normal_case_with_newline(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_normal_case_standard_string(self):
        self.assertEqual(remove_vowels("abcdef"), 'bcdf')

    def test_normal_case_only_consonants(self):
        self.assertEqual(remove_vowels("zbcd"), 'zbcd')

    def test_normal_case_mixed_case_and_punctuation(self):
        self.assertEqual(remove_vowels("Hello World!"), 'Hll Wrld!')

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_vowels(""), '')

    def test_edge_case_only_vowels(self):
        self.assertEqual(remove_vowels("aaaaa"), '')

    def test_edge_case_mixed_case_vowels_and_consonant(self):
        self.assertEqual(remove_vowels("aaBAA"), 'B')

    def test_edge_case_all_vowels_mixed_case(self):
        self.assertEqual(remove_vowels("AEIOUaeiou"), '')

    def test_edge_case_only_uppercase_consonants(self):
        self.assertEqual(remove_vowels("BCDFG"), 'BCDFG')

    def test_edge_case_non_alphabetic_characters(self):
        self.assertEqual(remove_vowels("12345!@#$"), '12345!@#$')