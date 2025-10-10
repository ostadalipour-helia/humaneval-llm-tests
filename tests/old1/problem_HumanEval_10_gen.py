import unittest
from sut.problem_HumanEval_10 import make_palindrome

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_character(self):
        self.assertEqual(make_palindrome('a'), 'a')

    def test_two_characters_not_palindrome(self):
        self.assertEqual(make_palindrome('ab'), 'aba')

    def test_two_characters_already_palindrome(self):
        self.assertEqual(make_palindrome('aa'), 'aa')

    def test_docstring_example_cat(self):
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_docstring_example_cata(self):
        self.assertEqual(make_palindrome('cata'), 'catac')

    def test_three_characters_not_palindrome(self):
        self.assertEqual(make_palindrome('abc'), 'abcba')

    def test_longer_string_simple_suffix(self):
        self.assertEqual(make_palindrome('race'), 'racecar')

    def test_longer_string_with_internal_palindrome_suffix(self):
        self.assertEqual(make_palindrome('banana'), 'bananab')

    def test_longer_string_no_internal_palindrome_suffix(self):
        self.assertEqual(make_palindrome('topcoder'), 'topcoderredocpot')

if __name__ == '__main__':
    unittest.main()