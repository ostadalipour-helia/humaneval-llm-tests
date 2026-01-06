import unittest
import sut.problem_HumanEval_118 as mod

class TestHybrid(unittest.TestCase):
    def test_typical_case_rightmost_vowel(self):
            # Test case from example, verifies basic functionality and right-to-left search.
            self.assertEqual(mod.get_closest_vowel("yogurt"), "u")

    def test_uppercase_vowel_and_consonants(self):
            # Test case from example, verifies handling of uppercase letters.
            self.assertEqual(mod.get_closest_vowel("FULL"), "U")

    def test_no_vowels_in_word(self):
            # Edge case: word contains no vowels.
            self.assertEqual(mod.get_closest_vowel("rhythm"), "")

    def test_all_vowels_no_consonants(self):
            # Edge case: word consists entirely of vowels, so no vowel can be between two consonants.
            self.assertEqual(mod.get_closest_vowel("aeiou"), "")

    def test_minimal_valid_string(self):
            # Boundary case: shortest possible string (length 3) that can satisfy the condition.
            self.assertEqual(mod.get_closest_vowel("bab"), "a")

    def test_vowels_at_boundaries_no_middle_match(self):
            # Boundary case: vowels at start/end, but no vowel in the middle meets the criteria.
            # 'a' and 'e' are at boundaries. 'p', 'p', 'l' are consonants.
            # No vowel is between two consonants.
            self.assertEqual(mod.get_closest_vowel("apple"), "")

    def test_multiple_potential_vowels_rightmost_wins(self):
            # Off-by-one/Logic mutation: Tests that the *closest from the right* vowel is returned.
            # 'e' is between 'r' and 'n' (both consonants).
            self.assertEqual(mod.get_closest_vowel("strength"), "e")

    def test_vowel_between_consonant_and_vowel(self):
            # Logic mutation: Tests the strict "between two consonants" condition.
            # 'u' is between 'q' (consonant) and 'i' (vowel) - invalid.
            # 'i' is between 'u' (vowel) and 'c' (consonant) - invalid.
            self.assertEqual(mod.get_closest_vowel("quick"), "")

    def test_short_string_length_one(self):
            # Edge case: string length 1, cannot have a vowel between two consonants.
            self.assertEqual(mod.get_closest_vowel("x"), "")

    def test_short_string_length_two(self):
            # Edge case: string length 2, cannot have a vowel between two consonants.
            self.assertEqual(mod.get_closest_vowel("xy"), "")

    def test_normal_yogurt(self):
            # Typical case with a vowel between two consonants.
            self.assertEqual(mod.get_closest_vowel("yogurt"), "u")

    def test_normal_full_uppercase(self):
            # Typical case with an uppercase vowel between two consonants.
            self.assertEqual(mod.get_closest_vowel("FULL"), "U")

    def test_normal_rightmost_vowel(self):
            # Multiple valid vowels, returns the rightmost one.
            self.assertEqual(mod.get_closest_vowel("zzzaUzzzzAzzzz"), "A")

    def test_edge_no_vowel_between_consonants(self):
            # Vowels are present but not between two consonants.
            self.assertEqual(mod.get_closest_vowel("quick"), "")

    def test_edge_vowel_at_beginning(self):
            # Vowel at the beginning, not counted.
            self.assertEqual(mod.get_closest_vowel("ab"), "")

    def test_edge_vowel_at_end(self):
            # Vowel at the end, not counted.
            self.assertEqual(mod.get_closest_vowel("apple"), "")

    def test_edge_empty_string(self):
            # Empty string input.
            self.assertEqual(mod.get_closest_vowel(""), "")

    def test_edge_all_vowels(self):
            # String composed entirely of vowels.
            self.assertEqual(mod.get_closest_vowel("aeiou"), "")

    def test_edge_no_vowels_at_all(self):
            # String with no vowels.
            self.assertEqual(mod.get_closest_vowel("rhythm"), "")

    def test_error_non_string_int(self):
            # Input 'word' is not a string (integer).
            with self.assertRaises(TypeError):
                mod.get_closest_vowel(123)

