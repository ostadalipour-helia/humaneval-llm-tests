import unittest
from sut_llm.problem_HumanEval_38 import decode_cyclic

class TestDecodeCyclic(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(decode_cyclic(""), "")

    def test_single_char_string(self):
        self.assertEqual(decode_cyclic("a"), "a")

    def test_two_char_string(self):
        self.assertEqual(decode_cyclic("ab"), "ab")

    def test_exact_three_chars(self):
        # Encoded "abc" is "bca"
        self.assertEqual(decode_cyclic("bca"), "abc")

    def test_four_chars_one_full_one_partial(self):
        # Encoded "abce" is "bcae"
        self.assertEqual(decode_cyclic("bcae"), "abce")

    def test_five_chars_one_full_one_partial(self):
        # Encoded "abcef" is "bcaef"
        self.assertEqual(decode_cyclic("bcaef"), "abcef")

    def test_six_chars_two_full_groups(self):
        # Encoded "abcdef" is "bcaefd"
        self.assertEqual(decode_cyclic("bcaefd"), "abcdef")

    def test_long_string_mixed_groups(self):
        # Encoded "abcdefghij" is "bcaefdhigj" (as per encode_cyclic function logic)
        self.assertEqual(decode_cyclic("bcaefdhigj"), "abcdefghij")

    def test_string_with_all_same_chars(self):
        # Encoded "aaaaaa" is "aaaaaa"
        self.assertEqual(decode_cyclic("aaaaaa"), "aaaaaa")

    def test_string_with_special_chars_and_numbers(self):
        # Encoded "!@#$12" is "@#!12$"
        self.assertEqual(decode_cyclic("@#!12$"), "!@#$12")