import unittest
from sut.problem_HumanEval_10 import make_palindrome

class Test_make_palindrome(unittest.TestCase):
    def test_normal_cat(self):
        self.assertEqual(make_palindrome("cat"), "catac")

    def test_normal_race(self):
        self.assertEqual(make_palindrome("race"), "racecar")

    def test_normal_google(self):
        self.assertEqual(make_palindrome("google"), "googleelgoog")

    def test_normal_cata(self):
        self.assertEqual(make_palindrome("cata"), "catatac")

    def test_edge_empty_string(self):
        self.assertEqual(make_palindrome(""), "")

    def test_edge_single_char(self):
        self.assertEqual(make_palindrome("a"), "a")

    def test_edge_already_palindrome(self):
        self.assertEqual(make_palindrome("aba"), "aba")

    def test_edge_two_chars(self):
        self.assertEqual(make_palindrome("ab"), "aba")

    def test_error_none_input(self):
        with self.assertRaises(TypeError):
            make_palindrome(None)

    def test_error_integer_input(self):
        with self.assertRaises(TypeError):
            make_palindrome(123)

    def test_error_list_input(self):
        with self.assertRaises(TypeError):
            make_palindrome(["a", "b"])