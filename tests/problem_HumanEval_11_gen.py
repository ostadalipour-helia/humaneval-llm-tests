import unittest
from sut.problem_HumanEval_11 import string_xor

class TestStringXor(unittest.TestCase):

    def test_01_single_char_zero_xor_zero(self):
        # Boundary: '0' XOR '0'
        self.assertEqual(string_xor('0', '0'), '0')

    def test_02_single_char_one_xor_one(self):
        # Boundary: '1' XOR '1'
        self.assertEqual(string_xor('1', '1'), '0')

    def test_03_single_char_zero_xor_one(self):
        # Boundary: '0' XOR '1'
        self.assertEqual(string_xor('0', '1'), '1')

    def test_04_single_char_one_xor_zero(self):
        # Boundary: '1' XOR '0'
        self.assertEqual(string_xor('1', '0'), '1')

    def test_05_empty_strings(self):
        # Edge Case: Empty strings
        self.assertEqual(string_xor('', ''), '')

    def test_06_two_char_mixed(self):
        # Off-by-one / Small string length
        self.assertEqual(string_xor('01', '10'), '11')

    def test_07_docstring_example(self):
        # Typical Input: Example from docstring
        self.assertEqual(string_xor('010', '110'), '100')

    def test_08_typical_mixed_longer(self):
        # Typical Input: Longer string with mixed values
        self.assertEqual(string_xor('10101', '01010'), '11111')

    def test_09_extreme_all_zeros_vs_all_ones(self):
        # Extreme Input: All zeros XOR all ones
        self.assertEqual(string_xor('0000000', '1111111'), '1111111')

    def test_10_extreme_long_self_xor_to_zeros(self):
        # Extreme Input: Long string XORed with itself
        self.assertEqual(string_xor('1010101010101010', '1010101010101010'), '0000000000000000')