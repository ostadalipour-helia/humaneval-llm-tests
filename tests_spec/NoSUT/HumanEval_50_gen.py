import unittest
from sut.problem_HumanEval_50 import decode_shift

class Test_decode_shift(unittest.TestCase):

    def test_normal_case_fghij_to_abcde(self):
        """
        A typical string where characters are shifted back without wrapping.
        """
        self.assertEqual(decode_shift("fghij"), "abcde")

    def test_normal_case_klmno_to_fghij(self):
        """
        Another typical string where characters are shifted back without wrapping.
        """
        self.assertEqual(decode_shift("klmno"), "fghij")

    def test_normal_case_cdefg_to_xyzab_wrap(self):
        """
        A string where characters wrap around from 'c' to 'x', 'd' to 'y', etc.
        """
        self.assertEqual(decode_shift("cdefg"), "xyzab")

    def test_edge_case_empty_string(self):
        """
        Decoding an empty string should result in an empty string.
        """
        self.assertEqual(decode_shift(""), "")

    def test_edge_case_single_char_f_to_a(self):
        """
        Decoding a single character that shifts back to 'a'.
        """
        self.assertEqual(decode_shift("f"), "a")

    def test_edge_case_abcde_to_vwxyz_full_wrap(self):
        """
        Decoding a string where all characters wrap around from 'a' to 'v', 'b' to 'w', etc.
        """
        self.assertEqual(decode_shift("abcde"), "vwxyz")

    def test_edge_case_vwxyz_to_qrstu_middle_alphabet(self):
        """
        Decoding a string where characters are in the middle of the alphabet.
        """
        self.assertEqual(decode_shift("vwxyz"), "qrstu")

    def test_error_non_alphabetic_chars(self):
        """
        Input contains non-alphabetic characters. Expected: ValueError.
        """
        with self.assertRaises(ValueError):
            decode_shift("123")

    def test_error_uppercase_chars(self):
        """
        Input contains uppercase characters. Expected: ValueError.
        """
        with self.assertRaises(ValueError):
            decode_shift("Hello")

    def test_error_input_is_none(self):
        """
        Input is not a string (None). Expected: TypeError.
        """
        with self.assertRaises(TypeError):
            decode_shift(None)

    def test_error_input_is_integer(self):
        """
        Input is an integer instead of a string. Expected: TypeError.
        """
        with self.assertRaises(TypeError):
            decode_shift(123)