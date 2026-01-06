import unittest
import sut.problem_HumanEval_16 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            """
            Test with an empty string.
            Expected: 0 distinct characters.
            Covers: Edge case (empty collection), boundary (minimum input).
            """
            self.assertEqual(mod.count_distinct_characters(""), 0)

    def test_single_lowercase_character(self):
            """
            Test with a string containing a single lowercase character.
            Expected: 1 distinct character.
            Covers: Edge case (single element collection), boundary (smallest non-zero output).
            """
            self.assertEqual(mod.count_distinct_characters("a"), 1)

    def test_single_uppercase_character(self):
            """
            Test with a string containing a single uppercase character.
            Expected: 1 distinct character.
            Covers: Edge case (single element collection), verifies case insensitivity for single char.
            """
            self.assertEqual(mod.count_distinct_characters("Z"), 1)

    def test_two_characters_same_but_different_case(self):
            """
            Test with two characters that are the same but differ in case.
            Expected: 1 distinct character.
            Covers: Critical boundary for case insensitivity, logic mutation (e.g., if 'a' and 'A' were counted separately).
            """
            self.assertEqual(mod.count_distinct_characters("aA"), 1)

    def test_two_distinct_characters_different_case(self):
            """
            Test with two distinct characters, one lowercase, one uppercase.
            Expected: 2 distinct characters.
            Covers: Boundary, basic counting, verifies case insensitivity doesn't merge truly distinct chars.
            """
            self.assertEqual(mod.count_distinct_characters("aB"), 2)

    def test_docstring_example_xyzXYZ(self):
            """
            Test with the first example from the docstring.
            Expected: 3 distinct characters.
            Covers: Typical input, verifies case insensitivity for multiple characters.
            """
            self.assertEqual(mod.count_distinct_characters("xyzXYZ"), 3)

    def test_docstring_example_jerry(self):
            """
            Test with the second example from the docstring.
            Expected: 4 distinct characters (J, e, r, y).
            Covers: Typical input, handles repeated characters and mixed case.
            """
            self.assertEqual(mod.count_distinct_characters("Jerry"), 4)

    def test_all_same_character_mixed_case(self):
            """
            Test with a string consisting of many repetitions of the same character, mixed case.
            Expected: 1 distinct character.
            Covers: Edge case (all same values), extreme input, robust case insensitivity.
            """
            self.assertEqual(mod.count_distinct_characters("AAAAAaaaaa"), 1)

    def test_all_lowercase_alphabet(self):
            """
            Test with the entire lowercase alphabet.
            Expected: 26 distinct characters.
            Covers: Extreme input (maximum distinct characters for alphabet), boundary.
            """
            self.assertEqual(mod.count_distinct_characters("abcdefghijklmnopqrstuvwxyz"), 26)

    def test_full_alphabet_mixed_case_with_duplicates(self):
            """
            Test with a string containing all letters of the alphabet, mixed case, with duplicates.
            Expected: 26 distinct characters.
            Covers: Extreme input, comprehensive test for case insensitivity and duplicate handling.
            """
            self.assertEqual(mod.count_distinct_characters("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"), 26)
    
    if __name__ == '__main__':
        unittest.main()

    def test_normal_mixed_case_distinct(self):
            """
            String with mixed case characters that are distinct when case is ignored.
            Input: "xyzXYZ", Expected Output: 3
            """
            self.assertEqual(mod.count_distinct_characters("xyzXYZ"), 3)

    def test_normal_repeated_mixed_case(self):
            """
            String with some repeated characters and mixed case.
            Input: "Jerry", Expected Output: 4
            """
            self.assertEqual(mod.count_distinct_characters("Jerry"), 4)

    def test_normal_sentence_with_space(self):
            """
            String with spaces and common words, testing case-insensitivity and character set.
            Input: "Hello World", Expected Output: 8
            """
            self.assertEqual(mod.count_distinct_characters("Hello World"), 8)

    def test_edge_empty_string(self):
            """
            Empty string should have zero distinct characters.
            Input: "", Expected Output: 0
            """
            self.assertEqual(mod.count_distinct_characters(""), 0)

    def test_edge_all_same_case_insensitive(self):
            """
            String with all characters being the same, regardless of case.
            Input: "aaaaaA", Expected Output: 1
            """
            self.assertEqual(mod.count_distinct_characters("aaaaaA"), 1)

    def test_edge_single_character(self):
            """
            String with a single character.
            Input: "a", Expected Output: 1
            """
            self.assertEqual(mod.count_distinct_characters("a"), 1)

    def test_edge_non_alphabetic_characters(self):
            """
            String with only non-alphabetic characters.
            Input: "123!@#", Expected Output: 6
            """
            self.assertEqual(mod.count_distinct_characters("123!@#"), 6)

    def test_edge_pairs_different_case(self):
            """
            String with pairs of same characters in different cases.
            Input: "AaBbCc", Expected Output: 3
            """
            self.assertEqual(mod.count_distinct_characters("AaBbCc"), 3)

