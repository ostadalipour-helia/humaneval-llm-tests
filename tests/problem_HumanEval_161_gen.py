import unittest
from sut.problem_HumanEval_161 import solve

class TestSolveFunction(unittest.TestCase):

    def test_empty_string(self):
        # Edge Case: Empty string. Should return an empty string.
        # Covers: Boundary (0 length), Edge Case (empty).
        self.assertEqual(solve(""), "")

    def test_only_non_letters(self):
        # Boundary Case: String contains only non-letters. Should be fully reversed.
        # Covers: Logic Mutation (triggers "no letters" path), Boundary (all non-letters).
        self.assertEqual(solve("1234"), "4321")

    def test_single_letter(self):
        # Edge Case: Single letter string. Should reverse its case.
        # Covers: Boundary (1 length), Edge Case (single element), Logic Mutation (triggers "has letters" path).
        self.assertEqual(solve("a"), "A")

    def test_single_non_letter(self):
        # Edge Case: Single non-letter string. Should remain unchanged.
        # Covers: Boundary (1 length), Edge Case (single element), Logic Mutation (triggers "no letters" path, but reversal of 1 char is itself).
        self.assertEqual(solve("#"), "#")

    def test_all_letters_mixed_case(self):
        # Typical Input: String with all letters, mixed case. All cases should be reversed.
        # Covers: Typical Input, Return Value (computed value path).
        self.assertEqual(solve("abCdeF"), "ABcDEf")

    def test_mixed_letters_and_non_letters(self):
        # Typical Input: String with mixed letters and non-letters. Only letters' cases should be reversed.
        # Covers: Typical Input, Return Value (computed value path), Logic Mutation (both conditions present).
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_all_uppercase_letters(self):
        # Logic Mutation: String with all uppercase letters. Should become all lowercase.
        # Covers: Off-by-One (all same case), Logic Mutation (case reversal logic).
        self.assertEqual(solve("HELLO"), "hello")

    def test_all_lowercase_letters(self):
        # Logic Mutation: String with all lowercase letters. Should become all uppercase.
        # Covers: Off-by-One (all same case), Logic Mutation (case reversal logic).
        self.assertEqual(solve("world"), "WORLD")

    def test_only_spaces(self):
        # Extreme/Unusual Input: String with only spaces. Spaces are not letters, so string should be reversed.
        # Covers: Extreme Input, Boundary (all non-letters, specific type), Logic Mutation (triggers "no letters" path).
        self.assertEqual(solve("   "), "   ")

    def test_long_mixed_string(self):
        # Extreme/Unusual Input: A longer string with a complex mix of letters and non-letters.
        # Covers: Extreme Input (length), Return Value (computed value path).
        self.assertEqual(solve("PyTh0n_Pr0gr@mminG_123"), "pYtH0N_pR0GR@MMINg_123")

if __name__ == '__main__':
    unittest.main()