import unittest
import sut.problem_HumanEval_64 as mod

class TestHybrid(unittest.TestCase):
    def test_example_one(self):
            # Typical input, basic vowel counting
            # Covers: Typical/Expected, Exact Output
            self.assertEqual(mod.vowels_count("abcde"), 2)

    def test_example_two(self):
            # Typical input, uppercase, 'y' at the end
            # Covers: Typical/Expected, Case-insensitivity, 'y' rule, Exact Output
            self.assertEqual(mod.vowels_count("ACEDY"), 3)

    def test_single_vowel(self):
            # Edge case: single character string, which is a vowel
            # Covers: Edge Case (single element), Boundary (first/last element), Exact Output
            self.assertEqual(mod.vowels_count("a"), 1)

    def test_single_consonant(self):
            # Edge case: single character string, which is a consonant
            # Covers: Edge Case (single element), Boundary (first/last element), Exact Output
            self.assertEqual(mod.vowels_count("b"), 0)

    def test_y_at_end_is_vowel(self):
            # Boundary/Logic: 'y' at the very end of the word
            # Covers: Boundary ('y' rule), Logic Mutation (y condition), Exact Output
            self.assertEqual(mod.vowels_count("lovely"), 3) # o, e, y

    def test_y_not_at_end_is_consonant(self):
            # Boundary/Logic: 'y' in the middle of the word
            # Covers: Boundary ('y' rule), Logic Mutation (y condition), Exact Output
            self.assertEqual(mod.vowels_count("python"), 1) # o

    def test_all_vowels_including_y_at_end(self):
            # Extreme input: string with all standard vowels and 'y' at the end
            # Covers: Extreme/Unusual, Off-by-One (loop boundaries), Exact Output
            self.assertEqual(mod.vowels_count("aeiouy"), 6)

    def test_no_vowels_all_consonants(self):
            # Extreme input: string with no vowels, including 'y' not at end
            # Covers: Extreme/Unusual, Logic Mutation (default count), Exact Output
            self.assertEqual(mod.vowels_count("rhythm"), 0)

    def test_long_mixed_case_string(self):
            # Extreme input: longer string with mixed case and no 'y' at end
            # Covers: Extreme/Unusual, Case-insensitivity, Off-by-One (longer string), Exact Output
            self.assertEqual(mod.vowels_count("ProgrammingIsFun"), 5) # o, a, i, i, u

    def test_normal_abcde(self):
            # Standard word with multiple vowels, no 'y' at end.
            self.assertEqual(mod.vowels_count("abcde"), 2)

    def test_normal_acedy(self):
            # Mixed case word with 'y' at the end counting as a vowel.
            self.assertEqual(mod.vowels_count("ACEDY"), 3)

    def test_normal_education(self):
            # Word with many vowels, mixed case.
            self.assertEqual(mod.vowels_count("Education"), 5)

    def test_edge_single_y(self):
            # Single character string, 'y' at the end.
            self.assertEqual(mod.vowels_count("y"), 1)

    def test_edge_rhythms(self):
            # Word with 'y' not at the end, no other vowels.
            self.assertEqual(mod.vowels_count("rhythms"), 0)

    def test_edge_syzygy(self):
            # Word with multiple 'y's, only the last one counts.
            self.assertEqual(mod.vowels_count("syzygy"), 1)

    def test_edge_crypt(self):
            # Word with no vowels according to the rules.
            self.assertEqual(mod.vowels_count("crypt"), 0)

    def test_error_none_input(self):
            # Input is `None` instead of a string.
            with self.assertRaises(TypeError):
                mod.vowels_count(None)

    def test_error_int_input(self):
            # Input is an integer instead of a string.
            with self.assertRaises(TypeError):
                mod.vowels_count(123)

