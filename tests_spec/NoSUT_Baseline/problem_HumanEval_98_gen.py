import unittest
import sut.problem_HumanEval_98 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            """
            Test with an empty string.
            Covers: Edge case (empty collection), boundary (loop start).
            """
            self.assertEqual(mod.count_upper(""), 0)

    def test_single_uppercase_vowel_at_even_index(self):
            """
            Test with a single uppercase vowel at index 0.
            Covers: Edge case (single element), boundary (index 0, uppercase, vowel).
            """
            self.assertEqual(mod.count_upper("A"), 1)

    def test_single_lowercase_vowel_at_even_index(self):
            """
            Test with a single lowercase vowel at index 0.
            Covers: Edge case (single element), logic mutation (is_upper check).
            """
            self.assertEqual(mod.count_upper("e"), 0)

    def test_single_uppercase_consonant_at_even_index(self):
            """
            Test with a single uppercase consonant at index 0.
            Covers: Edge case (single element), logic mutation (is_vowel check).
            """
            self.assertEqual(mod.count_upper("B"), 0)

    def test_docstring_example_1(self):
            """
            Test with the first example from the docstring.
            Covers: Typical input, mixed case, mixed vowels/consonants, even/odd indices.
            """
            self.assertEqual(mod.count_upper('aBCdEf'), 1) # E at index 4

    def test_docstring_example_2(self):
            """
            Test with the second example from the docstring.
            Covers: Typical input, all lowercase, zero count.
            """
            self.assertEqual(mod.count_upper('abcdefg'), 0)

    def test_docstring_example_3(self):
            """
            Test with the third example from the docstring.
            Covers: Typical input, mixed case, mixed vowels/consonants, zero count.
            """
            self.assertEqual(mod.count_upper('dBBE'), 0) # B at index 2 is consonant, E at index 3 is odd

    def test_uppercase_vowels_only_at_odd_indices(self):
            """
            Test with uppercase vowels present only at odd indices.
            Covers: Extreme/unusual input, ensures index parity check is robust.
            """
            self.assertEqual(mod.count_upper('xAyEzIwOu'), 0) # A@1, E@3, I@5, O@7, U@9 are all odd

    def test_long_string_no_matches(self):
            """
            Test a long string with no uppercase vowels at even indices (all consonants).
            Covers: Extreme/unusual input, ensures no false positives.
            """
            self.assertEqual(mod.count_upper('BCDFGHJKLMNPQRSTVWXYZ'), 0)

    def test_normal_mixed_case_vowel_even_index(self):
            # Normal case: E at index 4 is an uppercase vowel and at an even index.
            self.assertEqual(mod.count_upper("aBCdEf"), 1)

    def test_normal_all_uppercase_vowels_even_indices(self):
            # Normal case: A at index 0, I at index 2, U at index 4 are uppercase vowels at even indices.
            self.assertEqual(mod.count_upper("AEIOU"), 3)

    def test_normal_no_uppercase_vowels(self):
            # Normal case: No uppercase vowels at any index.
            self.assertEqual(mod.count_upper("abcdefg"), 0)

    def test_normal_vowel_even_index_multiple_vowels(self):
            # Normal case: O at index 4 is an uppercase vowel at an even index. E at index 1 is not at an even index.
            self.assertEqual(mod.count_upper("HELLOworld"), 1)

    def test_edge_empty_string(self):
            # Edge case: Empty string contains no characters, so count is 0.
            self.assertEqual(mod.count_upper(""), 0)

    def test_edge_single_uppercase_vowel_even_index(self):
            # Edge case: A at index 0 is an uppercase vowel at an even index.
            self.assertEqual(mod.count_upper("A"), 1)

    def test_edge_uppercase_vowels_only_odd_indices(self):
            # Edge case: Uppercase vowels are only at odd indices (A at 1, I at 3, U at 5).
            self.assertEqual(mod.count_upper("bAeIoU"), 0)

    def test_edge_non_alphabetic_characters(self):
            # Edge case: String contains no alphabetic characters, thus no vowels.
            self.assertEqual(mod.count_upper("123!@#"), 0)

    def test_error_integer_input(self):
            # Error case: Input is not a string.
            with self.assertRaises(TypeError):
                mod.count_upper(123)

    def test_error_none_input(self):
            # Error case: Input is not a string.
            with self.assertRaises(TypeError):
                mod.count_upper(None)

