import unittest
from sut.problem_HumanEval_93 import encode

class Test_encode(unittest.TestCase):

    def test_normal_case_from_docstring_1(self):
        self.assertEqual(encode("test"), 'TGST')

    def test_normal_case_from_docstring_2(self):
        self.assertEqual(encode("This is a message"), 'tHKS KS C MGSSCGG')

    def test_normal_case_common_phrase(self):
        self.assertEqual(encode("Hello World"), 'hGLLQ wQRLD')

    def test_normal_case_mixed_vowels_consonants(self):
        self.assertEqual(encode("Python"), 'pYTHQN')

    def test_edge_case_empty_string(self):
        self.assertEqual(encode(""), '')

    def test_edge_case_all_vowels(self):
        self.assertEqual(encode("aeiouAEIOU"), 'CGKQWcgkqw')

    def test_edge_case_all_consonants(self):
        self.assertEqual(encode("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"), 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz')

    def test_edge_case_non_alphabetic(self):
        self.assertEqual(encode("123!@#"), '123!@#')

    def test_edge_case_all_uppercase(self):
        self.assertEqual(encode("TEST"), 'tgst')

    def test_edge_case_spaces_only(self):
        self.assertEqual(encode("   "), '   ')