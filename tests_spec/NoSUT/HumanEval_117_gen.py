import unittest
from sut.problem_HumanEval_117 import select_words

class Test_select_words(unittest.TestCase):

    def test_normal_one_matching_word(self):
        # Standard case with one matching word.
        s = "Mary had a little lamb"
        n = 4
        expected_output = ["little"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_normal_multiple_matching_words(self):
        # Standard case with multiple matching words.
        s = "Mary had a little lamb"
        n = 3
        expected_output = ["Mary", "lamb"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_normal_capitalized_word(self):
        # Standard case with a capitalized word.
        s = "Uncle sam"
        n = 3
        expected_output = ["Uncle"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_edge_empty_input_string_n0(self):
        # Empty input string 's' with n=0.
        s = ""
        n = 0
        expected_output = []
        self.assertEqual(select_words(s, n), expected_output)

    def test_edge_empty_input_string_n_nonzero(self):
        # Empty input string 's' with non-zero 'n'.
        s = ""
        n = 5
        expected_output = []
        self.assertEqual(select_words(s, n), expected_output)

    def test_edge_words_only_vowels_n0(self):
        # Words consisting only of vowels, 'n' is 0.
        s = "a e i o u"
        n = 0
        expected_output = ["a", "e", "i", "o", "u"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_edge_word_only_consonants_match(self):
        # Word consisting only of consonants, 'n' matches.
        s = "rhythm"
        n = 6
        expected_output = ["rhythm"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_edge_string_only_spaces(self):
        # String containing only spaces.
        s = "   "
        n = 1
        expected_output = []
        self.assertEqual(select_words(s, n), expected_output)

    def test_edge_multiple_words_mixed_matches(self):
        # Multiple words, some matching, some not.
        s = "Python Programming Language"
        n = 5
        expected_output = ["Python", "Language"]
        self.assertEqual(select_words(s, n), expected_output)

    def test_error_s_not_string(self):
        # Input 's' is not a string.
        s = 123
        n = 1
        with self.assertRaises(TypeError):
            select_words(s, n)

    def test_error_n_negative_integer(self):
        # Input 'n' is a negative integer.
        s = "hello"
        n = -1
        with self.assertRaises(ValueError):
            select_words(s, n)

    def test_error_n_not_integer(self):
        # Input 'n' is not an integer.
        s = "hello"
        n = "two"
        with self.assertRaises(TypeError):
            select_words(s, n)