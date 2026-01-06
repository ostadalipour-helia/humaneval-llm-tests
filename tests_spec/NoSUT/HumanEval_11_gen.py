import unittest
from sut.problem_HumanEval_11 import string_xor

class Test_string_xor(unittest.TestCase):

    def test_normal_standard_xor(self):
        # Example from docstring: standard XOR operation.
        a = "010"
        b = "110"
        expected_output = "100"
        self.assertEqual(string_xor(a, b), expected_output)

    def test_normal_xor_with_zeros(self):
        # XORing with all zeros.
        a = "1111"
        b = "0000"
        expected_output = "1111"
        self.assertEqual(string_xor(a, b), expected_output)

    def test_normal_xor_identical_strings(self):
        # XORing identical strings.
        a = "10101"
        b = "10101"
        expected_output = "00000"
        self.assertEqual(string_xor(a, b), expected_output)

    def test_normal_xor_all_zeros(self):
        # XORing all zeros.
        a = "000"
        b = "000"
        expected_output = "000"
        self.assertEqual(string_xor(a, b), expected_output)

    def test_edge_empty_strings(self):
        # Empty strings as input.
        a = ""
        b = ""
        expected_output = ""
        self.assertEqual(string_xor(a, b), expected_output)

    def test_edge_single_char_different(self):
        # Single character strings, different.
        a = "0"
        b = "1"
        expected_output = "1"
        self.assertEqual(string_xor(a, b), expected_output)

    def test_edge_single_char_same(self):
        # Single character strings, same.
        a = "1"
        b = "1"
        expected_output = "0"
        self.assertEqual(string_xor(a, b), expected_output)

    def test_error_unequal_lengths(self):
        # Input strings have different lengths.
        a = "010"
        b = "1100"
        with self.assertRaises(ValueError): # As per spec, ValueError or AssertionError
            string_xor(a, b)

    def test_error_invalid_char_a(self):
        # Input string 'a' contains characters other than '0' or '1'.
        a = "012"
        b = "110"
        with self.assertRaises(ValueError):
            string_xor(a, b)

    def test_error_invalid_char_b(self):
        # Input string 'b' contains characters other than '0' or '1'.
        a = "010"
        b = "1X0"
        with self.assertRaises(ValueError):
            string_xor(a, b)

    def test_error_a_not_string(self):
        # Input 'a' is not a string.
        a = 123
        b = "110"
        with self.assertRaises(TypeError):
            string_xor(a, b)

    def test_error_b_not_string(self):
        # Input 'b' is not a string.
        a = "010"
        b = None
        with self.assertRaises(TypeError):
            string_xor(a, b)