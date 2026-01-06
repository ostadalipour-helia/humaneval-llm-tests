import unittest
import sut.problem_HumanEval_161 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            # Edge Case: Empty string. Should return an empty string.
            # Covers: Boundary (0 length), Edge Case (empty).
            self.assertEqual(mod.solve(""), "")

    def test_only_non_letters(self):
            # Boundary Case: String contains only non-letters. Should be fully reversed.
            # Covers: Logic Mutation (triggers "no letters" path), Boundary (all non-letters).
            self.assertEqual(mod.solve("1234"), "4321")

    def test_single_letter(self):
            # Edge Case: Single letter string. Should reverse its case.
            # Covers: Boundary (1 length), Edge Case (single element), Logic Mutation (triggers "has letters" path).
            self.assertEqual(mod.solve("a"), "A")

    def test_single_non_letter(self):
            # Edge Case: Single non-letter string. Should remain unchanged.
            # Covers: Boundary (1 length), Edge Case (single element), Logic Mutation (triggers "no letters" path, but reversal of 1 char is itself).
            self.assertEqual(mod.solve("#"), "#")

    def test_all_letters_mixed_case(self):
            # Typical Input: String with all letters, mixed case. All cases should be reversed.
            # Covers: Typical Input, Return Value (computed value path).
            self.assertEqual(mod.solve("abCdeF"), "ABcDEf")

    def test_mixed_letters_and_non_letters(self):
            # Typical Input: String with mixed letters and non-letters. Only letters' cases should be reversed.
            # Covers: Typical Input, Return Value (computed value path), Logic Mutation (both conditions present).
            self.assertEqual(mod.solve("#a@C"), "#A@c")

    def test_all_uppercase_letters(self):
            # Logic Mutation: String with all uppercase letters. Should become all lowercase.
            # Covers: Off-by-One (all same case), Logic Mutation (case reversal logic).
            self.assertEqual(mod.solve("HELLO"), "hello")

    def test_all_lowercase_letters(self):
            # Logic Mutation: String with all lowercase letters. Should become all uppercase.
            # Covers: Off-by-One (all same case), Logic Mutation (case reversal logic).
            self.assertEqual(mod.solve("world"), "WORLD")

    def test_only_spaces(self):
            # Extreme/Unusual Input: String with only spaces. Spaces are not letters, so string should be reversed.
            # Covers: Extreme Input, Boundary (all non-letters, specific type), Logic Mutation (triggers "no letters" path).
            self.assertEqual(mod.solve("   "), "   ")

    def test_long_mixed_string(self):
            # Extreme/Unusual Input: A longer string with a complex mix of letters and non-letters.
            # Covers: Extreme Input (length), Return Value (computed value path).
            self.assertEqual(mod.solve("PyTh0n_Pr0gr@mminG_123"), "pYtH0N_pR0GR@MMINg_123")
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_all_lowercase(self):
            # Description: String with all lowercase letters, all cases reversed.
            s = "ab"
            expected_output = "AB"
            self.assertEqual(mod.solve(s), expected_output)

    def test_normal_mixed_letters_non_letters(self):
            # Description: String with mixed letters and non-letters, cases reversed for letters.
            s = "#a@C"
            expected_output = "#A@c"
            self.assertEqual(mod.solve(s), expected_output)

    def test_normal_hello_world(self):
            # Description: String with mixed case letters, spaces, and punctuation.
            s = "Hello World!"
            expected_output = "hELLO wORLD!"
            self.assertEqual(mod.solve(s), expected_output)

    def test_edge_no_letters_reversed(self):
            # Description: String containing no letters, should be entirely reversed.
            s = "1234"
            expected_output = "4321"
            self.assertEqual(mod.solve(s), expected_output)

    def test_edge_empty_string(self):
            # Description: Empty string, contains no letters, reversed is itself.
            s = ""
            expected_output = ""
            self.assertEqual(mod.solve(s), expected_output)

    def test_edge_single_uppercase_letter(self):
            # Description: Single uppercase letter.
            s = "A"
            expected_output = "a"
            self.assertEqual(mod.solve(s), expected_output)

    def test_edge_single_lowercase_letter(self):
            # Description: Single lowercase letter.
            s = "z"
            expected_output = "Z"
            self.assertEqual(mod.solve(s), expected_output)

    def test_edge_single_non_letter(self):
            # Description: Single non-letter character, contains no letters, reversed is itself.
            s = "!"
            expected_output = "!"
            self.assertEqual(mod.solve(s), expected_output)

    def test_edge_mixed_case_and_spaces(self):
            # Description: String with mixed case letters and spaces.
            s = "aB cD"
            expected_output = "Ab Cd"
            self.assertEqual(mod.solve(s), expected_output)

    def test_error_input_none(self):
            # Description: Input `s` is not a string (e.g., None).
            with self.assertRaises((TypeError, AttributeError)):
                mod.solve(None)

    def test_error_input_integer(self):
            # Description: Input `s` is not a string (e.g., integer).
            with self.assertRaises((TypeError, AttributeError)):
                mod.solve(123)

