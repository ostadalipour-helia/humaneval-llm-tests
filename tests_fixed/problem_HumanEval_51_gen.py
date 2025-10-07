import unittest
from sut_llm.problem_HumanEval_51 import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_all_lowercase_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_mixed_case_vowels_and_consonants(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_string_with_no_vowels(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

    def test_standard_lowercase_string(self):
        self.assertEqual(remove_vowels('abcdef'), 'bcdf')

    def test_string_with_newline_and_vowels(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_string_with_only_consonants(self):
        self.assertEqual(remove_vowels('rhythm'), 'rhythm')

    def test_string_with_only_uppercase_vowels(self):
        self.assertEqual(remove_vowels('AEIOU'), '')

    def test_string_with_mixed_case_and_spaces(self):
        self.assertEqual(remove_vowels('Hello World!'), 'Hll Wrld!')

    def test_string_with_leading_trailing_vowels_and_mixed_case(self):
        self.assertEqual(remove_vowels('Orange Apple'), 'rng ppl')

if __name__ == '__main__':
    unittest.main()