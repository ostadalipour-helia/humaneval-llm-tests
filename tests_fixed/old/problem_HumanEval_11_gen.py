import unittest
from sut_llm.problem_HumanEval_11 import string_xor

class TestStringXOR(unittest.TestCase):
    def test_docstring_example(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_all_zeros(self):
        self.assertEqual(string_xor('0000', '0000'), '0000')

    def test_all_ones(self):
        self.assertEqual(string_xor('1111', '1111'), '0000')

    def test_zeros_xor_ones(self):
        self.assertEqual(string_xor('0000', '1111'), '1111')

    def test_ones_xor_zeros(self):
        self.assertEqual(string_xor('1111', '0000'), '1111')

    def test_alternating_pattern(self):
        self.assertEqual(string_xor('101010', '010101'), '111111')

    def test_mixed_pattern_1(self):
        self.assertEqual(string_xor('110011', '101010'), '011001')

    def test_mixed_pattern_2(self):
        self.assertEqual(string_xor('011010', '101101'), '110111')

    def test_single_char_zero_xor_one(self):
        self.assertEqual(string_xor('0', '1'), '1')

    def test_single_char_one_xor_one(self):
        self.assertEqual(string_xor('1', '1'), '0')