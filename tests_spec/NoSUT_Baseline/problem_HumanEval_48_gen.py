import unittest
import sut.problem_HumanEval_48 as mod

class TestHybrid(unittest.TestCase):
    def test_empty_string(self):
            # Edge case: Empty string is a palindrome.
            # Covers: Edge case (empty), Boundary (length 0), Off-by-one.
            self.assertEqual(mod.is_palindrome(''), True)

    def test_single_character_string(self):
            # Edge case: Single character string is a palindrome.
            # Covers: Edge case (single element), Boundary (length 1), Off-by-one.
            self.assertEqual(mod.is_palindrome('a'), True)

    def test_two_character_palindrome(self):
            # Boundary case: Two identical characters.
            # Covers: Boundary (length 2), Off-by-one.
            self.assertEqual(mod.is_palindrome('aa'), True)

    def test_simple_odd_length_palindrome(self):
            # Typical case: 'aba' from docstring.
            # Covers: Typical input, Boundary (length 3).
            self.assertEqual(mod.is_palindrome('aba'), True)

    def test_simple_even_length_palindrome(self):
            # Typical case: 'abba'.
            # Covers: Typical input, Boundary (length 4).
            self.assertEqual(mod.is_palindrome('abba'), True)

    def test_non_palindrome_first_last_differ(self):
            # Logic mutation: First and last characters differ.
            # Covers: Logic mutation, Off-by-one (for 3 chars).
            self.assertEqual(mod.is_palindrome('abc'), False)

    def test_non_palindrome_middle_differs(self):
            # Logic mutation: Ends match, but an internal character breaks palindrome.
            # Covers: Logic mutation, Extreme/Unusual input.
            self.assertEqual(mod.is_palindrome('abacabaX'), False)

    def test_all_same_characters_palindrome(self):
            # Edge case: String with all identical characters.
            # Covers: Edge case (all same values), Extreme input, Docstring example.
            self.assertEqual(mod.is_palindrome('aaaaa'), True)

    def test_long_complex_palindrome(self):
            # Extreme case: A longer, more complex palindrome.
            # Covers: Extreme/Unusual input, Exact output verification.
            self.assertEqual(mod.is_palindrome('madamimadam'), True)

    def test_long_complex_non_palindrome_subtle_diff(self):
            # Extreme case: A long string that is almost a palindrome, with a subtle difference.
            # Covers: Extreme/Unusual input, Logic mutation (subtle internal difference).
            self.assertEqual(mod.is_palindrome('madamimadax'), False)

    def test_normal_odd_length_palindrome(self):
            # A typical palindrome string.
            self.assertTrue(mod.is_palindrome("aba"))

    def test_normal_repeating_chars_palindrome(self):
            # A palindrome string with repeating characters.
            self.assertTrue(mod.is_palindrome("aaaaa"))

    def test_normal_non_palindrome(self):
            # A typical non-palindrome string.
            self.assertFalse(mod.is_palindrome("zbcd"))

    def test_normal_common_palindrome(self):
            # Another common palindrome example.
            self.assertTrue(mod.is_palindrome("racecar"))

    def test_normal_common_non_palindrome(self):
            # Another common non-palindrome example.
            self.assertFalse(mod.is_palindrome("hello"))

    def test_edge_empty_string(self):
            # An empty string is considered a palindrome.
            self.assertTrue(mod.is_palindrome(""))

    def test_edge_single_character(self):
            # A single-character string is considered a palindrome.
            self.assertTrue(mod.is_palindrome("a"))

    def test_edge_two_char_palindrome(self):
            # A two-character palindrome string.
            self.assertTrue(mod.is_palindrome("aa"))

    def test_edge_two_char_non_palindrome(self):
            # A two-character non-palindrome string.
            self.assertFalse(mod.is_palindrome("ab"))

    def test_edge_case_sensitive_non_palindrome(self):
            # A string that would be a palindrome if case-insensitive, but is not due to case-sensitivity.
            self.assertFalse(mod.is_palindrome("Madam"))

    def test_error_int_input(self):
            # Input is an integer instead of a string.
            with self.assertRaises(TypeError):
                mod.is_palindrome(123)

    def test_error_none_input(self):
            # Input is None instead of a string.
            with self.assertRaises(TypeError):
                mod.is_palindrome(None)

