import unittest
from sut.problem_HumanEval_16 import count_distinct_characters

class TestCountDistinctCharacters(unittest.TestCase):

    def test_empty_string(self):
        """
        Test with an empty string.
        Expected: 0 distinct characters.
        Covers: Edge case (empty collection), boundary (minimum input).
        """
        self.assertEqual(count_distinct_characters(""), 0)

    def test_single_lowercase_character(self):
        """
        Test with a string containing a single lowercase character.
        Expected: 1 distinct character.
        Covers: Edge case (single element collection), boundary (smallest non-zero output).
        """
        self.assertEqual(count_distinct_characters("a"), 1)

    def test_single_uppercase_character(self):
        """
        Test with a string containing a single uppercase character.
        Expected: 1 distinct character.
        Covers: Edge case (single element collection), verifies case insensitivity for single char.
        """
        self.assertEqual(count_distinct_characters("Z"), 1)

    def test_two_characters_same_but_different_case(self):
        """
        Test with two characters that are the same but differ in case.
        Expected: 1 distinct character.
        Covers: Critical boundary for case insensitivity, logic mutation (e.g., if 'a' and 'A' were counted separately).
        """
        self.assertEqual(count_distinct_characters("aA"), 1)

    def test_two_distinct_characters_different_case(self):
        """
        Test with two distinct characters, one lowercase, one uppercase.
        Expected: 2 distinct characters.
        Covers: Boundary, basic counting, verifies case insensitivity doesn't merge truly distinct chars.
        """
        self.assertEqual(count_distinct_characters("aB"), 2)

    def test_docstring_example_xyzXYZ(self):
        """
        Test with the first example from the docstring.
        Expected: 3 distinct characters.
        Covers: Typical input, verifies case insensitivity for multiple characters.
        """
        self.assertEqual(count_distinct_characters("xyzXYZ"), 3)

    def test_docstring_example_jerry(self):
        """
        Test with the second example from the docstring.
        Expected: 4 distinct characters (J, e, r, y).
        Covers: Typical input, handles repeated characters and mixed case.
        """
        self.assertEqual(count_distinct_characters("Jerry"), 4)

    def test_all_same_character_mixed_case(self):
        """
        Test with a string consisting of many repetitions of the same character, mixed case.
        Expected: 1 distinct character.
        Covers: Edge case (all same values), extreme input, robust case insensitivity.
        """
        self.assertEqual(count_distinct_characters("AAAAAaaaaa"), 1)

    def test_all_lowercase_alphabet(self):
        """
        Test with the entire lowercase alphabet.
        Expected: 26 distinct characters.
        Covers: Extreme input (maximum distinct characters for alphabet), boundary.
        """
        self.assertEqual(count_distinct_characters("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_full_alphabet_mixed_case_with_duplicates(self):
        """
        Test with a string containing all letters of the alphabet, mixed case, with duplicates.
        Expected: 26 distinct characters.
        Covers: Extreme input, comprehensive test for case insensitivity and duplicate handling.
        """
        self.assertEqual(count_distinct_characters("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"), 26)

if __name__ == '__main__':
    unittest.main()