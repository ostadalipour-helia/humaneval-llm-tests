import unittest
from sut.problem_HumanEval_125 import split_words

class Test_split_words(unittest.TestCase):

    def test_split_on_whitespace(self):
        self.assertEqual(split_words("Hello world!"), ['Hello', 'world!'])

    def test_split_on_comma(self):
        self.assertEqual(split_words("one,two,three"), ['one', 'two', 'three'])

    def test_count_odd_letters(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_empty_string(self):
        self.assertEqual(split_words(""), 0)

    def test_only_whitespace(self):
        self.assertEqual(split_words("   "), [])

    def test_only_commas(self):
        self.assertEqual(split_words(",,,"), [])

    def test_leading_trailing_whitespace(self):
        self.assertEqual(split_words("  hello  world  "), ['hello', 'world'])

    def test_multiple_commas_between_words(self):
        self.assertEqual(split_words("hello,,world"), ['hello', 'world'])

    def test_single_odd_letter(self):
        self.assertEqual(split_words("b"), 1)

    def test_whitespace_and_comma_present(self):
        self.assertEqual(split_words("Hello, World!"), ['Hello,', 'World!'])