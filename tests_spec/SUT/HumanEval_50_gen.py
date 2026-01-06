import unittest
from sut.problem_HumanEval_50 import decode_shift

class Test_decode_shift(unittest.TestCase):

    def test_normal_no_wrap(self):
        self.assertEqual(decode_shift("fghij"), "abcde")

    def test_normal_no_wrap_2(self):
        self.assertEqual(decode_shift("klmno"), "fghij")

    def test_normal_with_wrap(self):
        self.assertEqual(decode_shift("cdefg"), "xyzab")

    def test_edge_empty_string(self):
        self.assertEqual(decode_shift(""), "")

    def test_edge_single_char(self):
        self.assertEqual(decode_shift("f"), "a")

    def test_edge_all_wrap(self):
        self.assertEqual(decode_shift("abcde"), "vwxyz")

    def test_edge_middle_alphabet(self):
        self.assertEqual(decode_shift("vwxyz"), "qrstu")

    def test_duplicate_case_1(self):
        self.assertEqual(decode_shift("fghij"), "abcde")

    def test_duplicate_case_2(self):
        self.assertEqual(decode_shift("klmno"), "fghij")

    def test_duplicate_case_3(self):
        self.assertEqual(decode_shift("cdefg"), "xyzab")