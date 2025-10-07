import unittest
from sut_llm.problem_HumanEval_48 import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_simple_odd_palindrome(self):
        self.assertTrue(is_palindrome('aba'))

    def test_simple_even_palindrome(self):
        self.assertTrue(is_palindrome('abba'))

    def test_longer_odd_palindrome(self):
        self.assertTrue(is_palindrome('madam'))

    def test_longer_even_palindrome(self):
        self.assertTrue(is_palindrome('noon'))

    def test_simple_non_palindrome_odd(self):
        self.assertFalse(is_palindrome('abc'))

    def test_simple_non_palindrome_even(self):
        self.assertFalse(is_palindrome('abcd'))

    def test_docstring_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

    def test_another_non_palindrome(self):
        self.assertFalse(is_palindrome('python'))

if __name__ == '__main__':
    unittest.main()