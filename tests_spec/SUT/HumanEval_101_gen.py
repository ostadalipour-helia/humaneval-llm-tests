import unittest
from sut.problem_HumanEval_101 import words_string

class Test_words_string(unittest.TestCase):

    def test_normal_case_mixed_separators(self):
        self.assertEqual(words_string("Hi, my name is John"), ['Hi', 'my', 'name', 'is', 'John'])

    def test_normal_case_commas(self):
        self.assertEqual(words_string("One, two, three, four, five, six"), ['One', 'two', 'three', 'four', 'five', 'six'])

    def test_normal_case_spaces(self):
        self.assertEqual(words_string("hello world"), ['hello', 'world'])

    def test_normal_case_no_spaces(self):
        self.assertEqual(words_string("apple,banana,cherry"), ['apple', 'banana', 'cherry'])

    def test_empty_string(self):
        self.assertEqual(words_string(""), [])

    def test_only_spaces(self):
        self.assertEqual(words_string("   "), [])

    def test_only_commas(self):
        self.assertEqual(words_string(",,,"), [])

    def test_only_separators(self):
        self.assertEqual(words_string(" , , "), [])

    def test_single_word(self):
        self.assertEqual(words_string("singleword"), ['singleword'])

    def test_multiple_separators_and_padding(self):
        self.assertEqual(words_string("  word1,  word2 ,word3  "), ['word1', 'word2', 'word3'])