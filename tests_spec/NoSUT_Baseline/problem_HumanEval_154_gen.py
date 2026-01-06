import unittest
import sut.problem_HumanEval_154 as mod

class TestHybrid(unittest.TestCase):
    def test_docstring_example_hello_ell(self):
            # Typical case: 'ell' is a substring of 'hello'.
            self.assertEqual(mod.cycpattern_check("hello", "ell"), True)

    def test_docstring_example_abcd_abd(self):
            # Typical case: 'abd' is not a substring, nor any rotation.
            self.assertEqual(mod.cycpattern_check("abcd", "abd"), False)

    def test_edge_case_empty_strings(self):
            # Edge case: Both strings are empty. An empty string is a substring of itself.
            self.assertEqual(mod.cycpattern_check("", ""), True)

    def test_edge_case_empty_pattern(self):
            # Edge case: Pattern is empty. An empty string is always a substring of any string.
            self.assertEqual(mod.cycpattern_check("abc", ""), True)

    def test_boundary_pattern_longer_than_main(self):
            # Boundary case: Pattern is longer than the main string. Should always be False.
            self.assertEqual(mod.cycpattern_check("abc", "abcd"), False)

    def test_boundary_pattern_same_length_and_rotation(self):
            # Boundary case: Pattern has same length as main string and is a rotation.
            self.assertEqual(mod.cycpattern_check("abc", "bca"), True)

    def test_boundary_pattern_same_length_but_not_rotation(self):
            # Boundary case: Pattern has same length as main string but is not a rotation.
            self.assertEqual(mod.cycpattern_check("abc", "abd"), False)

    def test_logic_mutation_multiple_rotations_one_match(self):
            # Logic mutation: 'nana' rotations are 'nana', 'anan'. 'anan' is in 'banana'.
            # Ensures all rotations are checked and not just the original pattern.
            self.assertEqual(mod.cycpattern_check("banana", "nana"), True)

    def test_extreme_long_strings_no_match(self):
            # Extreme case: Long strings, no match found after checking all rotations.
            self.assertEqual(mod.cycpattern_check("abcdefghijklmnopqrstuvwxyz", "zyxw"), False)

    def test_normal_no_rotation_substring(self):
            # Normal case: Second word is not a substring, nor are its rotations.
            self.assertFalse(mod.cycpattern_check("abcd", "abd"))

    def test_normal_direct_substring(self):
            # Normal case: Second word is a direct substring.
            self.assertTrue(mod.cycpattern_check("hello", "ell"))

    def test_normal_rotation_is_substring(self):
            # Normal case: A rotation of the second word ('aab') is a substring of the first word.
            self.assertTrue(mod.cycpattern_check("abab", "baa"))

    def test_normal_rotation_is_substring_complex(self):
            # Normal case: A rotation of the second word ('imens') is a substring of the first word.
            self.assertTrue(mod.cycpattern_check("himenss", "simen"))

    def test_edge_b_longer_than_a(self):
            # Edge case: Second word is longer than the first word.
            self.assertFalse(mod.cycpattern_check("abc", "abcd"))

    def test_edge_b_is_empty_string(self):
            # Edge case: Second word is an empty string (empty string is a substring of any string).
            self.assertTrue(mod.cycpattern_check("test", ""))

    def test_edge_a_is_empty_string(self):
            # Edge case: First word is an empty string, second word is not empty.
            self.assertFalse(mod.cycpattern_check("", "abc"))

    def test_edge_both_empty_strings(self):
            # Edge case: Both words are empty strings.
            self.assertTrue(mod.cycpattern_check("", ""))

    def test_edge_b_is_rotation_of_a_same_length(self):
            # Edge case: Second word is a rotation of the first word, and they have the same length.
            self.assertTrue(mod.cycpattern_check("abc", "bca"))

    def test_edge_repeating_characters(self):
            # Edge case: Both words consist of repeating characters.
            self.assertTrue(mod.cycpattern_check("aaaaa", "aa"))

    def test_error_first_input_not_string(self):
            # Error case: First input is not a string.
            with self.assertRaises(TypeError):
                mod.cycpattern_check(123, "test")

    def test_error_second_input_not_string(self):
            # Error case: Second input is not a string.
            with self.assertRaises(TypeError):
                mod.cycpattern_check("test", None)

