import unittest
from sut_llm.problem_HumanEval_51 import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        # Edge case: empty string input
        self.assertEqual(remove_vowels(''), '')

    def test_all_lowercase_vowels(self):
        # Extreme case: string composed entirely of lowercase vowels
        self.assertEqual(remove_vowels('aeiou'), '')

    def test_all_uppercase_vowels(self):
        # Extreme case: string composed entirely of uppercase vowels (tests case-insensitivity)
        self.assertEqual(remove_vowels('AEIOU'), '')

    def test_mixed_case_vowels_and_consonants(self):
        # Typical input: mixed case, vowels and consonants, tests logic mutations (AND/OR)
        self.assertEqual(remove_vowels('Python is Fun'), 'Pythn s Fn')

    def test_no_vowels(self):
        # Boundary case: string with no vowels (all consonants or special chars)
        self.assertEqual(remove_vowels('rhythm'), 'rhythm')

    def test_single_vowel(self):
        # Edge case: single character input, which is a vowel
        self.assertEqual(remove_vowels('a'), '')

    def test_single_consonant(self):
        # Edge case: single character input, which is a consonant
        self.assertEqual(remove_vowels('b'), 'b')

    def test_string_with_newlines_and_spaces(self):
        # Typical input: includes special characters like newlines and spaces
        self.assertEqual(remove_vowels('Hello\nWorld!'), 'Hll\nWrld!')

    def test_string_with_numbers_and_symbols(self):
        # Unusual input: contains numbers and various symbols, ensuring they are preserved
        self.assertEqual(remove_vowels('123!@#$abcde'), '123!@#$bcd')

    def test_long_string_mixed_content(self):
        # Boundary/Typical: a longer string with a mix of cases, vowels, consonants, and spaces
        self.assertEqual(remove_vowels('The quick brown fox jumps over the lazy dog.'), 'Th qck brwn fx jmps vr th lzy dg.')

if __name__ == '__main__':
    unittest.main()