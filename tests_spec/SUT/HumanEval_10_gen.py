import unittest
from sut.problem_HumanEval_10 import make_palindrome

class Test_make_palindrome(unittest.TestCase):

    def test_normal_case_cat(self):
        self.assertEqual(make_palindrome("cat"), 'catac')

    def test_normal_case_race(self):
        self.assertEqual(make_palindrome("race"), 'racecar')

    def test_normal_case_google(self):
        self.assertEqual(make_palindrome("google"), 'googlelgoog')

    def test_normal_case_cata(self):
        self.assertEqual(make_palindrome("cata"), 'catac')

    def test_edge_case_empty(self):
        self.assertEqual(make_palindrome(""), '')

    def test_edge_case_single_char(self):
        self.assertEqual(make_palindrome("a"), 'a')

    def test_edge_case_already_palindrome(self):
        self.assertEqual(make_palindrome("aba"), 'aba')

    def test_edge_case_two_chars(self):
        self.assertEqual(make_palindrome("ab"), 'aba')

    def test_already_palindrome_again(self):
        self.assertEqual(make_palindrome("aba"), 'aba')

    def test_two_chars_again(self):
        self.assertEqual(make_palindrome("ab"), 'aba')

if __name__ == '__main__':
    unittest.main()