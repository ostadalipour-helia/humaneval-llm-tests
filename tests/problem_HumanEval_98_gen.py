import unittest
from sut.problem_HumanEval_98 import count_upper

class TestCountUpper(unittest.TestCase):

    def test_empty_string(self):
        """
        Test with an empty string.
        Covers: Edge case (empty collection), boundary (loop start).
        """
        self.assertEqual(count_upper(""), 0)

    def test_single_uppercase_vowel_at_even_index(self):
        """
        Test with a single uppercase vowel at index 0.
        Covers: Edge case (single element), boundary (index 0, uppercase, vowel).
        """
        self.assertEqual(count_upper("A"), 1)

    def test_single_lowercase_vowel_at_even_index(self):
        """
        Test with a single lowercase vowel at index 0.
        Covers: Edge case (single element), logic mutation (is_upper check).
        """
        self.assertEqual(count_upper("e"), 0)

    def test_single_uppercase_consonant_at_even_index(self):
        """
        Test with a single uppercase consonant at index 0.
        Covers: Edge case (single element), logic mutation (is_vowel check).
        """
        self.assertEqual(count_upper("B"), 0)

    def test_docstring_example_1(self):
        """
        Test with the first example from the docstring.
        Covers: Typical input, mixed case, mixed vowels/consonants, even/odd indices.
        """
        self.assertEqual(count_upper('aBCdEf'), 1) # E at index 4

    def test_docstring_example_2(self):
        """
        Test with the second example from the docstring.
        Covers: Typical input, all lowercase, zero count.
        """
        self.assertEqual(count_upper('abcdefg'), 0)

    def test_docstring_example_3(self):
        """
        Test with the third example from the docstring.
        Covers: Typical input, mixed case, mixed vowels/consonants, zero count.
        """
        self.assertEqual(count_upper('dBBE'), 0) # B at index 2 is consonant, E at index 3 is odd

    def test_multiple_uppercase_vowels_mixed_indices(self):
        """
        Test with multiple uppercase vowels, some at even, some at odd indices.
        Covers: Boundary (all vowels A, E, I, O, U), off-by-one (index check), logic mutations.
        """
        self.assertEqual(count_upper('AEIOUaeiouAEIOU'), 5) # A@0, I@4, U@8, A@10, I@14

    def test_uppercase_vowels_only_at_odd_indices(self):
        """
        Test with uppercase vowels present only at odd indices.
        Covers: Extreme/unusual input, ensures index parity check is robust.
        """
        self.assertEqual(count_upper('xAyEzIwOu'), 0) # A@1, E@3, I@5, O@7, U@9 are all odd

    def test_long_string_no_matches(self):
        """
        Test a long string with no uppercase vowels at even indices (all consonants).
        Covers: Extreme/unusual input, ensures no false positives.
        """
        self.assertEqual(count_upper('BCDFGHJKLMNPQRSTVWXYZ'), 0)