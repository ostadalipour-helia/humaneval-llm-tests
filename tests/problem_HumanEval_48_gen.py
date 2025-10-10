import unittest
from sut.problem_HumanEval_48 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        # Edge case: Empty string is a palindrome.
        # Covers: Edge case (empty), Boundary (length 0), Off-by-one.
        self.assertEqual(is_palindrome(''), True)

    def test_single_character_string(self):
        # Edge case: Single character string is a palindrome.
        # Covers: Edge case (single element), Boundary (length 1), Off-by-one.
        self.assertEqual(is_palindrome('a'), True)

    def test_two_character_palindrome(self):
        # Boundary case: Two identical characters.
        # Covers: Boundary (length 2), Off-by-one.
        self.assertEqual(is_palindrome('aa'), True)

    def test_simple_odd_length_palindrome(self):
        # Typical case: 'aba' from docstring.
        # Covers: Typical input, Boundary (length 3).
        self.assertEqual(is_palindrome('aba'), True)

    def test_simple_even_length_palindrome(self):
        # Typical case: 'abba'.
        # Covers: Typical input, Boundary (length 4).
        self.assertEqual(is_palindrome('abba'), True)

    def test_non_palindrome_first_last_differ(self):
        # Logic mutation: First and last characters differ.
        # Covers: Logic mutation, Off-by-one (for 3 chars).
        self.assertEqual(is_palindrome('abc'), False)

    def test_non_palindrome_middle_differs(self):
        # Logic mutation: Ends match, but an internal character breaks palindrome.
        # Covers: Logic mutation, Extreme/Unusual input.
        self.assertEqual(is_palindrome('abacabaX'), False)

    def test_all_same_characters_palindrome(self):
        # Edge case: String with all identical characters.
        # Covers: Edge case (all same values), Extreme input, Docstring example.
        self.assertEqual(is_palindrome('aaaaa'), True)

    def test_long_complex_palindrome(self):
        # Extreme case: A longer, more complex palindrome.
        # Covers: Extreme/Unusual input, Exact output verification.
        self.assertEqual(is_palindrome('madamimadam'), True)

    def test_long_complex_non_palindrome_subtle_diff(self):
        # Extreme case: A long string that is almost a palindrome, with a subtle difference.
        # Covers: Extreme/Unusual input, Logic mutation (subtle internal difference).
        self.assertEqual(is_palindrome('madamimadax'), False)