import unittest
from sut.problem_HumanEval_28 import concatenate

class Test_concatenate(unittest.TestCase):

    def test_concatenate_multiple_non_empty_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_concatenate_with_spaces_and_punctuation(self):
        self.assertEqual(concatenate(['hello', ' ', 'world', '!']), 'hello world!')

    def test_concatenate_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenate_single_string(self):
        self.assertEqual(concatenate(['single_string']), 'single_string')

    def test_concatenate_with_included_empty_strings(self):
        self.assertEqual(concatenate(['', 'test', '']), 'test')

    def test_concatenate_multiple_non_empty_strings_again(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_concatenate_with_spaces_and_punctuation_again(self):
        self.assertEqual(concatenate(['hello', ' ', 'world', '!']), 'hello world!')

    def test_concatenate_empty_list_again(self):
        self.assertEqual(concatenate([]), '')

    def test_concatenate_single_string_again(self):
        self.assertEqual(concatenate(['single_string']), 'single_string')

    def test_concatenate_with_included_empty_strings_again(self):
        self.assertEqual(concatenate(['', 'test', '']), 'test')