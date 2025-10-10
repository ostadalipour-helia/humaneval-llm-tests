import unittest
from sut_llm.problem_HumanEval_10 import make_palindrome

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        """
        Test with an empty string.
        Edge Case: Empty collection.
        """
        self.assertEqual(make_palindrome(''), '')

    def test_single_character_string(self):
        """
        Test with a single character string.
        Edge Case: Single element collection, already a palindrome.
        Boundary: String length 1.
        """
        self.assertEqual(make_palindrome('a'), 'a')

    def test_already_palindrome(self):
        """
        Test with a string that is already a palindrome.
        Boundary: Entire string is the longest palindromic postfix.
        """
        self.assertEqual(make_palindrome('racecar'), 'racecar')

    def test_simple_case_cat(self):
        """
        Test a typical case where the longest palindromic postfix is just the last character.
        Example from docstring.
        """
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_long_palindromic_suffix_cata(self):
        """
        Test a case where a significant part of the string is the longest palindromic postfix.
        Example from docstring.
        Boundary: Long palindromic suffix.
        Logic Mutation: Catches if it picks a shorter suffix like 'a' instead of 'ata'.
        """
        self.assertEqual(make_palindrome('cata'), 'catac')

    def test_no_obvious_palindromic_suffix(self):
        """
        Test a string where only single characters are palindromic postfixes.
        Extreme Input: Requires reversing almost the entire string.
        """
        self.assertEqual(make_palindrome('abcde'), 'abcdedcba')

    def test_two_chars_not_palindrome(self):
        """
        Test a two-character string that is not a palindrome.
        Boundary: String length 2.
        Off-by-one: Checks correct handling of minimal non-palindromic string.
        """
        self.assertEqual(make_palindrome('ab'), 'aba')

    def test_two_chars_palindrome(self):
        """
        Test a two-character string that is a palindrome.
        Boundary: String length 2, already a palindrome.
        """
        self.assertEqual(make_palindrome('aa'), 'aa')

    def test_complex_suffix_with_prefix_palindrome(self):
        """
        Test a longer string where the prefix is a palindrome, but the longest palindromic suffix is short.
        Extreme Input: Ensures the algorithm correctly identifies the *suffix* and not a prefix.
        Logic Mutation: Catches if it incorrectly considers 'abacaba' as the suffix.
        """
        self.assertEqual(make_palindrome('abacabaX'), 'abacabaXabacaba')

    def test_all_same_characters(self):
        """
        Test a string consisting of all identical characters.
        Edge Case: All same values.
        Boundary: Already a palindrome.
        """
        self.assertEqual(make_palindrome('aaaaa'), 'aaaaa')