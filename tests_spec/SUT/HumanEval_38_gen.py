import unittest
from sut.problem_HumanEval_38 import decode_cyclic, encode_cyclic

class Test_decode_cyclic(unittest.TestCase):

    def test_multiple_full_groups(self):
        self.assertEqual(decode_cyclic("bcaefdhig"), 'abcdefghi')

    def test_multiple_full_and_partial_two(self):
        self.assertEqual(decode_cyclic("bcaefdgh"), 'abcdefgh')

    def test_multiple_full_and_partial_one(self):
        self.assertEqual(decode_cyclic("bcaefdg"), 'abcdefg')

    def test_single_full_group(self):
        self.assertEqual(decode_cyclic("bca"), 'abc')

    def test_empty_string(self):
        self.assertEqual(decode_cyclic(""), '')

    def test_partial_group_of_two(self):
        self.assertEqual(decode_cyclic("ab"), 'ab')

    def test_partial_group_of_one(self):
        self.assertEqual(decode_cyclic("a"), 'a')

    def test_one_full_and_partial_two(self):
        self.assertEqual(decode_cyclic("bcade"), 'abcde')

    def test_one_full_and_partial_one(self):
        self.assertEqual(decode_cyclic("bcad"), 'abcd')

    def test_postcondition_reversibility(self):
        # Test the postcondition: encode_cyclic(decode_cyclic(s)) == s
        s = "bcaefdhig"
        decoded_s = decode_cyclic(s)
        re_encoded_s = encode_cyclic(decoded_s)
        self.assertEqual(re_encoded_s, s)