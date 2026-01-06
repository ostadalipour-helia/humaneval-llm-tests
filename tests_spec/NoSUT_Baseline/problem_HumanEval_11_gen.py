import unittest
import sut.problem_HumanEval_11 as mod

class TestHybrid(unittest.TestCase):
    def test_01_single_char_zero_xor_zero(self):
            # Boundary: '0' XOR '0'
            self.assertEqual(mod.string_xor('0', '0'), '0')

    def test_02_single_char_one_xor_one(self):
            # Boundary: '1' XOR '1'
            self.assertEqual(mod.string_xor('1', '1'), '0')

    def test_03_single_char_zero_xor_one(self):
            # Boundary: '0' XOR '1'
            self.assertEqual(mod.string_xor('0', '1'), '1')

    def test_04_single_char_one_xor_zero(self):
            # Boundary: '1' XOR '0'
            self.assertEqual(mod.string_xor('1', '0'), '1')

    def test_05_empty_strings(self):
            # Edge Case: Empty strings
            self.assertEqual(mod.string_xor('', ''), '')

    def test_06_two_char_mixed(self):
            # Off-by-one / Small string length
            self.assertEqual(mod.string_xor('01', '10'), '11')

    def test_07_docstring_example(self):
            # Typical Input: Example from docstring
            self.assertEqual(mod.string_xor('010', '110'), '100')

    def test_08_typical_mixed_longer(self):
            # Typical Input: Longer string with mixed values
            self.assertEqual(mod.string_xor('10101', '01010'), '11111')

    def test_09_extreme_all_zeros_vs_all_ones(self):
            # Extreme Input: All zeros XOR all ones
            self.assertEqual(mod.string_xor('0000000', '1111111'), '1111111')

    def test_10_extreme_long_self_xor_to_zeros(self):
            # Extreme Input: Long string XORed with itself
            self.assertEqual(mod.string_xor('1010101010101010', '1010101010101010'), '0000000000000000')

    def test_normal_standard_xor(self):
            # Example from docstring: standard XOR operation.
            a = "010"
            b = "110"
            expected_output = "100"
            self.assertEqual(mod.string_xor(a, b), expected_output)

    def test_normal_xor_with_zeros(self):
            # XORing with all zeros.
            a = "1111"
            b = "0000"
            expected_output = "1111"
            self.assertEqual(mod.string_xor(a, b), expected_output)

    def test_normal_xor_identical_strings(self):
            # XORing identical strings.
            a = "10101"
            b = "10101"
            expected_output = "00000"
            self.assertEqual(mod.string_xor(a, b), expected_output)

    def test_normal_xor_all_zeros(self):
            # XORing all zeros.
            a = "000"
            b = "000"
            expected_output = "000"
            self.assertEqual(mod.string_xor(a, b), expected_output)

    def test_edge_empty_strings(self):
            # Empty strings as input.
            a = ""
            b = ""
            expected_output = ""
            self.assertEqual(mod.string_xor(a, b), expected_output)

    def test_edge_single_char_different(self):
            # Single character strings, different.
            a = "0"
            b = "1"
            expected_output = "1"
            self.assertEqual(mod.string_xor(a, b), expected_output)

    def test_edge_single_char_same(self):
            # Single character strings, same.
            a = "1"
            b = "1"
            expected_output = "0"
            self.assertEqual(mod.string_xor(a, b), expected_output)

    def test_error_a_not_string(self):
            # Input 'a' is not a string.
            a = 123
            b = "110"
            with self.assertRaises(TypeError):
                mod.string_xor(a, b)

    def test_error_b_not_string(self):
            # Input 'b' is not a string.
            a = "010"
            b = None
            with self.assertRaises(TypeError):
                mod.string_xor(a, b)

