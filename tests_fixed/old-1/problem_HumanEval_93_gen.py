import unittest
from sut_llm.problem_HumanEval_93 import encode

class TestEncodeFunction(unittest.TestCase):

    def test_01_example_one(self):
        self.assertEqual(encode('test'), 'TGST')

    def test_02_example_two(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

    def test_03_all_lowercase_vowels(self):
        self.assertEqual(encode('aeiou'), 'CGKQW')

    def test_04_all_uppercase_vowels(self):
        self.assertEqual(encode('AEIOU'), 'CGKQW')

    def test_05_mixed_case_with_spaces(self):
        self.assertEqual(encode('Hello World'), 'hGLLQ wQRLD')

    def test_06_only_consonants(self):
        self.assertEqual(encode('rhythm'), 'RHYTHM')

    def test_07_empty_string(self):
        self.assertEqual(encode(''), '')

    def test_08_single_lowercase_vowel(self):
        self.assertEqual(encode('a'), 'C')

    def test_09_single_uppercase_consonant(self):
        self.assertEqual(encode('B'), 'b')

    def test_10_longer_mixed_string(self):
        self.assertEqual(encode('Python is Fun'), 'pYTHQN KS fWN')