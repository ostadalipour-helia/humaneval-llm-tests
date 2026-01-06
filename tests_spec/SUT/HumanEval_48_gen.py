import unittest
from sut.problem_HumanEval_48 import is_palindrome

class Test_is_palindrome(unittest.TestCase):

    def test_aba(self):
        self.assertEqual(is_palindrome("aba"), True)

    def test_aaaaa(self):
        self.assertEqual(is_palindrome("aaaaa"), True)

    def test_zbcd(self):
        self.assertEqual(is_palindrome("zbcd"), False)

    def test_racecar(self):
        self.assertEqual(is_palindrome("racecar"), True)

    def test_hello(self):
        self.assertEqual(is_palindrome("hello"), False)

    def test_empty_string(self):
        self.assertEqual(is_palindrome(""), True)

    def test_single_character(self):
        self.assertEqual(is_palindrome("a"), True)

    def test_two_char_palindrome(self):
        self.assertEqual(is_palindrome("aa"), True)

    def test_two_char_non_palindrome(self):
        self.assertEqual(is_palindrome("ab"), False)

    def test_case_sensitive(self):
        self.assertEqual(is_palindrome("Madam"), False)

if __name__ == '__main__':
    unittest.main()