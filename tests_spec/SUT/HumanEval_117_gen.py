import unittest
from sut.problem_HumanEval_117 import select_words

class Test_select_words(unittest.TestCase):

    def test_one_matching_word(self):
        s = "Mary had a little lamb"
        n = 4
        expected = ['little']
        self.assertEqual(select_words(s, n), expected)

    def test_multiple_matching_words(self):
        s = "Mary had a little lamb"
        n = 3
        expected = ['Mary', 'lamb']
        self.assertEqual(select_words(s, n), expected)

    def test_common_word(self):
        s = "Hello world"
        n = 4
        expected = ['world']
        self.assertEqual(select_words(s, n), expected)

    def test_capitalized_word(self):
        s = "Uncle sam"
        n = 3
        expected = ['Uncle']
        self.assertEqual(select_words(s, n), expected)

    def test_empty_string_n_zero(self):
        s = ""
        n = 0
        expected = []
        self.assertEqual(select_words(s, n), expected)

    def test_empty_string_n_non_zero(self):
        s = ""
        n = 5
        expected = []
        self.assertEqual(select_words(s, n), expected)

    def test_no_words_match(self):
        s = "simple white space"
        n = 2
        expected = []
        self.assertEqual(select_words(s, n), expected)

    def test_only_vowels_n_is_zero(self):
        s = "a e i o u"
        n = 0
        expected = ['a', 'e', 'i', 'o', 'u']
        self.assertEqual(select_words(s, n), expected)

    def test_only_consonants_match(self):
        s = "rhythm"
        n = 6
        expected = ['rhythm']
        self.assertEqual(select_words(s, n), expected)

    def test_string_with_only_spaces(self):
        s = "   "
        n = 1
        expected = []
        self.assertEqual(select_words(s, n), expected)