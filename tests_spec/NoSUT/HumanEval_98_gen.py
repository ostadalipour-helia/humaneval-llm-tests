import unittest
from sut.problem_HumanEval_98 import count_upper

class Test_count_upper(unittest.TestCase):
    def test_normal_mixed_case_vowel_even_index(self):
        # Normal case: E at index 4 is an uppercase vowel and at an even index.
        self.assertEqual(count_upper("aBCdEf"), 1)

    def test_normal_all_uppercase_vowels_even_indices(self):
        # Normal case: A at index 0, I at index 2, U at index 4 are uppercase vowels at even indices.
        self.assertEqual(count_upper("AEIOU"), 3)

    def test_normal_no_uppercase_vowels(self):
        # Normal case: No uppercase vowels at any index.
        self.assertEqual(count_upper("abcdefg"), 0)

    def test_normal_vowel_even_index_multiple_vowels(self):
        # Normal case: O at index 4 is an uppercase vowel at an even index. E at index 1 is not at an even index.
        self.assertEqual(count_upper("HELLOworld"), 1)

    def test_edge_empty_string(self):
        # Edge case: Empty string contains no characters, so count is 0.
        self.assertEqual(count_upper(""), 0)

    def test_edge_single_uppercase_vowel_even_index(self):
        # Edge case: A at index 0 is an uppercase vowel at an even index.
        self.assertEqual(count_upper("A"), 1)

    def test_edge_uppercase_vowels_only_odd_indices(self):
        # Edge case: Uppercase vowels are only at odd indices (A at 1, I at 3, U at 5).
        self.assertEqual(count_upper("bAeIoU"), 0)

    def test_edge_non_alphabetic_characters(self):
        # Edge case: String contains no alphabetic characters, thus no vowels.
        self.assertEqual(count_upper("123!@#"), 0)

    def test_error_integer_input(self):
        # Error case: Input is not a string.
        with self.assertRaises(TypeError):
            count_upper(123)

    def test_error_none_input(self):
        # Error case: Input is not a string.
        with self.assertRaises(TypeError):
            count_upper(None)

    def test_error_list_input(self):
        # Error case: Input is not a string.
        with self.assertRaises(TypeError):
            count_upper(["A", "B"])