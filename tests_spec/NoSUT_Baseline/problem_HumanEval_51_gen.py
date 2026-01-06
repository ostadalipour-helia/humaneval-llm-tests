import unittest
import sut.problem_HumanEval_51 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            # Edge case: empty string input
            self.assertEqual(mod.remove_vowels(''), '')

    def test_all_lowercase_vowels(self):
            # Extreme case: string composed entirely of lowercase vowels
            self.assertEqual(mod.remove_vowels('aeiou'), '')

    def test_all_uppercase_vowels(self):
            # Extreme case: string composed entirely of uppercase vowels (tests case-insensitivity)
            self.assertEqual(mod.remove_vowels('AEIOU'), '')

    def test_mixed_case_vowels_and_consonants(self):
            # Typical input: mixed case, vowels and consonants, tests logic mutations (AND/OR)
            self.assertEqual(mod.remove_vowels('Python is Fun'), 'Pythn s Fn')

    def test_no_vowels(self):
            # Boundary case: string with no vowels (all consonants or special chars)
            self.assertEqual(mod.remove_vowels('rhythm'), 'rhythm')

    def test_single_vowel(self):
            # Edge case: single character input, which is a vowel
            self.assertEqual(mod.remove_vowels('a'), '')

    def test_single_consonant(self):
            # Edge case: single character input, which is a consonant
            self.assertEqual(mod.remove_vowels('b'), 'b')

    def test_string_with_numbers_and_symbols(self):
            # Unusual input: contains numbers and various symbols, ensuring they are preserved
            self.assertEqual(mod.remove_vowels('123!@#$abcde'), '123!@#$bcd')

    def test_long_string_mixed_content(self):
            # Boundary/Typical: a longer string with a mix of cases, vowels, consonants, and spaces
            self.assertEqual(mod.remove_vowels('The quick brown fox jumps over the lazy dog.'), 'Th qck brwn fx jmps vr th lzy dg.')
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_mixed_case_newline(self):
            # String with mixed case, vowels, consonants, and a newline character.
            self.assertEqual(mod.remove_vowels("abcdef\nghijklm"), "bcdf\nghjklm")

    def test_normal_standard_string(self):
            # Standard string with both vowels and consonants.
            self.assertEqual(mod.remove_vowels("abcdef"), "bcdf")

    def test_normal_hello_world(self):
            # String with mixed case, spaces, and punctuation.
            self.assertEqual(mod.remove_vowels("Hello World!"), "Hll Wrld!")

    def test_edge_empty_string(self):
            # Empty string input.
            self.assertEqual(mod.remove_vowels(""), "")

    def test_edge_only_vowels(self):
            # String containing only vowels.
            self.assertEqual(mod.remove_vowels("aaaaa"), "")

    def test_edge_mixed_case_vowels_consonant(self):
            # String with mixed case vowels and a single consonant.
            self.assertEqual(mod.remove_vowels("aaBAA"), "B")

    def test_edge_all_vowels_mixed_case(self):
            # String containing all vowels, mixed case.
            self.assertEqual(mod.remove_vowels("AEIOUaeiou"), "")

    def test_edge_only_non_alphabetic(self):
            # String containing only non-alphabetic characters.
            self.assertEqual(mod.remove_vowels("12345!@#$"), "12345!@#$")

    def test_error_integer_input(self):
            # Input is an integer, not a string.
            with self.assertRaises(TypeError):
                mod.remove_vowels(123)

    def test_error_none_input(self):
            # Input is None, not a string.
            with self.assertRaises(TypeError):
                mod.remove_vowels(None)

