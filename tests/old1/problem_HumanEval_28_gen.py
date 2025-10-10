import unittest
from sut.problem_HumanEval_28 import concatenate

class TestConcatenate(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_basic_single_characters(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_single_string_list(self):
        self.assertEqual(concatenate(['hello']), 'hello')

    def test_list_with_empty_strings(self):
        self.assertEqual(concatenate(['', 'test', '', 'string']), 'teststring')

    def test_mixed_length_strings(self):
        self.assertEqual(concatenate(['Python', 'is', 'fun']), 'Pythonisfun')

    def test_strings_with_spaces(self):
        self.assertEqual(concatenate(['hello', ' ', 'world']), 'hello world')

    def test_numeric_strings(self):
        self.assertEqual(concatenate(['123', '456', '789']), '123456789')

    def test_special_characters_strings(self):
        self.assertEqual(concatenate(['!', '@', '#', '$']), '!@#$')

    def test_unicode_strings(self):
        self.assertEqual(concatenate(['你好', '世界', '！']), '你好世界！')

    def test_long_list_of_strings(self):
        self.assertEqual(concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']), 'abcdefghijk')

if __name__ == '__main__':
    unittest.main()