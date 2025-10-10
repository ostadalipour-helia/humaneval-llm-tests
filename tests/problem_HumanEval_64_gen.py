import unittest
from sut.problem_HumanEval_64 import vowels_count

class TestVowelsCount(unittest.TestCase):

    def test_example_one(self):
        # Typical input, basic vowel counting
        # Covers: Typical/Expected, Exact Output
        self.assertEqual(vowels_count("abcde"), 2)

    def test_example_two(self):
        # Typical input, uppercase, 'y' at the end
        # Covers: Typical/Expected, Case-insensitivity, 'y' rule, Exact Output
        self.assertEqual(vowels_count("ACEDY"), 3)

    def test_empty_string(self):
        # Edge case: empty string
        # Covers: Edge Case (empty), Boundary (0 elements), Exact Output
        self.assertEqual(vowels_count(""), 0)

    def test_single_vowel(self):
        # Edge case: single character string, which is a vowel
        # Covers: Edge Case (single element), Boundary (first/last element), Exact Output
        self.assertEqual(vowels_count("a"), 1)

    def test_single_consonant(self):
        # Edge case: single character string, which is a consonant
        # Covers: Edge Case (single element), Boundary (first/last element), Exact Output
        self.assertEqual(vowels_count("b"), 0)

    def test_y_at_end_is_vowel(self):
        # Boundary/Logic: 'y' at the very end of the word
        # Covers: Boundary ('y' rule), Logic Mutation (y condition), Exact Output
        self.assertEqual(vowels_count("lovely"), 3) # o, e, y

    def test_y_not_at_end_is_consonant(self):
        # Boundary/Logic: 'y' in the middle of the word
        # Covers: Boundary ('y' rule), Logic Mutation (y condition), Exact Output
        self.assertEqual(vowels_count("python"), 1) # o

    def test_all_vowels_including_y_at_end(self):
        # Extreme input: string with all standard vowels and 'y' at the end
        # Covers: Extreme/Unusual, Off-by-One (loop boundaries), Exact Output
        self.assertEqual(vowels_count("aeiouy"), 6)

    def test_no_vowels_all_consonants(self):
        # Extreme input: string with no vowels, including 'y' not at end
        # Covers: Extreme/Unusual, Logic Mutation (default count), Exact Output
        self.assertEqual(vowels_count("rhythm"), 0)

    def test_long_mixed_case_string(self):
        # Extreme input: longer string with mixed case and no 'y' at end
        # Covers: Extreme/Unusual, Case-insensitivity, Off-by-One (longer string), Exact Output
        self.assertEqual(vowels_count("ProgrammingIsFun"), 5) # o, a, i, i, u