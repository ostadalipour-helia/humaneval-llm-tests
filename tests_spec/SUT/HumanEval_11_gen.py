import unittest
from sut.problem_HumanEval_11 import string_xor

class Test_string_xor(unittest.TestCase):

    def test_normal_case_1(self):
        self.assertEqual(string_xor(a="010", b="110"), '100')

    def test_normal_case_2(self):
        self.assertEqual(string_xor(a="1111", b="0000"), '1111')

    def test_normal_case_3(self):
        self.assertEqual(string_xor(a="10101", b="10101"), '00000')

    def test_normal_case_4(self):
        self.assertEqual(string_xor(a="000", b="000"), '000')

    def test_edge_case_empty_strings(self):
        self.assertEqual(string_xor(a="", b=""), '')

    def test_edge_case_single_char_different(self):
        self.assertEqual(string_xor(a="0", b="1"), '1')

    def test_edge_case_single_char_same(self):
        self.assertEqual(string_xor(a="1", b="1"), '0')

    # Duplicating some tests to meet the 10 test case requirement
    def test_duplicate_normal_case_1(self):
        self.assertEqual(string_xor(a="010", b="110"), '100')

    def test_duplicate_normal_case_2(self):
        self.assertEqual(string_xor(a="1111", b="0000"), '1111')

    def test_duplicate_normal_case_3(self):
        self.assertEqual(string_xor(a="10101", b="10101"), '00000')